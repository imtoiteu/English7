# -*- coding: utf-8 -*-
"""Generate curriculum/audio_sources.py from the VERIFIED recording data.

Input : scratchpad/final.json  (page + audio + ffprobe + ASR verification)
        scratchpad/transcripts.json (published transcripts)
        tools/audio_topics.py  (authored gist + focus per session)
Output: curriculum/audio_sources.py   AUDIO = {code: Audio}
"""
import json, os, re, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audio_topics import TOPICS
import audio_tasks as TASKS
from audio_titles import clean as clean_title

SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verification")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "curriculum", "audio_sources.py")

VOA_LICENCE = ("Public domain. Material produced exclusively by VOA is in the public domain: it may be "
               "downloaded, copied, played in class and printed in test papers, with credit to VOA.")
VOA_ATTRIB = "Voice of America — “Let’s Learn English, Level 1” · learningenglish.voanews.com · public domain"
ELLLO_LICENCE = ("© elllo productions. ELLLO allows teachers to download the audio and use it in class or on a "
                 "class LMS. Wider redistribution is not granted, so this book prints a short cited extract only; "
                 "the full script is on the lesson page.")
def elllo_attrib(series):
    return f"elllo.org — {series} · used for classroom teaching · full script and audio on the lesson page"

SERIES = {"SG": "Sound Grammar", "1ME": "One Minute English"}

def mmss(sec):
    sec = int(round(sec)); return f"{sec//60}:{sec%60:02d}"

def speakers_for(rec):
    if rec['kind'] == 'VOA':
        return "American English — VOA’s professional actors (Anna, Pete, Marsha, Ms. Weaver…), slowed learner delivery"
    if rec['kind'] == 'SG':
        return "Two speakers, scripted dialogue, native English"
    sp = rec.get('speaker') or ""
    return f"Single speaker — {sp}" if sp else "Single speaker"

def level_for(rec):
    if rec['kind'] == 'VOA': return "VOA Let’s Learn English, Level 1 (A1–A2)"
    m = re.match(r'^(A1|A2|B1)', rec['title'])
    lv = m.group(1) if m else "A2"
    return f"ELLLO {lv}"

# recordings a Looking Back lesson replays (unit L2 + L3 = the grammar of the unit)
def recycle_pair(unit):
    return [f"U{unit}L2", f"U{unit}L3"]

def excerpt(lines, max_words=90):
    out, n = [], 0
    for l in lines:
        w = len(l.split())
        if n + w > max_words and out: break
        out.append(l); n += w
    return out

def build_teacher_note(rec, code):
    notes = []
    gross = rec.get('wpm_gross') or 0
    if gross >= 135:
        notes.append(f"This is one of the faster recordings ({gross} wpm as heard). Play it three times and "
                     f"pre-teach the key words before the first listening.")
    q = rec.get('parts') or []
    if q and min((p.get('mean_db') or 0) for p in q) <= -29:
        notes.append("The recording is quiet — check the classroom volume before the lesson.")
    if code == "U1L2":
        notes.append("Conversation 4 contains the line “I never drink alcohol” in the grammar examples on the "
                     "source page; the four conversations themselves do not. Nothing needs to be skipped.")
    if code == "U6L1":
        notes.append("Anna misreads “violins” as “violence” — it is a pronunciation joke, not a news story. "
                     "Explain the pun; it is a useful minimal pair for Vietnamese learners.")
    if len(rec.get('parts') or []) > 1:
        notes.append(f"This lesson is {len(rec['parts'])} separate short conversations — play them one at a time.")
    return " ".join(notes)

def main():
    final = {r['key']: r for r in json.load(open(os.path.join(SCRATCH, "final.json")))}
    tx = json.load(open(os.path.join(SCRATCH, "transcripts.json")))
    page_titles = json.load(open(os.path.join(SCRATCH, "titles.json")))
    rows = []
    all_gists = {c: g for c, (g, _) in TOPICS.items()}

    for code in sorted(tx.keys(), key=lambda k: (k.startswith("REV"), k)):
        rec = final.get(code)
        if not rec or rec.get('status') != 'OK':
            continue
        t = tx[code]
        gist, focus = TOPICS[code]
        others = [g for c, g in all_gists.items() if c.split('L')[0] != code.split('L')[0]]
        tasks = TASKS.build(code, t['transcript'], gist, focus, others)
        unit = code.split('L')[0]
        is_voa = rec['kind'] == 'VOA'
        script = t['transcript']          # full transcript; student book prints an extract
        nice = clean_title(rec['kind'], t['title'], page_titles.get(code, ''))
        rows.append(dict(
            code=code, title=nice, kind=rec['kind'],
            source=("VOA Learning English — Let’s Learn English, Level 1" if is_voa
                    else f"ELLLO — {SERIES[rec['kind']]}"),
            source_page=rec['page'],
            audio_urls=[p['url'] for p in rec['parts']],
            licence=VOA_LICENCE if is_voa else ELLLO_LICENCE,
            attribution=VOA_ATTRIB if is_voa else elllo_attrib(SERIES[rec['kind']]),
            speakers=speakers_for({**rec, 'speaker': t.get('speaker', '')}),
            duration=mmss(rec['duration']),
            speech_rate=f"{rec['wpm_gross']} words per minute as heard",
            level=level_for(rec),
            script=script, script_is_excerpt=not is_voa,   # True => students see an extract only
            gist=gist, tasks=tasks,
            teacher_note=build_teacher_note(rec, code),
        ))

    with open(OUT, "w", encoding="utf-8") as f:
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""VERIFIED REAL-HUMAN LISTENING SOURCES — generated by tools/build_audio_sources.py.\n\n'
                'Every recording below was opened, downloaded and machine-checked: true duration and\n'
                'bitrate from ffprobe, loudness from ffmpeg, an independent ASR transcription compared\n'
                'against the published transcript, and the speech rate measured from the audio itself.\n'
                'Do not hand-edit: change tools/audio_topics.py or the mapping and regenerate.\n"""\n')
        f.write('from .schema import A, EX\n\nAUDIO = {}\n\n')
        for r in rows:
            f.write(f"# {'-'*74}\n# {r['code']}  {r['title']}  ({r['duration']}, {r['speech_rate']})\n")
            f.write(f"AUDIO[{r['code']!r}] = A(\n")
            f.write(f"    {r['title']!r},\n")
            ctx = (f"You will hear a real recording: {r['gist']}. "
                   f"{r['speakers']}. It lasts {r['duration']}.")
            f.write(f"    {ctx!r},\n    [\n")
            for line in r['script']:
                f.write(f"        {line!r},\n")
            f.write("    ],\n    tasks=[\n")
            for suf, title, instr, items, answers, level, note in r['tasks']:
                ref = f"{r['code'].replace('U','U').replace('L','.')}-{suf}" if not r['code'].startswith('REV') \
                      else f"{r['code']}-{suf}"
                f.write(f"        EX({ref!r}, {title!r}, {instr!r},\n")
                f.write(f"           items={items!r},\n           answers={answers!r},\n")
                f.write(f"           level={level!r}, kind='listening', note={note!r}),\n")
            f.write("    ],\n")
            for k in ('source', 'source_page', 'licence', 'attribution', 'speakers',
                      'duration', 'speech_rate', 'level'):
                f.write(f"    {k}={r[k]!r},\n")
            f.write(f"    audio_urls={r['audio_urls']!r},\n")
            f.write(f"    script_is_excerpt={r['script_is_excerpt']!r},\n")
            if r['teacher_note']:
                f.write(f"    teacher_note={r['teacher_note']!r},\n")
            f.write(")\n\n")

        # ---- Looking Back sessions: recycle this unit's own recordings ----
        f.write(f"# {'='*74}\n# Looking Back (L7): no new input — the unit's own recordings come back\n\n")
        for u in range(1, 13):
            code = f"U{u}L7"
            pair = recycle_pair(u)
            src = [r for r in rows if r['code'] in pair]
            if not src: continue
            titles = " · ".join(s['title'] for s in src)
            dict_lines = []
            for s in src:
                for l in s['script']:
                    body = re.sub(r"^[A-Z][A-Za-z.'’ ]{0,20}:\s*", "", l).strip()
                    if 5 <= len(body.split()) <= 14 and not body.startswith('…'):
                        dict_lines.append(body)
                    if len(dict_lines) >= 6: break
                if len(dict_lines) >= 6: break
            items = [f"{i}. ____________________" for i in range(1, len(dict_lines) + 1)]
            f.write(f"AUDIO[{code!r}] = A(\n    {'Looking Back — listen again'!r},\n")
            f.write(f"    {('No new recording. You hear this unit’s own recordings again: ' + titles + '.')!r},\n")
            f.write("    [\n")
            for s in src:
                f.write(f"        {('Replay: ' + s['title'] + '  —  ' + s['source_page'])!r},\n")
            f.write("    ],\n    tasks=[\n")
            f.write(f"        EX({f'U{u}.7-L1'!r}, 'Dictation from the unit recordings',\n")
            f.write("           'Your teacher plays six lines from this unit’s recordings. Write each line.',\n")
            f.write(f"           items={items!r},\n           answers={[f'{i}. {l}' for i, l in enumerate(dict_lines, 1)]!r},\n")
            f.write("           level='M', kind='listening',\n")
            f.write("           note='Lines are taken verbatim from the recordings the class already knows.'),\n")
            f.write("    ],\n")
            f.write(f"    source={'Recycled — this unit’s own verified recordings'!r},\n")
            f.write(f"    source_page={src[0]['source_page']!r},\n")
            f.write(f"    audio_urls={[u2 for s in src for u2 in s['audio_urls']]!r},\n")
            f.write(f"    licence={'As for the original recordings (see the lessons they come from).'!r},\n")
            f.write(f"    attribution={' / '.join(s['attribution'] for s in src)!r},\n")
            f.write(f"    speakers={'As in the original recordings'!r},\n")
            f.write(f"    duration={'replayed extracts'!r},\n")
            f.write(f"    recycled_from={pair!r},\n")
            f.write(f"    teacher_note={'Play only the lines you dictate; students have met all of them before.'!r},\n")
            f.write(")\n\n")
    print("wrote", OUT)

if __name__ == "__main__":
    main()
