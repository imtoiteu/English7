# -*- coding: utf-8 -*-
"""THE ADAPTATION LAYER — what the diagnostic results actually change.

A diagnostic that produces a number and a filed sheet of paper has changed
nothing.  This module is the part that makes the course adaptive: it turns
marks into bands, bands into groups, and specific class-level results into
specific, named, dated changes to the 92 teaching sessions.

    BANDS        where each student is placed, and what happens to them
    GAP_RULE     why a total score is not enough
    TRIGGERS     eight class results that CHANGE the programme
    BRIDGES      B1–B6, the Grade 5–6 prerequisites Grade 7 assumes
    EXTENSIONS   E1–E6, greater demand rather than more exercises
    DECISION_TREE  the order the teacher works through all of it
    CHECKPOINTS  when this happens, four times a year

Nothing here fires automatically.  `curriculum/class_profile.py` is where a
real teacher records a real class, and until they do, the course builds exactly
as it did before.
"""
from .schema import Band, Trigger, Bridge, Extension, ST, EX


# ==========================================================================
# 1 · BANDS
# ==========================================================================

BANDS = [
    Band("foundation", "Foundation — below the expected Grade 7 level", 0, 35,
         "Grade 5–6 English is not consolidated. This student is not slow; they are missing "
         "specific prerequisites, and the Grade 7 syllabus assumes those prerequisites on day one.",
         looks_like=[
             "Scores on the pre-A1 items but not the A1+ ones — the profile drops off a cliff "
             "rather than sloping.",
             "Writing: five isolated sentences, or fewer, with no connectives.",
             "Speaking: single words, long silences, or Vietnamese.",
             "Grammar: the verb 'be' and the present simple are not yet reliable, so nothing built "
             "on them can be.",
         ],
         programme=[
             "Follows the normal Grade 7 programme — the same units, the same lessons, the same "
             "class. This group is never taught a separate, lesser course.",
             "PLUS the bridging lessons B1–B6, delivered in the mode set by how big the group is "
             "(see BRIDGE_DELIVERY below).",
             "In every lesson: the ★☆☆ column of the Practice Book, the sentence-frame card, and "
             "pair-work before any whole-class answer.",
             "Homework is shortened, not simplified: three items done properly beats eight items "
             "copied.",
             "Reassessed at every checkpoint. Movement out of this band is announced to the "
             "student in those words.",
         ],
         never=[
             "Never seat this group together at the back. Mixed-ability pairing is the single "
             "cheapest intervention available to a Vietnamese classroom of 45.",
             "Never give them the same worksheet with the hard questions crossed out.",
             "Never let 'Foundation' become a name the class uses out loud.",
         ]),

    Band("core", "Core — at the expected Grade 7 level", 36, 55,
         "Ready for the normal progression. This is what the 92 sessions were written for.",
         looks_like=[
             "Solid on pre-A1 and A1, patchy on A1+, mostly lost on A2 — a slope, not a cliff.",
             "Writing: a real paragraph, with 'and' and 'because', and missing verb endings.",
             "Speaking: answers in sentences, does not yet ask questions back without prompting.",
         ],
         programme=[
             "The course as written. No changes.",
             "★★☆ as the default Practice Book column, with ★★★ offered, not assigned.",
             "The only adaptation this group needs is the class-level one: whatever triggers fired "
             "apply to them too.",
         ],
         never=[
             "Never let this group become invisible. In a class with a wide spread, the teacher's "
             "attention goes to the two ends and the middle sixty per cent coasts.",
         ]),

    Band("extension", "Extension — above the expected Grade 7 level", 56, 80,
         "Already at or near the level the course is designed to reach by June. Repeating the "
         "syllabus at them for a year is not neutral; it teaches them that English lessons are "
         "where nothing happens.",
         looks_like=[
             "Scores on the A2 items, including the inference questions.",
             "Writing: organised, with a linker beyond 'and', and some risk-taking in vocabulary.",
             "Speaking: sometimes a HIGH accuracy score with a LOW range score — the student is "
             "playing safe, and is being under-read by the total.",
         ],
         programme=[
             "The same lessons and the same class — they are not withdrawn, and they are not "
             "given the next textbook.",
             "★★★ as the default Practice Book column.",
             "The extension bank E1–E6, one activity per two units, replacing the independent-"
             "practice stage for this group only.",
             "The `EXT` recording (153 wpm) instead of the lesson recording, in Skills 2 lessons.",
             "E6 turns them into teachers in the second semester, which is the only extension "
             "activity that also helps the Foundation group.",
         ],
         never=[
             "Never 'more of the same, faster'. Twelve extra gap-fills is a punishment for being "
             "good at English.",
             "Never make them the permanent unpaid teaching assistant. E6 is a designed, bounded "
             "role with preparation time, not a way of parking them.",
         ]),
]

BANDS_BY_KEY = {b.key: b for b in BANDS}


def band_for(marks, out_of=80):
    """Which band a score falls in. Paper B (46 marks) uses the same percentages."""
    pct = 100.0 * marks / out_of
    if pct < 45:
        return BANDS_BY_KEY["foundation"]
    if pct < 70:
        return BANDS_BY_KEY["core"]
    return BANDS_BY_KEY["extension"]


# ==========================================================================
# 2 · THE RELATIVE-GAP RULE
# ==========================================================================

GAP_RULE = {
    "rule": "For each student, work out the mean of their six strand percentages. Flag any strand "
            "that is 20 or more percentage points BELOW that student's own mean.",
    "why": [
        "A band is a summary, and every summary hides something. The two students below have the "
        "same total and need opposite lessons.",
        "Student 1 — 48/80. Listening 40%, reading 45%, vocabulary 50%, grammar 50%, writing 45%, "
        "speaking 42%. Flat. This student needs the Core programme and time.",
        "Student 2 — 48/80. Listening 25%, reading 80%, vocabulary 70%, grammar 65%, writing 60%, "
        "speaking 30%. Mean 55%. Listening and speaking are flagged. This student can read Grade 8 "
        "material and cannot follow a spoken instruction. Putting them on the Core programme and "
        "waiting will not fix it.",
        "The band tells you which group. The flags tell you what to do inside it.",
    ],
    "act_on_it": [
        "Listening flagged → sit them where they can see the teacher's mouth; give the "
        "pre-listening scaffold every time; let them read the script AFTER the second play.",
        "Speaking flagged with everything else fine → this is almost always confidence. Fixed "
        "pair, sentence frames, and never nominated first.",
        "Writing flagged → the sentence-frame ladder from B6 and the Unit 1 writing scaffold, "
        "regardless of band.",
        "Vocabulary flagged → a personal word box and cumulative retrieval, not more word lists.",
        "Grammar flagged with strong reading → they have learnt English as a decoding exercise. "
        "Production tasks, not more rules.",
    ],
    "caution": "A flag on a strand where the student scored above 70% anyway is noise. Apply the "
               "rule only to strands under 70%.",
}


# ==========================================================================
# 3 · TRIGGERS — class results that change the programme
# ==========================================================================

TRIGGERS = [
    Trigger(
        "T1", "The class cannot use the past simple",
        "Fewer than 50% of the class correct on A-G3.1 and A-G3.2 (regular and irregular past), "
        "OR fewer than 50% correct on A-L3.2.",
        "Grammar items A-G3.1, A-G3.2; listening item A-L3.2; the Grammar criterion of the "
        "Writing rubric where the script contains a past-time reference.",
        "Unit 3 is where the past simple is taught, and Unit 3 assumes students have met it in "
        "Grade 6. If half the class has not, Unit 3's three lessons will be an introduction "
        "rather than a consolidation, and everything after Unit 3 that recycles the past simple "
        "will fail quietly.",
        changes=[
            "Bridging lesson B5 becomes REQUIRED for the whole class, taught in the warm-up slots "
            "of U2L5, U2L6 and U2L7 (10 minutes each) — before Unit 3 starts, not during it.",
            "U3L3 (A Closer Look 2) gains an 8-minute ADAPTIVE INSERT: the -ed/irregular sorting "
            "drill from B5, run again with the Unit 3 verbs.",
            "Unit 3 homework changes from unit-local to cumulative: every homework set from U3L1 "
            "onwards opens with five irregular verbs drawn from all previous sets.",
            "The 'wall list' gains 'Yesterday I go' as a standing entry, checked in every review.",
            "Every Skills 2 writing task in Units 3–6 must contain at least one past-time "
            "reference, so the form keeps being produced and not only recognised.",
        ],
        resources=["B5", "U3L3", "audio: D1_3 (past simple in real speech, 140 wpm)"],
        affects=["U2L5", "U2L6", "U2L7", "U3L1", "U3L2", "U3L3", "U3L5", "U3L6"],
        retire_when="Paper B item B-G1.3 is above 70% class-correct. Re-check at Paper C item "
                    "C-G3.1, which is the same construct.",
        insert_at=["U2L5", "U2L6", "U2L7", "U3L1", "U3L2", "U3L3", "U3L5", "U3L6"],
        standing="Every Skills 2 writing task in Units 3–6 must contain at least one "
                 "past-time reference, and Unit 3 homework onwards opens with five "
                 "irregular verbs drawn from all previous sets."),

    Trigger(
        "T2", "Listening is far behind reading",
        "Class mean listening percentage is 15 or more points below class mean reading percentage.",
        "Section 1 total against Section 2 total. Both are 12 marks, which is why they are.",
        "The students know the written word and not its sound. This is the most common profile in "
        "a Vietnamese class that has been taught to pass written tests, and it is invisible on any "
        "instrument that does not weigh listening and reading equally.",
        changes=[
            "Every Skills 2 lesson in Units 1–6 gains a pre-listening scaffold: three key words "
            "on the board with stress marked, plus one gist question BEFORE the first play.",
            "A third play is permitted in Units 1–6 (and only there) — after the second play and "
            "the gist check, never instead of them.",
            "First play at 0.85× speed for Units 1–4, at full speed from Unit 5. Say out loud "
            "that you are doing this and when it will stop.",
            "The `BRIDGE` recording (88 words per minute, the slowest in the corpus) is added as "
            "extra listening input in the U1 and U2 warm-up slots.",
            "Read the script aloud while students follow, AFTER the tasks are done — the course "
            "already prescribes this; with T2 firing it becomes non-negotiable.",
            "Homework gains one 'listen again at home' task per unit using the lesson's own MP3.",
        ],
        resources=["audio: BRIDGE (88 wpm)", "the pre-listening routine in Book 1 front matter"],
        affects=["every Skills 2 lesson, U1L6 through U6L6"],
        retire_when="The Paper B listening/reading gap is under 10 points. If it is still 15+ in "
                    "January, the scaffold stays for the whole second semester.",
        insert_at=["U1L6", "U2L6", "U3L6", "U4L6", "U5L6", "U6L6"],
        standing="First play at 0.85× for Units 1–4, full speed from Unit 5. Say out loud "
                 "that you are doing it and when it stops. BRIDGE (88 wpm) is extra input "
                 "in the U1 and U2 warm-up slots."),

    Trigger(
        "T3", "Final consonants are being dropped across the class",
        "Class mean on Pronunciation criterion 1 (final consonants and clusters) is below 1.0 "
        "out of 2.",
        "Section 7, criterion 1, from the read-aloud card — sentences 1 and 2 specifically.",
        "This is the single largest intelligibility cost for Vietnamese learners and it is "
        "structural, not careless: Vietnamese syllables end in a small set of unreleased sounds. "
        "It also destroys the -s and -ed endings, so it is a grammar problem wearing a "
        "pronunciation costume.",
        changes=[
            "The 30-second final-consonant drill becomes 60 seconds, every lesson, Units 1–6.",
            "Bridging lesson B6 is taught to the whole class in the first week — this trigger is "
            "the one case where a bridging lesson is worth whole-class time even if the "
            "Foundation band is small.",
            "The three -ed endings (/t/ /d/ /ɪd/) get a full extra pass in Unit 3: U3L2's "
            "pronunciation slot is extended by 5 minutes and repeated in U3L7.",
            "Every new vocabulary item on the board is written with its final sound circled.",
            "In marking written work, missing -s and -ed are recorded under BOTH the grammar tally "
            "and the pronunciation tally until January. They are usually the same error.",
        ],
        resources=["B6", "the 'add-a-sound' routine in Book 1 front matter"],
        affects=["every lesson, U1L1 through U6L7", "U3L2", "U3L7"],
        retire_when="Paper B sampled pronunciation criterion 1 mean is at or above 1.2.",
        insert_at=["U3L2", "U3L7"],
        standing="The 30-second final-consonant drill becomes 60 seconds in every lesson of "
                 "Units 1–6. B6 is taught to the whole class in the first week. Every new "
                 "word on the board has its final sound circled."),

    Trigger(
        "T4", "Vocabulary is not being retained",
        "Section 3 (vocabulary) below 50% class mean AND the Unit 1 Revision Set below 50% "
        "class mean. Both conditions, not either.",
        "Section 3 total; the Unit 1 Revision Set marks; at Paper B, section B-S3 compared with "
        "the September vocabulary percentage.",
        "One low score is a starting point, two is a retention problem. Students who learn words "
        "for Friday and cannot use them in November are being taught vocabulary as an event "
        "instead of as a habit.",
        changes=[
            "Every lesson opens with a 5-item retrieval quiz — no notes, 90 seconds, self-marked, "
            "not recorded. Retrieval, not review: they must try to remember before they are shown.",
            "Items are drawn on a spacing schedule: 2 from the last lesson, 2 from the last unit, "
            "1 from any earlier unit.",
            "Homework word boxes become cumulative. From U2 onwards each set includes three items "
            "from earlier units.",
            "Each unit's new vocabulary is capped at what actually gets recycled: if a word does "
            "not come back in a later text or task, it is presented as receptive only and is not "
            "tested.",
            "Students keep a personal word box (paper, one word per card, English one side, "
            "Vietnamese and a stress mark the other). Checked in the review blocks, not weekly.",
        ],
        resources=["the Revision Sets already in the Homework Book",
                   "the review blocks after Units 3, 6, 9, 12"],
        affects=["every lesson"],
        retire_when="Paper B section B-S3 is at or above 65% AND the Unit 6 Revision Set is above "
                    "65%. Even when retired, keep the opening retrieval quiz — it costs 90 seconds.",
        insert_at=[],
        standing="Every lesson opens with a 90-second, 5-item retrieval quiz: 2 from the last "
                 "lesson, 2 from the last unit, 1 from any earlier unit. No notes, self-marked, "
                 "not recorded. Homework word boxes become cumulative from Unit 2."),

    Trigger(
        "T5", "Third-person -s is not stable",
        "Fewer than 60% of the class correct on A-G1.3 and A-G1.4 together, or on A-V2.5.",
        "Grammar items A-G1.3, A-G1.4; vocabulary item A-V2.5 (which tests word choice and "
        "inflection at once); the Grammar criterion of the Writing rubric.",
        "'He like football' is the most persistent error in Vietnamese secondary English, because "
        "Vietnamese does not inflect verbs at all. Unit 1 reviews the present simple on the "
        "assumption it is known. If it is not, Unit 1 is teaching on sand.",
        changes=[
            "U1L3 gains a 6-minute ADAPTIVE INSERT: the HE-SHE-IT sorting drill from B2.",
            "Bridging lesson B2 is delivered to the whole class across the warm-up slots of "
            "U1L1–U1L4 (8 minutes each).",
            "The HE-SHE-IT = S chant runs daily until the end of Unit 4, then twice a week.",
            "Error correction rule for Units 1–4: a missing third-person -s is always corrected, "
            "even in a fluency stage. It is the one exception to the course's own rule, and it is "
            "worth it.",
            "In every board plan the third-person form is written in a different colour.",
        ],
        resources=["B2", "U1L3"],
        affects=["U1L1", "U1L2", "U1L3", "U1L4", "and every lesson to U4L7"],
        retire_when="Paper B item B-G1.1 and the Writing rubric grammar criterion both show the "
                    "error in under a third of scripts. Final check: Paper C item C-G1.3 and "
                    "C-V2.1, which are the same two constructs.",
        insert_at=["U1L1", "U1L2", "U1L3", "U1L4"],
        standing="The HE-SHE-IT = S chant runs daily to the end of Unit 4, then twice a week. "
                 "Until Unit 4 a missing third-person -s is corrected even in a fluency stage "
                 "— the one exception to the course's own correction rule. Third-person forms "
                 "go on the board in a second colour."),

    Trigger(
        "T6", "A third of the class is writing below sentence level",
        "30% or more of the class score 4 or below out of 14 on Section 5 (writing).",
        "Section 5 rubric scores, specifically the Grammar and Organisation criteria. Look at the "
        "distribution, not the mean — a class mean of 7 can hide fifteen students at 3.",
        "These students can produce words and cannot produce a sentence, or can produce sentences "
        "and cannot connect two. Every writing task in the course from Unit 1 onwards asks for a "
        "paragraph. Without a ladder, those students will copy for a year.",
        changes=[
            "A three-rung scaffold ladder is applied to every Skills 2 writing task in Units 1–6: "
            "rung 1 sentence frames with gaps, rung 2 the same task with the frames as a word bank "
            "only, rung 3 the free task. Students choose their rung; the rung is not assigned.",
            "Bridging lesson B6's second half (sentence building) is taught to the whole class.",
            "Every writing task gets a two-minute planning stage with three bullet notes, on the "
            "board, before anyone writes a word.",
            "The two connectives 'and' and 'because' are drilled as chunks in Units 1–2 before any "
            "other linker is introduced.",
            "Marking changes: for these students, mark ONLY task completion and organisation until "
            "January. Correcting grammar on a script that has no sentences teaches nothing.",
        ],
        resources=["B6", "the ★☆☆ column of the Practice Book"],
        affects=["U1L6", "U2L6", "U3L6", "U4L6", "U5L6", "U6L6"],
        retire_when="Under 15% of the class scores 4 or below on Paper B section B-S5.",
        insert_at=["U1L6", "U2L6", "U3L6", "U4L6", "U5L6", "U6L6"],
        standing="Every writing task gets a two-minute planning stage with three bullet notes "
                 "on the board before anyone writes. For students scoring 4 or below, mark ONLY "
                 "task completion and organisation until January."),

    Trigger(
        "T7", "The class is very widely spread",
        "Standard deviation of the 80-mark totals is greater than 12, or the gap between the 10th "
        "and 90th percentile is greater than 30 marks.",
        "The distribution of Paper A totals. Compute it — do not eyeball it.",
        "A very wide class is not a worse class, but it is a different teaching problem. Teaching "
        "to the middle in a class with a 40-mark spread means two thirds of the room is in the "
        "wrong lesson at any moment.",
        changes=[
            "Fixed mixed-ability A/B pairs for the whole term: each pair spans roughly one band. "
            "A speaks first, B explains why.",
            "The ★/★★/★★★ columns of the Practice Book become the default route rather than an "
            "option — every practice stage is run at three levels simultaneously.",
            "Every task gets a stated minimum and an open ceiling: 'at least four sentences' "
            "rather than 'four sentences'.",
            "Nominate by number, never by hands up. In a wide class, hands up is a poll of the "
            "top third.",
            "Both bridging and extension run from Unit 1. In a wide class neither is optional.",
        ],
        resources=["the ★/★★/★★★ columns already in the Practice Book",
                   "the pair-work management routine in Book 1 front matter"],
        affects=["every lesson"],
        retire_when="Never retired within the year. Re-measure the spread at Paper B: if it has "
                    "narrowed, say so to the class.",
        insert_at=[],
        standing="Fixed mixed-ability A/B pairs for the term; A speaks first, B explains why. "
                 "The ★/★★/★★★ columns become the default route, run simultaneously. Every task "
                 "gets a stated minimum and an open ceiling. Nominate by number, never by hands."),

    Trigger(
        "T8", "A quarter of the class is already above Grade 7",
        "25% or more of the class in the Extension band.",
        "The band distribution from Paper A.",
        "A large Extension group changes the economics of the lesson. With three strong students "
        "you can enrich informally; with twelve you need a designed parallel route, or you will "
        "spend the year managing boredom.",
        changes=[
            "The extension bank runs from Unit 1, not from the first free moment in Unit 4.",
            "Extension students take ★★★ as the default and are not asked to do ★★ first.",
            "In Skills 2 lessons this group listens to the `EXT` recording (153 wpm) while the "
            "class does the lesson recording — same task sheet, harder input.",
            "E6 (peer-teaching) is brought forward from Units 11–12 to Unit 7, and the group "
            "teaches one grammar slot per unit for the rest of the year.",
            "Their writing is marked against the criterion descriptors one band up. Say so.",
        ],
        resources=["E1", "E2", "E3", "E4", "E5", "E6", "audio: EXT (153 wpm)"],
        affects=["every lesson"],
        retire_when="Not retired. Re-check the band distribution at Paper B; the group usually "
                    "grows.",
        insert_at=["U1L6", "U2L6", "U3L6", "U4L6", "U5L6", "U6L6", "U7L6", "U8L6"],
        standing="The extension bank runs from Unit 1. Extension students take ★★★ as their "
                 "default and are not asked to do ★★ first. Their writing is marked against "
                 "the descriptors one band up, and they are told so. E6 starts at Unit 7."),
]

TRIGGERS_BY_CODE = {t.code: t for t in TRIGGERS}


# ==========================================================================
# 4 · BRIDGING LESSONS — for the Foundation band
# ==========================================================================

BRIDGE_DELIVERY = [
    ("More than 40% of the class in the Foundation band",
     "Teach B1–B6 as a PRE-COURSE BLOCK, six periods, before Unit 1. Yes, this costs six periods. "
     "It costs less than teaching Units 1–6 to students who cannot use the verb 'be', which is "
     "what the alternative actually is.",
     "The year becomes 100 sessions. Take the six periods from the Unit 12 project and the two "
     "spare consolidation slots, or negotiate them: a school that will not give six periods in "
     "September will lose far more than six to reteaching in March."),
    ("15–40% in the Foundation band",
     "Deliver B1–B6 as WARM-UP INSERTS inside Units 1–3 — 10 to 15 minutes at the start of "
     "selected lessons, taught to the WHOLE class.",
     "Whole class, not the Foundation group alone. The Core students lose nothing from ten "
     "minutes on the verb 'be', and nobody gets publicly sorted."),
    ("Under 15% in the Foundation band",
     "Targeted homework from the bridging exercises, plus one 10-minute clinic a week with the "
     "named students — break time, or the last ten minutes of a Looking Back lesson.",
     "Name the students privately, tell them why, and tell them when it ends. An intervention "
     "with no announced end date reads as a permanent label."),
]

BRIDGES = [
    Bridge(
        "B1", "The verb 'be', personal pronouns and possessive adjectives",
        prerequisite_for="Every unit. Nothing in Grade 7 works without this.",
        why="Unit 1 opens with 'My hobby is…' and 'I'm interested in…'. A student who writes "
            "'I student' cannot produce either, and will spend the year copying.",
        objectives=[
            "use am / is / are correctly with I, you, he, she, it, we, they",
            "use my, your, his, her, our, their before a noun",
            "write five true sentences about themselves with no missing verb",
        ],
        content=[
            "I am · you are · he/she/it is · we are · they are — as a chant with actions.",
            "Contractions: I'm, he's, she's, it's, we're, they're. Vietnamese learners often "
            "know the full form and have never used the contraction aloud.",
            "The pitfall: Vietnamese has no copula before an adjective (tôi mệt = I tired). Put "
            "the two word orders on the board side by side and leave them there.",
            "he → his · she → her · they → their. Not 'he name' but 'his name'.",
        ],
        procedure=[
            ST("Chant", 6, ["Full chant with actions, three times: point to self, to partner, "
                            "to a third person. Speed it up each time."],
               "Chant and point.", "Whole class"),
            ST("Concept check in Vietnamese", 4,
               ["Write 'Tôi mệt' and 'I tired' on the board. Ask: what is missing? Elicit 'am'.",
                "Say once, in Vietnamese if needed: English always needs the verb, even when "
                "Vietnamese does not. Then drop the Vietnamese."],
               "Spot the missing word.", "Whole class"),
            ST("Guided practice", 12, ["Exercise B1-1 then B1-2 on the board, pair-check, "
                                       "whole-class check. Students say WHY."],
               "Complete and explain.", "Pairs"),
            ST("Substitution drill", 8,
               ["Hold up a picture, students produce 'He is a teacher. His name is…'. "
                "Round the class by number, not by hands."],
               "Produce full sentences.", "Whole class"),
            ST("Independent", 10, ["Exercise B1-3. Circulate; correct missing 'be' immediately."],
               "Write five true sentences.", "Individual"),
            ST("Exit check", 5, ["Every student says one true sentence about the person next to "
                                 "them, with 'is' and a possessive."],
               "Say one sentence.", "Whole class"),
        ],
        exercises=[
            EX("B1-1", "am, is or are?", "Complete with am, is or are.",
               items=["1. I ______ twelve years old.", "2. My father ______ a farmer.",
                      "3. My sisters ______ at school.", "4. You ______ my best friend.",
                      "5. It ______ very hot today.", "6. We ______ in Class 7A.",
                      "7. Hue ______ a beautiful city.", "8. My shoes ______ new."],
               answers=["1. am", "2. is", "3. are", "4. are", "5. is", "6. are", "7. is", "8. are"],
               level="E", kind="grammar",
               note="Items 3 and 8 are the ones to watch: a plural subject with no visible -s on "
                    "the noun in Vietnamese means learners default to 'is'."),
            EX("B1-2", "my, your, his, her, our, their",
               "Complete with the correct word.",
               items=["1. This is Nam. ______ bag is black.",
                      "2. This is Mai. ______ bag is red.",
                      "3. We are in Class 7A. ______ teacher is Ms Hoa.",
                      "4. I have a dog. ______ name is Milu.",
                      "5. They are my parents. ______ names are Hung and Lan.",
                      "6. You have a new bike. Is ______ bike expensive?"],
               answers=["1. His", "2. Her", "3. Our", "4. Its", "5. Their", "6. your"],
               level="E", kind="grammar",
               note="Item 4 ('Its', no apostrophe) is included on purpose and is expected to be "
                    "wrong. Teach it, do not test it."),
            EX("B1-3", "About you", "Write five TRUE sentences about yourself and your family. "
               "Every sentence must have am, is or are.",
               items=["1. I ______", "2. My mother ______", "3. My best friend ______",
                      "4. My school ______", "5. My favourite food ______"],
               answers=["Students' own answers. Check ONE thing only: is the verb there?"],
               level="M", kind="writing", lines=6),
        ],
        success="Every student writes five sentences about themselves with no missing 'be'. "
                "If a student still drops it, they repeat B1 as homework — not B2."),

    Bridge(
        "B2", "The present simple: third-person -s, and do / does questions",
        prerequisite_for="Unit 1, and every unit that recycles the present simple (all of them).",
        why="U1L3 reviews the present simple as known. If it is not known, the review teaches "
            "nothing and the error fossilises for the year.",
        objectives=[
            "add -s / -es to the verb after he, she and it",
            "form questions with do and does",
            "form negatives with don't and doesn't",
        ],
        content=[
            "HE–SHE–IT = S. The chant, with the fist bump on S.",
            "Spelling: go → goes, watch → watches, study → studies, play → plays.",
            "Questions: Do you…? / Does he…? — and the rule that the -s moves to 'does', so the "
            "main verb loses it. 'Does he plays' is the commonest overcorrection.",
            "Negative: don't / doesn't, same rule.",
        ],
        procedure=[
            ST("Chant and sort", 8,
               ["HE-SHE-IT = S chant. Then sort twelve verb cards into +s and +es columns on "
                "the board."],
               "Chant, then sort.", "Whole class"),
            ST("Present the question form", 8,
               ["Build 'You play football.' → 'Do you play football?' on the board with arrows.",
                "Then 'He plays football.' → 'Does he play football?' Circle the S moving from "
                "the verb to 'does'. Say: only ONE S in the sentence."],
               "Copy the two transformations.", "Whole class"),
            ST("Guided", 12, ["B2-1, then B2-2. Pair-check between them."],
               "Complete and check.", "Pairs"),
            ST("Find someone who", 10,
               ["Each student gets three questions to ask five classmates. Report back: "
                "'Nam plays football. Mai doesn't play football.'"],
               "Ask, note, report.", "Mingle"),
            ST("Exit check", 7, ["B2-3 written, collected."], "Write six sentences.", "Individual"),
        ],
        exercises=[
            EX("B2-1", "Add the ending", "Write the he/she/it form.",
               items=["1. play → he ______", "2. go → she ______", "3. watch → he ______",
                      "4. study → she ______", "5. live → he ______", "6. do → she ______",
                      "7. have → he ______", "8. finish → it ______"],
               answers=["1. plays", "2. goes", "3. watches", "4. studies", "5. lives", "6. does",
                        "7. has", "8. finishes"], level="E", kind="grammar",
               note="6 and 7 are irregular and must simply be learnt. Do not let a student conclude "
                    "the rule is unreliable."),
            EX("B2-2", "Questions and negatives", "Complete with do, does, don't or doesn't.",
               items=["1. ______ you like football?", "2. ______ your sister play the piano?",
                      "3. I ______ like coffee.", "4. He ______ live in Hanoi.",
                      "5. ______ they go to your school?", "6. My mother ______ drive a car."],
               answers=["1. Do", "2. Does", "3. don't", "4. doesn't", "5. Do", "6. doesn't"],
               level="E", kind="grammar"),
            EX("B2-3", "Six sentences", "Write three sentences about YOU and three about a FRIEND. "
               "Use the present simple.",
               items=["1. I ______", "2. I ______", "3. I ______",
                      "4. My friend ______", "5. He/She ______", "6. He/She ______"],
               answers=["Students' own answers. Check ONE thing: is the -s on sentences 4–6?"],
               level="M", kind="writing", lines=7),
        ],
        success="Five out of six correct on B2-1, and the -s present in all three friend "
                "sentences of B2-3."),

    Bridge(
        "B3", "There is / there are, a / an / some, and the plural -s",
        prerequisite_for="Units 5 and 6, and every description task from Unit 1 onwards.",
        why="Vietnamese does not mark the plural on the noun, so 'three book' is not carelessness "
            "— it is the L1 rule being applied. Unit 5's countable/uncountable work is impossible "
            "without it.",
        objectives=[
            "add -s / -es to plural nouns, including the common irregulars",
            "choose a or an",
            "use there is with singular and there are with plural",
        ],
        content=[
            "one book → two books · one box → two boxes · one city → two cities.",
            "Irregulars worth teaching: children, people, men, women, feet, teeth.",
            "a + consonant sound, an + vowel sound. SOUND, not letter: an hour, a university.",
            "There is a … / There are … . The verb agrees with what comes AFTER it.",
        ],
        procedure=[
            ST("Count the room", 6,
               ["Point and elicit: one door, two windows, thirty-five chairs. Write them up with "
                "the -s in a second colour."],
               "Count aloud.", "Whole class"),
            ST("a / an sorting", 8,
               ["Sixteen word cards to the a-column or the an-column. Then add 'hour' and "
                "'university' and let the rule break, then explain it."],
               "Sort and argue.", "Groups of four"),
            ST("Guided", 12, ["B3-1 and B3-2."], "Complete and check.", "Pairs"),
            ST("Describe a picture", 12,
               ["Pairs describe a classroom picture: 'There is a…', 'There are…'. Six sentences."],
               "Describe.", "Pairs"),
            ST("Exit check", 7, ["B3-3."], "Write.", "Individual"),
        ],
        exercises=[
            EX("B3-1", "Plurals", "Write the plural.",
               items=["1. book →", "2. box →", "3. city →", "4. child →", "5. watch →",
                      "6. person →", "7. knife →", "8. day →"],
               answers=["1. books", "2. boxes", "3. cities", "4. children", "5. watches",
                        "6. people", "7. knives", "8. days"], level="E", kind="grammar"),
            EX("B3-2", "a, an or some?", "Complete with a, an or some.",
               items=["1. ______ apple", "2. ______ book", "3. ______ water",
                      "4. ______ orange", "5. ______ rice", "6. ______ hour",
                      "7. ______ umbrella", "8. ______ milk"],
               answers=["1. an", "2. a", "3. some", "4. an", "5. some", "6. an", "7. an", "8. some"],
               level="E", kind="grammar",
               note="Item 6 is the sound rule. If nobody gets it, that is fine — teach it now."),
            EX("B3-3", "There is / There are", "Write six sentences about your classroom.",
               items=["Use There is … three times and There are … three times."],
               answers=["Students' own answers. Check: singular after 'is', plural after 'are', "
                        "and the -s on the plural noun."],
               level="M", kind="writing", lines=7),
        ],
        success="Six out of eight on B3-1, and the plural -s present in all three 'There are' "
                "sentences."),

    Bridge(
        "B4", "Question words and question word order",
        prerequisite_for="Units 1 and 9, and every speaking task in the course.",
        why="Every Communication lesson asks students to ask each other questions. A student who "
            "cannot form one participates by answering only, for a year.",
        objectives=[
            "choose the right question word for the information wanted",
            "put the auxiliary before the subject",
            "ask three questions of a classmate without a written model",
        ],
        content=[
            "What · Where · When · Who · Why · How · How many · How often.",
            "The order: QUESTION WORD + do/does/is/are + SUBJECT + VERB. Build it as a physical "
            "line of students holding word cards, then swap two of them.",
            "The pitfall: Vietnamese keeps statement order and marks the question with a particle. "
            "'You go where?' is the L1 shape and is very persistent.",
        ],
        procedure=[
            ST("Question word matching", 7,
               ["Eight answers on the board; students supply the question word."],
               "Match.", "Whole class"),
            ST("Human sentence", 10,
               ["Five students hold word cards and stand in statement order. Physically swap two "
                "to make the question. Repeat with three different sentences."],
               "Be a word; move.", "Whole class"),
            ST("Guided", 12, ["B4-1 and B4-2."], "Complete and check.", "Pairs"),
            ST("Interview", 10,
               ["Each student writes three questions, then interviews two classmates and reports "
                "one answer to the class."],
               "Write, ask, report.", "Mingle"),
            ST("Exit check", 6, ["Each student asks the teacher one correctly-formed question."],
               "Ask.", "Whole class"),
        ],
        exercises=[
            EX("B4-1", "Which question word?", "Complete with What, Where, When, Who, Why or How.",
               items=["1. ______ is your name?", "2. ______ do you live?",
                      "3. ______ do you go to bed?", "4. ______ is your teacher?",
                      "5. ______ do you like English?", "6. ______ old are you?",
                      "7. ______ many brothers do you have?",
                      "8. ______ often do you play football?"],
               answers=["1. What", "2. Where", "3. When", "4. Who", "5. Why", "6. How",
                        "7. How", "8. How"], level="E", kind="grammar"),
            EX("B4-2", "Put it in order", "Put the words in the correct order to make a question.",
               items=["1. you / where / live / do / ?", "2. does / what / your father / do / ?",
                      "3. is / how old / your sister / ?",
                      "4. do / go / how / to school / you / ?",
                      "5. your / what / favourite / is / subject / ?",
                      "6. often / how / you / do / watch TV / ?"],
               answers=["1. Where do you live?", "2. What does your father do?",
                        "3. How old is your sister?", "4. How do you go to school?",
                        "5. What is your favourite subject?", "6. How often do you watch TV?"],
               level="M", kind="grammar",
               note="If more than half the class produces 'You live where?' the human-sentence "
                    "stage needs repeating before you move on. Do not just mark it wrong."),
        ],
        success="Five out of six on B4-2, and one correctly-formed spoken question each."),

    Bridge(
        "B5", "The past simple: was/were, regular -ed, and the top twenty irregulars",
        prerequisite_for="Unit 3, and everything after it that recycles the past.",
        why="Unit 3 teaches the past simple in three lessons on the assumption that Grade 6 "
            "introduced it. This is the bridging lesson that trigger T1 makes compulsory.",
        objectives=[
            "use was and were correctly",
            "form the past of regular verbs with -ed and pronounce the three endings",
            "recognise and produce twenty common irregular past forms",
        ],
        content=[
            "was / were — and the fact that the past is marked ONCE, on the verb, not on every "
            "word in the sentence.",
            "-ed spelling: play → played, live → lived, study → studied, stop → stopped.",
            "-ed sound: /t/ after voiceless (helped, worked, watched), /d/ after voiced (played, "
            "cleaned, lived), /ɪd/ after t or d (visited, wanted, needed). This is the single "
            "highest-value pronunciation point in the year.",
            "Top twenty irregulars: go/went, have/had, do/did, see/saw, get/got, make/made, "
            "come/came, take/took, eat/ate, give/gave, buy/bought, think/thought, say/said, "
            "tell/told, find/found, leave/left, meet/met, write/wrote, read/read, sit/sat.",
            "The pitfall: with a past time word present, students often leave the verb in the "
            "present ('Yesterday I go'). Vietnamese marks past with a particle and leaves the "
            "verb alone, so this is the L1 rule showing through.",
        ],
        procedure=[
            ST("Yesterday line", 6,
               ["Draw a timeline. Say five things you did yesterday. Students repeat, then say "
                "one thing each."],
               "Listen, repeat, produce.", "Whole class"),
            ST("The -ed sound sort", 10,
               ["Fifteen -ed verbs, three columns: /t/ /d/ /ɪd/. Say each one, students point to "
                "the column. Then they sort cards in fours."],
               "Listen and sort.", "Groups of four"),
            ST("Irregular pairs drill", 8,
               ["Twenty pairs, called and answered: teacher 'go', class 'went'. Twice through, "
                "then half the class calls and half answers."],
               "Call and answer.", "Whole class"),
            ST("Guided", 12, ["B5-1 and B5-2."], "Complete and check.", "Pairs"),
            ST("Exit check", 9, ["B5-3, collected. Then each student says one true past sentence."],
               "Write and say.", "Individual"),
        ],
        exercises=[
            EX("B5-1", "was or were?", "Complete with was or were.",
               items=["1. I ______ at home yesterday.", "2. They ______ very tired.",
                      "3. It ______ hot last Sunday.", "4. We ______ in Hue last summer.",
                      "5. My brother ______ ill last week.", "6. You ______ late this morning."],
               answers=["1. was", "2. were", "3. was", "4. were", "5. was", "6. were"],
               level="E", kind="grammar"),
            EX("B5-2", "The past simple", "Write the past form.",
               items=["1. play →", "2. study →", "3. stop →", "4. go →", "5. have →",
                      "6. see →", "7. eat →", "8. buy →", "9. visit →", "10. take →"],
               answers=["1. played", "2. studied", "3. stopped", "4. went", "5. had", "6. saw",
                        "7. ate", "8. bought", "9. visited", "10. took"],
               level="E", kind="grammar"),
            EX("B5-3", "Last weekend", "Write five sentences about last weekend. Use at least two "
               "regular verbs and two irregular verbs.",
               items=["Begin: Last weekend I ______"],
               answers=["Students' own answers. Check ONE thing: is every verb in the past?"],
               level="M", kind="writing", lines=7,
               note="Underline every present-tense verb but do not correct it. Count them. That "
                    "count is your T1 evidence for the class."),
        ],
        success="Eight out of ten on B5-2, and no present-tense verbs in B5-3."),

    Bridge(
        "B6", "Sound to spelling: final consonants, the -ed endings, and word stress",
        prerequisite_for="Units 2 and 3, and every pronunciation slot in the course.",
        why="Trigger T3 makes this whole-class. It is also the bridging lesson with the widest "
            "reach: fixing final consonants fixes plurals, third-person -s and past -ed at once, "
            "because they are all the same sound problem.",
        objectives=[
            "produce a final consonant audibly",
            "produce the three -ed endings",
            "hear and mark the stressed syllable in a three-syllable word",
        ],
        content=[
            "The add-a-sound routine: boo → book, li → like, fine → finds. Feel the tongue or "
            "lips stop the air. Hand on throat for the voiced ones.",
            "Clusters: /sk/ /st/ /nd/ /ks/. Break it, then rebuild: s-k-oo-l → skool.",
            "-ed: /t/ /d/ /ɪd/, as in B5.",
            "Stress bubbles: Oo (TEAcher), oO (aBOUT), Ooo (PHOtograph), ooO (voluntEER). Clap it.",
            "Say plainly: Vietnamese syllables end in a small set of unreleased sounds and every "
            "syllable carries equal weight. This is not carelessness, it is a different sound "
            "system, and it takes months, not minutes.",
        ],
        procedure=[
            ST("Add a sound", 8,
               ["Ten pairs: boo/book, li/like, fine/finds, ni/nine, ba/bag, sea/seat…",
                "Choral, then rows, then individuals. Hand gesture for the final stop."],
               "Repeat and feel.", "Whole class"),
            ST("Minimal pair race", 8,
               ["Two columns on the board. Say one word; teams point. Ten rounds."],
               "Listen and point.", "Teams"),
            ST("-ed three columns", 10, ["As B5, but produced rather than sorted."],
               "Produce.", "Whole class"),
            ST("Stress bubbles", 10,
               ["Twelve words. Clap the stress, draw the bubble, then students draw their own."],
               "Clap and draw.", "Pairs"),
            ST("Exit check", 9,
               ["Each student reads two sentences from the read-aloud card aloud. Note criterion 1 "
                "only. This is a teaching check, NOT a re-test — do not record it as a score."],
               "Read aloud.", "Individual"),
        ],
        exercises=[
            EX("B6-1", "Final sounds", "Read each pair aloud. Then circle the word your partner says.",
               items=["1. boo / book", "2. li / like", "3. fine / finds", "4. ba / bag",
                      "5. sea / seat", "6. why / wife", "7. no / nose", "8. play / played"],
               answers=["A speaking and listening task — no written answer. Success is the partner "
                        "circling correctly more than six times out of eight."],
               level="E", kind="pron"),
            EX("B6-2", "The three -ed endings", "Write each verb in the correct column: "
               "/t/, /d/ or /ɪd/.",
               wordbank=["helped", "played", "visited", "watched", "cleaned", "wanted", "worked",
                         "lived", "needed", "stopped", "opened", "started"],
               items=["/t/ ______", "/d/ ______", "/ɪd/ ______"],
               answers=["/t/ helped, watched, worked, stopped",
                        "/d/ played, cleaned, lived, opened",
                        "/ɪd/ visited, wanted, needed, started"],
               level="M", kind="pron",
               note="The rule is about the sound before the ending, not the letter. Do not give "
                    "the rule first — let them sort, then extract it."),
            EX("B6-3", "Where is the stress?", "Mark the stressed syllable: Oo, oO, Ooo or ooO.",
               items=["1. teacher", "2. about", "3. photograph", "4. volunteer", "5. delicious",
                      "6. hobby", "7. computer", "8. afternoon"],
               answers=["1. Oo", "2. oO", "3. Ooo", "4. ooO", "5. oOo", "6. Oo", "7. oOo",
                        "8. ooO"], level="M", kind="pron"),
        ],
        success="Six out of eight correct on the B6-1 partner check, and a final consonant audible "
                "in the exit read-aloud."),
]

BRIDGES_BY_CODE = {b.code: b for b in BRIDGES}


# ==========================================================================
# 5 · EXTENSION BANK — for the Extension band
# ==========================================================================

EXTENSION_RULES = [
    "Different demand, never more volume. Twelve extra gap-fills is a punishment for being good "
    "at English, and students read it exactly that way.",
    "Each activity replaces the independent-practice stage for this group. It does not replace "
    "the lesson, and it does not remove them from the class.",
    "Every activity ends in something the rest of the class sees or hears. Extension work done "
    "in private stops being motivating within a month.",
    "The task is open at the top. 'At least three arguments' has a ceiling of infinity; "
    "'three arguments' has a ceiling of three.",
    "They are still assessed on the course rubrics — but read one band up, and tell them that.",
]

EXTENSIONS = [
    Extension(
        "E1", "Class survey and data report", "1–2",
        demand="Collect real data, quantify it, and report it in English. The core lesson asks "
               "them to say how often THEY do something; this asks them to say how often "
               "THIRTY-FIVE people do, which forces frequency adverbs, plural agreement and "
               "quantifiers into production rather than recognition.",
        steps=[
            "Write four survey questions about hobbies or health habits, with the teacher checking "
            "the question forms before you start.",
            "Survey at least fifteen classmates during the Communication lesson.",
            "Tally the results. Work out how many, and roughly what fraction.",
            "Write a report of 80–100 words: 'Twelve students out of fifteen play a sport. Most of "
            "them play football. Only two students never do any exercise.'",
            "Present the findings to the class in 90 seconds, with the tally chart on the board.",
        ],
        output="A 90-second presentation and an 80–100 word written report.",
        assess="The Writing rubric, read one band up. Additionally: are the quantifiers accurate "
               "against their own tally? That is the part the core task cannot test.",
        resources=["U1L4 Communication", "U2L4 Communication"],
        minutes="Across two lessons plus homework"),

    Extension(
        "E2", "Opinion paragraph with concession", "3–4",
        demand="Hold two ideas in tension in one paragraph. 'Although' and 'however' are Unit 8 "
               "language, brought forward — not to run ahead of the syllabus, but because this "
               "group is already writing paragraphs that need them and is using 'but' four times "
               "instead.",
        steps=[
            "Read the model: one paragraph, opinion, two supports, one concession, restated "
            "opinion.",
            "Learn the two shapes: 'Although X, Y.' and 'X. However, Y.' Note the comma and the "
            "full stop — they are different, and both are usually got wrong first time.",
            "Choose a topic with a real second side: school uniform, mobile phones at school, "
            "homework at the weekend, community-service days.",
            "Write 100–120 words including at least one concession.",
            "Swap with another Extension student. Mark each other against the checklist, then "
            "rewrite once.",
        ],
        output="A 100–120 word opinion paragraph, peer-reviewed and rewritten.",
        assess="The Writing rubric, one band up, with an extra look at Organisation: does the "
               "concession actually concede something, or is it decoration?",
        resources=["U3L6 Skills 2", "U4L6 Skills 2", "the Unit 8 grammar box, brought forward"],
        minutes="One lesson's independent-practice stage plus homework"),

    Extension(
        "E3", "Ninety-second vlog script", "5–6",
        demand="Write for the ear rather than the eye, then perform it. Scripting forces choices "
               "about rhythm and stress that written tasks never surface, and recording makes "
               "pronunciation self-correcting in a way teacher feedback does not.",
        steps=[
            "Choose: a favourite dish and how to make it, or a tour of your school for a visitor.",
            "Write a 90-second script — about 150 words at the speed of the course recordings.",
            "Mark the script up: underline the stressed word in each sentence, slash the pauses.",
            "Rehearse three times against a timer. Ninety seconds means ninety seconds.",
            "Record on a phone if one is available; perform live to the class if not. Either is "
            "acceptable and no student is required to own a phone.",
            "Peer-review against the checklist: Was it 90 seconds? Could you hear every final "
            "sound? Was there one clear idea per sentence?",
        ],
        output="A 90-second recorded or performed vlog, plus the marked-up script.",
        assess="The Speaking and Pronunciation rubrics together, one band up. The marked-up "
               "script is assessed for whether the stress marks are right, not whether they were "
               "followed.",
        resources=["U5L4 Communication", "U6L6 Skills 2"],
        minutes="Two independent-practice stages plus homework"),

    Extension(
        "E4", "Structured debate", "7–8",
        demand="Argue a position that is not yours, and answer an argument you did not anticipate. "
               "Every speaking task in the course is cooperative; this is the first one that is "
               "not, and it needs a different set of language.",
        steps=[
            "The motion is given a week ahead: 'This class believes students should not use "
            "motorbikes to come to school' or 'This class believes films are better than books'.",
            "Sides are ASSIGNED, not chosen. Arguing the side you disagree with is the point.",
            "Prepare three arguments with one piece of evidence each.",
            "Learn the rebuttal frames: 'I understand that…, but…', 'That may be true, however…', "
            "'Can you explain why…?'",
            "Debate: 2 minutes each side, then 2 minutes of rebuttal, then the class votes.",
            "Afterwards, each debater writes 60 words on the strongest argument the OTHER side "
            "made.",
        ],
        output="A four-minute debate and a 60-word written reflection.",
        assess="The Speaking rubric one band up, with Range weighted most heavily — rebuttal is "
               "where range shows. The reflection is assessed on whether it steelmans the other "
               "side honestly.",
        resources=["U7L4 Communication", "U8L5 Skills 1"],
        minutes="One full Communication lesson plus preparation homework"),

    Extension(
        "E5", "Research summary from an authentic source", "9–10",
        demand="Take real, unsimplified input at 153 words per minute and render it in their own "
               "words. Everything else in the course is graded for them. This is not, and the "
               "gap between understanding something and re-expressing it is exactly the gap this "
               "group needs to feel.",
        steps=[
            "Listen to the `EXT` recording (VOA, 'I Was Minding My Own Business', 3:01, 153 wpm) "
            "twice, without the script.",
            "Write down what happened, in order, in note form. Notes, not sentences.",
            "Listen once more with the script and correct your notes in a different colour.",
            "Write a 100-word summary IN YOUR OWN WORDS. Copied phrases from the script score "
            "nothing.",
            "Find the past continuous in the script ('I was minding', 'she was hitting'). Work "
            "out for yourself what it is doing that the past simple does not. Write one sentence "
            "explaining it.",
        ],
        output="A 100-word summary and a one-sentence grammatical observation.",
        assess="The Writing rubric one band up. The observation is not marked for correctness — "
               "it is marked for whether they noticed something real. A wrong but genuine "
               "observation beats a right one copied from a grammar book.",
        resources=["audio: EXT (153 wpm)", "U9L6 Skills 2", "U10L6 Skills 2"],
        minutes="One lesson plus homework"),

    Extension(
        "E6", "Peer-teaching a grammar slot", "11–12",
        demand="Teach it. This is the only extension activity that also raises the Foundation "
               "group's outcomes, and it is the hardest one — explaining the third-person -s to "
               "somebody who does not have it requires understanding it far better than using it "
               "does.",
        steps=[
            "Pairs of Extension students are given one grammar point from an earlier unit — the "
            "one the class actually got wrong, from the trigger list.",
            "Prepare a 10-minute slot: one explanation, one board example, one two-minute "
            "activity, one check question. The teacher approves the plan before it is taught.",
            "Teach it to a group of six, not to the whole class. Six is teachable; forty-five is "
            "a performance.",
            "The teacher observes and says nothing during the slot.",
            "Afterwards: what did the group get wrong, and what would you change? Written, "
            "60 words.",
            "If trigger T8 fired, this starts at Unit 7 and runs once per unit to the end of "
            "the year.",
        ],
        output="A taught 10-minute slot, plus a 60-word written reflection.",
        assess="Not on a rubric. Assessed on whether the six students could do the check question "
               "at the end. That is the only measure of teaching that means anything.",
        resources=["any earlier unit's grammar box", "the trigger list", "the wall list of errors"],
        minutes="10 minutes per unit, plus preparation"),
]

EXTENSIONS_BY_CODE = {e.code: e for e in EXTENSIONS}


# ==========================================================================
# 6 · CHECKPOINTS — when adaptation happens
# ==========================================================================

CHECKPOINTS = [
    ("Checkpoint 0", "after period 2",
     "Provisional banding from the 60 written marks of Paper A.",
     ["Band every student provisionally. Do not tell them yet — speaking data is missing and it "
      "moves people.",
      "Compute the class aggregates and see which triggers fire on written evidence alone: "
      "T1, T2, T4, T5, T6, T7, T8 can all be evaluated now.",
      "If T2 fires, start the listening scaffold IMMEDIATELY, in U1L1. It costs nothing to be "
      "wrong about this and a lot to be late.",
      "Decide the bridging delivery mode from the provisional Foundation count."]),

    ("Checkpoint 1", "after period 9 (end of Unit 1)",
     "The real one. Full six-strand profile including speaking and pronunciation.",
     ["Confirm bands. Some students move — a student who wrote nothing and speaks fluently is "
      "not Foundation.",
      "Evaluate all eight triggers, including T3, which needs the pronunciation data.",
      "Fill in curriculum/class_profile.py and rebuild the books. The adaptive inserts appear in "
      "the lesson plans from Unit 2 onwards.",
      "Give every student their profile card. Name one strength and one target, in that order.",
      "Tell the Foundation students what the bridging work is, and when it ends.",
      "Start the extension bank if T8 fired."]),

    ("Checkpoint 2", "after period 48 (Paper B, mid-year)",
     "Did the adaptations work?",
     ["Re-band on percentages. Announce every student who moved up, by name, to them.",
      "For each fired trigger: closed, closing, or not moved? Use the stated retire_when.",
      "A trigger that has not moved after a semester means the intervention was wrong, not that "
      "the students were. Change the intervention.",
      "Retire what has closed. Keep the T4 retrieval quiz whatever happens — it costs 90 seconds.",
      "Update class_profile.py and rebuild."]),

    ("Checkpoint 3", "after periods 93–94 (Paper C, final)",
     "The handover.",
     ["Report per strand and per rubric criterion, never as one number.",
      "Write the Grade 8 handover: which triggers closed, which did not, which students are "
      "still Foundation and what specifically they still need.",
      "Give every student their September script next to their May script, stapled. Say nothing "
      "for a minute.",
      "Write down what you would change about the diagnostic itself. You now know which items "
      "discriminated and which were dead weight."]),
]


# ==========================================================================
# 7 · THE DECISION TREE
# ==========================================================================

DECISION_TREE = [
    ("1. Mark Paper A and enter the six strand percentages per student.",
     ["Written sections within four days of the test.",
      "Speaking and pronunciation as the rolling assessment completes, by period 9."]),

    ("2. Band each student on the 80-mark total.",
     ["Under 45% → Foundation.  45–69% → Core.  70% and above → Extension.",
      "Then apply the relative-gap rule and flag the strands. The band decides the group; the "
      "flags decide what happens inside it."]),

    ("3. Count the Foundation band and choose the bridging delivery mode.",
     ["Over 40% → B1–B6 as a pre-course block, before Unit 1.",
      "15–40% → B1–B6 as whole-class warm-up inserts inside Units 1–3.",
      "Under 15% → targeted homework plus a weekly ten-minute clinic."]),

    ("4. Compute the class aggregates and test all eight triggers.",
     ["Do this arithmetically, from the item-level totals. A trigger you decide has fired because "
      "the class 'feels weak' is not a trigger, it is a mood.",
      "Record which fired and which did not. The ones that did NOT fire matter too — they are "
      "what you tell the head of department when asked why you did not change more."]),

    ("5. Apply every fired trigger's changes, in the lessons it names.",
     ["Write them into curriculum/class_profile.py and rebuild. The inserts then appear in the "
      "Teacher's Coursebook in the right lessons, so you are not remembering them in March.",
      "If two triggers touch the same lesson, both inserts apply — the lesson runs long, and you "
      "cut the warm-up, not the insert."]),

    ("6. Count the Extension band.",
     ["25% or more → T8 has fired; the extension bank runs from Unit 1.",
      "Under 25% → the bank still runs, one activity per two units, for the named students."]),

    ("7. Teach the programme as adapted.",
     ["Units 1–12 as written, plus the inserts, plus the bridging mode, plus the extension bank.",
      "Do not re-plan continuously. The next scheduled change is Checkpoint 2, in January."]),

    ("8. At Paper B, re-band and re-test every trigger.",
     ["Closed → retire it and say so to the class.",
      "Closing → keep it for one more semester.",
      "Not moved → the intervention was wrong. Change the intervention, not the target."]),

    ("9. At Paper C, report growth per strand and write the handover.",
     ["Per strand, per criterion, against September. Never one number.",
      "Name what did not work. A handover that says everything went well is worth nothing to the "
      "Grade 8 teacher."]),
]


# ==========================================================================
# 8 · WHAT THIS SYSTEM WILL NOT DO
# ==========================================================================

LIMITS = [
    "It will not stream the class. Every student stays in every lesson; the bands change what "
    "they do inside it, not which room they are in.",
    "It will not produce a CEFR certificate. The bands are teaching decisions calibrated to this "
    "course, not to an external scale, and calling them A1 or A2 on a report would be a claim "
    "this instrument cannot support.",
    "It will not equate Papers A and C statistically. They are structurally parallel and matched "
    "on speech rate; that supports 'her listening improved', not 'she improved by 11.4 marks'.",
    "It will not survive being marked late. A diagnostic marked in week four has already lost the "
    "three weeks of teaching it existed to change.",
    "It will not work if the results are read as a judgement on the students. They are a "
    "description of what has been taught so far, which is not the same thing and is not their "
    "responsibility.",
]
