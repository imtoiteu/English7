# -*- coding: utf-8 -*-
"""Marking rubrics for the productive sections of the diagnostic papers.

Three rules shaped these rubrics:

1.  **Every descriptor is observable.**  "Good vocabulary" is not markable;
    "uses at least six words beyond the 100 commonest" is.  Two teachers
    marking the same script should land within half a mark.

2.  **Every criterion is diagnostic.**  A rubric that only produces a number
    tells you who is weak, not what to teach.  Each criterion here maps onto
    a trigger in `curriculum.adaptive`, so the marking itself generates the
    teaching decision.

3.  **The Vietnamese-learner note names the real interference.**  Not "watch
    for errors" but the specific L1 transfer to expect, so a teacher marking
    forty scripts knows what they are looking at.

The same three rubrics mark Paper A, Paper B and Paper C.  That is deliberate:
if the instrument changes between September and May, the comparison is
worthless.
"""
from .schema import RB, CR


# --------------------------------------------------------------------------
# WRITING — 14 marks
# --------------------------------------------------------------------------
WRITING = RB(
    "Writing", 14,
    criteria=[
        CR("Task completion", 4,
           [["4", "Does everything the task asked. All content points covered and developed "
                  "with at least one extra detail each. Length is within range."],
            ["3", "All content points covered but some only named, not developed. Length within "
                  "range or slightly short."],
            ["2", "One content point missing, or all present but very thin. Noticeably short."],
            ["1", "Two or more content points missing. Under half the required length."],
            ["0", "No relevant content, or the answer is copied from the prompt."]],
           "Vietnamese students often answer the topic rather than the task — they write about "
           "'my family' when asked to write to a friend about their family. Mark the task, not "
           "the topic."),
        CR("Organisation", 2,
           [["2", "Clear order. Related ideas sit together. Uses at least two linkers "
                  "(and, but, because, then, first, after that)."],
            ["1", "Ideas are mostly in a sensible order but linkers are missing or repeated "
                  "(and… and… and…)."],
            ["0", "A list of unconnected sentences, or the order makes the meaning hard to follow."]],
           "Because … so … in the same sentence is a direct calque of vì … nên …. Mark it here, "
           "not under grammar, and teach the fix once."),
        CR("Grammar", 3,
           [["3", "The target structure is used correctly. Occasional slips do not obscure meaning. "
                  "Third-person -s and past endings are present."],
            ["2", "The target structure is attempted and is right more often than wrong. Some "
                  "missing verb endings."],
            ["1", "The target structure is attempted but usually wrong, or avoided by writing only "
                  "very simple sentences."],
            ["0", "Below sentence level: no finite verb, or Vietnamese word order throughout."]],
           "Expect missing -s (He like football), missing be (I student), and no past ending "
           "(Yesterday I go). Count these separately while marking — the totals feed triggers "
           "T1 and T5."),
        CR("Vocabulary", 3,
           [["3", "Words are well chosen and varied. At least three items from the topic set are "
                  "used correctly."],
            ["2", "Adequate but repetitive. Some approximations that still communicate."],
            ["1", "Very limited. Repeats two or three words; some words used in the wrong sense."],
            ["0", "Too little language to judge, or Vietnamese words are used."]],
           "Word-for-word translation shows up here first: I very like it, She has 13 years old, "
           "I go to school by my father."),
        CR("Spelling, punctuation and handwriting", 2,
           [["2", "Spelling is mostly accurate. Capital letters and full stops are used. Legible."],
            ["1", "Frequent spelling errors but the meaning survives. Punctuation is patchy."],
            ["0", "Spelling or handwriting makes the answer hard to read."]],
           "Missing capital I and missing full stops are near-universal at entry and are worth "
           "one whole-class lesson, not forty individual corrections."),
    ],
    how_to_use=[
        "Read the whole answer once before you mark anything. Marking sentence by sentence "
        "produces a grammar score dressed up as a writing score.",
        "Mark task completion first and independently. It is the criterion teachers most often "
        "let the other four contaminate.",
        "Half marks are allowed on Task completion only. Everything else is whole marks.",
        "Underline — do not correct — the first three errors of each type. You are collecting "
        "evidence today, not teaching.",
        "Write nothing on the script except the five criterion scores. The student sees the "
        "profile card later, not the marked paper.",
    ],
    diagnostic_use=[
        "Task completion low, everything else fine → a test-taking problem, not a language "
        "problem. Teach reading the rubric.",
        "Grammar 0–1 for 30% or more of the class → trigger T6 (writing below sentence level).",
        "Vocabulary 0–1 across the class → trigger T4 (vocabulary retention).",
        "Organisation 0 with Grammar 3 → a strong student who has never been taught paragraph "
        "shape. Extension E2 fixes this in one activity.",
    ])


# --------------------------------------------------------------------------
# SPEAKING — 12 marks
# --------------------------------------------------------------------------
SPEAKING = RB(
    "Speaking", 12,
    criteria=[
        CR("Task completion", 3,
           [["3", "Answers every question and asks the partner at least two. Stays on the task "
                  "for the full three minutes."],
            ["2", "Answers most questions; asks at least one. Needs one prompt from the teacher."],
            ["1", "Answers with single words or short phrases only. Needs repeated prompting."],
            ["0", "Silent, or answers in Vietnamese."]],
           "Silence at entry is usually fear, not ignorance. Before scoring 0, give the sentence "
           "frame once and ask again. Score what they do on the second attempt."),
        CR("Fluency and interaction", 3,
           [["3", "Speaks in connected sentences. Pauses are natural. Reacts to the partner "
                  "(Really? Me too. And you?)."],
            ["2", "Speaks in short sentences with some long pauses, but keeps going without help."],
            ["1", "Long pauses, frequent restarts, waits to be rescued."],
            ["0", "Cannot sustain an exchange."]],
           "Do not penalise a Vietnamese-accented rhythm here — that belongs to the pronunciation "
           "rubric. Fluency is about keeping going."),
        CR("Accuracy", 3,
           [["3", "Basic structures are correct. Errors are slips, and are often self-corrected."],
            ["2", "Basic structures are right more often than wrong. Errors do not block meaning."],
            ["1", "Frequent errors in basic structures; the listener has to work."],
            ["0", "Errors make most utterances hard to understand."]],
           "Listen specifically for the missing verb: I student, He like football, Yesterday I go. "
           "Tally these three — they feed triggers T1 and T5."),
        CR("Range", 3,
           [["3", "Uses a variety of words and at least two structures beyond the simplest "
                  "(a because-clause, a past tense, a comparison)."],
            ["2", "Adequate range for the task; mostly one structure."],
            ["1", "Very limited; the same three or four phrases recycled."],
            ["0", "Isolated words only."]],
           "A student who says only what is safe may be scoring 3 for accuracy and 1 for range. "
           "That is an Extension candidate hiding, not a Core student."),
    ],
    how_to_use=[
        "Three minutes per pair, and use a timer. Untimed speaking tests drift and stop being "
        "comparable between the first pair and the fortieth.",
        "Assess both students in the pair at once, on one sheet. Do not let the stronger one "
        "carry the exchange — the second question in each set is addressed to the weaker speaker "
        "by name.",
        "Score immediately, before the next pair sits down. Scores written from memory at the end "
        "of a session regress to the class mean.",
        "If a student freezes, offer the sentence frame once, then move on. Note 'needed frame' — "
        "it is diagnostic information, not a penalty.",
        "Say nothing evaluative during the test. 'Thank you, that's the end' is the whole exit line.",
    ],
    diagnostic_use=[
        "Accuracy high, Range low → the student is playing safe. Extension, not Core.",
        "Task completion 0–1 with a decent written score → confidence, not competence. Pair-work "
        "routines and sentence frames, not remedial grammar.",
        "Fluency and Accuracy both 0–1 across the class → the speaking programme needs frames and "
        "thinking time from Unit 1, not from the first Communication lesson.",
    ])


# --------------------------------------------------------------------------
# PRONUNCIATION — 8 marks
# --------------------------------------------------------------------------
PRONUNCIATION = RB(
    "Pronunciation", 8,
    criteria=[
        CR("Final consonants and clusters", 2,
           [["2", "Final sounds are audible most of the time, including -s and -ed endings and "
                  "clusters like /st/ /sk/ /nd/."],
            ["1", "Single final consonants are usually audible; clusters are simplified "
                  "(asked → ask, schools → school)."],
            ["0", "Final consonants are routinely dropped (like → li, book → boo, finds → fine)."]],
           "This is the single biggest intelligibility cost for Vietnamese learners, because "
           "Vietnamese syllables end in a small set of unreleased sounds. Score it first."),
        CR("Word stress", 2,
           [["2", "Stress is on the right syllable in most multi-syllable words."],
            ["1", "Stress is right in familiar words, flat or wrong in longer ones "
                  "(volunteer, delicious, photograph)."],
            ["0", "Every syllable carries equal weight."]],
           "Vietnamese is syllable-timed and tonal, so equal weighting is the default, not "
           "carelessness. It responds very well to clapping the stressed syllable."),
        CR("Target sounds /θ/ /ð/ /ʃ/ /ʒ/ /v/ /z/", 2,
           [["2", "At least four of the six are produced recognisably."],
            ["1", "Two or three are produced; the rest are substituted "
                  "(think → tink, this → dis, very → dery)."],
            ["0", "All six are substituted."]],
           "These phonemes do not exist in Vietnamese. Expect substitution, mark progress rather "
           "than perfection, and never let this criterion depress the intelligibility score twice."),
        CR("Overall intelligibility", 2,
           [["2", "A patient listener who does not know the script understands throughout."],
            ["1", "Understood with effort; the listener re-reads or asks again."],
            ["0", "Largely unintelligible without the script."]],
           "Judge this as if you had not seen the card. Teachers who know the text always "
           "over-score intelligibility."),
    ],
    how_to_use=[
        "Use the read-aloud card, not free speech. Free speech lets students avoid every sound "
        "they cannot make, which is exactly the information you need.",
        "Forty-five seconds per student. Let them read it silently once first — you are testing "
        "pronunciation, not sight-reading.",
        "Mark criterion 1 (final consonants) on the first pass and the other three on the second. "
        "Trying to hear all four at once is how teachers end up giving everyone a 4.",
        "Record nothing unless you have permission. A tally sheet is enough.",
        "The card is the same in September, January and May. That is what makes the comparison mean "
        "something.",
    ],
    diagnostic_use=[
        "Criterion 1 mean below 1.0 across the class → trigger T3: the 30-second final-consonant "
        "drill becomes 60 seconds for Units 1–6.",
        "Criterion 2 mean below 1.0 → put the stress bubble (Oo / oO) on every new word in the "
        "board plan from Unit 1, not from Unit 4.",
        "Criterion 4 scoring higher than criteria 1–3 → the student is intelligible despite the "
        "errors. Do not spend their lesson time on phonemes; spend it on range.",
    ])


ALL_RUBRICS = [WRITING, SPEAKING, PRONUNCIATION]
BY_NAME = {r.name: r for r in ALL_RUBRICS}
