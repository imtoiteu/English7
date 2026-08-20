# -*- coding: utf-8 -*-
"""THE CLASS PROFILE — the one file a teacher edits to make the course adapt.

This is the hinge of the whole adaptive system.  Everything else describes what
COULD change; this file records what a real class actually needs, and the
generators read it.

    DIAGNOSED = False   →  the course builds exactly as it always did.
    DIAGNOSED = True    →  the Teacher's Coursebook grows ADAPTIVE INSERT boxes
                           in the lessons the fired triggers name, the bridging
                           delivery mode is printed in the front matter, and
                           Book 6 prints this class's own teaching plan instead
                           of a generic one.

HOW TO USE IT
    1.  Teach periods 1–2 (Paper A).  Mark it.
    2.  At Checkpoint 1 — after period 9, when the rolling speaking assessment
        is finished — fill in the numbers below.
    3.  Run `python3 build.py`.
    4.  Teach from the rebuilt books.
    5.  Come back at Checkpoint 2 (period 48) and again at Checkpoint 3
        (periods 93–94), update the numbers, and rebuild.

Everything below is class-level.  Individual student records do not belong in
a source file that gets committed to a repository; keep them in the class
register or the tracking grid printed in Book 6.

The worked example at the bottom is a REAL-SHAPED class, not a tidy one, and it
is commented out.  It is there so you can see what a filled-in profile looks
like before you fill in your own.
"""

# ==========================================================================
# Has this class been diagnosed yet?
# ==========================================================================
DIAGNOSED = False

CLASS_NAME = ""          # e.g. "7A"
SCHOOL_YEAR = ""         # e.g. "2026–2027"
STUDENTS = 0             # number of students who sat Paper A
CHECKPOINT = ""          # "0" | "1" | "2" | "3" — which checkpoint these numbers are from
DATE = ""                # date the numbers were entered, e.g. "2026-09-12"


# ==========================================================================
# Class mean, per strand, as a PERCENTAGE of that strand's marks
#   listening /12 · reading /12 · vocab /10 · grammar /12
#   writing /14 · speaking /12 · pron /8
# Percentages, not raw marks — that is what makes September, January and May
# comparable when the papers have different totals.
# ==========================================================================
STRANDS = {
    "listening": None,
    "reading": None,
    "vocab": None,
    "grammar": None,
    "writing": None,
    "speaking": None,
    "pron": None,
}


# ==========================================================================
# Band distribution — the NUMBER of students in each band, not the percentage
# ==========================================================================
BANDS = {
    "foundation": None,
    "core": None,
    "extension": None,
}

SPREAD_SD = None         # standard deviation of the 80-mark totals (for trigger T7)
P10_P90_GAP = None       # 90th percentile total minus 10th percentile total (also T7)


# ==========================================================================
# Item-level class percentages needed by specific triggers.
# Enter the percentage of the class that got the item RIGHT.
# ==========================================================================
ITEM_CORRECT = {
    "A-G3.1": None,      # past simple, regular      → T1
    "A-G3.2": None,      # past simple, irregular    → T1
    "A-L3.2": None,      # past simple in listening  → T1
    "A-G1.3": None,      # third-person -s           → T5
    "A-G1.4": None,      # does + base form          → T5
    "A-V2.5": None,      # third-person -s in a vocabulary frame → T5
}

# Rubric criterion means, for the triggers that need them.
CRITERION_MEANS = {
    "pron.final_consonants": None,   # /2  → T3
    "pron.word_stress": None,        # /2
    "writing.grammar": None,         # /3  → T6
    "writing.organisation": None,    # /2  → T6
}

# Percentage of the class scoring 4 or below out of 14 on the writing section → T6
WRITING_AT_OR_BELOW_4 = None

# Class mean on the Unit 1 Revision Set, as a percentage → T4
# (Leave as None at Checkpoint 0 — the Revision Set has not been done yet.)
UNIT1_REVISION = None


# ==========================================================================
# Which triggers have fired.
#
# `evaluate_triggers()` below computes this from the numbers above, but you may
# also set it by hand — a teacher who can see something the arithmetic cannot
# is allowed to overrule the arithmetic, as long as they write down why.
# ==========================================================================
FIRED = []               # e.g. ["T1", "T2", "T5"]
FIRED_BY_HAND = {}       # e.g. {"T3": "Half the class is inaudible in the back row."}


# ==========================================================================
# Bridging delivery mode — set from the Foundation count.
#   "pre-course" | "warm-up" | "homework" | "" (not yet decided)
# ==========================================================================
BRIDGE_MODE = ""
BRIDGE_NOTE = ""


# ==========================================================================
# Computation
# ==========================================================================

def _pct(n):
    return n if isinstance(n, (int, float)) else None


def foundation_share():
    """Foundation students as a fraction of the class, or None."""
    if not STUDENTS or BANDS.get("foundation") is None:
        return None
    return BANDS["foundation"] / STUDENTS


def extension_share():
    if not STUDENTS or BANDS.get("extension") is None:
        return None
    return BANDS["extension"] / STUDENTS


def suggested_bridge_mode():
    """Which delivery mode the Foundation count implies."""
    f = foundation_share()
    if f is None:
        return ""
    if f > 0.40:
        return "pre-course"
    if f >= 0.15:
        return "warm-up"
    return "homework"


def _mean(keys):
    vals = [ITEM_CORRECT[k] for k in keys if ITEM_CORRECT.get(k) is not None]
    return sum(vals) / len(vals) if vals else None


def evaluate_triggers():
    """Work out which of T1–T8 fire from the numbers entered above.

    Returns (fired, reasons, undecidable).  A trigger whose evidence has not
    been entered lands in `undecidable`, NOT in `fired` — silence is not a
    negative result, and a teacher should be told which questions they have
    not answered yet.
    """
    fired, reasons, undecidable = [], {}, []

    def decide(code, condition, reason, have_data):
        if not have_data:
            undecidable.append(code)
            return
        if condition:
            fired.append(code)
            reasons[code] = reason

    # T1 — past simple
    past = _mean(["A-G3.1", "A-G3.2"])
    l32 = ITEM_CORRECT.get("A-L3.2")
    decide("T1", (past is not None and past < 50) or (l32 is not None and l32 < 50),
           f"past-simple items at {past}% (threshold 50%)",
           past is not None or l32 is not None)

    # T2 — listening behind reading
    li, re_ = _pct(STRANDS.get("listening")), _pct(STRANDS.get("reading"))
    decide("T2", li is not None and re_ is not None and (re_ - li) >= 15,
           f"listening {li}% vs reading {re_}% — a gap of "
           f"{(re_ - li) if (li is not None and re_ is not None) else '?'} points",
           li is not None and re_ is not None)

    # T3 — final consonants
    fc = CRITERION_MEANS.get("pron.final_consonants")
    decide("T3", fc is not None and fc < 1.0,
           f"final-consonant criterion mean {fc}/2 (threshold 1.0)", fc is not None)

    # T4 — vocabulary retention (needs BOTH conditions)
    vo, u1 = _pct(STRANDS.get("vocab")), _pct(UNIT1_REVISION)
    decide("T4", vo is not None and u1 is not None and vo < 50 and u1 < 50,
           f"vocabulary {vo}% and Unit 1 revision {u1}% — both under 50%",
           vo is not None and u1 is not None)

    # T5 — third-person -s
    third = _mean(["A-G1.3", "A-G1.4"])
    v25 = ITEM_CORRECT.get("A-V2.5")
    decide("T5", (third is not None and third < 60) or (v25 is not None and v25 < 60),
           f"third-person items at {third}% (threshold 60%)",
           third is not None or v25 is not None)

    # T6 — writing below sentence level
    w4 = WRITING_AT_OR_BELOW_4
    decide("T6", w4 is not None and w4 >= 30,
           f"{w4}% of the class scoring 4 or below out of 14 (threshold 30%)", w4 is not None)

    # T7 — spread
    sd, gap = SPREAD_SD, P10_P90_GAP
    decide("T7", (sd is not None and sd > 12) or (gap is not None and gap > 30),
           f"standard deviation {sd}, 10th–90th percentile gap {gap}",
           sd is not None or gap is not None)

    # T8 — extension-heavy
    ex = extension_share()
    decide("T8", ex is not None and ex >= 0.25,
           f"{round(ex * 100) if ex is not None else '?'}% of the class in the Extension band",
           ex is not None)

    for code, why in FIRED_BY_HAND.items():
        if code not in fired:
            fired.append(code)
            reasons[code] = f"set by hand: {why}"
        if code in undecidable:
            undecidable.remove(code)

    return fired, reasons, undecidable


def active_triggers():
    """The trigger codes the generators should act on."""
    if not DIAGNOSED:
        return []
    if FIRED:
        return list(FIRED)
    return evaluate_triggers()[0]


def bridge_mode():
    if not DIAGNOSED:
        return ""
    return BRIDGE_MODE or suggested_bridge_mode()


def summary():
    """One-paragraph description of this class, for the front matter of Book 1."""
    if not DIAGNOSED:
        return ("This class has not been diagnosed yet. The course is printed as designed. "
                "Teach periods 1–2 (Paper A), mark it, fill in curriculum/class_profile.py at "
                "Checkpoint 1, and rebuild — the adaptive inserts will then appear in the lessons "
                "that need them.")
    fired = active_triggers()
    bits = [f"{CLASS_NAME or 'This class'}"]
    if STUDENTS:
        bits.append(f"{STUDENTS} students")
    if all(BANDS.get(k) is not None for k in ("foundation", "core", "extension")):
        bits.append(f"{BANDS['foundation']} Foundation / {BANDS['core']} Core / "
                    f"{BANDS['extension']} Extension")
    head = " · ".join(bits)
    trig = ", ".join(fired) if fired else "no triggers fired"
    mode = bridge_mode() or "not set"
    return (f"{head}. Checkpoint {CHECKPOINT or '?'}"
            f"{' (' + DATE + ')' if DATE else ''}. Triggers active: {trig}. "
            f"Bridging delivery: {mode}.")


# ==========================================================================
# WORKED EXAMPLE — a real-shaped class, not a tidy one.
#
# 7A, 44 students, entered at Checkpoint 1.  Copy the block below over the
# defaults above and rebuild to see what an adapted course looks like.
#
#   DIAGNOSED   = True
#   CLASS_NAME  = "7A"
#   SCHOOL_YEAR = "2026–2027"
#   STUDENTS    = 44
#   CHECKPOINT  = "1"
#   DATE        = "2026-09-12"
#
#   STRANDS = {"listening": 38, "reading": 57, "vocab": 49, "grammar": 44,
#              "writing": 41, "speaking": 46, "pron": 43}
#   BANDS   = {"foundation": 16, "core": 22, "extension": 6}
#   SPREAD_SD = 13.8
#   P10_P90_GAP = 34
#   ITEM_CORRECT = {"A-G3.1": 34, "A-G3.2": 27, "A-L3.2": 31,
#                   "A-G1.3": 52, "A-G1.4": 61, "A-V2.5": 45}
#   CRITERION_MEANS = {"pron.final_consonants": 0.8, "pron.word_stress": 1.1,
#                      "writing.grammar": 1.4, "writing.organisation": 0.9}
#   WRITING_AT_OR_BELOW_4 = 34
#   UNIT1_REVISION = 47
#   BRIDGE_MODE = "warm-up"
#   BRIDGE_NOTE = ("16 of 44 is 36% — warm-up inserts, whole class, inside Units 1–3. "
#                  "B5 and B6 come first because T1 and T3 both fired.")
#
# That class fires T1, T2, T3, T4, T5, T6 and T7 — seven of the eight.  That is
# not a disaster and it is not unusual; it is what an honest instrument reports
# about a Grade 7 class in September.  The response is not to change all seven
# things at once with equal energy: T2 and T3 start in week one because they
# cost minutes, T5 and T1 are scheduled before the units that need them, and
# T4's ninety-second retrieval quiz runs all year because it is nearly free.
# ==========================================================================
