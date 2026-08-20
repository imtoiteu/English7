# -*- coding: utf-8 -*-
"""BOOK 7 — Diagnostic Test Papers (photocopiable, student-facing).

Papers A, B and C exactly as the students see them: no answers, no marking
notes, no difficulty bands, no transcripts. Everything a student must not see
lives in Book 6.

Each paper is followed by the cards that are handed to the pairs, which are
identical in September, January and May — an instrument that changes cannot
measure change.
"""
from generators.common import *
from curriculum import load_papers
from curriculum.course import COURSE

SPEAKING_STRANDS = ("speaking", "pron")


def teacher_note(doc):
    doc.add_heading("Before you photocopy", level=1)
    bullets(doc, [
        "This book contains ONLY the student papers. Answers, marking notes, transcripts and "
        "the difficulty band of every item are in Book 6 — do not photocopy from that one.",
        "Paper A: copy Sections 1–4 for period 1 and Section 5 for period 2, as separate sheets. "
        "Students must not see the writing task while they are doing the listening.",
        "Paper B: one sheet, all five sections, for period 48.",
        "Paper C: Section 5 for period 93, Sections 1–4 for period 94.",
        "The speaking card and the read-aloud card at the end of Paper A are used again in "
        "January and May. Laminate them if you can — they are handled by every student three "
        "times.",
        "The read-aloud card is IDENTICAL in all three papers. Do not improve it, do not "
        "modernise it, do not swap a word.",
        "Print the audio credit line at the foot of the listening page. VOA material is public "
        "domain and may be printed in a test paper with credit.",
    ])
    box(doc, "To the student, printed at the top of every paper", [
        "This is not a test. Nothing here goes in your report.",
        "Some questions will be easy and some will be too hard. That is on purpose.",
        "Never leave a blank. Guess."], "objectives", "📝")
    page_break(doc)


def _answer_space(doc, item, size=10):
    """Blank space sized to the kind of answer expected."""
    ans = item.answer or ""
    long = len(ans) > 60 or "sentence" in (item.tests or "").lower()
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.9)
    p.paragraph_format.space_after = Pt(6 if long else 4)
    r = p.add_run("." * (100 if long else 62))
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor(0xAA, 0xAA, 0xAA)
    if long:
        writing_lines(doc, 1, indent=0.9)


def paper(doc, P):
    doc.add_heading(f"PAPER {P.code} — {P.name}", level=1)
    rich(doc, [(P.when, {'i': True, 'c': GREY, 'size': 9.5})])
    table(doc, [["Name", "", "Class", "", "Date", ""]],
          header=False, widths=[1.8, 5.4, 1.6, 3.0, 1.5, 3.7], size=10)
    box(doc, "", [
        "This is not a test. Nothing here goes in your report.",
        "Some questions will be easy and some will be too hard — that is on purpose.",
        "Never leave a blank. Guess."], "objectives", "", size=9.5)

    rows = [["Section", "", "Marks", "Time"]]
    for s in P.sections:
        rows.append([s.code.split("-")[-1], s.name, f"{s.marks:g}", f"{s.minutes}′"])
    rows.append(["", "TOTAL", f"{P.total:g}", ""])
    table(doc, rows, widths=[2.0, 8.0, 3.4, 3.6], size=9.5)
    page_break(doc)

    for s in P.sections:
        if s.strand in SPEAKING_STRANDS:
            continue
        doc.add_heading(f"Section {s.code.split('-')[-1][1:]} — {s.name}"
                        f"   ({s.marks:g} marks, {s.minutes} minutes)", level=2)
        para(doc, s.instruction, italic=True, size=10)

        for t in s.tasks:
            doc.add_heading(f"{t.code}   {t.title}   [{t.marks:g} marks]", level=3)
            para(doc, t.instruction, size=10, italic=True)

            if t.audio_key:
                para(doc, "🎧  You will hear this recording " +
                     ("twice." if t.plays == 2 else f"{t.plays} times."),
                     size=9.5, color=BLUE, indent=0.2)

            if t.text:
                if t.text_title:
                    para(doc, t.text_title, bold=True, size=10.5, color=NAVY, indent=0.2)
                for ln in t.text:
                    para(doc, ln if ln else " ", size=10, indent=0.4, space_after=2)
            if t.wordbank:
                box(doc, "", ["   ·   ".join(t.wordbank)], "vocab", "", size=10)

            if t.rubric:
                if t.lines:
                    writing_lines(doc, t.lines, indent=0.5)
                continue

            for it in t.items:
                rich(doc, [(f"{it.n}. ", {'b': True, 'size': 10}), (it.prompt, {'size': 10})],
                     indent=0.2)
                if it.options:
                    for o in it.options:
                        para(doc, "     " + o, size=10, indent=0.5, space_after=1)
                    para(doc, "     Answer: ..........", size=10, indent=0.5)
                else:
                    _answer_space(doc, it)
            rule(doc)

        if s.strand == "listening":
            para(doc, "Audio: Voice of America — “Let’s Learn English, Level 1” · "
                      "learningenglish.voanews.com · public domain.",
                 size=7.5, color=GREY, italic=True)
        page_break(doc)

    # ---- the cards ----
    oral = [s for s in P.sections if s.strand in SPEAKING_STRANDS]
    for s in oral:
        for t in s.tasks:
            doc.add_heading(f"CARD — {t.title}   (Paper {P.code}, {s.name})", level=2)
            para(doc, t.instruction, italic=True, size=10)
            box(doc, "", [ln if ln else " " for ln in t.text], "speaking", "", size=10)
    page_break(doc)


def build(path):
    doc = new_doc(COURSE["title"], COURSE["subtitle"],
                  "Book 7 · Diagnostic Test Papers", colour=NAVY)
    add_toc(doc)
    teacher_note(doc)
    for P in load_papers():
        paper(doc, P)
    doc.save(path)
    return path
