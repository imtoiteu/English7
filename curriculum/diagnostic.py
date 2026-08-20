# -*- coding: utf-8 -*-
"""THE DIAGNOSTIC PAPERS — A (initial), B (mid-year), C (final).

Calibration is the whole design problem here.  Grade 7 entry under the MOET
framework is consolidated A1 moving to A1+; the course targets A1+ → A2.  So
the papers span pre-A1 → A2, weighted roughly 40% below level, 40% at level,
20% above.

Weighting the FLOOR is the single most important decision in this file.  A
paper that only discriminates at A2 produces a wall of low scores and tells the
teacher nothing about what to reteach.  Every task below carries a `band`, and
every item carries `band` and `tests`, because a wrong answer is only useful if
you know what it was a wrong answer to.

Marks
    Paper A   60 written + 20 oral = 80
    Paper B   46 written; oral sampled and reported separately
    Paper C   60 written + 20 oral = 80, a parallel form of Paper A

Papers A and C are placement instruments and must discriminate at the bottom, so
at least 45% of their objective items sit at or below A1.  Paper B is doing a
different job — it measures movement on content that has actually been taught in
Units 1-6 — so its floor is deliberately higher (about a third of its objective
items).  It still carries enough floor to re-band a student who is still
Foundation in January, which is the one thing it must not miss.

Papers A and C are STRUCTURALLY parallel — same sections, same mark
allocation, same task types, same rubrics, listening matched on words per
minute.  They are not statistically equated, and nothing in this course claims
they are.  Progress is read per strand as a percentage, never as a raw-total
difference.

The listening stimuli are real published recordings; see
`curriculum/audio_diagnostic.py`.  Reading texts are written for this course.
"""
from .schema import IT, TA, SEC, Paper
from .audio_diagnostic import DIAG_AUDIO, DIAG_FILES


# ==========================================================================
# PAPER A — INITIAL DIAGNOSTIC
# Periods 1 and 2, first week of the school year
# ==========================================================================

# --------------------------------------------------------------------------
# A · Section 1 — LISTENING  (12 marks, 12 minutes)
# --------------------------------------------------------------------------
A_L1 = TA(
    "A-L1", "Where are you?", "Listen to Anna and Marsha in a house. Answer the questions.",
    audio_key="D1_1", plays=2, band="pre-A1 / A1",
    items=[
        IT(1, "Where is Marsha at the beginning of the recording?",
           "A — at her friend's house", band="pre-A1", tests="listening for gist",
           options=["A. at her friend's house", "B. at school", "C. at Anna's house"],
           note="Anna says it in the first line. A student who misses this is not listening for "
                "meaning at all yet."),
        IT(2, "Write TWO things they do in the kitchen.", "cook / eat (both needed)",
           band="A1", tests="listening for detail; everyday verbs",
           note="Marsha: 'We cook in the kitchen.' Anna: 'I eat in the kitchen.' One mark only if "
                "both verbs are there."),
        IT(3, "Which room do they relax in?", "the living room",
           band="pre-A1", tests="listening for detail; rooms of a house"),
        IT(4, "Complete the sentence you hear: “I ______ in the bathroom.”", "wash",
           band="A1", tests="noticing the verb form in connected speech",
           note="The word is short and unstressed. Students who write 'washing' have heard it but "
                "not the form — half a mark is not available, but note it: it is T5 evidence."),
    ])

A_L2 = TA(
    "A-L2", "Come over to my place",
    "Listen to Anna and Ashley on the telephone. Answer the questions.",
    audio_key="D1_2", plays=2, band="A1",
    items=[
        IT(1, "Why does Ashley telephone Anna?",
           "B — she cannot find Anna's apartment / she needs directions",
           band="A1", tests="listening for gist",
           options=["A. She is going to be late.", "B. She cannot find the apartment.",
                    "C. She wants to buy coffee."]),
        IT(2, "Put the directions in the order you hear them: "
              "go straight ahead · turn left · turn right",
           "turn right → turn left → go straight ahead",
           band="A1", tests="listening for sequence; directions",
           note="All three must be in the right order for the mark. This item separates students "
                "who catch content words from students who catch the order they came in."),
        IT(3, "Anna's apartment is across from a ______.", "big department store",
           band="A1", tests="listening for detail; prepositions of place",
           note="Accept 'department store'."),
        IT(4, "How many coffee shops are there?", "three",
           band="pre-A1", tests="listening for a number"),
    ])

A_L3 = TA(
    "A-L3", "I can't come in",
    "Listen to Anna telephone her boss, Ms Weaver. Answer the questions.",
    audio_key="D1_3", plays=2, band="A2",
    excerpt="Play 0:00–1:20 only. Stop after Anna says “I'll call right now. I'm calling my doctor.”",
    items=[
        IT(1, "Why does Anna telephone Ms Weaver?",
           "To say she cannot come to work (because she is sick).",
           band="A1+", tests="listening for gist"),
        IT(2, "Write TWO things Anna did yesterday.",
           "any two of: painted (for hours) · cut wood · built a fire",
           band="A2", tests="listening for detail; past simple, irregular verbs",
           note="The three verbs come in one fast run. Students who write present-tense forms "
                "(paint, cut, build) heard the content but not the tense — record that separately, "
                "it is direct T1 evidence."),
        IT(3, "What did Ms Weaver do when she had the flu? Write TWO things.",
           "She slept a lot. She drank a lot of water.",
           band="A2", tests="listening for detail; irregular past forms"),
        IT(4, "What advice does Ms Weaver give Anna?",
           "She should call her doctor (and get lots of rest).",
           band="A2", tests="listening for function: advice with should",
           note="Accept either half. Reporting it as 'You should call your doctor' is fine."),
    ])

A_S1 = SEC("A-S1", "Listening", "listening", 12, 12, 1,
           "You will hear three recordings. You will hear each one TWICE. "
           "Write your answers on the question paper.",
           tasks=[A_L1, A_L2, A_L3],
           admin=[
               "Play from the local MP3 files. Do not read the scripts aloud — the whole point of "
               "this section is that every student hears the same authentic delivery at the same speed.",
               "Before each recording give 30 seconds to read the questions. Say the number of the "
               "task clearly.",
               "Play twice, with a 20-second gap between plays and 30 seconds after the second play.",
               "Do NOT play a third time, even if the class asks. A third play is a teaching act; "
               "today you are measuring.",
               "Task 3 is an excerpt. Watch the counter and stop it on the cue line — playing past "
               "it gives away the answer to nothing but wastes 2 minutes.",
           ],
           reads="Listening comprehension at three calibrated speeds: 104, 108 and 140 words per "
                 "minute. The gap between a student's score on task 1 and task 3 is more "
                 "informative than the total.")


# --------------------------------------------------------------------------
# A · Section 2 — READING  (12 marks, 14 minutes)
# --------------------------------------------------------------------------
A_R1 = TA(
    "A-R1", "Class 7A noticeboard", "Read the noticeboard and answer the questions.",
    band="pre-A1", text_title="CLASS 7A — NOTICEBOARD",
    text=[
        "MONDAY TIMETABLE",
        "7:30 English   ·   8:20 Maths   ·   9:10 Science",
        "",
        "FOOTBALL CLUB",
        "Every Wednesday, 4 p.m., on the school field. All students welcome.",
        "",
        "SCHOOL TRIP — Friday 12 October",
        "Bring: water, a hat, and 50,000 VND. Do not bring food.",
        "",
        "REMEMBER: No mobile phones in the classroom.",
    ],
    items=[
        IT(1, "What time does English start on Monday?", "7:30 / half past seven",
           band="pre-A1", tests="reading for a specific number"),
        IT(2, "When is football club?", "(every) Wednesday at 4 p.m.",
           band="pre-A1", tests="reading for day and time",
           note="Both day and time needed for the mark."),
        IT(3, "Write TWO things you must bring on the school trip.",
           "any two of: water · a hat · 50,000 VND",
           band="pre-A1", tests="reading a list"),
        IT(4, "TRUE or FALSE: You can use your mobile phone in the classroom.",
           "FALSE", band="A1", tests="reading a negative instruction",
           note="The commonest wrong answer is TRUE, from students who saw 'mobile phones' and "
                "stopped reading. That is a reading-strategy problem, not a vocabulary one."),
    ])

A_R2 = TA(
    "A-R2", "An email from a new friend", "Read Linh's email and answer the questions.",
    band="A1", text_title="From: linh.nguyen@email.vn   ·   Subject: Hello from Hue!",
    text=[
        "Hi Nam,",
        "My name is Linh and I am twelve years old. I live in Hue with my parents and my "
        "younger brother, Duc. He is eight.",
        "I go to school by bike. It takes fifteen minutes. My favourite subject is English "
        "because we sing songs in the lessons and the teacher is very funny. I don't like "
        "Maths very much.",
        "After school I play badminton with my friends on Tuesday and Thursday. At the weekend "
        "I help my mother in the garden. I don't like getting up early, but on Sunday I get up "
        "at six o'clock to go to the market with her.",
        "Please write to me and tell me about your school.",
        "Your friend,",
        "Linh",
    ],
    items=[
        IT(1, "Who does Linh live with?", "her parents and her younger brother (Duc)",
           band="A1", tests="reading for detail; family words",
           note="'Her family' alone is not enough — the text is specific."),
        IT(2, "How does Linh go to school?", "by bike / by bicycle",
           band="pre-A1", tests="reading for detail; means of transport"),
        IT(3, "Why does Linh like English? Give ONE reason.",
           "they sing songs in the lessons / the teacher is very funny",
           band="A1", tests="reading for reason; because-clause"),
        IT(4, "Linh says she does not like getting up early. When does she get up at six o'clock, "
              "and why?",
           "On Sunday, to go to the market with her mother.",
           band="A1+", tests="reading across a contrast (but); two-part answer",
           note="Needs both halves. This is the first item in the paper that asks a student to "
                "hold two pieces of information together."),
    ])

A_R3 = TA(
    "A-R3", "The Saturday that changed 7B", "Read the text and answer the questions.",
    band="A2", text_title="The Saturday that changed 7B",
    text=[
        "Last April, the students of class 7B did something they had never done before. Their "
        "teacher, Ms Hoa, showed them a photograph of the small canal behind the school. It was "
        "full of plastic bags, bottles and old shoes. Nobody in the class said anything.",
        "“I walk past it every day,” said Mai. “I never really looked at it.”",
        "The next Saturday, twenty-eight students met at the school gate at seven o'clock in the "
        "morning. They wore old clothes and gloves. Ms Hoa brought forty rubbish bags. It was hot, "
        "and the work was harder than they expected. By eleven o'clock they were tired and dirty, "
        "and they had filled thirty-one bags.",
        "Then something happened that nobody planned. Three women from the houses along the canal "
        "came out with cold water and bread for the students. One of them, Mrs Tam, said she had "
        "wanted to clean the canal for years, but she could not do it alone.",
        "Class 7B now goes to the canal on the first Saturday of every month. Mrs Tam and her "
        "neighbours come too. Mai says it is still hard work, but she does not mind it now.",
    ],
    items=[
        IT(1, "What is the text mainly about?",
           "C — a class that started cleaning a canal and kept doing it",
           band="A2", tests="reading for main idea",
           options=["A. a teacher who takes photographs",
                    "B. a school that is next to a dirty canal",
                    "C. a class that started cleaning a canal and kept doing it",
                    "D. three women who live near a canal"],
           note="B is the trap: it is true, but it is not what the text is about. Students who "
                "choose B are reading for facts rather than for the point."),
        IT(2, "How many rubbish bags did the students fill, and how many did Ms Hoa bring?",
           "They filled thirty-one; she brought forty.",
           band="A1+", tests="reading for two numbers without confusing them",
           note="Both numbers, the right way round."),
        IT(3, "Find a word in the LAST paragraph that means “people who live near you”.",
           "neighbours",
           band="A2", tests="vocabulary in context",
           note="Accept 'neighbours' only. Students who write 'women' have found the referent "
                "but not the word, which is a comprehension success and a vocabulary miss — "
                "worth noting, not worth a mark."),
        IT(4, "Mai says she “does not mind it now”. What changed for her, and why? "
              "Answer in one sentence.",
           "She used to walk past the canal without noticing it / thought the work was hard, and "
           "now she does not mind because the class keeps going back and the neighbours help them. "
           "(Accept any answer that links her change to doing it regularly or to the help from "
           "the women.)",
           band="A2", tests="inference across paragraphs",
           note="This is the ceiling item of the reading section. Award the mark for a defensible "
                "inference, not for a particular wording."),
    ])

A_S2 = SEC("A-S2", "Reading", "reading", 12, 14, 1,
           "Read the three texts and answer the questions. Write your answers on the question paper.",
           tasks=[A_R1, A_R2, A_R3],
           admin=[
               "Announce the time at 7 minutes and at 12 minutes.",
               "Dictionaries are not allowed in this section.",
               "If a student asks what a word means, say: 'Guess from the sentence.' That "
               "instruction is itself part of what you are measuring.",
           ],
           reads="Reading comprehension at three levels, and — by comparison with Section 1 — "
                 "whether the class's listening is out of step with its reading. That comparison "
                 "is trigger T2 and it is the reason these two sections carry equal marks.")


# --------------------------------------------------------------------------
# A · Section 3 — VOCABULARY  (10 marks, 7 minutes)
# --------------------------------------------------------------------------
A_V1 = TA(
    "A-V1", "Everyday words", "Match the word to the meaning. Write the letter.",
    band="pre-A1 / A1",
    wordbank=["A. kitchen", "B. teacher", "C. bicycle", "D. hungry", "E. Saturday",
              "F. expensive", "G. borrow"],
    items=[
        IT(1, "the room where you cook", "A (kitchen)", band="pre-A1", tests="core noun"),
        IT(2, "you ride it to school", "C (bicycle)", band="pre-A1", tests="core noun"),
        IT(3, "you feel this when you want to eat", "D (hungry)", band="A1", tests="core adjective"),
        IT(4, "it costs a lot of money", "F (expensive)", band="A1", tests="adjective, A1+ frequency"),
        IT(5, "to take something and give it back later", "G (borrow)",
           band="A1+", tests="verb; borrow/lend confusion",
           note="Students who cannot do this one but got 1–4 have a vocabulary that stops at "
                "concrete nouns. That is normal at entry and is what Unit 1 is for."),
    ])

A_V2 = TA(
    "A-V2", "Complete the paragraph",
    "Complete the paragraph with words from the box. There are TWO extra words.",
    band="A1 / A1+",
    wordbank=["breakfast", "healthy", "homework", "often", "tired", "watches", "weekend"],
    text=["My brother gets up at half past five. He is never (1) ______ in the morning. "
          "He always eats (2) ______ before school — usually rice and eggs, which is very "
          "(3) ______. After school he does his (4) ______ first, and then he "
          "(5) ______ television for one hour."],
    items=[
        IT(1, "(1)", "tired", band="A1", tests="adjective in context"),
        IT(2, "(2)", "breakfast", band="pre-A1", tests="core noun"),
        IT(3, "(3)", "healthy", band="A1", tests="adjective in context"),
        IT(4, "(4)", "homework", band="pre-A1", tests="core noun"),
        IT(5, "(5)", "watches", band="A1+", tests="noun/verb choice AND third-person -s",
           note="Two things are being tested at once here on purpose. A student who writes 'watch' "
                "has chosen correctly and inflected wrongly — mark it wrong, but tally it: it is "
                "T5 evidence, not a vocabulary failure."),
    ])

A_S3 = SEC("A-S3", "Vocabulary", "vocab", 10, 7, 1,
           "Answer both tasks. Write your answers on the question paper.",
           tasks=[A_V1, A_V2],
           admin=["Read the two extra words in the box aloud once so nobody loses marks to "
                  "handwriting.",
                  "No dictionaries."],
           reads="Whether the student holds a working everyday vocabulary, and whether it extends "
                 "past concrete nouns into adjectives and verbs. Task 2 item 5 doubles as grammar "
                 "evidence.")


# --------------------------------------------------------------------------
# A · Section 4 — GRAMMAR  (12 marks, 10 minutes)
# --------------------------------------------------------------------------
A_G1 = TA(
    "A-G1", "Be, pronouns and the present simple",
    "Choose the correct word or write the correct form.", band="pre-A1 / A1",
    items=[
        IT(1, "My sister ______ twelve years old.  (is / are / have)", "is",
           band="pre-A1", tests="verb be, third person",
           note="'have' is the Vietnamese-shaped error (cô ấy có 12 tuổi). Tally it separately."),
        IT(2, "This is my friend. ______ name is Tuan.  (He / His / Him)", "His",
           band="A1", tests="possessive adjective"),
        IT(3, "My father ______ (work) in a hospital.", "works",
           band="A1", tests="present simple, third-person -s",
           note="Core T5 item. Count the class total on items 3 and 4 together."),
        IT(4, "______ your mother like coffee?  (Do / Does / Is)", "Does",
           band="A1", tests="present simple question, third person"),
    ])

A_G2 = TA(
    "A-G2", "Questions, plurals and place",
    "Choose the correct word or write the correct form.", band="A1",
    items=[
        IT(1, "There ______ three books on the desk.  (is / are / has)", "are",
           band="A1", tests="there is / there are + plural"),
        IT(2, "______ do you live?  (What / Where / Who)", "Where",
           band="pre-A1", tests="question words"),
        IT(3, "Put the words in order: to school / by bus / I / go / every day",
           "I go to school by bus every day.",
           band="A1", tests="word order with adverbials",
           note="'I go every day to school by bus' is the Vietnamese-shaped order. Half the class "
                "getting this wrong is a word-order problem worth a whole lesson."),
        IT(4, "We have English ______ Monday and Thursday.  (in / on / at)", "on",
           band="A1", tests="prepositions of time"),
    ])

A_G3 = TA(
    "A-G3", "Past, comparison and quantity",
    "Choose the correct word or write the correct form.", band="A1+ / A2",
    items=[
        IT(1, "Yesterday we ______ (visit) my grandmother.", "visited",
           band="A1+", tests="past simple, regular -ed",
           note="THE key item of the paper. With item 2 it decides trigger T1. A student who "
                "writes 'visit' has not met the past simple as a productive form."),
        IT(2, "Last summer they ______ (go) to Da Nang.", "went",
           band="A1+", tests="past simple, irregular"),
        IT(3, "My bag is ______ than yours.  (heavy / heavier / heaviest)", "heavier",
           band="A2", tests="comparative adjectives"),
        IT(4, "How ______ water do you drink every day?  (many / much / lot)", "much",
           band="A2", tests="countable / uncountable quantifiers"),
    ])

A_S4 = SEC("A-S4", "Grammar", "grammar", 12, 10, 1,
           "Answer all three tasks. Write full words, not letters, where the task asks for a form.",
           tasks=[A_G1, A_G2, A_G3],
           admin=["Announce the time at 5 minutes.",
                  "Tell students to attempt every item: there is no penalty for a wrong answer, "
                  "and a blank tells you nothing about what they know.",
                  "Collect Period 1 papers before the bell. Do not let them leave the room with "
                  "the paper."],
           reads="Four constructs the Grade 7 course assumes on day one: be and pronouns, the "
                 "present simple with third-person -s, basic question and word order, and the "
                 "past simple. Items A-G3.1 and A-G3.2 alone decide whether Unit 3 needs "
                 "rebuilding before you teach it.")


# --------------------------------------------------------------------------
# A · Section 5 — WRITING  (14 marks, 20 minutes, period 2)
# --------------------------------------------------------------------------
A_W1 = TA(
    "A-W1", "About you", "PART 1. Answer the five questions. Write ONE full sentence for each. "
    "PART 2. Now use your five sentences to write ONE paragraph about yourself (50–60 words). "
    "You may add more information.",
    band="pre-A1 → A2", rubric="Writing", lines=16,
    items=[
        IT(1, "What is your name and how old are you?",
           "Marked by the Writing rubric (14 marks) across Parts 1 and 2 together — "
           "see curriculum/rubrics.py.",
           marks=14, band="pre-A1 → A2",
           tests="controlled sentence writing, then connected paragraph writing",
           note="The two-part design is the diagnostic. A Foundation student produces five "
                "sentences and stops. A Core student joins them into a paragraph. An Extension "
                "student adds detail and linkers unprompted. Do not award Part 1 and Part 2 "
                "separately — one rubric, one score out of 14."),
    ],
    text=["1. What is your name and how old are you?",
          "2. Where do you live, and who do you live with?",
          "3. How do you go to school?",
          "4. What is your favourite subject? Why?",
          "5. What do you do after school?"])

A_S5 = SEC("A-S5", "Writing", "writing", 14, 20, 2,
           "You have 20 minutes. Spend 5 minutes on Part 1 and 15 minutes on Part 2.",
           tasks=[A_W1],
           admin=[
               "Write the two timings on the board and announce them. Students who spend all "
               "twenty minutes on Part 1 produce no paragraph, and you learn nothing about "
               "their writing.",
               "Bilingual dictionaries are NOT allowed. This is a baseline.",
               "While the class writes, call pairs out for Sections 6 and 7. Keep the room silent "
               "so the pairs can be heard.",
               "Collect every script, including empty ones. An empty script is data.",
           ],
           reads="Whether the student can operate above the sentence. The single most common "
                 "entry profile in a Vietnamese Grade 7 class is a student who can produce five "
                 "correct isolated sentences and cannot connect them — that is trigger T6, and "
                 "it is invisible unless the task has both parts.")


# --------------------------------------------------------------------------
# A · Section 6 — SPEAKING  (12 marks, 3 minutes per pair, rolling)
# --------------------------------------------------------------------------
A_SP1 = TA(
    "A-SP1", "Paired interview", "Work with your partner. The teacher will ask questions. "
    "Answer, and ask your partner the questions marked ➤.",
    band="A1 → A2", rubric="Speaking",
    items=[
        IT(1, "Interlocutor frame — see the script below.",
           "Marked by the Speaking rubric (12 marks) — see curriculum/rubrics.py.",
           marks=12, band="A1 → A2",
           tests="task completion, fluency and interaction, accuracy, range"),
    ],
    text=[
        "PHASE 1 — warm-up (30 seconds, teacher to each student in turn)",
        "  · What's your name?   · How old are you?   · Where do you live?",
        "",
        "PHASE 2 — individual turn (1 minute each)",
        "  Student A: Tell me about your family.  (prompt if needed: How many people? What do "
        "they do?)",
        "  Student B: Tell me about your school day.  (prompt if needed: What time? Which "
        "subjects?)",
        "",
        "PHASE 3 — interaction (1 minute, the pair together)",
        "  ➤ Ask your partner about their free time. Ask at least TWO questions.",
        "  Sentence frames on the desk card, for students who freeze:",
        "     What do you do on Saturday?  ·  Do you like …?  ·  Why?  ·  Me too. / I don't.",
    ],
    note="The frames are on the card for everyone, not only for weak students. A frame offered "
         "only to the strugglers is a public label.")

A_S6 = SEC("A-S6", "Speaking", "speaking", 12, 3, 2,
           "Three minutes per pair, with the Speaking rubric.",
           tasks=[A_SP1],
           admin=[
               "ROLLING ASSESSMENT. Twenty-two pairs at three minutes is sixty-six minutes; it "
               "does not fit one period, and pretending otherwise produces rushed, incomparable "
               "scores.",
               "Assess about six pairs during Period 2 while the rest of the class writes.",
               "Assess the remaining pairs in three-minute slots during the warm-up and "
               "independent-practice stages of U1L1–U1L7.",
               "DEADLINE: every student assessed by the end of period 9. The Checkpoint 1 "
               "decisions cannot be taken without this data.",
               "Use a timer. Score on the sheet before the next pair sits down.",
               "Assess both students of a pair at once, and address the second question of each "
               "phase to the weaker speaker by name so the stronger one cannot carry the exchange.",
           ],
           reads="Basic communicative ability: can the student start, sustain and respond in an "
                 "exchange. Read Accuracy against Range — a student scoring 3 and 1 is playing "
                 "safe, and belongs in Extension, not Core.")


# --------------------------------------------------------------------------
# A · Section 7 — PRONUNCIATION  (8 marks, 45 seconds per student, rolling)
# --------------------------------------------------------------------------
A_P1 = TA(
    "A-P1", "Read-aloud card", "Read the six sentences aloud. You may read them silently first.",
    band="diagnostic across all bands", rubric="Pronunciation",
    items=[
        IT(1, "The read-aloud card below.",
           "Marked by the Pronunciation rubric (8 marks) — see curriculum/rubrics.py.",
           marks=8, band="—",
           tests="final consonants and clusters, word stress, /θ ð ʃ ʒ v z/, intelligibility"),
    ],
    text=[
        "READ-ALOUD CARD  ·  the same card in September, January and May",
        "",
        "1. My brother walked to school and asked his friends to come.",
        "2. She finds three books and puts them on the desks.",
        "3. This is the thing I think about on Thursday.",
        "4. My favourite village has a very nice river.",
        "5. The photographer visited a delicious restaurant in the afternoon.",
        "6. She usually watches television, but she never washes the dishes.",
    ],
    note="Each sentence targets one criterion. 1: final /t/ /d/ and the cluster /skt/. "
         "2: final /s/ /z/ and /nd/ /ts/ /ks/. 3: /θ/ and /ð/. 4: /v/ and /f/. "
         "5: word stress in four- and five-syllable words. 6: /ʃ/ /ʒ/ /z/ and the three "
         "-es endings. Do not tell the students this.")

A_S7 = SEC("A-S7", "Pronunciation", "pron", 8, 1, 2,
           "45 seconds per student, with the Pronunciation rubric.",
           tasks=[A_P1],
           admin=[
               "Runs inside the speaking slot: read-aloud first, then the paired interview.",
               "Give 20 seconds of silent reading first. You are testing pronunciation, not "
               "sight-reading.",
               "Mark criterion 1 (final consonants) on the first pass and criteria 2–4 on the "
               "second. Trying to hear all four at once is how every student ends up with a 4.",
               "Say nothing evaluative. Do not model the correct sound — that is teaching, and "
               "it contaminates the next student who overhears it.",
               "Keep the card. The identical card is used in January and May.",
           ],
           reads="Which of the four documented Vietnamese pronunciation problems this class "
                 "actually has. Criterion 1 alone decides trigger T3.")


PAPER_A = Paper(
    "A", "Initial diagnostic", "Periods 1–2, first week of the school year", 80,
    sections=[A_S1, A_S2, A_S3, A_S4, A_S5, A_S6, A_S7],
    purpose=[
        "Find out what these students actually know, not what Grade 6 was supposed to teach them.",
        "Produce a six-strand profile per student: listening, reading, vocabulary, grammar, "
        "writing, speaking — with pronunciation reported both inside speaking and separately.",
        "Produce class aggregates strong enough to change the teaching programme, at the level of "
        "'Unit 3 needs an extra pass at the past simple', not 'the class is weak'.",
        "Give every student a baseline they will be measured against in May — by themselves, not "
        "against each other.",
    ],
    admin=[
        "Two 45-minute periods, the first week of the year, before Unit 1 is taught.",
        "Period 1: Sections 1–4 (listening, reading, vocabulary, grammar), 60 marks, all written.",
        "Period 2: Section 5 (writing) for everyone, with Sections 6–7 (speaking, pronunciation) "
        "assessed rolling, finishing by period 9.",
        "Tell the class the truth about what this is: 'This does not go in your report. It tells "
        "me what to teach you.' Test anxiety depresses the floor items most, which is exactly "
        "where you need clean data.",
        "Do not teach anything during the paper. Not one word, not one gesture.",
        "Mark within four days. A diagnostic marked in week three has already lost two weeks of "
        "the teaching it was supposed to change.",
    ])


# ==========================================================================
# PAPER B — MID-YEAR DIAGNOSTIC
# Period 48 (Review 2 block), replacing Progress Test 2
# ==========================================================================

B_L1 = TA(
    "B-L1", "What is it?", "Listen to Anna, Pete and Marsha. Answer the questions.",
    audio_key="M1_1", plays=2, band="A1",
    items=[
        IT(1, "Where does the conversation happen and what do they want to do?",
           "In the city / D.C.; they want to get coffee.",
           band="A1", tests="listening for gist"),
        IT(2, "What does Anna say she has in her bag?", "a pen",
           band="pre-A1", tests="listening for a repeated key noun"),
        IT(3, "Write THREE things Anna actually takes out of her bag.",
           "any three of: a (big) book · a toy · a pillow · a map (of the world) · a lamp",
           band="A1", tests="listening for a list of details"),
        IT(4, "Pete asks Anna a question about the map. What does he ask?",
           "Why do you have a map of the world?",
           band="A1+", tests="listening for a question form"),
    ])

B_L2 = TA(
    "B-L2", "Welcome to the treehouse", "Listen and answer the questions.",
    audio_key="M1_2", plays=2, band="A2",
    excerpt="Play 0:00–1:40 only. Stop after MINDY says “My name means Massive Information "
            "Navigation Device, for You!”",
    items=[
        IT(1, "Why is today a big day for Anna?",
           "Her first children's show is on television.",
           band="A1+", tests="listening for gist"),
        IT(2, "What will the people in the conference room do after they watch the show?",
           "They will tell Ms Weaver what they liked and what they didn't like.",
           band="A2", tests="listening for a future form (they'll tell me…)",
           note="'going to' and 'will' are both in this recording and neither is taught until "
                "Unit 10. That is deliberate: this is the ceiling item."),
        IT(3, "What is special about the treehouse?", "It can time travel.",
           band="A1+", tests="listening for detail; can"),
        IT(4, "What does MINDY's name mean?",
           "Massive Information Navigation Device, for You",
           band="A2", tests="listening to a long unfamiliar noun phrase",
           note="Accept any answer with three of the four words. Nobody is expected to catch all "
                "of it; what you are measuring is how much survives."),
    ])

B_S1 = SEC("B-S1", "Listening", "listening", 8, 10, 48,
           "You will hear two recordings, each TWICE.", tasks=[B_L1, B_L2],
           admin=["Same protocol as September: 30 seconds to read, two plays, no third play.",
                  "Task 2 is an excerpt — stop on the cue line."],
           reads="Listening at 125 and 124 words per minute — faster than the September floor "
                 "item, deliberately. Compare the percentage, not the raw score, with Paper A.")

B_R1 = TA(
    "B-R1", "A message to a classmate", "Read and answer.", band="A1",
    text_title="Message",
    text=["Nam,",
          "I can't come to football practice on Wednesday because I have to go to the dentist "
          "with my mother. Can you tell the coach? I'm really sorry.",
          "I'll be there on Friday. Should I bring the new balls? Ms Hoa gave them to me last "
          "week and they are still in my house.",
          "Thanks!",
          "Duc"],
    items=[
        IT(1, "Why can't Duc come on Wednesday?", "He has to go to the dentist with his mother.",
           band="A1", tests="reading for a reason"),
        IT(2, "What does Duc ask Nam to do?", "Tell the coach (that he can't come).",
           band="A1", tests="reading for a request"),
        IT(3, "When will Duc come to practice?", "On Friday.",
           band="pre-A1", tests="reading for a day"),
        IT(4, "Who has the new balls now?", "Duc (they are in his house).",
           band="A1+", tests="inference — the text never says 'Duc has them'",
           note="A student who answers 'Ms Hoa' read the sentence but not the tense."),
    ])

B_R2 = TA(
    "B-R2", "Two ways to get to school", "Read and answer.", band="A2",
    text_title="Two ways to get to school",
    text=[
        "Last year, most students at Le Loi Secondary School came by motorbike. Their parents "
        "drove them, and at half past six every morning there were more than a hundred motorbikes "
        "outside the gate. It was noisy, and it was not safe.",
        "In September the school tried something different. Any student who lived less than two "
        "kilometres away was asked to walk or cycle, and the school built a covered place for a "
        "hundred and twenty bicycles.",
        "It did not work immediately. In the first month only thirty students cycled, because the "
        "road near the market has no pavement and parents were worried. So the school asked the "
        "district to paint a cycle lane. After that the number went up to ninety-four.",
        "Ms Hoa, who teaches Class 7B, says the biggest change is not the traffic. “The students "
        "who cycle arrive awake,” she says. “They talk to each other before the first lesson. "
        "Last year they arrived and sat down in silence.”",
    ],
    items=[
        IT(1, "What problem did the school have last year?",
           "Too many motorbikes outside the gate — it was noisy and not safe.",
           band="A1+", tests="reading for a problem"),
        IT(2, "Why did only thirty students cycle in the first month?",
           "The road near the market had no pavement, so parents were worried.",
           band="A2", tests="reading for cause"),
        IT(3, "How many students cycled after the cycle lane was painted?", "ninety-four / 94",
           band="A1+", tests="reading for a number after a change"),
        IT(4, "According to Ms Hoa, what is the biggest change? Why does she think it matters?",
           "The students who cycle arrive awake and talk to each other before the first lesson "
           "(instead of sitting down in silence).",
           band="A2", tests="reading a quotation and its point"),
    ])

B_S2 = SEC("B-S2", "Reading", "reading", 8, 10, 48, "Read the two texts and answer the questions.",
           tasks=[B_R1, B_R2],
           admin=["No dictionaries.", "Announce the time at 5 minutes."],
           reads="Whether the listening–reading gap found in September has closed. This is the "
                 "single most important comparison in Paper B.")

B_V1 = TA(
    "B-V1", "Words from Units 1–6", "Complete each sentence with ONE word.", band="A1 / A2",
    items=[
        IT(1, "My hobby is c______ stamps. I have four hundred.", "collecting",
           band="A1", tests="Unit 1 vocabulary"),
        IT(2, "You shouldn't eat too much j______ food.", "junk", band="A1", tests="Unit 2"),
        IT(3, "A person who helps other people and is not paid is a v______.", "volunteer",
           band="A2", tests="Unit 3"),
        IT(4, "Pho is my favourite d______ .", "dish", band="A1+", tests="Unit 5",
           note="Accept 'drink' only if the student wrote a drink; 'dish' or 'food' is expected."),
        IT(5, "Please be quiet — the c______ is starting.  (a music performance)", "concert",
           band="A1+", tests="Unit 4"),
        IT(6, "We wear a school u______ every day.", "uniform", band="A1", tests="Unit 6"),
    ])

B_S3 = SEC("B-S3", "Vocabulary", "vocab", 6, 5, 48, "Complete the six sentences.", tasks=[B_V1],
           admin=["First letters are given so that spelling failure is not counted twice."],
           reads="Retention of taught vocabulary after one semester. Read alongside the September "
                 "vocabulary score: a class that scored well in September and badly here has a "
                 "retention problem, not a vocabulary problem, and needs T4.")

B_G1 = TA(
    "B-G1", "Grammar from Units 1–6", "Write the correct form or choose the correct word.",
    band="A1 / A2",
    items=[
        IT(1, "She enjoys ______ (read) comic books.", "reading", band="A1+", tests="U1 verb + V-ing"),
        IT(2, "You ______ drink so much cola.  (should / shouldn't)", "shouldn't",
           band="A1", tests="U2 advice"),
        IT(3, "Last Sunday we ______ (clean) the beach.", "cleaned",
           band="A1+", tests="U3 past simple regular — the T1 item"),
        IT(4, "They ______ (not / go) to the museum last week.", "didn't go",
           band="A2", tests="U3 past simple negative"),
        IT(5, "This song is ______ than that one.  (good / better / best)", "better",
           band="A2", tests="U4 irregular comparative"),
        IT(6, "There isn't ______ milk in the fridge.  (some / any / many)", "any",
           band="A1+", tests="U5 some/any"),
        IT(7, "How ______ eggs do we need?  (much / many)", "many", band="A1+", tests="U5 quantifiers"),
        IT(8, "Look! The teacher ______ (come) now.", "is coming",
           band="A2", tests="U6 present continuous"),
        IT(9, "My brother usually ______ (walk) to school, but today he ______ (take) the bus.",
           "walks / is taking", band="A2", tests="U6 present simple vs continuous",
           note="Both halves needed. This item is the clearest read on whether Unit 6 landed."),
        IT(10, "Put in order: is / who / that / girl / ?", "Who is that girl?",
            band="A1", tests="question word order"),
    ])

B_S4 = SEC("B-S4", "Grammar", "grammar", 10, 10, 48, "Answer all ten items.", tasks=[B_G1],
           admin=["Announce the time at 5 minutes.", "Attempt every item; blanks tell you nothing."],
           reads="Whether the six grammar points of the first semester are productive. Item 3 is "
                 "deliberately the same construct as A-G3.1 so that T1 can be tested for closure.")

B_W1 = TA(
    "B-W1", "An email to a friend",
    "Write an email of 70–90 words to a friend in another school. Tell them: "
    "(1) what you did last weekend, (2) one thing you like about your school this year, "
    "(3) one piece of advice about staying healthy.",
    band="A1+ / A2", rubric="Writing", lines=14,
    items=[
        IT(1, "The email.", "Marked by the Writing rubric (14 marks) — the same rubric as "
           "September and May.", marks=14, band="A1+ / A2",
           tests="past simple in production, opinion, advice with should, paragraph organisation",
           note="The three content points are chosen so the script also yields T1 evidence "
                "(point 1), T6 evidence (organisation) and Unit 2 retention (point 3)."),
    ])

B_S5 = SEC("B-S5", "Writing", "writing", 14, 10, 48,
           "You have 10 minutes. Plan for 2 minutes, write for 8.", tasks=[B_W1],
           admin=["Write the two timings on the board.",
                  "No dictionaries — same conditions as September."],
           reads="Production under the same rubric as Papers A and C. Compare the five criterion "
                 "scores, not the total: a class whose Task completion rose while Grammar stayed "
                 "flat has learnt the exam, not the language.")

PAPER_B = Paper(
    "B", "Mid-year diagnostic", "Period 48, in the Review 2 block (replaces Progress Test 2)", 46,
    sections=[B_S1, B_S2, B_S3, B_S4, B_S5],
    purpose=[
        "Measure movement since September on the same six strands.",
        "Test whether each trigger fired in September has closed, is closing, or has not moved.",
        "Re-band the class, and move students between groups. A student who was Foundation in "
        "September and is Core in January must be told so, in those words.",
        "Catch the students the September paper mis-placed. Every diagnostic mis-places someone.",
    ],
    admin=[
        "One 45-minute period. 46 written marks.",
        "Speaking and pronunciation are SAMPLED, not sat by everyone: take a third of the class, "
        "two minutes each, using the same rubrics and the same read-aloud card. Rotate so that "
        "every student is sampled once across Papers B and C.",
        "The sampled oral scores are reported separately and are NOT added into the 46. Comparison "
        "between papers is always per strand as a percentage.",
        "Mark within three days: the second semester starts immediately.",
    ],
    parallel_to="A")


# ==========================================================================
# PAPER C — FINAL DIAGNOSTIC (parallel form of Paper A)
# Period 94 (Review 4 block), replacing Progress Test 4
# ==========================================================================

C_L1 = TA(
    "C-L1", "Is it cold?", "Listen to Anna and her phone. Answer the questions.",
    audio_key="F1_1", plays=2, band="A1",
    items=[
        IT(1, "Why does Anna check the forecast every day?",
           "Because the weather in Washington changes often.",
           band="A1", tests="listening for gist — parallel to A-L1.1"),
        IT(2, "The phone says it is 18 degrees. Why is Anna surprised, and what is the "
              "temperature really like?",
           "She thinks 18 degrees is cold, but it is 18 degrees Celsius = 65 Fahrenheit, "
           "which is warm.",
           band="A1+", tests="listening for detail across two turns — parallel to A-L1.2"),
        IT(3, "Is it windy? Is it sunny?", "Not windy. Sunny.",
           band="pre-A1", tests="yes/no detail — parallel to A-L1.3"),
        IT(4, "At the end, whose weather was the phone really describing?",
           "Mexico City's (in Mexico) — not Washington's.",
           band="A2", tests="inference — parallel to A-L1.4 but one band higher",
           note="The September paper's task 1 had no inference item. This one does, on purpose: "
                "by May the floor item should no longer be a floor for most of the class."),
    ])

C_L2 = TA(
    "C-L2", "Are you busy?", "Listen to Anna at her new job. Answer the questions.",
    audio_key="F1_2", plays=2, band="A1+",
    items=[
        IT(1, "What does Anna want to do today?",
           "Apologise / say sorry to her co-workers (for yesterday).",
           band="A1+", tests="listening for gist — parallel to A-L2.1"),
        IT(2, "What is Anne doing at 10 a.m.?", "She is writing (she does her morning show).",
           band="A1+", tests="present continuous in speech — parallel to A-L2.2"),
        IT(3, "When Jonathan is recording his evening show, what can you see?",
           "The studio light is on.",
           band="A2", tests="listening for a condition — parallel to A-L2.3"),
        IT(4, "What time does Ms Weaver tell Anna to come to her office, and what happens there?",
           "5 p.m.; there is a surprise party.",
           band="A1+", tests="time detail + outcome — parallel to A-L2.4"),
    ])

C_L3 = TA(
    "C-L3", "She's my best friend", "Listen to Anna and Penelope. Answer the questions.",
    audio_key="F1_3", plays=2, band="A2",
    excerpt="Play 0:00–1:20 only. Stop after Anna says “But we are great roommates.”",
    items=[
        IT(1, "Who is Penelope and why is Anna excited?",
           "Her best friend from her hometown; she is coming to visit / arriving by train.",
           band="A1+", tests="listening for gist — parallel to A-L3.1"),
        IT(2, "How does Anna pay less rent?", "She has a roommate, so they split the rent.",
           band="A2", tests="listening for an explanation — parallel to A-L3.2"),
        IT(3, "Write TWO things Anna says about Marsha.",
           "any two of: she is the nicest person Anna knows in the city · sometimes she worries "
           "too much · she says Anna is the messiest cook she knows · they are great roommates",
           band="A2", tests="superlatives in speech — parallel to A-L3.3"),
        IT(4, "Anna says Marsha is “the nicest person I know in this city”. "
              "What does Marsha say about Anna?",
           "That Anna is the messiest cook she knows.",
           band="A2", tests="holding two superlatives apart — parallel to A-L3.4"),
    ])

C_S1 = SEC("C-S1", "Listening", "listening", 12, 12, 94,
           "You will hear three recordings, each TWICE.", tasks=[C_L1, C_L2, C_L3],
           admin=["Identical protocol to September. Same number of plays, same reading time.",
                  "Task 3 is an excerpt — stop on the cue line."],
           reads="Listening at 104, 105 and 124 words per minute — matched to September's 104, "
                 "108 and 140. The May ceiling item is slightly slower than September's and one "
                 "band harder in task design; report the strand percentage, not the raw score.")

C_R1 = TA(
    "C-R1", "Sports day notice", "Read the notice and answer the questions.", band="pre-A1 / A1",
    text_title="LE LOI SECONDARY SCHOOL — SPORTS DAY",
    text=[
        "SATURDAY 18 MAY  ·  7:00 a.m. – 11:30 a.m.  ·  School field",
        "",
        "7:00  Meet your class teacher at the gate",
        "7:30  Running (100 m and 400 m)",
        "9:00  Football and badminton",
        "10:30 Prizes",
        "",
        "Bring: sports clothes, a hat, water. The school will give every student lunch.",
        "Do NOT bring: money, phones.",
        "",
        "If it rains, Sports Day moves to Saturday 25 May.",
    ],
    items=[
        IT(1, "What time does the running start?", "7:30 (a.m.)",
           band="pre-A1", tests="reading a timetable — parallel to A-R1.1"),
        IT(2, "Write TWO things you must bring.",
           "any two of: sports clothes · a hat · water",
           band="pre-A1", tests="reading a list — parallel to A-R1.3"),
        IT(3, "TRUE or FALSE: You must bring your own lunch.", "FALSE",
           band="A1", tests="reading against an expectation — parallel to A-R1.4",
           note="The text says the school gives lunch. Students who answer TRUE pattern-matched "
                "'lunch' without reading the sentence."),
        IT(4, "What happens if it rains?", "Sports Day moves to Saturday 25 May.",
           band="A1", tests="reading a conditional"),
    ])

C_R2 = TA(
    "C-R2", "An email from a pen friend", "Read Minh's email and answer the questions.",
    band="A1 / A1+", text_title="From: minh@email.vn   ·   Subject: My year",
    text=[
        "Hi Linh,",
        "Thank you for your last email. You asked what changed for me this year, so here it is.",
        "In September I hated English. I never spoke in class because I was afraid the other "
        "students would laugh. My marks were not good.",
        "In October my teacher put us in fixed pairs. My partner is Hung. He is not better than "
        "me at English, but he is not afraid of anything. In the first week he made me answer "
        "three questions. It was terrible. In the second week it was easier.",
        "Now I speak in every lesson. I still make a lot of mistakes — yesterday I said “I very "
        "like it” and everybody laughed, including me. But I don't mind. Last month I got 8.5 in "
        "the speaking test. In September I got 4.",
        "What about you? Has anything changed?",
        "Minh",
    ],
    items=[
        IT(1, "Why didn't Minh speak in class in September?",
           "He was afraid the other students would laugh (at him).",
           band="A1", tests="reading for a reason — parallel to A-R2.3"),
        IT(2, "What did his teacher do in October?",
           "She put the students in fixed pairs.",
           band="A1", tests="reading for detail; past simple — parallel to A-R2.1"),
        IT(3, "Minh says Hung “is not better than me at English”. So why does Hung help him?",
           "Because Hung is not afraid — he made Minh answer questions.",
           band="A1+", tests="inference across a contrast — parallel to A-R2.4"),
        IT(4, "How much did Minh's speaking mark change?",
           "From 4 in September to 8.5 last month — it went up by 4.5.",
           band="A1+", tests="reading two numbers and comparing them"),
    ])

C_R3 = TA(
    "C-R3", "The library that nobody used", "Read the text and answer the questions.", band="A2",
    text_title="The library that nobody used",
    text=[
        "For eleven years, the library at Nguyen Trai Secondary School was open every lunchtime "
        "and almost nobody went in. It had four thousand books. The librarian, Mr Binh, counted "
        "the visitors: in one week in 2022, nine students came, and six of them came to shelter "
        "from the rain.",
        "Mr Binh did not think the students were lazy. He thought the room was wrong. It had no "
        "windows on the playground side, the lights were white and cold, and the chairs were the "
        "same hard chairs as the classrooms. “We built a room that looked like a lesson,” he said, "
        "“and then we were surprised that nobody came in their free time.”",
        "So he changed it. He moved sixty of the most popular books to a low shelf by the door, "
        "where students could see the covers, not the spines. He asked the art club to paint one "
        "wall. He brought in eight old armchairs from a hotel that was closing, and he stopped "
        "asking students to be silent — talking was allowed, as long as it was about the books.",
        "Not everything worked. The armchairs were popular, but some students slept in them, and "
        "Mr Binh had to make a rule about that. The painted wall took three months, because the "
        "art club kept changing its mind.",
        "By May 2024, the library had between forty and sixty visitors every lunchtime. Mr Binh "
        "still counts them. “The books did not change,” he says. “Four thousand books, the same "
        "four thousand books. Only the room changed.”",
    ],
    items=[
        IT(1, "What is the main point of the text?",
           "C — a room can stop people using something, even when the thing itself is good",
           band="A2", tests="main idea — parallel to A-R3.1",
           options=["A. School libraries need more books.",
                    "B. Mr Binh is a good librarian who counts visitors.",
                    "C. A room can stop people using something, even when the thing itself is good.",
                    "D. Students prefer armchairs to hard chairs."],
           note="B is the trap, as in September: true, but not the point."),
        IT(2, "In one week in 2022, nine students came to the library. Why is that number even "
              "worse than it looks?",
           "Because six of the nine only came to shelter from the rain — so only three came for "
           "the library.",
           band="A2", tests="reading a number in its context"),
        IT(3, "Find a word in paragraph 3 that means “making no sound”.", "silent",
           band="A1+", tests="vocabulary in context — parallel to A-R3.3",
           note="Accept 'silent'. The earlier version of this item asked for a word meaning "
                "'allowed to happen', whose answer was 'allowed' — a clue that contains its own "
                "answer tests nothing."),
        IT(4, "Mr Binh says “The books did not change… Only the room changed.” "
              "What is he trying to explain? Answer in one sentence.",
           "That the problem was never the books or the students — it was the space, and changing "
           "the space changed the behaviour. (Accept any answer that separates the thing from the "
           "conditions around it.)",
           band="A2", tests="inference from a quotation — parallel to A-R3.4"),
    ])

C_S2 = SEC("C-S2", "Reading", "reading", 12, 14, 94, "Read the three texts and answer the questions.",
           tasks=[C_R1, C_R2, C_R3],
           admin=["No dictionaries.", "Announce the time at 7 and 12 minutes."],
           reads="Reading at the same three levels as September. C-R3 is longer than A-R3 by "
                 "about eighty words — that is the year's growth, built into the instrument.")

C_V1 = TA(
    "C-V1", "Everyday words", "Match the word to the meaning. Write the letter.", band="pre-A1 / A1",
    wordbank=["A. library", "B. dentist", "C. umbrella", "D. thirsty", "E. Wednesday",
              "F. dangerous", "G. lend"],
    items=[
        IT(1, "the room or building where you borrow books", "A (library)",
           band="pre-A1", tests="core noun — parallel to A-V1.1"),
        IT(2, "you use it when it rains", "C (umbrella)", band="pre-A1", tests="core noun"),
        IT(3, "you feel this when you want to drink", "D (thirsty)",
           band="A1", tests="core adjective — parallel to A-V1.3"),
        IT(4, "it can hurt you", "F (dangerous)", band="A1", tests="adjective"),
        IT(5, "to give something to someone for a short time", "G (lend)",
           band="A1+", tests="borrow/lend — the September item, the other way round",
           note="A-V1.5 tested 'borrow'. This tests 'lend'. A student who got one and not the "
                "other has the concept and not the pair."),
    ])

C_V2 = TA(
    "C-V2", "Complete the paragraph",
    "Complete the paragraph with words from the box. There are TWO extra words.",
    band="A1 / A1+",
    wordbank=["already", "difficult", "festival", "practises", "proud", "traffic", "twice"],
    text=["My sister plays the guitar. She (1) ______ for an hour every evening, and she has "
          "played at the school (2) ______ (3) ______ this year. The first time was very "
          "(4) ______ for her because she was nervous. Now my parents are very (5) ______ of her."],
    items=[
        IT(1, "(1)", "practises", band="A1+", tests="verb choice AND third-person -s",
           note="Same double test as A-V2.5. Compare the class total on the two directly: it is "
                "the cleanest read on whether T5 closed."),
        IT(2, "(2)", "festival", band="A1", tests="Unit 9 vocabulary"),
        IT(3, "(3)", "twice", band="A1", tests="frequency"),
        IT(4, "(4)", "difficult", band="A1", tests="adjective in context"),
        IT(5, "(5)", "proud", band="A1+", tests="adjective, lower frequency"),
    ])

C_S3 = SEC("C-S3", "Vocabulary", "vocab", 10, 7, 94, "Answer both tasks.", tasks=[C_V1, C_V2],
           admin=["Read the two extra words aloud once.", "No dictionaries."],
           reads="Vocabulary at the same two levels as September, with the borrow/lend pair "
                 "reversed and the third-person -s item repeated.")

C_G1 = TA(
    "C-G1", "Be, pronouns and the present simple", "Choose or write the correct form.",
    band="pre-A1 / A1",
    items=[
        IT(1, "My cousins ______ fourteen years old.  (is / are / have)", "are",
           band="pre-A1", tests="verb be, plural — parallel to A-G1.1"),
        IT(2, "That is Mai's bag. ______ bag is red.  (She / Her / Hers)", "Her",
           band="A1", tests="possessive adjective — parallel to A-G1.2"),
        IT(3, "My mother ______ (teach) at a primary school.", "teaches",
           band="A1", tests="third-person -s — parallel to A-G1.3"),
        IT(4, "______ your brother play football?  (Do / Does / Is)", "Does",
           band="A1", tests="present simple question — parallel to A-G1.4"),
    ])

C_G2 = TA(
    "C-G2", "Questions, plurals and place", "Choose or write the correct form.", band="A1",
    items=[
        IT(1, "There ______ a lot of noise in the street.  (is / are / have)", "is",
           band="A1", tests="there is + uncountable — parallel to A-G2.1"),
        IT(2, "______ do you go to bed?  (What / When / Who)", "When",
           band="pre-A1", tests="question words — parallel to A-G2.2"),
        IT(3, "Put the words in order: to the market / on Sunday / my mother / goes / usually",
           "My mother usually goes to the market on Sunday.",
           band="A1", tests="word order with frequency adverb — parallel to A-G2.3",
           note="Harder than the September item by one element: the adverb of frequency has to go "
                "before the verb. Accept 'Usually my mother goes…' as well."),
        IT(4, "My birthday is ______ May.  (in / on / at)", "in",
           band="A1", tests="prepositions of time — parallel to A-G2.4"),
    ])

C_G3 = TA(
    "C-G3", "Past, comparison and quantity", "Choose or write the correct form.", band="A1+ / A2",
    items=[
        IT(1, "Last weekend my family ______ (travel) to Sa Pa.", "travelled",
           band="A1+", tests="past simple regular — the T1 closure item, parallel to A-G3.1",
           note="Compare the class percentage on this item directly with A-G3.1. If it has not "
                "moved after a year of teaching, the reinforcement did not work and the Grade 8 "
                "teacher needs to know."),
        IT(2, "Yesterday I ______ (see) a very good film.", "saw",
           band="A1+", tests="past simple irregular — parallel to A-G3.2"),
        IT(3, "This exercise is ______ than the last one.  (easy / easier / easiest)", "easier",
           band="A2", tests="comparatives — parallel to A-G3.3"),
        IT(4, "How ______ students are there in your class?  (many / much / lot)", "many",
           band="A2", tests="quantifiers — parallel to A-G3.4, countable instead of uncountable"),
    ])

C_S4 = SEC("C-S4", "Grammar", "grammar", 12, 10, 94,
           "Answer all three tasks.", tasks=[C_G1, C_G2, C_G3],
           admin=["Announce the time at 5 minutes.", "Attempt every item."],
           reads="Item for item, the same constructs as September. This is where the year's "
                 "grammar teaching is actually audited.")

C_W1 = TA(
    "C-W1", "About you — again",
    "PART 1. Answer the five questions. Write ONE full sentence for each. "
    "PART 2. Now use your five sentences to write ONE paragraph about yourself (50–60 words). "
    "You may add more information.",
    band="pre-A1 → A2", rubric="Writing", lines=16,
    items=[
        IT(1, "The paragraph.", "Marked by the Writing rubric (14 marks) — the same rubric as "
           "September and January.", marks=14, band="pre-A1 → A2",
           tests="controlled sentence writing, then connected paragraph writing",
           note="The task is deliberately the SAME shape as A-W1, with two questions changed. "
                "Hand the September script back next to the May script, stapled, after the paper "
                "is collected. That comparison teaches more than the mark does."),
    ],
    text=["1. What is your name and how old are you?",
          "2. Where do you live, and who do you live with?",
          "3. How do you go to school?",
          "4. What did you enjoy most this year? Why?",
          "5. What do you want to do better next year?"])

C_S5 = SEC("C-S5", "Writing", "writing", 14, 20, 93,
           "You have 20 minutes. Spend 5 minutes on Part 1 and 15 minutes on Part 2.",
           tasks=[C_W1],
           admin=[
               "Same conditions as September: no dictionaries, same timings on the board.",
               "AFTER the papers are collected, hand each student their September script stapled "
               "to their May script. Say nothing for one minute. Let them read.",
           ],
           reads="Growth on five stable criteria. Compare criterion by criterion — a class whose "
                 "Task completion rose while Grammar stayed flat learnt the exam, not the language.")

C_S6 = SEC("C-S6", "Speaking", "speaking", 12, 3, 94,
           "Three minutes per pair, with the Speaking rubric and the same phase structure as "
           "September.", tasks=[A_SP1],
           admin=[
               "Rolling again: about six pairs in the test period, the rest during the Review 4 "
               "consolidation lesson and the last week of term.",
               "Use the SAME phase structure as September. Phase 2 prompts change to 'Tell me "
               "about something you did this year' and 'Tell me about a place you would like to "
               "visit'; phases 1 and 3 are unchanged.",
               "Keep the sentence-frame card on the desk, as in September, for everyone.",
           ],
           reads="Communicative ability against the September baseline. The number that matters "
                 "most is Task completion: students who scored 0–1 in September because they "
                 "froze, and score 2–3 now, are the clearest evidence the year worked.")

C_S7 = SEC("C-S7", "Pronunciation", "pron", 8, 1, 94,
           "45 seconds per student, with the same read-aloud card as September and January.",
           tasks=[A_P1],
           admin=[
               "The card is IDENTICAL to September's. Do not improve it, do not modernise it, do "
               "not swap a word. An instrument that changes cannot measure change.",
               "Mark criterion 1 first, then 2–4, exactly as in September.",
               "Compare criterion 1 with the September figure before you write any report comment "
               "about pronunciation.",
           ],
           reads="Whether the four Vietnamese pronunciation problems moved. Criterion 1 (final "
                 "consonants) is the one to report on: it is the one the course drills daily.")

PAPER_C = Paper(
    "C", "Final diagnostic",
    "Periods 93–94, in the Review 4 block (writing in the last 20 minutes of the consolidation session; the rest replaces Progress Test 4)", 80,
    sections=[C_S1, C_S2, C_S3, C_S4, C_S5, C_S6, C_S7],
    purpose=[
        "Measure the year against the September baseline on the same six strands and the same "
        "three rubrics.",
        "Report per strand and per rubric criterion, never as one number. 'She went from 41 to 62' "
        "is a school report; 'her listening went from 33% to 75% and her writing organisation is "
        "still 0' is a handover.",
        "Produce the handover the Grade 8 teacher actually needs: which triggers closed, which "
        "did not, and which three students are still Foundation.",
        "Show each student their own September script next to their May script. For most of them "
        "it is the first evidence they have ever seen that they got better at anything.",
    ],
    admin=[
        "TWO sittings, because a parallel form of Paper A cannot be anything else. Paper A's "
        "written sections need 63 minutes; so do Paper C's. Compressing them into one period "
        "would change the instrument, and an instrument that changes cannot measure change.",
        "Period 93 (the Review 4 consolidation session): the first 25 minutes stay as revision; "
        "the last 20 minutes are Section 5, Writing.",
        "Period 94 (the Progress Test 4 slot): Sections 1–4, 46 marks, 43 minutes.",
        "Speaking and pronunciation roll through the last two weeks of term, as in September.",
        "Identical conditions to September: same reading time, same number of plays, same "
        "dictionaries rule, same read-aloud card.",
        "Mark before the end of term. A final diagnostic marked in the holidays helps nobody.",
        "Write the handover sheet the same week, while you still remember which student is which.",
    ],
    parallel_to="A")


PAPERS = {"A": PAPER_A, "B": PAPER_B, "C": PAPER_C}
ALL_PAPERS = [PAPER_A, PAPER_B, PAPER_C]

# Which recordings each paper needs, for the teacher's pre-flight check.
PAPER_AUDIO = {
    "A": ["D1_1", "D1_2", "D1_3"],
    "B": ["M1_1", "M1_2"],
    "C": ["F1_1", "F1_2", "F1_3"],
}


# ==========================================================================
# THE TWO DIAGNOSTIC SESSIONS AS TEACHING PERIODS
#
# Periods 1 and 2 of the school year.  They are Lesson objects so that the
# Teacher's Coursebook renders them in sequence with everything else — a
# teacher should not have to hold a separate document to run the first two
# lessons of the year.
# ==========================================================================
from .schema import Lesson, ST, TK, Unit

D0L1 = Lesson(
    code="D0L1", unit=0, number=1, period=1,
    lesson_type="Diagnostic",
    title="Initial diagnostic, Part A — listening, reading, vocabulary, grammar",
    objectives=[
        "sit the four written sections of the initial diagnostic under fair, quiet conditions",
        "understand that this paper does not go in their report and does not decide anything "
        "about them",
        "attempt every item rather than leaving blanks",
    ],
    recycled=["Everything from Grade 6 — that is the point. Nothing is pre-taught."],
    listening=DIAG_AUDIO["D1_1"],
    procedure=[
        ST("Before the students arrive", 0,
           ["Test the audio. Play thirty seconds of D1_1 from the back of the room and check you "
            "can hear the final consonants from there. If you cannot, neither can they, and the "
            "listening scores you get today will be a measurement of your speakers.",
            "Have all three MP3s open, in order, with the counter visible.",
            "Desks apart. Papers face down.",
            "Write on the board: 12' listening · 14' reading · 7' vocabulary · 10' grammar."],
           "—", "Teacher only", "—"),
        ST("Setting up", 3,
           ["Say the truth about what this is (see the teacher talk below). Take thirty seconds "
            "over it — anxiety costs you the floor items, which are the ones you most need.",
            "Names on the paper. Nobody turns over."],
           "Listen; write their name.", "Whole class", "—"),
        ST("Section 1 — Listening", 12,
           ["Three recordings, each played TWICE. 30 seconds to read the questions before each.",
            "Task 3 is an excerpt: stop it on the cue line.",
            "No third play. Not for anyone."],
           "Listen and answer.", "Individual", "Test paper, Section 1"),
        ST("Section 2 — Reading", 14,
           ["Announce the time at 7 minutes and at 12 minutes.",
            "If asked what a word means: 'Guess from the sentence.'"],
           "Read and answer.", "Individual", "Test paper, Section 2"),
        ST("Section 3 — Vocabulary", 7,
           ["Read the two extra words in the box aloud once, so nobody loses a mark to your "
            "handwriting."],
           "Match and complete.", "Individual", "Test paper, Section 3"),
        ST("Section 4 — Grammar", 9,
           ["Announce the time at 5 minutes.",
            "Remind once: attempt everything. A blank tells you nothing about what they know."],
           "Complete.", "Individual", "Test paper, Section 4"),
        ST("Collect", 0,
           ["Collect every paper before the bell, including the empty ones. An empty paper is data.",
            "Say when they will hear about it — and then actually do it."],
           "Hand in.", "Whole class", "—"),
    ],
    teacher_talk=[
        TK("At the start, before anyone turns the paper over",
           ["This is not a test. Nothing here goes in your report.",
            "I have never taught you before. I do not know what you already know, and if I guess "
            "I will guess wrong — I will teach you things you learned two years ago, and skip "
            "things you have never seen.",
            "So this paper is for me, not for you. It tells me where to start.",
            "Some of it will be easy. Some of it will be too hard, and that is on purpose — I "
            "have to find the top as well as the bottom. If you cannot do something, that is "
            "information, and it is useful information.",
            "One rule: never leave a blank. Guess. A guess tells me something; a blank tells me "
            "nothing.",
            "Turn over. Section 1 is listening. Here we go."]),
        TK("If a student is visibly panicking",
           ["Stop for a second. Look at me.",
            "There is nothing you can fail today. There is no mark that goes anywhere.",
            "Do the ones you can. Leave the ones you cannot — no, actually, guess those.",
            "That's all. Carry on."]),
    ],
    support=[
        "Read the section instructions aloud in Vietnamese for the whole class, once. The "
        "instructions are not what is being tested.",
        "Sit students with hearing difficulties at the front for Section 1, and check it.",
        "Extra time is NOT given. It changes what the paper measures, and the students who need "
        "it are the ones you most need clean data about.",
    ],
    challenge=[
        "Nothing. Do not add anything for strong students today — the ceiling items are already "
        "in the paper, and their scores on those items are how you find them.",
    ],
    assessment=[
        "60 written marks: listening 12 · reading 12 · vocabulary 10 · grammar 12 (Section 5 "
        "writing is tomorrow).",
        "Mark within four days. Enter percentages per strand, not raw totals.",
        "Compute the item-level class percentages for A-G3.1, A-G3.2, A-L3.2, A-G1.3, A-G1.4 and "
        "A-V2.5 — six numbers, and they decide triggers T1 and T5.",
    ],
    board_plan=[
        "Section 1 Listening 12 marks (12') | Section 2 Reading 12 (14') | "
        "Section 3 Vocabulary 10 (7') | Section 4 Grammar 12 (10')",
        "RULE: never leave a blank. Guess.",
    ],
    materials=[
        "Test papers — Book 7, Paper A, Sections 1–4, one per student",
        "The three MP3s: audio/FD1_1…, audio/FD1_2…, audio/FD1_3… (see Book 6 pre-flight check)",
        "Speakers, tested from the back of the room",
        "A clock the whole room can see",
    ])


D0L2 = Lesson(
    code="D0L2", unit=0, number=2, period=2,
    lesson_type="Diagnostic",
    title="Initial diagnostic, Part B — writing, and the first speaking pairs",
    objectives=[
        "write the two-part writing task under timed conditions",
        "sit a three-minute paired speaking interview and a 45-second read-aloud",
        "leave the room having spoken English to the teacher once, whatever the score",
    ],
    recycled=["Everything from Grade 6."],
    listening=DIAG_AUDIO["D1_1"],
    procedure=[
        ST("Setting up", 3,
           ["Same conditions as yesterday. Say: 'Twenty minutes of writing. Five minutes on "
            "Part 1, fifteen on Part 2.' Write both on the board.",
            "Explain the rolling speaking: 'While you write, I will call pairs to the front. "
            "Everyone will do it — some today, the rest over the next two weeks.'",
            "Say it in that order. Students who think they have been singled out perform worse."],
           "Listen; write their name.", "Whole class", "—"),
        ST("Section 5 — Writing", 20,
           ["Announce the switch from Part 1 to Part 2 at 5 minutes. Students who spend all "
            "twenty minutes on Part 1 produce no paragraph, and the paragraph is the part that "
            "discriminates.",
            "No dictionaries.",
            "Keep the room silent — the speaking pairs have to be audible."],
           "Write Part 1, then Part 2.", "Individual", "Test paper, Section 5"),
        ST("Sections 6 and 7 — speaking and pronunciation, rolling", 20,
           ["Call the first pair. Read-aloud card first (20 seconds silent reading, then 45 "
            "seconds aloud), then the three-minute paired interview.",
            "Score both students before the next pair sits down. Scores written from memory at "
            "the end of the session regress to the class mean.",
            "About six pairs fit in this period. That is expected, not a failure.",
            "Say nothing evaluative. Do not model a correct sound — the next pair can hear you."],
           "In pairs: read aloud, then the interview.", "Pairs, rolling", "Speaking card, "
           "read-aloud card, tracking grid"),
        ST("Collect and finish", 2,
           ["Collect every script.",
            "Tell them when the rest of the speaking will happen, and that it happens to everyone.",
            "Then say the last line of the teacher talk and mean it."],
           "Hand in.", "Whole class", "—"),
    ],
    teacher_talk=[
        TK("Before the writing",
           ["Twenty minutes. Five on the five questions, fifteen on the paragraph.",
            "The paragraph is the part I care about. Five separate sentences is fine — joining "
            "them into a paragraph is better. Do what you can.",
            "If you do not know a word, write it in Vietnamese and carry on. Do not stop.",
            "Begin."]),
        TK("To each pair, before the speaking",
           ["Sit down. Take a breath.",
            "You are going to read six sentences aloud, then the two of you are going to talk to "
            "me for three minutes. There is a card on the desk with sentences you can use if you "
            "get stuck — it is there for everybody, not just for you.",
            "I am not going to correct you and I am not going to tell you your score.",
            "Ready? Read the six sentences to yourself first. Take your time."]),
        TK("At the very end of the session",
           ["That is the whole thing. It is over.",
            "I will have your papers marked by Friday. I am not going to read out any marks — "
            "not yours, not anybody's.",
            "What I am going to do is tell each of you one thing you are already good at and one "
            "thing we are going to work on. That is what this was for.",
            "Tomorrow we start Unit 1. Hobbies."]),
    ],
    support=[
        "The sentence-frame card sits on the desk for every pair, not only the weak ones. A frame "
        "offered only to strugglers is a public label.",
        "If a student freezes, give the frame once and ask again. Score the second attempt, and "
        "note 'needed frame' — that is diagnostic information, not a penalty.",
        "A student who answers in Vietnamese scores 0 for task completion and is not told so.",
    ],
    challenge=[
        "Nothing added. Strong students reveal themselves in the Range criterion — watch for the "
        "student scoring 3 for accuracy and 1 for range. That is an Extension candidate hiding.",
    ],
    assessment=[
        "Writing 14 marks (Writing rubric) · Speaking 12 (Speaking rubric) · Pronunciation 8 "
        "(Pronunciation rubric).",
        "Paper A total 80. Band on the total; then apply the relative-gap rule per student.",
        "DEADLINE: every student's speaking and pronunciation done by period 9. Checkpoint 1 "
        "cannot happen without it.",
    ],
    board_plan=[
        "PART 1 — five questions (5 minutes)   PART 2 — one paragraph, 50–60 words (15 minutes)",
        "While you write, pairs come to the front. Everyone does it.",
    ],
    materials=[
        "Test papers — Book 7, Paper A, Section 5, one per student",
        "Speaking card and read-aloud card (Book 7), laminated if possible — they are reused in "
        "January and May",
        "The speaking tracking grid (Book 6), to record who has been assessed",
        "A timer",
    ])


DIAGNOSTIC_BLOCK = Unit(
    number=0,
    title="Initial Diagnostic",
    theme="Finding out what these students actually know, before teaching them anything",
    can_do=["show what I can already do in English, so that my teacher knows where to start"],
    grammar_focus=["Diagnostic only — nothing is taught in these two periods"],
    pron_focus="Read-aloud card: final consonants, word stress, /θ ð ʃ ʒ v z/, intelligibility",
    vocab_focus="Diagnostic only",
    lessons=[D0L1, D0L2])
