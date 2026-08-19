# -*- coding: utf-8 -*-
"""BOOK 3 — Exercise & Practice Book (graded Easy → Medium → Difficult)."""
from generators.common import *
from curriculum import load_units, load_reviews
from curriculum.course import COURSE, ICONS

ORDER = {"E": 0, "M": 1, "D": 2}


def _task(doc, e, default_lines=0):
    rich(doc, [(f"{e.ref}  ", {'b': True, 'c': ORANGE, 'size': 10}),
               (e.title, {'b': True, 'c': NAVY, 'size': 10}),
               (f"   {LEVEL_STAR.get(e.level,'')} {LEVEL_NAME.get(e.level,'')}",
                {'size': 8.5, 'c': GREY})])
    para(doc, e.instruction, italic=True, size=9.5, indent=0.3)
    if e.wordbank:
        box(doc, "", ["   ".join("[ " + w + " ]" for w in e.wordbank)], "vocab", size=9.5)
    for t in e.text:
        para(doc, t, size=9.5, indent=0.5, align="justify")
    for it in e.items:
        para(doc, it, size=9.5, indent=0.6, space_after=3)
    n = e.lines or default_lines
    if n:
        writing_lines(doc, n)
    else:
        writing_lines(doc, 1) if e.kind in ("writing",) else None


def lesson_section(doc, L):
    doc.add_heading(f"{L.code} — {L.lesson_type}: {L.title}", level=2)
    rich(doc, [("Practise after Lesson ", {'i': True, 'size': 9, 'c': GREY}),
               (f"{L.number} of Unit {L.unit}", {'i': True, 'size': 9, 'c': GREY}),
               ("  ·  Answers: Teacher's Answer Key, section " + L.code,
                {'i': True, 'size': 9, 'c': GREY})])

    exs = sorted(L.workbook, key=lambda e: ORDER.get(e.level, 1))
    cur = None
    for e in exs:
        if e.level != cur:
            cur = e.level
            rich(doc, [(f"{LEVEL_STAR.get(cur,'')}  {LEVEL_NAME.get(cur,'')} level",
                        {'b': True, 'c': TEAL, 'size': 10.5})])
        _task(doc, e)

    # Pronunciation practice generated from the lesson focus (always present)
    if L.pron:
        rich(doc, [(f"{L.code}-PRON  Pronunciation practice", {'b': True, 'c': NAVY, 'size': 10}),
                   ("   ★☆☆ Easy", {'size': 8.5, 'c': GREY})])
        para(doc, f"Focus: {L.pron.focus}. Read the words and sentences aloud five times. "
                  f"Tick the box each time. □ □ □ □ □", italic=True, size=9.5, indent=0.3)
        for i in L.pron.items:
            para(doc, "• " + i, size=9.5, indent=0.6, space_after=1)
        for d in L.pron.drill:
            para(doc, "→ " + d, size=9.5, indent=0.6, space_after=1)
    # Speaking prompt (always present)
    if L.communication:
        rich(doc, [(f"{L.code}-SPEAK  Speaking prompt", {'b': True, 'c': NAVY, 'size': 10}),
                   ("   ★★★ Difficult", {'size': 8.5, 'c': GREY})])
        para(doc, L.communication.get("roleplay", ""), italic=True, size=9.5, indent=0.3)
        if L.communication.get("phrases"):
            box(doc, "Use at least three of these", ["   ".join(L.communication["phrases"])],
                "speaking", "💬", size=9.5)
    rule(doc)


def build(path):
    units = load_units()
    reviews = {r.number: r for r in load_reviews()}
    doc = new_doc(COURSE["title"], COURSE["subtitle"], "Book 3 · Exercise & Practice Book", colour=ORANGE)
    add_toc(doc)
    doc.add_heading("How the exercises are graded", level=1)
    table(doc, [
        ["Level", "Symbol", "What it means", "Who should do it"],
        ["Easy", "★☆☆", "One right answer, the model is in front of you", "Everybody"],
        ["Medium", "★★☆", "You must choose and change the language yourself", "Everybody"],
        ["Difficult", "★★★", "You produce your own English; more than one answer is possible",
         "Everybody tries; stronger students finish"],
    ], widths=[2.5, 2.0, 8.0, 4.5])
    bullets(doc, [
        "Do the Easy exercises first — they build the model you need for the harder ones.",
        "Never leave a Difficult exercise empty. Write something, even if you are not sure.",
        "Every lesson ends with a pronunciation drill and a speaking prompt. Say them ALOUD.",
        "Your teacher has the answers in Book 5 (Teacher's Answer Key), under the same reference number.",
    ])
    page_break(doc)
    for u in units:
        doc.add_heading(f"UNIT {u.number}: {u.title.upper()}", level=1)
        for L in u.lessons:
            lesson_section(doc, L)
        if u.number in reviews:
            for L in reviews[u.number].lessons:
                lesson_section(doc, L)
        page_break(doc)
    doc.save(path)
    return path
