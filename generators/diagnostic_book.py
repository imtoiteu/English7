# -*- coding: utf-8 -*-
"""BOOK 6 — Diagnostic & Adaptive Teaching System (teacher pack).

Everything the teacher needs to run the diagnostic, read it, and change the
course because of it: administration, full answer keys, rubrics, the scoring
framework, band interpretation, the six-strand profile, the eight triggers,
the decision tree, the bridging lessons, the extension bank and the tracking
grids.

The student-facing papers are Book 7 and carry no answers.
"""
import os
from generators.common import *
from curriculum import load_papers, load_adaptive, load_profile
from curriculum.course import COURSE
from curriculum.rubrics import ALL_RUBRICS
from curriculum.audio_diagnostic import DIAG_AUDIO, DIAG_FILES
from curriculum.diagnostic import PAPER_AUDIO
from curriculum.audio_links import diagnostic_audio, targets

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STRAND_LABEL = {
    "listening": "Listening", "reading": "Reading", "vocab": "Vocabulary",
    "grammar": "Grammar", "writing": "Writing", "speaking": "Speaking",
    "pron": "Pronunciation",
}
STRAND_FILL = {
    "listening": "listening", "reading": "reading", "vocab": "vocab",
    "grammar": "grammar", "writing": "writing", "speaking": "speaking",
    "pron": "pron",
}


# --------------------------------------------------------------------------
# front matter
# --------------------------------------------------------------------------
def front_matter(doc, A):
    doc.add_heading("Why this book exists", level=1)
    para(doc, "The other five books assume every student starts in the same place. No Vietnamese "
              "Grade 7 class does. A typical class of forty-four contains students who never "
              "consolidated the verb 'be' sitting next to students who can already read A2 texts "
              "for meaning. Teaching the same lesson at both of them, for a year, fails both.",
         size=10.5)
    para(doc, "This book turns that problem into a procedure:", size=10.5)
    box(doc, "The loop", [
        "  DIAGNOSE  →  IDENTIFY GAPS  →  ADJUST THE TEACHING  →  TEACH  →  REASSESS  →  ADJUST AGAIN",
        "",
        "  Periods 1–2      Paper A, the initial diagnostic",
        "  After period 2   Checkpoint 0 — provisional bands from the written sections",
        "  After period 9   Checkpoint 1 — full profile, triggers fire, the programme changes",
        "  Period 48        Paper B, mid-year — Checkpoint 2, re-band and re-test every trigger",
        "  Periods 93–94    Paper C, final — Checkpoint 3, growth per strand and the handover",
    ], "objectives", "🔁")
    para(doc, "The 92 teaching sessions are not fixed. They are a starting position. What the "
              "diagnostic finds decides which lessons gain a reinforcement insert, which "
              "prerequisites have to be taught before the unit that assumes them, and which "
              "students spend their independent-practice time on something else entirely.",
         size=10.5)

    doc.add_heading("What is measured, and why those things", level=2)
    table(doc, [
        ["Strand", "Marks (Paper A)", "What a low score here actually means"],
        ["Listening", "12", "The student may know the written word and not its sound. Compare "
         "with reading before concluding anything."],
        ["Reading", "12", "Decoding, or comprehension, or both — the three graded texts separate "
         "them."],
        ["Vocabulary", "10", "Breadth at pre-A1/A1, and whether it reaches past concrete nouns."],
        ["Grammar", "12", "Four constructs Grade 7 assumes on day one: be, third-person -s, "
         "question order, past simple."],
        ["Writing", "14", "Whether the student can operate above the sentence."],
        ["Speaking", "12", "Basic communicative ability — can they start, sustain and respond."],
        ["Pronunciation", "8", "Which of the four documented Vietnamese problems this class has."],
        ["TOTAL", "80", "Bands the student. The strand profile decides what happens to them."],
    ], widths=[3.0, 2.6, 11.4], size=9)

    doc.add_heading("Calibration — why the paper contains easy questions", level=2)
    para(doc, "Roughly 40% of the items are below Grade 7 level, 40% at it, and 20% above. "
              "Teachers sometimes object that a diagnostic should be harder. It should not. A "
              "paper that only discriminates at A2 produces a wall of low scores that all look "
              "the same, and the students whose teaching most needs to change are exactly the "
              "ones it cannot tell apart. The floor items are the ones that generate teaching "
              "decisions.", size=10.5)
    para(doc, "The ceiling items matter for the opposite reason: without them the Extension "
              "group is invisible, and a class where a quarter of the students are already at "
              "the June target is a different teaching problem from one where nobody is.",
         size=10.5)

    doc.add_heading("Pre-flight check — before period 1", level=2)
    para(doc, "Every listening stimulus is a real published recording, downloaded and stored in "
              "the project. None of it is synthetic and none of it is read by the teacher. Check "
              "each file plays, from the back of the room, before the students arrive.",
         size=10.5, italic=True)
    order = [(code, k, f"{code}-L{i}")
             for code, keys in PAPER_AUDIO.items()
             for i, k in enumerate(keys, 1)]
    order += [("—", k, k) for k in ("BRIDGE", "EXT")]
    rows = [["Paper", "Task", "Local file (full name)", "Length", "Speed", "On disk", "Play"]]
    for code, k, task in order:
        a = DIAG_AUDIO[k]
        f = DIAG_FILES[k]
        here = "✔" if os.path.exists(os.path.join(ROOT, f)) else "✖ MISSING"
        rows.append([code, task, os.path.basename(f), a.duration,
                     a.speech_rate.replace(" as heard", ""), here, ""])
    t = table(doc, rows, widths=[1.2, 1.6, 6.4, 1.4, 2.6, 1.4, 2.4], size=8.5)
    for r, (code, k, task) in enumerate(order, start=1):
        audio_links_in_cell(t.cell(r, 6), targets(diagnostic_audio(k), 1),
                            label="▶ Play", size=8.5)
    box(doc, "Licence", [
        DIAG_AUDIO["D1_1"].licence,
        "",
        "Credit line to print on any paper that uses them:",
        "   " + DIAG_AUDIO["D1_1"].attribution,
    ], "note", "©")
    page_break(doc)


# --------------------------------------------------------------------------
# a paper, with the full answer key
# --------------------------------------------------------------------------
def paper_section(doc, P):
    doc.add_heading(f"PAPER {P.code} — {P.name}", level=1)
    rich(doc, [(P.when, {'i': True, 'c': GREY, 'size': 9.5})])
    if P.parallel_to:
        rich(doc, [("Parallel form of Paper ", {'size': 9.5, 'c': GREY}),
                   (P.parallel_to, {'b': True, 'size': 9.5, 'c': GREY}),
                   (" — same sections, same marks, same rubrics.", {'size': 9.5, 'c': GREY})])

    box(doc, "What this paper is for", [f"• {p}" for p in P.purpose], "objectives", "🎯")

    doc.add_heading("Structure", level=2)
    rows = [["Section", "Strand", "Marks", "Minutes", "Period", "Tasks", "Items"]]
    for s in P.sections:
        rows.append([s.code, s.name, f"{s.marks:g}", str(s.minutes), str(s.period),
                     str(len(s.tasks)), str(sum(len(t.items) for t in s.tasks))])
    rows.append(["", "TOTAL", f"{P.total:g}", "", "", "", ""])
    table(doc, rows, widths=[2.2, 3.0, 1.8, 2.0, 1.8, 1.6, 1.6], size=9)

    box(doc, "How to run it", [f"• {a}" for a in P.admin], "note", "⏱")

    for s in P.sections:
        doc.add_heading(f"{s.code}  {s.name}   ({s.marks:g} marks, {s.minutes}′, period {s.period})",
                        level=2)
        if s.reads:
            box(doc, "What this section reads", [s.reads], STRAND_FILL.get(s.strand, "note"), "🔎")
        rich(doc, [("Instruction to students: ", {'b': True, 'size': 9.5}),
                   (s.instruction, {'i': True, 'size': 9.5})])
        if s.admin:
            doc.add_heading("Administration", level=4)
            bullets(doc, s.admin, size=9.5)

        for t in s.tasks:
            doc.add_heading(f"{t.code}  {t.title}   [{t.marks:g} marks · {t.band or s.strand}]",
                            level=3)
            rich(doc, [(t.instruction, {'i': True, 'size': 9.5})])

            if t.audio_key:
                a = DIAG_AUDIO[t.audio_key]
                lines = [f"Recording: {a.title}",
                         f"File: {DIAG_FILES[t.audio_key]}",
                         f"Length {a.duration} · {a.speech_rate} · {a.level}",
                         f"Plays: {t.plays}"]
                if t.excerpt:
                    lines.append("EXCERPT — " + t.excerpt)
                lines.append(f"Source: {a.source_page}")
                bx = box(doc, "Audio", lines, "listening", "🎧", size=9)
                audio_links_in_cell(bx.cell(0, 0),
                                    targets(diagnostic_audio(t.audio_key), 1),
                                    label="▶ Play audio", size=9.5)
                doc.add_heading("Transcript (published by the source — do NOT give to students "
                                "before the second play)", level=4)
                for ln in a.script:
                    para(doc, ln, size=8.5, indent=0.4, space_after=1, color=GREY)

            if t.text:
                if t.text_title:
                    para(doc, t.text_title, bold=True, size=10, color=NAVY, indent=0.2)
                for ln in t.text:
                    para(doc, ln if ln else " ", size=9.5, indent=0.4, space_after=2)
            if t.wordbank:
                box(doc, "Word box", ["   ".join(t.wordbank)], "vocab", "📕", size=9.5)

            doc.add_heading("Answer key", level=4)
            if t.rubric:
                box(doc, f"Marked with the {t.rubric} rubric",
                    [t.items[0].answer,
                     "Criterion descriptors are printed in full later in this book."],
                    "answer", "📊", size=9.5)
                if t.note:
                    rich(doc, [("Diagnostic note: ", {'b': True, 'c': TEAL, 'size': 9}),
                               (t.note, {'i': True, 'size': 9})], indent=0.4)
                continue

            rows = [["#", "Question", "Answer", "Mk", "Band", "Tests"]]
            for it in t.items:
                q = it.prompt
                if it.options:
                    q += "   " + "  ".join(it.options)
                rows.append([it.n, q, it.answer, f"{it.marks:g}", it.band, it.tests])
            table(doc, rows, widths=[0.8, 5.6, 4.6, 0.9, 1.4, 3.5], size=8.5)
            for it in t.items:
                if it.note:
                    rich(doc, [(f"Item {it.n} — ", {'b': True, 'c': ORANGE, 'size': 8.5}),
                               (it.note, {'i': True, 'size': 8.5})], indent=0.4)
            if t.note:
                rich(doc, [("Task note: ", {'b': True, 'c': TEAL, 'size': 9}),
                           (t.note, {'i': True, 'size': 9})], indent=0.4)
        rule(doc)
    page_break(doc)


# --------------------------------------------------------------------------
# rubrics
# --------------------------------------------------------------------------
def rubrics_section(doc):
    doc.add_heading("MARKING RUBRICS", level=1)
    para(doc, "The same three rubrics mark Paper A, Paper B and Paper C. That is deliberate: if "
              "the instrument changes between September and May, the comparison is worthless.",
         italic=True, size=10)
    for R in ALL_RUBRICS:
        doc.add_heading(f"{R.name} — {R.total:g} marks", level=2)
        if R.counted != R.total:
            para(doc, f"WARNING: criteria sum to {R.counted:g}, not {R.total:g}.",
                 bold=True, color=RED)
        for c in R.criteria:
            doc.add_heading(f"{c.name}   ({c.max:g} marks)", level=3)
            rows = [["Marks", "The student…"]] + [[d[0], d[1]] for d in c.descriptors]
            table(doc, rows, widths=[1.6, 15.4], size=9)
            if c.vn_note:
                box(doc, "Vietnamese learners", [c.vn_note], "warn", "⚠", size=9)
        if R.how_to_use:
            box(doc, "How to mark it", [f"• {h}" for h in R.how_to_use], "note", "✍", size=9.5)
        if R.diagnostic_use:
            box(doc, "Reading it diagnostically", [f"• {d}" for d in R.diagnostic_use],
                "answer", "🔎", size=9.5)
        rule(doc)
    page_break(doc)


# --------------------------------------------------------------------------
# scoring framework and interpretation
# --------------------------------------------------------------------------
def scoring_section(doc, AD, A):
    doc.add_heading("SCORING FRAMEWORK", level=1)
    para(doc, "Mark the paper. Then do three things with the marks, in this order: record them "
              "per strand as percentages, band each student on the total, and flag the gaps. "
              "Skipping the third step is how a diagnostic turns back into a test.", size=10.5)

    doc.add_heading("1 · The class record sheet", level=2)
    para(doc, "One row per student. Percentages, not raw marks — that is what makes September, "
              "January and May comparable when the papers have different totals.", size=10)
    rows = [["Student", "L /12", "R /12", "V /10", "G /12", "W /14", "S /12", "P /8",
             "TOTAL /80", "%", "Band", "Flags"]]
    for i in range(1, 6):
        rows.append([f"{i}.", "", "", "", "", "", "", "", "", "", "", ""])
    rows.append(["…", "", "", "", "", "", "", "", "", "", "", ""])
    rows.append(["CLASS MEAN %", "", "", "", "", "", "", "", "", "", "", ""])
    table(doc, rows, widths=[3.0, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.7, 1.1, 1.6, 1.3], size=8)

    doc.add_heading("2 · The six numbers that decide triggers T1 and T5", level=2)
    para(doc, "These are item-level class percentages — the share of the class that got the item "
              "right. Six numbers, and they carry two of the eight triggers between them. Compute "
              "them; do not estimate them.", size=10)
    table(doc, [
        ["Item", "What it tests", "Feeds", "% correct"],
        ["A-G3.1", "past simple, regular -ed", "T1", ""],
        ["A-G3.2", "past simple, irregular", "T1", ""],
        ["A-L3.2", "past simple heard in real speech", "T1", ""],
        ["A-G1.3", "third-person -s", "T5", ""],
        ["A-G1.4", "does + base form", "T5", ""],
        ["A-V2.5", "third-person -s in a vocabulary frame", "T5", ""],
    ], widths=[2.2, 7.6, 2.0, 5.2], size=9)

    doc.add_heading("3 · The speaking and pronunciation tracking grid", level=2)
    para(doc, "Rolling assessment needs a grid or students get missed. Twenty-two pairs at three "
              "minutes is sixty-six minutes; about six pairs fit in period 2 and the rest happen "
              "in three-minute slots during U1L1–U1L7. Tick as you go.", size=10)
    rows = [["Pair", "Student A", "Student B", "Date", "Read-aloud /8 A", "B",
             "Speaking /12 A", "B", "Done"]]
    for i in range(1, 8):
        rows.append([str(i), "", "", "", "", "", "", "", "☐"])
    rows.append(["…", "", "", "", "", "", "", "", "☐"])
    table(doc, rows, widths=[1.2, 3.0, 3.0, 1.8, 2.2, 1.0, 2.2, 1.0, 1.2], size=8.5)
    box(doc, "Deadline", [
        "Every student assessed by the end of period 9. Checkpoint 1 cannot happen without it, "
        "and Checkpoint 1 is where the course actually changes."], "warn", "⏳")
    page_break(doc)

    # ---- bands ----
    doc.add_heading("LEVEL INTERPRETATION — the three bands", level=1)
    table(doc, [["Band", "Marks /80", "Percentage"]] +
          [[b.name, f"{b.lo:g}–{b.hi:g}",
            "under 45%" if b.key == "foundation" else ("45–69%" if b.key == "core" else "70%+")]
           for b in AD.BANDS], widths=[9.0, 4.0, 4.0], size=9.5)
    para(doc, "Paper B is out of 46 and uses the same percentage cut-offs.", italic=True, size=9)

    for b in AD.BANDS:
        doc.add_heading(b.name, level=2)
        para(doc, b.meaning, size=10)
        box(doc, "What it looks like on the paper", [f"• {x}" for x in b.looks_like],
            "note", "👁", size=9.5)
        box(doc, "What this group gets", [f"• {x}" for x in b.programme],
            "objectives", "📚", size=9.5)
        box(doc, "What NOT to do", [f"• {x}" for x in b.never], "warn", "⛔", size=9.5)
        rule(doc)
    page_break(doc)

    # ---- gap rule ----
    doc.add_heading("THE RELATIVE-GAP RULE — why the total is not enough", level=1)
    box(doc, "The rule", [AD.GAP_RULE["rule"]], "grammar", "📐")
    for line in AD.GAP_RULE["why"]:
        para(doc, line, size=10, indent=0.3)
    box(doc, "Acting on a flag", [f"• {x}" for x in AD.GAP_RULE["act_on_it"]], "answer", "→", size=9.5)
    box(doc, "Caution", [AD.GAP_RULE["caution"]], "warn", "⚠", size=9.5)

    doc.add_heading("The six-strand profile card", level=2)
    para(doc, "One per student, handed over at Checkpoint 1. Name one strength before one target, "
              "in that order, and never read marks aloud to the class.", size=10)
    table(doc, [
        ["", "Listening", "Reading", "Vocabulary", "Grammar", "Writing", "Speaking"],
        ["Score", "/12", "/12", "/10", "/12", "/14", "/12"],
        ["%", "", "", "", "", "", ""],
        ["Flag?", "", "", "", "", "", ""],
    ], widths=[2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.6], size=9)
    table(doc, [
        ["Pronunciation", "Final consonants /2", "Word stress /2", "/θ ð ʃ ʒ v z/ /2",
         "Intelligibility /2"],
        ["", "", "", "", ""],
    ], widths=[3.4, 3.4, 3.0, 3.4, 3.4], size=9)
    table(doc, [
        ["Band", ""],
        ["One thing you are already good at", ""],
        ["One thing we will work on", ""],
        ["We check again in", "January (Paper B)"],
    ], widths=[6.0, 11.0], size=9.5)
    page_break(doc)


# --------------------------------------------------------------------------
# triggers, decision tree, checkpoints
# --------------------------------------------------------------------------
def triggers_section(doc, AD):
    doc.add_heading("DIAGNOSTIC OUTCOMES THAT CHANGE THE PROGRAMME", level=1)
    para(doc, "Eight class-level results. Each one names a threshold, the evidence it is computed "
              "from, and the specific lessons that change. A trigger you decide has fired because "
              "the class 'feels weak' is not a trigger; it is a mood. Compute them.",
         size=10.5, italic=True)

    table(doc, [["#", "Trigger", "Fires when"]] +
          [[t.code, t.name, t.fires_when] for t in AD.TRIGGERS],
          widths=[1.2, 5.4, 10.4], size=9)
    page_break(doc)

    for t in AD.TRIGGERS:
        doc.add_heading(f"{t.code} — {t.name}", level=2)
        box(doc, "Fires when", [t.fires_when], "warn", "⚡", size=9.5)
        rich(doc, [("Evidence: ", {'b': True, 'c': TEAL, 'size': 9.5}), (t.evidence, {'size': 9.5})])
        para(doc, t.interpretation, size=10, indent=0.2)
        doc.add_heading("What changes in the programme", level=4)
        bullets(doc, t.changes, size=9.5)
        if t.affects:
            rich(doc, [("Lessons affected: ", {'b': True, 'size': 9}),
                       ("; ".join(t.affects), {'size': 9, 'c': GREY})])
        if t.resources:
            rich(doc, [("Resources: ", {'b': True, 'size': 9}),
                       ("; ".join(t.resources), {'size': 9, 'c': GREY})])
        if t.retire_when:
            box(doc, "Retire it when", [t.retire_when], "answer", "✔", size=9.5)
        rule(doc)
    page_break(doc)

    doc.add_heading("THE DECISION TREE", level=1)
    para(doc, "Work through it in this order, once, at Checkpoint 1. Then teach, and do not "
              "re-plan continuously — the next scheduled change is January.", italic=True, size=10)
    for step, details in AD.DECISION_TREE:
        doc.add_heading(step, level=3)
        bullets(doc, details, size=9.5)
    page_break(doc)

    doc.add_heading("CHECKPOINTS", level=1)
    for name, when, what, actions in AD.CHECKPOINTS:
        doc.add_heading(f"{name} — {when}", level=2)
        para(doc, what, italic=True, size=10, color=TEAL)
        bullets(doc, actions, size=9.5)
    rule(doc)
    page_break(doc)


# --------------------------------------------------------------------------
# bridging and extension
# --------------------------------------------------------------------------
def bridging_section(doc, AD):
    doc.add_heading("BRIDGING LESSONS — for the Foundation band", level=1)
    para(doc, "Six lessons covering the Grade 5–6 prerequisites that Grade 7 silently assumes. "
              "Each is a full 45 minutes, and each also works as two 20-minute warm-up inserts.",
         size=10.5)
    doc.add_heading("How to deliver them depends on how big the group is", level=2)
    for condition, mode, note in AD.BRIDGE_DELIVERY:
        box(doc, condition, [mode, "", note], "objectives", "→", size=9.5)

    table(doc, [["Code", "Lesson", "Prerequisite for"]] +
          [[b.code, b.title, b.prerequisite_for] for b in AD.BRIDGES],
          widths=[1.4, 7.4, 8.2], size=9)
    page_break(doc)

    for b in AD.BRIDGES:
        doc.add_heading(f"{b.code} — {b.title}", level=2)
        rich(doc, [(f"{b.minutes} minutes  ·  prerequisite for {b.prerequisite_for}",
                    {'i': True, 'c': GREY, 'size': 9})])
        box(doc, "Why this lesson exists", [b.why], "warn", "⚠", size=9.5)
        box(doc, "By the end students can", [f"• {o}" for o in b.objectives],
            "objectives", "🎯", size=9.5)
        doc.add_heading("Language content", level=4)
        bullets(doc, b.content, size=9.5)
        doc.add_heading("Procedure", level=4)
        rows = [["Stage", "Min", "Teacher", "Students", "Mode"]]
        for st in b.procedure:
            rows.append([st.name, str(st.minutes), " ".join(st.teacher), st.students, st.mode])
        table(doc, rows, widths=[2.8, 1.0, 7.4, 3.2, 2.6], size=8.5)
        doc.add_heading("Exercises", level=4)
        for e in b.exercises:
            rich(doc, [(f"{e.ref}  ", {'b': True, 'c': ORANGE, 'size': 9.5}),
                       (e.title, {'b': True, 'size': 9.5}),
                       (f"   [{LEVEL_STAR.get(e.level, '')}]", {'size': 8.5, 'c': GREY})])
            para(doc, e.instruction, italic=True, size=9, indent=0.3)
            if e.wordbank:
                para(doc, "Word box:  " + "   ".join(e.wordbank), size=9, indent=0.3, color=NAVY)
            for it in e.items:
                para(doc, it, size=9, indent=0.6, space_after=1)
            for a in e.answers:
                para(doc, "✔ " + a, size=9, indent=0.6, space_after=1, color=TEAL)
            if e.note:
                rich(doc, [("Note: ", {'b': True, 'c': TEAL, 'size': 8.5}),
                           (e.note, {'i': True, 'size': 8.5})], indent=0.6)
        box(doc, "Exit check", [b.success], "answer", "✔", size=9.5)
        rule(doc)
        page_break(doc)


def extension_section(doc, AD):
    doc.add_heading("EXTENSION BANK — for the Extension band", level=1)
    box(doc, "The design rule", [f"• {r}" for r in AD.EXTENSION_RULES], "warn", "⛔")
    table(doc, [["Code", "Activity", "Units", "Output"]] +
          [[e.code, e.title, e.units, e.output] for e in AD.EXTENSIONS],
          widths=[1.4, 5.0, 1.6, 9.0], size=9)
    page_break(doc)

    for e in AD.EXTENSIONS:
        doc.add_heading(f"{e.code} — {e.title}   (Units {e.units})", level=2)
        box(doc, "What extra demand this adds", [e.demand], "objectives", "🚀", size=9.5)
        doc.add_heading("Steps", level=4)
        numbered(doc, e.steps, size=9.5)
        rich(doc, [("Output: ", {'b': True, 'c': TEAL, 'size': 9.5}), (e.output, {'size': 9.5})])
        rich(doc, [("Assessment: ", {'b': True, 'c': TEAL, 'size': 9.5}), (e.assess, {'size': 9.5})])
        if e.resources:
            rich(doc, [("Use with: ", {'b': True, 'size': 9}),
                       ("; ".join(e.resources), {'size': 9, 'c': GREY})])
        if e.minutes:
            rich(doc, [("Time: ", {'b': True, 'size': 9}), (e.minutes, {'size': 9, 'c': GREY})])
        rule(doc)
    page_break(doc)


# --------------------------------------------------------------------------
# this class
# --------------------------------------------------------------------------
def this_class_section(doc, AD, CP):
    doc.add_heading("THIS CLASS", level=1)
    if CP is None:
        para(doc, "No class profile module found.", italic=True)
        return
    para(doc, CP.summary(), size=10.5)
    if not CP.DIAGNOSED:
        box(doc, "Not diagnosed yet", [
            "Everything in this book so far describes what COULD change. Nothing has, because "
            "this class has not been tested.",
            "",
            "1. Teach periods 1–2 (Paper A). 2. Mark it. 3. Fill in curriculum/class_profile.py "
            "at Checkpoint 1. 4. Run python3 build.py. 5. Teach from the rebuilt books.",
            "",
            "After that, this page prints the fired triggers, the bridging mode and the resulting "
            "teaching plan for THIS class, and the Teacher's Coursebook grows an ADAPTIVE INSERT "
            "box in every lesson a trigger names.",
        ], "note", "📋")
        return

    fired = CP.active_triggers()
    _, reasons, undecidable = CP.evaluate_triggers()
    table(doc, [["", "Value"],
                ["Class", CP.CLASS_NAME or "—"],
                ["Year", CP.SCHOOL_YEAR or "—"],
                ["Students", str(CP.STUDENTS or "—")],
                ["Checkpoint", CP.CHECKPOINT or "—"],
                ["Date", CP.DATE or "—"]], widths=[4.0, 13.0], size=9.5)

    doc.add_heading("Strand profile", level=2)
    rows = [["Strand"] + [STRAND_LABEL[k] for k in CP.STRANDS]]
    rows.append(["Class mean %"] + [("—" if v is None else f"{v}%") for v in CP.STRANDS.values()])
    table(doc, rows, widths=None, size=9)

    doc.add_heading("Bands", level=2)
    table(doc, [["Band", "Students"]] +
          [[AD.BANDS_BY_KEY[k].name, str(v if v is not None else "—")]
           for k, v in CP.BANDS.items()], widths=[10.0, 7.0], size=9.5)

    doc.add_heading("Triggers", level=2)
    if fired:
        rows = [["#", "Trigger", "Why it fired"]]
        for c in fired:
            t = AD.TRIGGERS_BY_CODE.get(c)
            rows.append([c, t.name if t else "—", reasons.get(c, "")])
        table(doc, rows, widths=[1.2, 5.4, 10.4], size=9)
    else:
        para(doc, "No triggers fired. The course runs as written.", italic=True)
    if undecidable:
        box(doc, "Cannot be decided yet — evidence not entered",
            [", ".join(undecidable),
             "These are not 'did not fire'. They are questions you have not answered."],
            "warn", "?", size=9.5)

    doc.add_heading("The teaching plan that follows from this", level=2)
    mode = CP.bridge_mode()
    if mode:
        label = {"pre-course": "B1–B6 as a pre-course block, before Unit 1",
                 "warm-up": "B1–B6 as whole-class warm-up inserts inside Units 1–3",
                 "homework": "Targeted bridging homework plus a weekly ten-minute clinic"}
        box(doc, "Bridging delivery", [label.get(mode, mode),
                                       CP.BRIDGE_NOTE or ""], "objectives", "🧱", size=9.5)
    for c in fired:
        t = AD.TRIGGERS_BY_CODE.get(c)
        if not t:
            continue
        doc.add_heading(f"{t.code} — {t.name}", level=3)
        bullets(doc, t.changes, size=9.5)
    page_break(doc)


def limits_section(doc, AD):
    doc.add_heading("WHAT THIS SYSTEM WILL NOT DO", level=1)
    para(doc, "An instrument that claims more than it can support does damage. These are the "
              "limits, and they belong in the same book as the claims.", italic=True, size=10)
    bullets(doc, AD.LIMITS, size=10)
    rule(doc)


# --------------------------------------------------------------------------
def build(path):
    papers = load_papers()
    AD = load_adaptive()
    CP = load_profile()
    A = papers[0] if papers else None

    doc = new_doc(COURSE["title"], COURSE["subtitle"],
                  "Book 6 · Diagnostic & Adaptive Teaching System", colour=ORANGE)
    add_toc(doc)
    front_matter(doc, A)
    for P in papers:
        paper_section(doc, P)
    rubrics_section(doc)
    scoring_section(doc, AD, A)
    triggers_section(doc, AD)
    bridging_section(doc, AD)
    extension_section(doc, AD)
    this_class_section(doc, AD, CP)
    limits_section(doc, AD)
    doc.save(path)
    return path
