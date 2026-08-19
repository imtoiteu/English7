# -*- coding: utf-8 -*-
"""Point every lesson at its VERIFIED real recording.

Rewrites, in curriculum/units/*.py and curriculum/reviews.py:
  listening=A(...)          ->  listening=AUDIO["U1L1"]
  materials "Audio 1.1"     ->  the real citation
  stage material="Audio 1.1"->  the real citation
and rewrites stage/teacher lines that describe the old invented audio.
"""
import ast, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
FILES = [os.path.join(ROOT, "curriculum", "units", f"u{n:02d}.py") for n in range(1, 13)] \
        + [os.path.join(ROOT, "curriculum", "reviews.py")]

AUDIO_REF = re.compile(r'^Audio (\d+\.\d+|Test \d)$')
AUDIO_ANY = re.compile(r'Audio (\d+\.\d+|Test \d)')


def offsets(src_bytes):
    """ast col_offset is a UTF-8 BYTE offset, so we index the encoded source."""
    lines = src_bytes.splitlines(keepends=True)
    start = [0]
    for l in lines:
        start.append(start[-1] + len(l))
    return lambda ln, col: start[ln - 1] + col


def citation(meta):
    """Short citation used in `materials` and stage `material` fields."""
    if meta.get('recycled_from'):
        return f"Recording: {meta['title']} (replay — see the lesson page)"
    return f"Recording: {meta['title']} — {meta['source']} ({meta['duration']})"


def main():
    from curriculum.audio_sources import AUDIO
    meta = {c: dict(title=a.title, source=a.source, duration=a.duration,
                    page=a.source_page, recycled_from=a.recycled_from)
            for c, a in AUDIO.items()}

    total = {"listening": 0, "materials": 0, "stage": 0, "prose": 0}
    for path in FILES:
        src = open(path, encoding="utf-8").read()
        raw = src.encode("utf-8")
        tree = ast.parse(src)
        off = offsets(raw)
        edits = []          # (start, end, replacement)

        for node in ast.walk(tree):
            if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == "Lesson"):
                continue
            kw = {k.arg: k.value for k in node.keywords if k.arg}
            code_node = kw.get("code")
            if not isinstance(code_node, ast.Constant):
                continue
            code = code_node.value
            if code not in meta:
                continue
            m = meta[code]

            # 1. listening=A(...) -> AUDIO["code"]
            ln = kw.get("listening")
            if ln is not None:
                edits.append((off(ln.lineno, ln.col_offset),
                              off(ln.end_lineno, ln.end_col_offset),
                              f'AUDIO[{code!r}]'))
                total["listening"] += 1

            # 2. materials list entries
            mats = kw.get("materials")
            if isinstance(mats, ast.List):
                for el in mats.elts:
                    if isinstance(el, ast.Constant) and isinstance(el.value, str) \
                            and AUDIO_ANY.search(el.value):
                        v = el.value.strip()
                        new_v = citation(m) if AUDIO_REF.match(v) else AUDIO_ANY.sub(citation(m), el.value)
                        edits.append((off(el.lineno, el.col_offset),
                                      off(el.end_lineno, el.end_col_offset),
                                      repr(new_v)))
                        total["materials"] += 1

            # 3. procedure stages: material="Audio x.y" and prose that names the old audio
            proc = kw.get("procedure")
            if isinstance(proc, ast.List):
                for st in proc.elts:
                    if not (isinstance(st, ast.Call) and isinstance(st.func, ast.Name)
                            and st.func.id == "ST"):
                        continue
                    for k in st.keywords:
                        if k.arg == "material" and isinstance(k.value, ast.Constant) \
                                and isinstance(k.value.value, str):
                            v = k.value.value
                            if AUDIO_REF.match(v.strip()):
                                edits.append((off(k.value.lineno, k.value.col_offset),
                                              off(k.value.end_lineno, k.value.end_col_offset),
                                              repr(citation(m))))
                                total["stage"] += 1
                    # teacher lines that describe playing the invented recording
                    for arg in list(st.args) + [k.value for k in st.keywords]:
                        if isinstance(arg, ast.List):
                            for el in arg.elts:
                                if isinstance(el, ast.Constant) and isinstance(el.value, str):
                                    new = rewrite_prose(el.value, m)
                                    if new != el.value:
                                        edits.append((off(el.lineno, el.col_offset),
                                                      off(el.end_lineno, el.end_col_offset),
                                                      repr(new)))
                                        total["prose"] += 1
                        elif isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                            new = rewrite_prose(arg.value, m)
                            if new != arg.value:
                                edits.append((off(arg.lineno, arg.col_offset),
                                              off(arg.end_lineno, arg.end_col_offset),
                                              repr(new)))
                                total["prose"] += 1

        if edits:
            edits.sort(key=lambda e: e[0], reverse=True)
            seen = set()
            for s, e, rep in edits:
                if (s, e) in seen:
                    continue
                seen.add((s, e))
                raw = raw[:s] + rep.encode("utf-8") + raw[e:]
            src = raw.decode("utf-8")
            if "from curriculum.audio_sources import AUDIO" not in src:
                src = src.replace("from curriculum.schema import *",
                                  "from curriculum.schema import *\nfrom curriculum.audio_sources import AUDIO", 1)
            open(path, "w", encoding="utf-8").write(src)
            print(f"  {os.path.basename(path):14} edits={len(seen)}")
    print("totals:", total)


PLAY = re.compile(r'(?:^|(?<=[.;]\s))[^.;]*\bPlay\b[^.;]*(?:[.;]|$)')
# a Play-sentence is about AUDIO only if it also carries one of these cues ...
AUDIO_CUE = re.compile(r'\b(recording|audio|script|conversation|listening|listen|clip|interview|'
                       r'twice|again|third time|three times|two times|caller|dialogue|track)\b', re.I)
# ... and never if it is one of the classroom games that also use the verb "play"
NOT_AUDIO = re.compile(r'\b(bingo|charades|board game|card game|a game|the game|role-?play|'
                       r'guessing game|memory game|dominoes|snap)\b', re.I)


def rewrite_prose(s, m):
    """Replace sentences that describe the OLD invented audio with an accurate
    instruction for the real recording. Classroom games are left alone."""
    if 'Audio ' in s:
        s = re.sub(r'Audio (\d+\.\d+|Test \d)', citation(m), s)

    def repl(mo):
        seg = mo.group(0)
        if NOT_AUDIO.search(seg) or not AUDIO_CUE.search(seg):
            return seg                       # a game, or not about the recording
        tail = '.' if seg.rstrip().endswith('.') else (';' if seg.rstrip().endswith(';') else '')
        if m.get('recycled_from'):
            return (f'Play the lines you have chosen from this unit\u2019s own recordings '
                    f'({", ".join(m["recycled_from"])}); students write them down{tail or "."}')
        return (f'Play the recording \u201c{m["title"]}\u201d twice (three times if the class asks); '
                f'students do the listening tasks{tail or "."}')

    return PLAY.sub(repl, s)


if __name__ == "__main__":
    main()
