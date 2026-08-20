# -*- coding: utf-8 -*-
"""Loads every unit module that exists and exposes the whole course.

Running order for the year (94 sessions):

    periods  1–2    the initial diagnostic  (Paper A)
    periods  3–23   Units 1–3
    periods 24–25   Review 1
    periods 26–46   Units 4–6
    periods 47–48   Review 2  — period 48 is the mid-year diagnostic (Paper B)
    periods 49–69   Units 7–9
    periods 70–71   Review 3
    periods 72–92   Units 10–12
    periods 93–94   Review 4  — the final diagnostic (Paper C) sits across both
"""
import importlib

UNIT_NUMBERS = list(range(1, 13))


def load_units():
    units = []
    for n in UNIT_NUMBERS:
        try:
            mod = importlib.import_module(f"curriculum.units.u{n:02d}")
        except ModuleNotFoundError:
            continue
        units.append(mod.UNIT)
    return units


def load_reviews():
    try:
        mod = importlib.import_module("curriculum.reviews")
    except (ModuleNotFoundError, ImportError):
        return []
    return mod.REVIEWS


def load_diagnostic():
    """The two diagnostic sessions that open the year, as a Unit-shaped block.

    Returns None if the diagnostic module is absent, so the course still builds
    without it.
    """
    try:
        mod = importlib.import_module("curriculum.diagnostic")
    except (ModuleNotFoundError, ImportError):
        return None
    return mod.DIAGNOSTIC_BLOCK


def load_papers():
    try:
        mod = importlib.import_module("curriculum.diagnostic")
    except (ModuleNotFoundError, ImportError):
        return []
    return mod.ALL_PAPERS


def load_adaptive():
    try:
        return importlib.import_module("curriculum.adaptive")
    except (ModuleNotFoundError, ImportError):
        return None


def load_profile():
    try:
        return importlib.import_module("curriculum.class_profile")
    except (ModuleNotFoundError, ImportError):
        return None


def all_lessons(include_diagnostic=True):
    """Every teaching session in running order.

    The two diagnostic sessions come first; reviews are inserted after units
    3, 6, 9 and 12.  Pass include_diagnostic=False to get the 92 taught
    sessions on their own — the audio checks in tools/check_course.py use that,
    because the diagnostic recordings live in a different module.
    """
    seq = []
    if include_diagnostic:
        d = load_diagnostic()
        if d is not None:
            seq.extend(d.lessons)
    units = load_units()
    reviews = {r.number: r for r in load_reviews()}
    for u in units:
        seq.extend(u.lessons)
        if u.number in reviews:
            seq.extend(reviews[u.number].lessons)
    return seq


def teaching_lessons():
    """The 92 taught sessions, without the diagnostic."""
    return all_lessons(include_diagnostic=False)
