# -*- coding: utf-8 -*-
"""BOOK 4 — Homework Book."""
from generators.common import *
from curriculum import load_units, load_reviews
from curriculum.course import COURSE

TIME = {"E": 5, "M": 8, "D": 12}


def _task(doc, e, default_lines=2):
    rich(doc, [(f"{e.ref}  ", {'b': True, 'c': ORANGE, 'size': 10}),
               (e.title, {'b': True, 'c': NAVY, 'size': 10}),
               (f"   ({e.kind}, about {TIME.get(e.level,8)} minutes)", {'size': 8.5, 'c': GREY})])
    para(doc, e.instruction, italic=True, size=9.5, indent=0.3)
    if e.wordbank:
        box(doc, "", ["   ".join("[ " + w + " ]" for w in e.wordbank)], "vocab", size=9.5)
    for t in e.text:
        para(doc, t, size=9.5, indent=0.5, align="justify")
    for it in e.items:
        para(doc, it, size=9.5, indent=0.6, space_after=4)
    writing_lines(doc, e.lines or default_lines)


def lesson_section(doc, L):
    total = sum(TIME.get(h.level, 8) for h in L.homework)
    doc.add_heading(f"Homework {L.code} — {L.lesson_type}: {L.title}", level=2)
    rich(doc, [(f"After period {L.period}", {'i': True, 'size': 9, 'c': GREY}),
               (f"   ·   about {total} minutes in total", {'i': True, 'size': 9, 'c': GREY}),
               ("   ·   Name: ............................  Date: ..................",
                {'size': 9, 'c': GREY})])
    for h in L.homework:
        _task(doc, h)
    box(doc, "Before you close your book", [
        " □ I checked the spelling of every new word.",
        " □ I checked -s after he / she / it.",
        " □ I read my writing aloud once.",
        " □ I said the pronunciation words five times."], "answer", "✔", size=9.5)
    rule(doc)


def build(path):
    units = load_units()
    reviews = {r.number: r for r in load_reviews()}
    doc = new_doc(COURSE["title"], COURSE["subtitle"], "Book 4 · Homework Book", colour=BLUE)
    add_toc(doc)
    doc.add_heading("A word to students and parents", level=1)
    bullets(doc, [
        "Homework in this course is short: 20–35 minutes per lesson, never more.",
        "Every task practises something that was taught in class the same day. There are no surprises.",
        "Every homework set mixes skills: words, grammar, and one task where you write or speak.",
        "After each unit there is a longer Revision Set. Do it before the unit test.",
        "Speaking homework is real homework. Say it aloud — to a mirror, a brother, a phone recording.",
        "If you cannot do a task, write one line saying why. Never leave the page empty.",
    ])
    table(doc, [
        ["Task type", "Time", "How to do it well"],
        ["Vocabulary", "5'", "Write the word, the pronunciation and one example sentence."],
        ["Grammar", "8'", "Write the FULL sentence, not only the missing word."],
        ["Reading", "8'", "Underline the part of the text that gives you the answer."],
        ["Writing", "12'", "Plan first (3 notes), then write, then read it aloud once."],
        ["Speaking", "5'", "Stand up, speak aloud, five times. Silent reading does not count."],
    ], widths=[3.5, 1.8, 11.5])
    page_break(doc)
    for u in units:
        doc.add_heading(f"UNIT {u.number}: {u.title.upper()}", level=1)
        for L in u.lessons:
            lesson_section(doc, L)
        if u.revision:
            doc.add_heading(f"REVISION SET — UNIT {u.number}", level=2)
            para(doc, "Do this set before the unit test. Allow about 45 minutes. "
                      "Mark: 10 points (2 points for each exercise).", italic=True)
            for e in u.revision:
                _task(doc, e)
            rule(doc)
        if u.number in reviews:
            for L in reviews[u.number].lessons:
                lesson_section(doc, L)
        page_break(doc)
    doc.save(path)
    return path
