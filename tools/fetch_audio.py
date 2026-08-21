#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download the 99 recordings this course plays, into audio/.

The MP3s are not in the repository. Half of them are © ELLLO, licensed for
classroom use but not for redistribution, and this repository is public; and
273 MB of audio would sit in the git history forever. So the repository keeps
the *references* — every source page and direct URL lives in
`curriculum/audio_sources.py` and `curriculum/audio_diagnostic.py` — and this
script turns those references back into files.

    python3 tools/fetch_audio.py              download whatever is missing
    python3 tools/fetch_audio.py --verify     check what is already there
    python3 tools/fetch_audio.py --html       write audio/DOWNLOADS.html
    python3 tools/fetch_audio.py --list       print the manifest as TSV

Downloading is resumable: anything already present and non-trivial in size is
skipped, so re-running after a dropped connection costs nothing.

Licence, restated because it matters: VOA material is public domain. ELLLO
material may be downloaded and used in class or on a class LMS; it may not be
redistributed more widely. Downloading it for your own teaching is exactly what
the licence permits. Re-uploading it somewhere public is not.
"""
import os, sys, argparse, subprocess, html as _html
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
AUDIO_DIR = os.path.join(ROOT, "audio")

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120 Safari/537.36")


# --------------------------------------------------------------------------
def manifest():
    """Every distinct recording the course needs: one row per physical file.

    The filename is derived, not stored: F<lesson code>_<part>_<source basename>.
    The twelve *Looking Back* lessons carry `recycled_from` — they replay their
    own unit's Lesson 2 and Lesson 3 audio rather than holding a copy — so they
    contribute no file of their own.
    """
    from curriculum.audio_sources import AUDIO
    from curriculum.audio_diagnostic import DIAG_AUDIO, DIAG_FILES

    def _order(code):
        """Sort key that puts each review block after the units it reviews."""
        if code.startswith("U"):
            return float(code[1:].split("L")[0])
        if code.startswith("REV"):
            return int(code[3]) * 3 + 0.5      # REV1 -> 3.5, REV2 -> 6.5 …
        return 0.0

    rows = []
    for code, a in AUDIO.items():
        if a.recycled_from:
            continue
        for i, url in enumerate(a.audio_urls, 1):
            rows.append(dict(
                key=code, part=i, kind="course",
                unit=_order(code),
                name=f"F{code}_{i}_{url.split('/')[-1]}",
                url=url, page=a.source_page, title=a.title,
                source=a.source, licence=a.licence,
                duration=a.duration, rate=a.speech_rate))
    for key, a in DIAG_AUDIO.items():
        rows.append(dict(
            key=key, part=1, kind="diagnostic", unit=99,
            name=os.path.basename(DIAG_FILES[key]),
            url=a.audio_urls[0], page=a.source_page, title=a.title,
            source=a.source, licence=a.licence,
            duration=a.duration, rate=a.speech_rate))

    rows.sort(key=lambda r: (r["kind"] != "course", r["unit"], r["key"], r["part"]))
    return rows


def is_elllo(row):
    return "elllo" in (row["page"] or "").lower() or "ELLLO" in (row["source"] or "")


# --------------------------------------------------------------------------
def fetch(rows, force=False):
    os.makedirs(AUDIO_DIR, exist_ok=True)
    have = skipped = got = failed = 0
    for n, r in enumerate(rows, 1):
        path = os.path.join(AUDIO_DIR, r["name"])
        if os.path.exists(path) and os.path.getsize(path) > 100_000 and not force:
            have += 1
            continue
        try:
            req = urllib.request.Request(r["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = resp.read()
            if len(data) < 100_000:
                raise RuntimeError(f"only {len(data)} bytes")
            with open(path, "wb") as f:
                f.write(data)
            got += 1
            print(f"  [{n:3}/{len(rows)}] ✓ {r['name'][:58]:58} {len(data)/1048576:5.1f} MB")
        except Exception as e:
            failed += 1
            print(f"  [{n:3}/{len(rows)}] ✗ {r['name'][:58]:58} {e}")
    print(f"\n  {got} downloaded · {have} already present · {failed} failed "
          f"· {len(rows)} total")
    if failed:
        print("  Re-run to retry only the failures — anything already on disk is skipped.")
    return failed


def verify(rows):
    missing, small, bad = [], [], []
    total = 0
    for r in rows:
        path = os.path.join(AUDIO_DIR, r["name"])
        if not os.path.exists(path):
            missing.append(r["name"])
            continue
        size = os.path.getsize(path)
        total += size
        if size < 100_000:
            small.append(r["name"])
            continue
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", path], capture_output=True, text=True)
        if out.returncode != 0 or not out.stdout.strip():
            bad.append(r["name"])
    print(f"  {len(rows) - len(missing)}/{len(rows)} present · {total/1048576:.0f} MB")
    for label, items in (("missing", missing), ("truncated", small), ("unreadable", bad)):
        if items:
            print(f"  {len(items)} {label}:")
            for i in items[:10]:
                print("     ", i)
    if not (missing or small or bad):
        print("  ✓ every recording is present and readable")
    return 1 if (missing or small or bad) else 0


# --------------------------------------------------------------------------
def write_html(rows, path=None):
    """A click-to-download index that works offline in any browser."""
    path = path or os.path.join(AUDIO_DIR, "DOWNLOADS.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    e = _html.escape

    groups = {}
    for r in rows:
        if r["kind"] == "diagnostic":
            g = "Diagnostic papers"
        elif r["key"].startswith("REV"):
            g = "Review & test blocks"
        else:
            g = f"Unit {int(r['unit'])}"
        groups.setdefault(g, []).append(r)

    n_voa = sum(1 for r in rows if not is_elllo(r))
    n_ell = len(rows) - n_voa

    parts = ["""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>English 7 — audio downloads</title>
<style>
  :root{--bg:#fff;--fg:#1a1a1a;--mut:#5a6472;--line:#dfe3e8;--card:#f7f9fb;
        --accent:#1f3b63;--voa:#0e7c66;--ell:#c05a11}
  @media (prefers-color-scheme:dark){:root:not([data-theme=light]){
        --bg:#12151a;--fg:#e8eaed;--mut:#9aa5b1;--line:#2a3038;--card:#1a1f27;
        --accent:#7fa8dd;--voa:#4dbfa4;--ell:#e0913f}}
  :root[data-theme=dark]{--bg:#12151a;--fg:#e8eaed;--mut:#9aa5b1;--line:#2a3038;
        --card:#1a1f27;--accent:#7fa8dd;--voa:#4dbfa4;--ell:#e0913f}
  *{box-sizing:border-box}
  body{margin:0;padding:2rem 1.25rem 4rem;background:var(--bg);color:var(--fg);
       font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
  .wrap{max-width:1000px;margin:0 auto}
  h1{font-size:1.7rem;margin:0 0 .3rem;color:var(--accent)}
  .sub{color:var(--mut);margin:0 0 1.5rem}
  .note{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--ell);
        border-radius:6px;padding:.9rem 1.1rem;margin:0 0 1.5rem;font-size:.9rem}
  .note b{color:var(--ell)}
  h2{font-size:1.05rem;margin:2rem 0 .6rem;padding-bottom:.3rem;
     border-bottom:1px solid var(--line);color:var(--accent)}
  .scroll{overflow-x:auto}
  table{border-collapse:collapse;width:100%;font-size:.86rem;min-width:640px}
  th{text-align:left;font-weight:600;color:var(--mut);padding:.4rem .5rem;
     border-bottom:1px solid var(--line);font-size:.78rem;text-transform:uppercase;
     letter-spacing:.03em}
  td{padding:.4rem .5rem;border-bottom:1px solid var(--line);vertical-align:top}
  tr:hover td{background:var(--card)}
  a{color:var(--accent)}
  a.dl{font-weight:600;text-decoration:none}
  a.dl:hover{text-decoration:underline}
  .tag{display:inline-block;font-size:.72rem;font-weight:600;padding:.05rem .4rem;
       border-radius:3px;border:1px solid currentColor}
  .voa{color:var(--voa)} .ell{color:var(--ell)}
  .mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.78rem;
        color:var(--mut);word-break:break-all}
  code{background:var(--card);border:1px solid var(--line);border-radius:4px;
       padding:.1rem .35rem;font-size:.85em}
  footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--line);
         color:var(--mut);font-size:.82rem}
</style></head><body><div class="wrap">
<h1>English 7 — audio downloads</h1>"""]
    parts.append(f'<p class="sub">{len(rows)} recordings · {n_voa} VOA (public domain) · '
                 f'{n_ell} ELLLO (classroom use) · about 273&nbsp;MB in total</p>')
    parts.append("""<div class="note">
<p style="margin:.1rem 0"><b>Save each file with the name in the “Save as” column.</b>
The course looks for that exact filename in <code>audio/</code>. Right-click a link and
choose “Save link as…”, or run <code>python3 tools/fetch_audio.py</code> to get all
""" + str(len(rows)) + """ in one command.</p>
<p style="margin:.55rem 0 .1rem"><b>Licence.</b> VOA recordings are public domain — copy,
play and print them freely with credit. ELLLO recordings may be downloaded and used in
class or on a class LMS, but <em>not</em> redistributed more widely. That is why they are
linked here rather than hosted.</p></div>""")

    order = (["Diagnostic papers"]
             + [f"Unit {i}" for i in range(1, 13)]
             + ["Review & test blocks"])
    for g in order:
        rs = groups.get(g)
        if not rs:
            continue
        parts.append(f"<h2>{e(g)} <span style='color:var(--mut);font-weight:400'>"
                     f"— {len(rs)} file{'s' if len(rs) != 1 else ''}</span></h2>")
        parts.append('<div class="scroll"><table><thead><tr>'
                     '<th>Lesson</th><th>Recording</th><th>Length</th><th>Speed</th>'
                     '<th>Source</th><th>Save as</th><th>Get it</th>'
                     '</tr></thead><tbody>')
        for r in rs:
            tag = ('<span class="tag ell">ELLLO</span>' if is_elllo(r)
                   else '<span class="tag voa">VOA</span>')
            parts.append(
                f'<tr><td><b>{e(r["key"])}</b>'
                + (f"<br><span class='mono'>part {r['part']}</span>" if r["part"] > 1 else "")
                + f'</td><td>{e(r["title"])}</td>'
                f'<td>{e(r["duration"])}</td>'
                f'<td>{e(r["rate"].replace(" as heard", ""))}</td>'
                f'<td>{tag}<br><a href="{e(r["page"])}" target="_blank" rel="noopener noreferrer" '
                f'class="mono">lesson page</a></td>'
                f'<td class="mono">{e(r["name"])}</td>'
                f'<td><a class="dl" href="{e(r["url"])}" target="_blank" rel="noopener noreferrer" '
                f'download>MP3 &darr;</a></td></tr>')
        parts.append("</tbody></table></div>")

    parts.append("""<footer>
<p><b>One command instead of clicking:</b> <code>python3 tools/fetch_audio.py</code>
downloads everything missing into <code>audio/</code> and skips what you already have.
Then <code>python3 tools/fetch_audio.py --verify</code> confirms every file is present and
readable, and <code>python3 tools/check_diagnostic.py --probe</code> confirms each
diagnostic recording matches its declared duration and format.</p>
<p>Credit line for anything printed: Voice of America — “Let’s Learn English” ·
learningenglish.voanews.com · public domain. ELLLO material © elllo productions,
elllo.org.</p>
<p>Generated by <code>tools/fetch_audio.py --html</code> from
<code>curriculum/audio_sources.py</code> and <code>curriculum/audio_diagnostic.py</code>.
Regenerate it after any change to the recordings.</p>
</footer></div></body></html>""")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    return path


# --------------------------------------------------------------------------
def write_artifact(rows, path=None):
    """Body-only HTML for publishing as a shareable Artifact page.

    Same manifest as write_html(), different wrapper: an Artifact is served
    inside a supplied <html>/<head>/<body> skeleton, so this emits content
    only. Kept in this file so the page can never drift from the recordings
    it lists.
    """
    path = path or os.path.join(ROOT, "planning", "audio-downloads.artifact.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    e = _html.escape

    groups, order = {}, []
    for r in rows:
        if r["kind"] == "diagnostic":
            g = "Diagnostic papers"
        elif r["key"].startswith("REV"):
            g = f"Review {int(r['unit']) // 3}"
        else:
            g = f"Unit {int(r['unit'])}"
        if g not in groups:
            groups[g] = []
            order.append(g)
        groups[g].append(r)

    n_voa = sum(1 for r in rows if not is_elllo(r))
    n_ell = len(rows) - n_voa
    total_mb = 273

    out = ['<title>English 7 Audio Library</title>',
           '<link rel="preconnect" href="https://fonts.googleapis.com">',
           '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
           'family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&'
           'family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap">',
           """<style>
:root{
  --ground:#fbfcfd; --raised:#f1f4f8; --ink:#16202e; --muted:#5b6878;
  --line:#dde3ea; --navy:#1f3b63; --teal:#0e7c66; --ochre:#b4560f;
  --teal-bg:#e4f2ed; --ochre-bg:#fbeee2; --focus:#1e6fb8;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#10151c; --raised:#19212c; --ink:#e6ebf2; --muted:#94a3b5;
  --line:#28323f; --navy:#8fb3e0; --teal:#4dbfa4; --ochre:#e0913f;
  --teal-bg:#14302a; --ochre-bg:#33220f; --focus:#6fa8dd;
}}
:root[data-theme="dark"]{
  --ground:#10151c; --raised:#19212c; --ink:#e6ebf2; --muted:#94a3b5;
  --line:#28323f; --navy:#8fb3e0; --teal:#4dbfa4; --ochre:#e0913f;
  --teal-bg:#14302a; --ochre-bg:#33220f; --focus:#6fa8dd;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font-family:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1060px;margin:0 auto;padding:2.5rem 1.25rem 5rem;
  display:flex;flex-direction:column;gap:1.5rem}
h1{font-family:"Source Serif 4",Georgia,serif;font-weight:700;font-size:2.05rem;
  line-height:1.15;margin:0;color:var(--ink);text-wrap:balance;letter-spacing:-.01em}
.lede{margin:0;color:var(--muted);max-width:62ch}
.bar{position:sticky;top:0;z-index:5;background:var(--ground);
  border-bottom:1px solid var(--line);padding:.7rem 0;margin-bottom:-.4rem;
  display:flex;flex-wrap:wrap;gap:.6rem;align-items:center}
.stat{display:flex;flex-direction:column;padding-right:1.1rem;margin-right:.2rem;
  border-right:1px solid var(--line)}
.stat:last-of-type{border-right:0}
.stat b{font-size:1.15rem;font-variant-numeric:tabular-nums;line-height:1.1}
.stat span{font-size:.7rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
button{font:inherit;font-size:.82rem;font-weight:500;cursor:pointer;
  background:var(--raised);color:var(--ink);border:1px solid var(--line);
  border-radius:5px;padding:.42rem .8rem}
button:hover{border-color:var(--navy);color:var(--navy)}
button:focus-visible,a:focus-visible,input:focus-visible{outline:2px solid var(--focus);
  outline-offset:2px}
.panel{background:var(--raised);border:1px solid var(--line);border-radius:8px;
  padding:1rem 1.15rem;display:flex;flex-direction:column;gap:.5rem}
.panel h2{font-family:"IBM Plex Sans",sans-serif;font-size:.74rem;font-weight:600;
  text-transform:uppercase;letter-spacing:.07em;color:var(--muted);margin:0}
.panel p{margin:0;font-size:.9rem}
code{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.85em;
  background:var(--ground);border:1px solid var(--line);border-radius:4px;padding:.1rem .35rem}
h2.grp{font-family:"Source Serif 4",Georgia,serif;font-weight:600;font-size:1.15rem;
  margin:1.4rem 0 0;display:flex;align-items:baseline;gap:.6rem;color:var(--ink)}
h2.grp em{font-style:normal;font-size:.74rem;font-weight:500;color:var(--muted);
  text-transform:uppercase;letter-spacing:.06em}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--raised)}
table{border-collapse:collapse;width:100%;min-width:720px;font-size:.85rem}
th{text-align:left;font-size:.68rem;font-weight:600;text-transform:uppercase;
  letter-spacing:.06em;color:var(--muted);padding:.55rem .7rem;
  border-bottom:1px solid var(--line);white-space:nowrap}
td{padding:.5rem .7rem;border-bottom:1px solid var(--line);vertical-align:middle}
tr:last-child td{border-bottom:0}
tr.done td{opacity:.45}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap;color:var(--muted)}
.code{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.78rem;
  font-weight:500;color:var(--navy);white-space:nowrap}
.fname{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.72rem;
  color:var(--muted);word-break:break-all;max-width:26ch;display:inline-block}
.chip{display:inline-block;font-size:.66rem;font-weight:600;letter-spacing:.04em;
  padding:.1rem .42rem;border-radius:3px;white-space:nowrap}
.chip.voa{color:var(--teal);background:var(--teal-bg)}
.chip.ell{color:var(--ochre);background:var(--ochre-bg)}
a{color:var(--navy)}
a.get{font-weight:600;text-decoration:none;white-space:nowrap}
a.get:hover{text-decoration:underline}
input[type=checkbox]{width:15px;height:15px;accent-color:var(--navy);cursor:pointer}
footer{margin-top:1.5rem;padding-top:1.1rem;border-top:1px solid var(--line);
  color:var(--muted);font-size:.83rem;display:flex;flex-direction:column;gap:.5rem}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
</style>""",
           '<div class="wrap">',
           '<div>',
           '<h1>English 7 Audio Library</h1>',
           f'<p class="lede">The {len(rows)} recordings the course plays, with a direct link to '
           f'each one. They are hosted by VOA and ELLLO and linked here rather than re-published, '
           f'because the ELLLO licence covers classroom use but not redistribution.</p>',
           '</div>']

    out.append('<div class="bar">'
               f'<div class="stat"><b>{len(rows)}</b><span>recordings</span></div>'
               f'<div class="stat"><b>{n_voa}</b><span>VOA · public domain</span></div>'
               f'<div class="stat"><b>{n_ell}</b><span>ELLLO · classroom</span></div>'
               f'<div class="stat"><b>~{total_mb} MB</b><span>total</span></div>'
               '<div class="stat" style="border:0"><b id="done">0</b><span>you have</span></div>'
               '<button type="button" id="copyall">Copy all URLs</button>'
               '<button type="button" id="reset">Clear ticks</button>'
               '</div>')

    out.append('<div class="panel">'
               '<h2>Two ways to get them</h2>'
               '<p><b>All at once.</b> From a clone of the repository, run '
               '<code>python3 tools/fetch_audio.py</code>. It downloads whatever is missing into '
               '<code>audio/</code>, skips what you already have, and is safe to re-run after a '
               'dropped connection. Then <code>python3 tools/fetch_audio.py --verify</code> '
               'confirms all ' + str(len(rows)) + ' are present and readable.</p>'
               '<p><b>One at a time.</b> Right-click a link below and choose '
               '&ldquo;Save link as&hellip;&rdquo;, then save it under the exact name in the '
               '<b>Save as</b> column &mdash; the course looks for that filename. Tick a row to '
               'remember you have it; the ticks are stored in this browser only.</p>'
               '<p><b>Into a download manager.</b> <i>Copy all URLs</i> puts the whole list on '
               'your clipboard, one per line.</p>'
               '</div>')

    for g in order:
        rs = groups[g]
        urls = " ".join(r["url"] for r in rs)
        out.append(f'<h2 class="grp">{e(g)} <em>{len(rs)} file'
                   f'{"s" if len(rs) != 1 else ""}</em></h2>')
        out.append('<div class="scroll"><table><thead><tr>'
                   '<th style="width:1.6rem"></th><th>Lesson</th><th>Recording</th>'
                   '<th>Length</th><th>Speed</th><th>Licence</th><th>Save as</th><th>Get it</th>'
                   '</tr></thead><tbody>')
        for r in rs:
            chip = ('<span class="chip ell">ELLLO</span>' if is_elllo(r)
                    else '<span class="chip voa">VOA</span>')
            label = e(r["key"]) + (f" &middot; {r['part']}" if r["part"] > 1 else "")
            rate = e(r["rate"].replace(" words per minute as heard", " wpm"))
            out.append(
                f'<tr data-f="{e(r["name"])}">'
                f'<td><input type="checkbox" aria-label="I have {e(r["name"])}"></td>'
                f'<td class="code">{label}</td>'
                f'<td>{e(r["title"])}<br>'
                f'<a href="{e(r["page"])}" target="_blank" rel="noopener noreferrer" '
                f'style="font-size:.74rem">lesson page &nearr;</a></td>'
                f'<td class="num">{e(r["duration"])}</td>'
                f'<td class="num">{rate}</td>'
                f'<td>{chip}</td>'
                f'<td><span class="fname">{e(r["name"])}</span></td>'
                f'<td><a class="get" href="{e(r["url"])}" target="_blank" '
                f'rel="noopener noreferrer">MP3 &darr;</a></td></tr>')
        out.append('</tbody></table></div>')
        out.append(f'<div><button type="button" class="copygrp" data-u="{e(urls)}">'
                   f'Copy the {len(rs)} URLs in {e(g)}</button></div>')

    out.append('<footer>'
               '<p><b>Credit.</b> Voice of America &mdash; &ldquo;Let&rsquo;s Learn '
               'English&rdquo; &middot; learningenglish.voanews.com &middot; public domain, so '
               'VOA recordings may be copied, played and printed in test papers with credit. '
               'ELLLO material &copy; elllo productions, elllo.org &mdash; teachers may download '
               'and use it in class or on a class LMS; wider redistribution is not granted.</p>'
               '<p>Generated from <code>curriculum/audio_sources.py</code> and '
               '<code>curriculum/audio_diagnostic.py</code>, so this list cannot drift from the '
               'recordings the lessons actually reference.</p>'
               '</footer>')
    out.append('</div>')

    out.append("""<script>
(function(){
  var KEY = "en7-audio-have";
  function load(){ try { return JSON.parse(localStorage.getItem(KEY)) || {}; }
                   catch(e){ return {}; } }
  function save(s){ try { localStorage.setItem(KEY, JSON.stringify(s)); } catch(e){} }
  var state = load();
  var rows = Array.prototype.slice.call(document.querySelectorAll("tr[data-f]"));
  var counter = document.getElementById("done");

  function paint(){
    var n = 0;
    rows.forEach(function(tr){
      var on = !!state[tr.dataset.f];
      tr.classList.toggle("done", on);
      tr.querySelector("input").checked = on;
      if (on) n++;
    });
    if (counter) counter.textContent = n;
  }
  rows.forEach(function(tr){
    tr.querySelector("input").addEventListener("change", function(ev){
      if (ev.target.checked) state[tr.dataset.f] = 1; else delete state[tr.dataset.f];
      save(state); paint();
    });
  });
  paint();

  function copy(text, btn){
    var label = btn.textContent;
    function ok(){ btn.textContent = "Copied"; setTimeout(function(){
      btn.textContent = label; }, 1400); }
    function fallback(){
      var ta = document.createElement("textarea");
      ta.value = text; ta.setAttribute("readonly","");
      ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      try { document.execCommand("copy"); ok(); }
      catch(e){ btn.textContent = "Press Ctrl+C"; ta.style.opacity = "1"; return; }
      document.body.removeChild(ta);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(ok, fallback);
    } else { fallback(); }
  }

  var all = rows.map(function(tr){
    return tr.querySelector("a.get").href; }).join("\n");
  var ca = document.getElementById("copyall");
  if (ca) ca.addEventListener("click", function(){ copy(all, ca); });

  document.querySelectorAll(".copygrp").forEach(function(b){
    b.addEventListener("click", function(){
      copy(b.dataset.u.split(" ").join("\n"), b); });
  });

  var rs = document.getElementById("reset");
  if (rs) rs.addEventListener("click", function(){
    state = {}; save(state); paint(); });
})();
</script>""")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return path


# --------------------------------------------------------------------------
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verify", action="store_true", help="check what is already on disk")
    ap.add_argument("--html", action="store_true", help="write audio/DOWNLOADS.html")
    ap.add_argument("--artifact", action="store_true",
                    help="write planning/audio-downloads.artifact.html for publishing")
    ap.add_argument("--list", action="store_true", help="print the manifest as TSV")
    ap.add_argument("--force", action="store_true", help="re-download even if present")
    args = ap.parse_args()

    rows = manifest()

    if args.list:
        try:
            print("key\tpart\tkind\tfile\tduration\trate\turl")
            for r in rows:
                print(f"{r['key']}\t{r['part']}\t{r['kind']}\t{r['name']}\t"
                      f"{r['duration']}\t{r['rate']}\t{r['url']}")
        except BrokenPipeError:      # `--list | head` is a normal thing to do
            os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(0)

    if args.artifact:
        p = write_artifact(rows)
        print(f"  ✓ {os.path.relpath(p, ROOT)} — {len(rows)} recordings, ready to publish")
        sys.exit(0)

    if args.html:
        p = write_html(rows)
        print(f"  ✓ {os.path.relpath(p, ROOT)} — {len(rows)} recordings, click to download")
        sys.exit(0)

    if args.verify:
        sys.exit(verify(rows))

    print(f"  Fetching {len(rows)} recordings into audio/ …")
    sys.exit(1 if fetch(rows, force=args.force) else 0)
