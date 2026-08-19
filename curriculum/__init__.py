# -*- coding: utf-8 -*-
"""Loads every unit module that exists and exposes the whole course."""
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


def all_lessons():
    """Every teaching session in running order, reviews inserted after units 3/6/9/12."""
    units = load_units()
    reviews = {r.number: r for r in load_reviews()}
    seq = []
    for u in units:
        seq.extend(u.lessons)
        if u.number in reviews:
            seq.extend(reviews[u.number].lessons)
    return seq
