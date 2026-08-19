# -*- coding: utf-8 -*-
"""BOOK 2 — Student Coursebook / Learning Materials."""
from generators.common import *
from curriculum import load_units, load_reviews
from curriculum.course import COURSE, ICONS


def _task(doc, e, lines_default=0):
    rich(doc, [(f"{e.ref}  ", {'b': True, 'c': ORANGE, 'size': 10}),
               (e.title, {'b': True, 'c': NAVY, 'size': 10}),
               (f"   {LEVEL_STAR.get(e.level,'')}", {'size': 8.5, 'c': GREY})])
    para(doc, e.instruction, italic=True, size=9.5, indent=0.3)
    if e.wordbank:
        box(doc, "", ["   ".join("[ " + w + " ]" for w in e.wordbank)], "vocab", size=9.5)
    for t in e.text:
        para(doc, t, size=9.5, indent=0.5, align="justify")
    for it in e.items:
        para(doc, it, size=9.5, indent=0.6, space_after=2)
    n = e.lines or lines_default
    if n:
        writing_lines(doc, n)


def lesson_pages(doc, L):
    doc.add_heading(L.full_title, level=2)
    rich(doc, [(f"Period {L.period}", {'i': True, 'c': GREY, 'size': 9})])

    box(doc, "In this lesson you will learn to:", [f"• {o}" for o in L.objectives],
        "objectives", ICONS['objectives'])

    if L.vocab:
        doc.add_heading("New words", level=3)
        table(doc, [["Word", "Type", "Say it like this", "Tiếng Việt", "Example"]]
              + [w.as_row() for w in L.vocab], widths=[3.4, 1.4, 3.2, 3.0, 6.0], size=9)
    if L.phrases:
        box(doc, "Useful phrases", [" • " + p for p in L.phrases], "vocab", ICONS['vocab'])

    if L.grammar:
        doc.add_heading(f"Grammar: {L.grammar.point}", level=3)
        for u in L.grammar.use:
            para(doc, "• " + u, indent=0.3)
        if L.grammar.form:
            table(doc, L.grammar.form, size=9)
        if L.grammar.examples:
            box(doc, "Examples", [" • " + e for e in L.grammar.examples], "grammar", ICONS['grammar'])
        if L.grammar.pitfall:
            box(doc, "Be careful! (a common mistake)", [L.grammar.pitfall], "warn", "⚠")

    if L.pron:
        doc.add_heading(f"Pronunciation: {L.pron.focus}", level=3)
        para(doc, L.pron.tip)
        if L.pron.items:
            box(doc, "Say these", [" • " + i for i in L.pron.items], "pron", ICONS['pron'])
        if L.pron.drill:
            box(doc, "Now say the sentences", [" • " + d for d in L.pron.drill], "pron", "🗣")

    if L.listening:
        a = L.listening
        doc.add_heading(f"Listening: {a.title}", level=3)
        para(doc, a.context, italic=True)
        where = []
        if a.source:      where.append(f"Recording: {a.source}")
        if a.duration and a.duration != "replayed extracts":
            where.append(f"Length: {a.duration}")
        if a.source_page: where.append(f"Listen again at home: {a.source_page}")
        if a.attribution: where.append(a.attribution)
        if where:
            box(doc, "🎧 Where this recording comes from", where, "listening", size=8.5)
        for t in a.tasks:
            _task(doc, t)
        if a.script_is_excerpt:
            shown, n = [], 0
            for line in a.script:
                w = len(line.split())
                if n + w > 90 and shown:
                    break
                shown.append(line); n += w
            shown.append("… — the full script is on the lesson page (see the box above).")
            title = "Transcript — extract (look ONLY after you have listened twice)"
        else:
            shown, title = a.script, "Transcript (look ONLY after you have listened twice)"
        box(doc, title, shown, "listening", ICONS['listening'], size=9)

    if L.reading:
        doc.add_heading(f"Reading: {L.reading.title}", level=3)
        for b in L.reading.body:
            para(doc, b, align="justify", indent=0.3)
        for t in L.reading.tasks:
            _task(doc, t)

    if L.guided:
        doc.add_heading("Practice", level=3)
        for t in L.guided:
            _task(doc, t)
    if L.independent:
        doc.add_heading("Now you try", level=3)
        for t in L.independent:
            _task(doc, t)
    if L.speaking:
        doc.add_heading("Speaking", level=3)
        for t in L.speaking:
            _task(doc, t)
    if L.communication:
        c = L.communication
        doc.add_heading("Real-life English", level=3)
        rich(doc, [("You will learn to: ", {'b': True}), (c.get("function", ""), {})])
        if c.get("phrases"):
            box(doc, "Say it like this", [" • " + p for p in c["phrases"]], "speaking", ICONS['communication'])
        if c.get("roleplay"):
            rich(doc, [("Role play: ", {'b': True, 'c': TEAL}), (c["roleplay"], {})])
        if c.get("real_life"):
            rich(doc, [("You can use this when: ", {'b': True, 'c': TEAL}), (c["real_life"], {})])
    if L.writing:
        doc.add_heading("Writing", level=3)
        for t in L.writing:
            _task(doc, t, lines_default=4)

    if L.review:
        box(doc, "Remember from this lesson", [" ✓ " + r for r in L.review], "answer", ICONS['review'])
    if L.homework:
        box(doc, "Homework", [f" • {h.ref}  {h.title} — {h.instruction}" for h in L.homework],
            "writing", ICONS['homework'])
    page_break(doc)


def build(path):
    units = load_units()
    reviews = {r.number: r for r in load_reviews()}
    doc = new_doc(COURSE["title"], COURSE["subtitle"], "Book 2 · Student Coursebook", colour=TEAL)
    add_toc(doc)
    doc.add_heading("How to use this book", level=1)
    bullets(doc, [
        "Every lesson has the same parts, so you always know where you are.",
        "New words come first. Copy them into your vocabulary notebook with the stress mark.",
        "Do not look at the audio script before you have listened twice. Train your ears!",
        "In Speaking, it is fine to make mistakes. Say something. Silence teaches you nothing.",
        "The 'Be careful!' box shows a mistake that Vietnamese students often make. Read it twice.",
        "At the end of each lesson, cover the page and try to remember five new words.",
    ])
    box(doc, "Your five learning promises", [
        " 1. I say every new word out loud at least five times.",
        " 2. I always pronounce the last sound of the word (like-S, book-K, and-D).",
        " 3. I do not translate word by word from Vietnamese.",
        " 4. I write my homework the same day, not the next morning.",
        " 5. I speak English in the English lesson, even when it is difficult."], "objectives", "🤝")
    page_break(doc)
    for u in units:
        doc.add_heading(f"UNIT {u.number}: {u.title.upper()}", level=1)
        para(doc, u.theme, italic=True, color=GREY)
        box(doc, "By the end of this unit I can:", [f"□ {c}" for c in u.can_do], "objectives", "🎯")
        if u.project:
            box(doc, f"Unit project: {u.project.get('name','')}",
                [u.project.get("goal", "")] + [f"{i+1}. {s}" for i, s in enumerate(u.project.get("steps", []))],
                "writing", "🛠")
        page_break(doc)
        for L in u.lessons:
            lesson_pages(doc, L)
        if u.number in reviews:
            R = reviews[u.number]
            doc.add_heading(f"REVIEW {R.title}", level=1)
            for L in R.lessons:
                lesson_pages(doc, L)
    doc.save(path)
    return path
