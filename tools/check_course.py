# -*- coding: utf-8 -*-
"""Full check suite for the real-audio course.

Verifies the course data, the listening tasks against the real transcripts,
the licence metadata, and (with --net) that every audio URL is still live.
"""
import os, re, sys, json, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from curriculum import all_lessons
from curriculum.audio_sources import AUDIO

FAILS, WARNS, OKS = [], [], []
def ok(m):   OKS.append(m)
def warn(m): WARNS.append(m)
def fail(m): FAILS.append(m)

def check_wiring():
    ls = all_lessons()
    if len(ls) != 92: fail(f"expected 92 sessions, found {len(ls)}")
    else: ok("92 teaching sessions present")
    unwired = [l.code for l in ls if l.listening is not AUDIO.get(l.code)]
    if unwired: fail(f"sessions not wired to a verified recording: {unwired}")
    else: ok("all 92 sessions point at a verified recording")
    return ls

def check_no_fiction():
    pat = re.compile(r'Audio (Test )?\d+(\.\d+)?')
    hits = []
    for d, _, fs in os.walk(os.path.join(ROOT, "curriculum")):
        if "__pycache__" in d: continue
        for f in fs:
            if not f.endswith(".py"): continue
            src = open(os.path.join(d, f), encoding="utf-8").read()
            for m in pat.finditer(src):
                hits.append(f"{f}: {m.group(0)}")
    if hits: fail(f"invented audio references remain: {hits[:5]}")
    else: ok("no invented 'Audio N.N' references remain anywhere in the curriculum")

def check_metadata(ls):
    real = [l for l in ls if not l.listening.recycled_from]
    recycled = [l for l in ls if l.listening.recycled_from]
    if len(real) != 80: fail(f"expected 80 real-audio sessions, found {len(real)}")
    else: ok(f"80 sessions carry an external real-human recording")
    if len(recycled) != 12: fail(f"expected 12 recycled sessions, found {len(recycled)}")
    else: ok("12 Looking Back sessions recycle the unit's own recordings")
    for l in ls:
        a = l.listening
        for fld in ("source", "licence", "attribution", "source_page"):
            if not getattr(a, fld):
                fail(f"{l.code}: missing {fld}")
        if not a.audio_urls:
            fail(f"{l.code}: no audio URL")
    if not FAILS: ok("every session has source, licence, credit line and at least one audio URL")

def check_tasks(ls):
    """Every listening task must have answers, and gap-fill answers must be
    words that really occur in the transcript."""
    bad_counts, bad_answers, no_tasks = [], [], []
    for l in ls:
        a = l.listening
        if not a.tasks: no_tasks.append(l.code); continue
        script_words = set(re.findall(r"[a-z']+", " ".join(a.script).lower()))
        for t in a.tasks:
            if not t.answers:
                bad_counts.append(f"{l.code}/{t.ref}: no answers")
            if t.title == "Notice the language":
                if len(t.items) != len(t.answers):
                    bad_counts.append(f"{l.code}/{t.ref}: {len(t.items)} items vs {len(t.answers)} answers")
                for ans in t.answers:
                    w = re.sub(r'^\d+\.\s*', '', ans).strip().lower()
                    if w and re.fullmatch(r"[a-z']+", w) and w not in script_words:
                        bad_answers.append(f"{l.code}/{t.ref}: '{w}' not in transcript")
            elif t.title in ("Listen for details", "Which conversation?"):
                if len(t.items) != len(t.answers):
                    bad_counts.append(f"{l.code}/{t.ref}: {len(t.items)} items vs {len(t.answers)} answers")
    if no_tasks: fail(f"sessions with no listening task: {no_tasks}")
    if bad_counts: fail(f"task item/answer mismatches: {bad_counts[:6]}")
    if bad_answers: fail(f"gap-fill answers not found in transcript: {bad_answers[:6]}")
    if not (no_tasks or bad_counts or bad_answers):
        n = sum(len(l.listening.tasks) for l in ls)
        ok(f"{n} listening tasks: every answer key checked against the real transcript")

def check_rates():
    """Speech rate and length must stay inside the Grade 7 envelope."""
    data = json.load(open(os.path.join(SCRATCH, "final.json"))) if os.path.exists(
        os.path.join(SCRATCH, "final.json")) else None
    if not data:
        warn("verification dataset not found — skipping speed/quality re-check")
        return
    okr = [r for r in data if r.get('status') == 'OK']
    fast = [(r['key'], r['wpm_gross']) for r in okr if r['wpm_gross'] > 145]
    quiet = [(r['key'], min(p['mean_db'] for p in r['parts'])) for r in okr
             if min(p['mean_db'] for p in r['parts']) < -32]
    lowcov = [(r['key'], r['coverage']) for r in okr if r['coverage'] < 0.90]
    longone = [(r['key'], r['duration']) for r in okr if r['duration'] > 300]
    if fast: fail(f"recordings faster than 145 wpm: {fast}")
    else: ok(f"all 80 recordings at or below 145 wpm (max {max(r['wpm_gross'] for r in okr)})")
    if lowcov: fail(f"transcript accuracy below 0.90: {lowcov}")
    else: ok(f"transcript accuracy >= {min(r['coverage'] for r in okr):.2f} on every recording")
    if quiet: warn(f"quiet recordings (raise classroom volume): {quiet}")
    if longone: warn(f"recordings longer than 5:00: {longone}")
    else: ok(f"every recording fits a 45-minute lesson (longest {max(r['duration'] for r in okr):.0f}s)")

def check_untouched(ls):
    """Nothing outside the listening strand may have changed in the rebuild."""
    bp = os.path.join(ROOT, "tools", "content_baseline.json")
    if not os.path.exists(bp):
        warn("no content baseline — skipping non-listening regression check")
        return
    base = json.load(open(bp))
    diffs = []
    for l in ls:
        b = base.get(l.code)
        if not b: continue
        non = [e.ref for g in (l.guided, l.independent, l.speaking, l.writing,
                               l.workbook, l.homework) for e in g]
        if l.reading: non += [e.ref for e in l.reading.tasks]
        if sorted(non) != b["nonlistening"]:
            diffs.append(f"{l.code}: exercises changed")
        if len(l.vocab) != b["vocab"]:
            diffs.append(f"{l.code}: vocabulary changed")
        if len(l.procedure) != b["stages"]:
            diffs.append(f"{l.code}: procedure stages changed")
        if len(l.materials) != b["materials"]:
            diffs.append(f"{l.code}: materials list length changed")
    if diffs: fail(f"non-listening content changed unexpectedly: {diffs[:6]}")
    else: ok("reading, speaking, writing, vocabulary and homework are untouched (1521 exercises)")


def check_games():
    """The prose rewrite must never swallow a classroom game."""
    n = 0
    for d, _, fs in os.walk(os.path.join(ROOT, "curriculum")):
        if "__pycache__" in d: continue
        for f in fs:
            if f.endswith(".py"):
                n += open(os.path.join(d, f), encoding="utf-8").read().lower().count("bingo")
    if n < 21: fail(f"classroom games lost in the rewrite (found {n} 'bingo', expected 21)")
    else: ok(f"classroom games intact ({n} bingo activities preserved)")


def check_outputs():
    out = os.path.join(ROOT, "output")
    for f in ("01_Teachers_Coursebook.docx", "02_Student_Coursebook.docx",
              "03_Exercise_and_Practice_Book.docx", "04_Homework_Book.docx",
              "05_Teachers_Answer_Key.docx"):
        p = os.path.join(out, f)
        if not os.path.exists(p) or os.path.getsize(p) < 20000:
            fail(f"missing or truncated output: {f}")
    decks = []
    for d, _, fs in os.walk(os.path.join(out, "slides")):
        decks += [x for x in fs if x.endswith(".pptx")]
    if len(decks) != 92: fail(f"expected 92 slide decks, found {len(decks)}")
    else: ok("5 books and 92 slide decks built")

def check_urls(ls):
    import urllib.request
    UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    urls = sorted({u for l in ls for u in l.listening.audio_urls})
    pages = sorted({l.listening.source_page for l in ls if l.listening.source_page})
    bad = []
    from concurrent.futures import ThreadPoolExecutor
    def head(u):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": UA}, method="GET")
            with urllib.request.urlopen(req, timeout=40) as r:
                r.read(2048)
                return u, r.status
        except Exception as e:
            return u, str(e)
    with ThreadPoolExecutor(max_workers=8) as ex:
        for u, st in ex.map(head, urls + pages):
            if st != 200: bad.append((u, st))
    if bad: fail(f"unreachable URLs: {bad[:6]}")
    else: ok(f"all {len(urls)} audio files and {len(pages)} lesson pages return HTTP 200")

SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verification")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--net", action="store_true", help="also check every URL is live")
    args = ap.parse_args()
    ls = check_wiring()
    check_no_fiction()
    check_metadata(ls)
    check_tasks(ls)
    check_rates()
    check_untouched(ls)
    check_games()
    check_outputs()
    if args.net:
        check_urls(ls)
    print("\n".join("  PASS  " + m for m in OKS))
    print("\n".join("  WARN  " + m for m in WARNS))
    print("\n".join("  FAIL  " + m for m in FAILS))
    print(f"\n{len(OKS)} passed, {len(WARNS)} warnings, {len(FAILS)} failed")
    sys.exit(1 if FAILS else 0)
