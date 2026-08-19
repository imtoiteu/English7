#!/usr/bin/env python3
"""Real audio verification harness.
For each candidate: fetch page -> extract audio + transcript -> download audio ->
ffprobe (duration/codec/rate/channels) -> ffmpeg volumedetect (levels/clipping) ->
faster-whisper ASR -> compare ASR vs published transcript -> WPM.
"""
import re, html, json, os, subprocess, sys, urllib.parse, hashlib, time
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
BASE = os.path.dirname(os.path.abspath(__file__))
ADIR = os.path.join(BASE, "audio")
os.makedirs(ADIR, exist_ok=True)

def get(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()

INLINE = r'(?:b|i|u|em|strong|span|font|small|sub|sup|a|mark)'
def page_text(h):
    t = re.sub(r'<script.*?</script>', ' ', h, flags=re.S | re.I)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    # inline formatting must NOT break a sentence
    t = re.sub(r'</?' + INLINE + r'(?:\s[^>]*)?>', '', t, flags=re.I)
    t = re.sub(r'<br\s*/?>', ' ', t, flags=re.I)
    t = re.sub(r'<[^>]+>', '\n', t)
    return html.unescape(t)

def fetch_audio(url, name):
    path = os.path.join(ADIR, name)
    if os.path.exists(path) and os.path.getsize(path) > 2000:
        return path
    st, data = get(url)
    if st != 200 or len(data) < 2000:
        raise RuntimeError(f"audio fetch {st} len={len(data)}")
    open(path, 'wb').write(data)
    return path

def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
        "format=duration,bit_rate:stream=codec_name,sample_rate,channels",
        "-of", "json", path], capture_output=True, text=True).stdout
    j = json.loads(out)
    s = (j.get("streams") or [{}])[0]
    f = j.get("format", {})
    return {
        "duration": round(float(f.get("duration", 0)), 1),
        "bitrate_kbps": int(f.get("bit_rate", 0) or 0) // 1000,
        "codec": s.get("codec_name"), "sample_rate": s.get("sample_rate"),
        "channels": s.get("channels"),
    }

def levels(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
        "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    d = {}
    for k, pat in (("mean_db", r"mean_volume:\s*(-?[\d.]+) dB"),
                   ("max_db", r"max_volume:\s*(-?[\d.]+) dB")):
        m = re.search(pat, r)
        if m: d[k] = float(m.group(1))
    return d

_model = None
def asr(path):
    global _model
    from faster_whisper import WhisperModel
    if _model is None:
        _model = WhisperModel("small", device="cpu", compute_type="int8")
    segs, info = _model.transcribe(path, language="en", beam_size=5, vad_filter=True)
    segs = list(segs)
    text = " ".join(s.text.strip() for s in segs)
    speech = sum(s.end - s.start for s in segs)
    return text, speech, info.duration

WORD = re.compile(r"[a-z']+")
def norm(t):
    t = t.lower().replace("’", "'")
    return WORD.findall(t)

def similarity(a, b):
    """token-level overlap, order-insensitive multiset F1 (robust proxy for transcript fidelity)"""
    from collections import Counter
    ca, cb = Counter(a), Counter(b)
    inter = sum((ca & cb).values())
    if not inter: return 0.0
    p = inter / max(1, len(b)); r = inter / max(1, len(a))
    return round(2 * p * r / (p + r), 3)

def extract_media(page_url, h):
    """Return list of absolute media URLs found on the page."""
    urls = []
    for m in re.finditer(r'(?:src|href)\s*=\s*"([^"]+\.(?:mp3|mp4|m4a))"', h, re.I):
        urls.append(urllib.parse.urljoin(page_url, m.group(1)))
    for m in re.finditer(r'https?://[^\s"\'<>\\]+?\.(?:mp3|mp4|m4a)', h, re.I):
        urls.append(m.group(0))
    seen, out = set(), []
    for u in urls:
        u = u.split('&quot;')[0]
        if u in seen: continue
        seen.add(u); out.append(u)
    return out

def clean_transcript(h):
    t = page_text(h)
    lines = [re.sub(r'\s+', ' ', l).strip() for l in t.split('\n')]
    return [l for l in lines if l]
