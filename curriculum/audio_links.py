# -*- coding: utf-8 -*-
"""Which local MP3(s) does a given lesson or diagnostic task need?

One resolver, used by every generator, so a play button in the Student Book, a
link in the Teacher's Coursebook and a link on a slide can never disagree about
which recording a lesson uses.

Two rules do all the work, and both are load-bearing:

1.  A file is named  F<lesson code>_<part>_<source basename>.mp3 .  The name is
    DERIVED from the recorded URL, never stored, so it cannot drift.

2.  The twelve *Looking Back* lessons carry `recycled_from`. They replay their
    own unit's Lesson 2 and Lesson 3 recordings rather than holding a copy, so
    their files are named after the SOURCE lesson — U1L7 links to
    FU1L2_… and FU1L3_…, never to a non-existent FU1L7_… .  Getting this wrong
    is the single most likely way to produce a link to a file that is not there.

A multipart recording (U7L3, U10L6 and U12L3 are published as four separate
conversations) resolves to all of its parts, in the order the source lists
them. Nothing is ever collapsed into one file.
"""
import os

AUDIO_DIRNAME = "audio"


def _lesson_files(code, seen=None):
    """[(filename, source_page), …] — the page travels with the file so that a
    missing recording can still be reached at its official source."""
    from .audio_sources import AUDIO
    a = AUDIO.get(code)
    if a is None:
        return []
    seen = seen or set()
    if code in seen:                      # defensive: no infinite recycling
        return []
    seen = seen | {code}
    if a.recycled_from:
        out = []
        for src in a.recycled_from:
            out.extend(_lesson_files(src, seen))
        return out
    return [(f"F{code}_{i}_{u.split('/')[-1]}", a.source_page)
            for i, u in enumerate(a.audio_urls, 1)]


def lesson_audio(code):
    """[(part_label, filename, source_page), …] for a code such as 'U1L1'.

    For a Looking Back lesson the label names the lesson the recording is
    borrowed from, because that is what the teacher needs to recognise.
    """
    from .audio_sources import AUDIO
    a = AUDIO.get(code)
    if a is None:
        return []
    files = _lesson_files(code)
    if a.recycled_from:
        labels = []
        for src in a.recycled_from:
            n = len(_lesson_files(src))
            for i in range(n):
                labels.append(f"{src}" + (f" part {i + 1}" if n > 1 else ""))
        return [(lbl, fn, pg) for lbl, (fn, pg) in zip(labels, files)]
    if len(files) == 1:
        return [(code, files[0][0], files[0][1])]
    return [(f"{code} part {i}", fn, pg) for i, (fn, pg) in enumerate(files, 1)]


def diagnostic_audio(key):
    """[(label, filename, source_page)] for a key such as 'D1_1'."""
    from .audio_diagnostic import DIAG_FILES, DIAG_AUDIO
    rel = DIAG_FILES.get(key)
    if not rel:
        return []
    return [(key, os.path.basename(rel), DIAG_AUDIO[key].source_page)]


def rel_path(filename, depth):
    """Path to a recording, relative to a document `depth` folders below the root.

    depth 1 → output/BOOK.docx            → ../audio/x.mp3
    depth 3 → output/slides/Unit01/x.pptx → ../../../audio/x.mp3

    The link is resolved by Word/PowerPoint against the document's own location
    on disk, so the depth must match where the file is actually written, not
    where it looks like it should be.
    """
    return "../" * depth + f"{AUDIO_DIRNAME}/{filename}"


def exists(filename, root=None):
    root = root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.exists(os.path.join(root, AUDIO_DIRNAME, filename))


def targets(triples, depth):
    """Turn resolver output into link targets.

    Returns [(label, target, is_local), …].  The local MP3 always wins when it
    is on disk; only when it is absent does the link fall back to the official
    lesson page where that exact recording is published.  A generic page is
    never substituted for an available recording, and a fallback is never
    silently presented as if it were the file.

    The fallback is not hypothetical: audio/ is gitignored, so a fresh clone
    has no recordings until `python3 tools/fetch_audio.py` has been run, and
    the books have to stay usable in that state.
    """
    out = []
    for label, filename, page in triples:
        if exists(filename):
            out.append((label, rel_path(filename, depth), True))
        elif page:
            out.append((label, page, False))
    return out


def audit():
    """Every (owner, label, filename, source_page, on_disk) the project references."""
    from .audio_sources import AUDIO
    from .audio_diagnostic import DIAG_FILES
    rows = []
    for code in AUDIO:
        for label, fn, pg in lesson_audio(code):
            rows.append((code, label, fn, pg, exists(fn)))
    for key in DIAG_FILES:
        for label, fn, pg in diagnostic_audio(key):
            rows.append((key, label, fn, pg, exists(fn)))
    return rows
