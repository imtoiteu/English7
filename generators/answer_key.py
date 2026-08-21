# -*- coding: utf-8 -*-
"""BOOK 5 — Teacher's Answer Key."""
from generators.common import *
from curriculum import load_units, load_reviews
from curriculum.audio_links import lesson_audio, link_set
from curriculum.course import COURSE

KIND_LABEL = {"vocab": "Vocabulary", "grammar": "Grammar", "pron": "Pronunciation",
              "reading": "Reading", "listening": "Listening", "speaking": "Speaking (suggested answer)",
              "writing": "Writing (model answer)", "mixed": "Mixed skills"}


def _answer_block(doc, e, source):
    rich(doc, [(f"{e.ref}  ", {'b': True, 'c': ORANGE, 'size': 10}),
               (e.title, {'b': True, 'c': NAVY, 'size': 10}),
               (f"   [{source} · {KIND_LABEL.get(e.kind, e.kind)} · {LEVEL_NAME.get(e.level,'')}]",
                {'size': 8.5, 'c': GREY, 'i': True})])
    if not e.answers:
        para(doc, "Students' own answers — accept any answer that uses the target language correctly.",
             italic=True, size=9.5, indent=0.4)
    for a in e.answers:
        para(doc, "✔ " + a, size=9.5, indent=0.4, space_after=1)
    if e.note:
        rich(doc, [("Explanation: ", {'b': True, 'c': TEAL, 'size': 9}), (e.note, {'i': True, 'size': 9})],
             indent=0.4)


def lesson_section(doc, L):
    doc.add_heading(f"{L.code} — {L.lesson_type}: {L.title}", level=2)
    rich(doc, [(f"Student Coursebook & Practice Book, Unit {L.unit} Lesson {L.number}; "
                f"Homework Book {L.code}", {'i': True, 'size': 9, 'c': GREY})])
    groups = [("Student Book – Practice", L.guided),
              ("Student Book – Now you try", L.independent),
              ("Student Book – Speaking", L.speaking),
              ("Student Book – Writing", L.writing),
              ("Student Book – Reading", L.reading.tasks if L.reading else []),
              ("Student Book – Listening", L.listening.tasks if L.listening else []),
              ("Practice Book", L.workbook),
              ("Homework Book", L.homework)]
    seen = set()
    for name, group in groups:
        first = True
        for e in group:
            if e.ref in seen:
                continue
            seen.add(e.ref)
            if first:
                doc.add_heading(name, level=4)
                first = False
            _answer_block(doc, e, name)
    if L.listening:
        pairs = lesson_audio(L.code)
        if pairs:
            loc, onl = link_set(pairs, 1)
            audio_links(doc, loc, onl, label="▶ Play audio", size=9,
                        intro="To check a listening answer, replay it:")
    if L.pron:
        doc.add_heading("Pronunciation drill (Practice Book, " + L.code + "-PRON)", level=4)
        para(doc, "Listen for: " + L.pron.focus + ". " + L.pron.tip, size=9.5, indent=0.4)
        para(doc, "Common Vietnamese-learner problem: " + (L.pron.vn_note or "—"),
             size=9.5, indent=0.4, italic=True)
    rule(doc)


def build(path):
    units = load_units()
    reviews = {r.number: r for r in load_reviews()}
    doc = new_doc(COURSE["title"], COURSE["subtitle"], "Book 5 · Teacher's Answer Key", colour=RED)
    add_toc(doc)
    doc.add_heading("How to use the Answer Key", level=1)
    bullets(doc, [
        "Every exercise in the course has a unique reference (for example U1.3-P4). "
        "The same reference is used in the Student Book, the Practice Book, the Homework Book "
        "and here — so you can find any answer in seconds.",
        "Objective exercises (matching, gap-fill, multiple choice, transformation) have exact answers.",
        "Writing tasks have a MODEL answer. It shows the expected length and structures; "
        "accept any answer of the same quality.",
        "Speaking tasks have a SUGGESTED answer. Use it as a model for the class, not as the only "
        "correct version.",
        "Where an exercise contains a well-known Vietnamese-learner error, an Explanation line tells "
        "you what to say.",
    ])
    box(doc, "Marking guide for productive work", [
        " Writing (10): content 4 · organisation 2 · grammar 2 · vocabulary 1 · spelling & neatness 1",
        " Speaking (10): task completion 3 · fluency 2.5 · pronunciation 2.5 · accuracy 2",
        " Project (10): content 3 · language 3 · design 2 · presentation 2"], "answer", "📊")
    page_break(doc)
    for u in units:
        doc.add_heading(f"UNIT {u.number}: {u.title.upper()}", level=1)
        for L in u.lessons:
            lesson_section(doc, L)
        if u.revision:
            doc.add_heading(f"Revision Set — Unit {u.number} (Homework Book)", level=2)
            for e in u.revision:
                _answer_block(doc, e, "Revision Set")
            rule(doc)
        if u.number in reviews:
            for L in reviews[u.number].lessons:
                lesson_section(doc, L)
        page_break(doc)
    doc.save(path)
    return path
