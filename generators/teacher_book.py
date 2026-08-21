# -*- coding: utf-8 -*-
"""BOOK 1 — Teacher's Coursebook / Teaching Guide."""
from generators.common import *
from curriculum import (load_units, load_reviews, load_diagnostic, load_adaptive,
                        load_profile)
from curriculum.audio_links import lesson_audio, diagnostic_audio, link_set
from curriculum.course import (COURSE, PHILOSOPHY, VN_DIFFICULTIES, CLASSROOM_ROUTINES,
                               ASSESSMENT, ICONS)


def front_matter(doc, units):
    doc.add_heading("How to use this teaching system", level=1)
    para(doc, "This course is a complete teaching system for one school year. Seven books and a "
              "deck per session work together, every page is cross-referenced, and the whole set "
              "adapts to what the diagnostic finds about your class.")
    table(doc, [
        ["Book", "Who uses it", "What it contains"],
        ["1. Teacher's Coursebook", "Teacher", "Full lesson plans, procedures, timing, teacher language, "
         "differentiation, assessment"],
        ["2. Student Coursebook", "Student, in class", "Explanations, vocabulary, grammar, texts, "
         "listening scripts, tasks, review"],
        ["3. Exercise & Practice Book", "Student, in class / at home", "Graded practice: Easy → Medium → "
         "Difficult for every lesson"],
        ["4. Homework Book", "Student, at home", "Homework for every lesson + revision sets after each unit"],
        ["5. Teacher's Answer Key", "Teacher", "Every answer, model writing, suggested speaking answers"],
        ["6. Diagnostic & Adaptive System", "Teacher", "Papers A/B/C with answer keys, rubrics, "
         "bands, triggers, decision tree, bridging lessons, extension bank"],
        ["7. Diagnostic Test Papers", "Student", "The three papers as students see them — "
         "no answers, photocopiable"],
        ["Teaching Slides (PPTX)", "Teacher, in class", "One deck per taught session, built from "
         "these plans"],
    ], widths=[4.5, 3.5, 9.0])

    doc.add_heading("The teaching principles behind every lesson", level=2)
    bullets(doc, PHILOSOPHY)

    doc.add_heading("The shape of a 45-minute lesson", level=2)
    table(doc, [
        ["Stage", "Time", "Purpose"],
        ["Warm-up / recycling", "5'", "Bring back the language of the last lesson through a game"],
        ["Presentation", "8–10'", "Meaning first, then form, then pronunciation"],
        ["Guided practice", "8–10'", "Controlled, everyone can succeed, mistakes corrected at once"],
        ["Independent practice", "8–10'", "Students choose their own words inside a safe structure"],
        ["Communication", "8–10'", "Real speaking or writing; fluency, not accuracy"],
        ["Wrap-up + homework", "4–5'", "Consolidate, correct 2 errors, set homework"],
    ], widths=[5.0, 2.0, 10.0])

    doc.add_heading("Vietnamese learners: the eight difficulties this course attacks", level=2)
    para(doc, "Every difficulty below is addressed by a named routine that comes back in every unit.", italic=True)
    rows = [["Difficulty", "What you will hear in class", "What to do"]]
    rows += [[a, b, c] for a, b, c in VN_DIFFICULTIES]
    table(doc, rows, widths=[4.0, 6.0, 7.0])

    doc.add_heading("Classroom routines for large Vietnamese classes", level=2)
    for name, detail in CLASSROOM_ROUTINES:
        rich(doc, [(f"{name}: ", {'b': True, 'c': TEAL}), (detail, {})])

    doc.add_heading("Assessment plan", level=2)
    table(doc, [["Type", "When and what"]] + [[a, b] for a, b in ASSESSMENT], widths=[5.0, 12.0])

    doc.add_heading("Scope and sequence", level=1)
    rows = [["Unit", "Topic", "Grammar", "Pronunciation", "Periods"]]
    p = 1
    for u in units:
        n = len(u.lessons)
        rows.append([str(u.number), u.title, "; ".join(u.grammar_focus), u.pron_focus,
                     f"{p}–{p + n - 1}"])
        p += n
    table(doc, rows, widths=[1.3, 3.2, 6.0, 4.5, 2.0], size=9)
    page_break(doc)


def lesson_plan(doc, L):
    doc.add_heading(f"{L.full_title}", level=2)
    rich(doc, [(f"Period {L.period}  ·  45 minutes  ·  Code {L.code}", {'i': True, 'c': GREY, 'size': 9})])

    box(doc, "Learning objectives — by the end of the lesson students can:",
        [f"• {o}" for o in L.objectives], "objectives", ICONS['objectives'])

    if L.recycled:
        box(doc, "Language recycled in this lesson", [f"• {r}" for r in L.recycled], "note", ICONS['review'])

    if L.materials:
        rich(doc, [("Materials: ", {'b': True}), ("; ".join(L.materials), {})])

    # --- language content -------------------------------------------------
    doc.add_heading("1. Language content", level=3)
    if L.vocab:
        doc.add_heading("Vocabulary", level=4)
        table(doc, [["Word", "Type", "Pronunciation", "Vietnamese", "Example sentence"]]
              + [w.as_row() for w in L.vocab], widths=[3.4, 1.4, 3.2, 3.0, 6.0], size=9)
    if L.phrases:
        box(doc, "Useful phrases and collocations", [" • " + p for p in L.phrases], "vocab", ICONS['vocab'])
    if L.grammar:
        doc.add_heading(f"Grammar — {L.grammar.point}", level=4)
        if L.grammar.use:
            bullets(doc, L.grammar.use)
        if L.grammar.form:
            table(doc, L.grammar.form, widths=None, size=9)
        if L.grammar.examples:
            box(doc, "Model sentences for the board", [" • " + e for e in L.grammar.examples],
                "grammar", ICONS['grammar'])
        if L.grammar.pitfall:
            box(doc, "Vietnamese-learner pitfall", [L.grammar.pitfall], "warn", "⚠")
        if L.grammar.note:
            rich(doc, [("Teacher note: ", {'b': True, 'c': ORANGE}), (L.grammar.note, {'i': True})])
    if L.pron:
        doc.add_heading(f"Pronunciation — {L.pron.focus}", level=4)
        para(doc, L.pron.tip)
        if L.pron.items:
            box(doc, "Drill items", [" • " + i for i in L.pron.items], "pron", ICONS['pron'])
        if L.pron.drill:
            box(doc, "Drill sentences", [" • " + d for d in L.pron.drill], "pron", "🗣")
        if L.pron.vn_note:
            rich(doc, [("Why this is hard for Vietnamese students: ", {'b': True, 'c': RED}),
                       (L.pron.vn_note, {'i': True})])

    # --- procedure --------------------------------------------------------
    doc.add_heading("2. Teaching procedure", level=3)
    rows = [["Stage / time", "Teacher does and says", "Students do", "Mode / material"]]
    for s in L.procedure:
        rows.append([f"{s.name}\n({s.minutes}')", "\n".join("• " + t for t in s.teacher),
                     s.students, f"{s.mode}\n{s.material}"])
    table(doc, rows, widths=[3.0, 7.5, 4.0, 2.5], size=9)

    if L.teacher_talk:
        doc.add_heading("3. Suggested teacher explanations (say it like this)", level=3)
        for t in L.teacher_talk:
            rich(doc, [(t.cue, {'b': True, 'c': BLUE})])
            box(doc, "", ['“' + s + '”' for s in t.say], "note", size=9.5)

    if L.board_plan:
        box(doc, "Board plan", [" • " + b for b in L.board_plan], "note", "🧑‍🏫")

    # --- skills -----------------------------------------------------------
    doc.add_heading("4. Skills material and answers", level=3)
    if L.listening:
        a = L.listening
        doc.add_heading(f"Listening — {a.title}", level=4)
        rich(doc, [("Set the scene: ", {'b': True}), (a.context, {'i': True})])
        _recording_panel(doc, a, _audio_pairs(L))
        script_title = ("Full transcript — for your use in class (students' book prints an extract)"
                        if a.script_is_excerpt else "Full transcript (public domain — may be printed)")
        box(doc, script_title, a.script, "listening", ICONS['listening'], size=9.5)
        for t in a.tasks:
            _task(doc, t, with_answers=True)
    if L.reading:
        doc.add_heading(f"Reading — {L.reading.title}", level=4)
        for b in L.reading.body:
            para(doc, b, align="justify", indent=0.3)
        for t in L.reading.tasks:
            _task(doc, t, with_answers=True)
    for group, name in ((L.guided, "Guided practice"), (L.independent, "Independent practice"),
                        (L.speaking, "Speaking activities"), (L.writing, "Writing activities")):
        if group:
            doc.add_heading(name, level=4)
            for t in group:
                _task(doc, t, with_answers=True)

    if L.communication:
        c = L.communication
        doc.add_heading("Communication / real-life English", level=4)
        rich(doc, [("Function: ", {'b': True}), (c.get("function", ""), {})])
        if c.get("phrases"):
            box(doc, "Phrase box", [" • " + p for p in c["phrases"]], "speaking", ICONS['communication'])
        if c.get("roleplay"):
            rich(doc, [("Role play: ", {'b': True, 'c': TEAL}), (c["roleplay"], {})])
        if c.get("real_life"):
            rich(doc, [("Real-life use: ", {'b': True, 'c': TEAL}), (c["real_life"], {})])

    # --- differentiation, review, homework --------------------------------
    doc.add_heading("5. Differentiation", level=3)
    t = doc.add_table(rows=1, cols=2)
    borders(t)
    for i, (title, items, fill) in enumerate([
            ("Support — weaker students", L.support, "answer"),
            ("Challenge — stronger students", L.challenge, "objectives")]):
        cell = t.cell(0, i)
        shade(cell, FILL[fill])
        cell.paragraphs[0].text = ""
        r = cell.paragraphs[0].add_run(title); r.bold = True; r.font.size = Pt(10)
        for it in items:
            p = cell.add_paragraph(); p.paragraph_format.space_after = Pt(1)
            rr = p.add_run("• " + it); rr.font.size = Pt(9.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

    if L.review:
        box(doc, "Review and consolidation — what must be secure before the next lesson",
            [" • " + r for r in L.review], "answer", ICONS['review'])
    if L.assessment:
        box(doc, "Quick assessment checks", [" • " + a for a in L.assessment], "note", "✔")
    if L.homework:
        doc.add_heading("6. Homework set this lesson", level=3)
        rows = [["Ref", "Task", "Skill", "Level"]]
        for h in L.homework:
            rows.append([h.ref, f"{h.title} — {h.instruction}", h.kind, LEVEL_NAME.get(h.level, h.level)])
        table(doc, rows, widths=[2.4, 9.6, 2.5, 2.5], size=9)
        rich(doc, [("Answers: see the Teacher's Answer Key, section ", {'i': True, 'size': 9}),
                   (L.code, {'i': True, 'b': True, 'size': 9}), (".", {'i': True, 'size': 9})])
    adaptive_insert(doc, L)
    page_break(doc)



def _audio_pairs(L):
    """The recordings this lesson plays. D0L1/D0L2 are the diagnostic sessions,
    whose audio lives in curriculum/audio_diagnostic.py rather than the course
    corpus, so they resolve through a different table."""
    if L.code == "D0L1":
        out = []
        for k in ("D1_1", "D1_2", "D1_3"):
            out += diagnostic_audio(k)
        return out
    if L.code == "D0L2":
        return []          # Part B is writing and speaking; no recording is played
    return lesson_audio(L.code)


def _recording_panel(doc, a, pairs=()):
    """Everything the teacher needs to find, play and credit the real recording."""
    rows = []
    if a.source:      rows.append(("Source", a.source))
    if a.speakers:    rows.append(("Speakers", a.speakers))
    if a.level:       rows.append(("Level", a.level))
    if a.duration:    rows.append(("Length", a.duration))
    if a.speech_rate: rows.append(("Speed", a.speech_rate))
    if a.recycled_from:
        rows.append(("Replays", ", ".join(a.recycled_from)))
    if a.source_page: rows.append(("Lesson page", a.source_page))
    for i, u in enumerate(a.audio_urls, 1):
        label = "Audio file" if len(a.audio_urls) == 1 else f"Audio file {i}"
        rows.append((label, u))
    if a.licence:     rows.append(("Licence / use", a.licence))
    if a.attribution: rows.append(("Credit line", a.attribution))
    if a.teacher_note:rows.append(("Before you play", a.teacher_note))
    t = box(doc, "🎧 The recording", [f"{k}: {v}" for k, v in rows], "listening", size=8.5)
    if pairs:
        loc, onl = link_set(pairs, 1)
        audio_links_in_cell(t.cell(0, 0), loc, onl, label="▶ Play audio", size=9)


def _task(doc, e, with_answers=False):
    rich(doc, [(f"{e.ref}  {e.title} ", {'b': True, 'c': NAVY}),
               (f"[{LEVEL_STAR.get(e.level,'')} {LEVEL_NAME.get(e.level,'')} · {e.kind}]",
                {'i': True, 'size': 8.5, 'c': GREY})])
    para(doc, e.instruction, italic=True, size=9.5, indent=0.3)
    if e.wordbank:
        box(doc, "", ["   ".join("[" + w + "]" for w in e.wordbank)], "vocab", size=9.5)
    for t in e.text:
        para(doc, t, size=9.5, indent=0.5, align="justify")
    for it in e.items:
        para(doc, it, size=9.5, indent=0.6, space_after=1)
    if with_answers and e.answers:
        box(doc, "Answers", [" " + a for a in e.answers], "answer", "✔", size=9.5, title_color=TEAL)
    if with_answers and e.note:
        rich(doc, [("Note: ", {'b': True, 'c': ORANGE, 'size': 9}), (e.note, {'i': True, 'size': 9})])


# --------------------------------------------------------------------------
# ADAPTIVE INSERTS — stamped into a lesson plan when a trigger names it
# --------------------------------------------------------------------------
def _fired_triggers():
    CP, AD = load_profile(), load_adaptive()
    if CP is None or AD is None or not CP.DIAGNOSED:
        return []
    return [AD.TRIGGERS_BY_CODE[c] for c in CP.active_triggers()
            if c in AD.TRIGGERS_BY_CODE]


def _inserts_for(lesson_code):
    """Which fired triggers put a full box in THIS lesson.

    Only `insert_at` counts. A trigger's standing change — a daily drill, a
    pairing rule, a marking rule — is printed once in the front matter instead.
    Stamping 'open every lesson with a retrieval quiz' onto ninety-four lesson
    plans does not make a teacher more likely to do it; it makes them stop
    reading the boxes.
    """
    return [t for t in _fired_triggers() if lesson_code in t.insert_at]


def adaptive_insert(doc, L):
    for t in _inserts_for(L.code):
        lines = [f"Fired for this class: {t.fires_when}", ""]
        lines += [f"• {c}" for c in t.changes]
        if t.retire_when:
            lines += ["", f"Retire when: {t.retire_when}"]
        box(doc, f"ADAPTIVE INSERT — {t.code}: {t.name}", lines, "warn", "⚡", size=9)


def standing_changes(doc):
    """Changes that run across the year, printed once."""
    fired = _fired_triggers()
    standing = [t for t in fired if t.standing]
    if not standing:
        return
    box(doc, "STANDING CHANGES FOR THIS CLASS — every lesson, all year",
        ["These come from the diagnostic and are not repeated on each lesson plan. "
         "Copy them onto the inside cover of your planner.", ""]
        + [f"{t.code}  {t.standing}" for t in standing],
        "warn", "⚡", size=9.5)
    per_lesson = [t for t in fired if t.insert_at]
    if per_lesson:
        para(doc, "The remaining changes are moment-specific and are printed as an ADAPTIVE "
                  "INSERT box under the procedure of the lesson they belong to:",
             size=9.5, italic=True)
        table(doc, [["#", "Trigger", "Lessons that carry an insert"]] +
              [[t.code, t.name, ", ".join(t.insert_at)] for t in per_lesson],
              widths=[1.2, 5.4, 10.4], size=9)


def diagnostic_front(doc):
    """The two diagnostic sessions, and this class's adapted plan."""
    D = load_diagnostic()
    if D is None:
        return
    CP, AD = load_profile(), load_adaptive()
    doc.add_heading("PERIODS 1–2: THE INITIAL DIAGNOSTIC", level=1)
    para(doc, D.theme, italic=True, color=GREY)
    box(doc, "Before you teach a single lesson", [
        "The 92 teaching sessions that follow assume a starting point. These two periods find out "
        "what the starting point actually is.",
        "Full papers, answer keys, rubrics, bands, triggers, bridging lessons and the extension "
        "bank are in Book 6. The photocopiable papers are in Book 7.",
        "Nothing is taught in these two periods. Do not pre-teach, do not hint, do not help.",
    ], "objectives", "🔍")
    if CP is not None:
        box(doc, "This class", [CP.summary()],
            "note" if not CP.DIAGNOSED else "answer", "📋", size=9.5)
        if CP.DIAGNOSED and AD is not None:
            fired = CP.active_triggers()
            if fired:
                table(doc, [["#", "Trigger", "Retire when"]] +
                      [[t.code, t.name, t.retire_when]
                       for t in (AD.TRIGGERS_BY_CODE[c] for c in fired if c in AD.TRIGGERS_BY_CODE)],
                      widths=[1.2, 6.0, 9.8], size=9)
                standing_changes(doc)
            mode = CP.bridge_mode()
            if mode:
                label = {"pre-course": "Bridging lessons B1–B6 run as a PRE-COURSE BLOCK, before "
                                       "Unit 1 (Book 6).",
                         "warm-up": "Bridging lessons B1–B6 run as WHOLE-CLASS WARM-UP INSERTS "
                                    "inside Units 1–3 (Book 6).",
                         "homework": "Bridging work is TARGETED HOMEWORK plus a weekly "
                                     "ten-minute clinic (Book 6)."}
                box(doc, "Bridging delivery for this class",
                    [label.get(mode, mode), CP.BRIDGE_NOTE or ""], "objectives", "🧱", size=9.5)
    page_break(doc)
    for L in D.lessons:
        lesson_plan(doc, L)


def build(path):
    units = load_units()
    reviews = {r.number: r for r in load_reviews()}
    doc = new_doc(COURSE["title"], COURSE["subtitle"], "Book 1 · Teacher's Coursebook")
    add_toc(doc)
    front_matter(doc, units)
    diagnostic_front(doc)
    for u in units:
        doc.add_heading(f"UNIT {u.number}: {u.title.upper()}", level=1)
        para(doc, u.theme, italic=True, color=GREY)
        box(doc, "Unit outcomes — by the end of the unit students can:",
            [f"• {c}" for c in u.can_do], "objectives", "🎯")
        table(doc, [["Grammar", "; ".join(u.grammar_focus)],
                    ["Pronunciation", u.pron_focus],
                    ["Vocabulary", u.vocab_focus],
                    ["Project", u.project.get("name", "")]],
              header=False, widths=[3.5, 13.5], size=9.5)
        if u.project:
            box(doc, f"Project: {u.project.get('name','')}",
                [u.project.get("goal", "")] + [f"{i+1}. {s}" for i, s in enumerate(u.project.get("steps", []))]
                + [f"Marking: {u.project.get('marking','')}"], "writing", "🛠")
        page_break(doc)
        for L in u.lessons:
            lesson_plan(doc, L)
        if u.number in reviews:
            R = reviews[u.number]
            doc.add_heading(f"REVIEW & TEST {R.title}", level=1)
            for L in R.lessons:
                lesson_plan(doc, L)
    doc.save(path)
    return path
