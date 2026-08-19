# -*- coding: utf-8 -*-
"""Course-level information: front matter shared by all six books."""

COURSE = {
    "title": "ENGLISH 7 – A Complete Communicative Course",
    "subtitle": "For Vietnamese Grade 7 students (Tiếng Anh 7 – MOET framework)",
    "level": "CEFR A1+ moving towards A2",
    "year": "Full school year – 2 semesters",
    "periods": "92 teaching sessions of 45 minutes (12 units × 7 lessons + 4 review & test blocks × 2)",
    "author_line": "Teacher's edition – complete teaching system",
}

PHILOSOPHY = [
    "Every lesson moves along the same path: PRESENT → GUIDED PRACTICE → INDEPENDENT PRACTICE → COMMUNICATION. "
    "Students never meet new language and are immediately asked to use it freely.",
    "Every lesson contains all four skills. The lesson type only decides which skill is the MAIN focus; "
    "the other skills still appear as short warm-ups, checks or exits.",
    "Language is recycled on purpose. Vocabulary and grammar from earlier units come back in later reading texts, "
    "listening scripts and speaking tasks. Each lesson lists exactly what is being recycled.",
    "Accuracy first, then fluency. Controlled drills come before free speaking so that weaker students "
    "always have a model sentence to hold on to.",
    "Vietnamese is a resource, not an enemy. It is used for quick concept checks and for contrastive "
    "explanation (Vietnamese vs English word order, final sounds, tenses), then dropped.",
    "Speaking confidence is built by structure: students first repeat, then substitute, then produce. "
    "Nobody is asked to 'just talk'.",
]

VN_DIFFICULTIES = [
    ("Final consonants dropped",
     "Vietnamese syllables end in a small set of unreleased sounds, so learners say 'like' for 'liked', "
     "'boo' for 'book', 'fine' for 'finds'.",
     "Drill final sounds every lesson (30 seconds). Use the 'add-a-sound' routine: boo–book, li–like, "
     "fine–finds. Ask students to feel the tongue/lips stop the air."),
    ("Consonant clusters simplified",
     "'schools' becomes 'school', 'asked' becomes 'ask', 'strong' becomes 'trong'.",
     "Break the cluster, then rebuild it: /s/ + /k/ + /s/ → skools. Use slow-fast repetition."),
    ("Word stress flattened",
     "Vietnamese is a tonal, syllable-timed language; every syllable gets equal weight, so 'volunteer', "
     "'delicious', 'photograph' come out unstressed.",
     "Always mark stress with a bubble (Oo / oO). Clap or tap the stressed syllable. Test stress in every review."),
    ("Sounds /θ/ /ð/ /ʃ/ /ʒ/ /v/ /z/ missing or replaced",
     "'think' → 'tink', 'this' → 'dis', 'she' → 'se', 'very' → 'dery/yery'.",
     "Teach tongue and lip position explicitly; use minimal pairs and a mirror. Accept progress, not perfection."),
    ("Listening: cannot catch connected speech",
     "Students know the written word but not its sound in a sentence ('What do you' → /wɒdʒə/).",
     "Pre-teach 3–5 key words, play twice, give a gist task first and a detail task second, then read the "
     "script aloud while students follow."),
    ("Word-for-word translation from Vietnamese",
     "'I very like it', 'She has 13 years old', 'I go to school by my father'.",
     "Teach chunks, not single words. Show the two word orders side by side on the board and drill the "
     "English chunk until it is automatic."),
    ("Confusing similar structures",
     "present simple vs present continuous; much vs many; is/are vs do/does; comparative vs superlative.",
     "Use contrast tables and 'choose the right one' exercises. Every review lesson revisits the contrast."),
    ("Missing verb endings and articles",
     "'He like football', 'I go to school by bus every day' → 'He go...', 'I am student'.",
     "Use the 'HE-SHE-IT = S' chant and an article checklist during writing correction."),
    ("Low speaking confidence, fear of mistakes",
     "Large classes, fear of losing face, no habit of speaking in front of others.",
     "Pair work before whole-class work; give thinking time; use fixed sentence frames; praise attempts; "
     "never correct every error during fluency stages."),
]

CLASSROOM_ROUTINES = [
    ("Warm-up bank", "Slap the board, Hot seat, Word chain, Noughts and crosses, Kim's game, Chinese whispers, "
                     "Find someone who…, Backs to the board."),
    ("Pair-work management", "A/B seating fixed for the whole term. 'Turn to your partner' = A speaks first, "
                             "then swap on the teacher's clap."),
    ("Group-work management", "Groups of four (two pairs turning round). Roles: leader, writer, timekeeper, reporter."),
    ("Error correction", "Accuracy stage → correct immediately and drill. Fluency stage → note errors on paper, "
                         "put 5 sentences on the board at the end and correct together."),
    ("Board plan", "Left = new vocabulary with stress marks. Centre = grammar form + one model sentence. "
                   "Right = today's task and homework."),
    ("Checking answers", "Pair-check → whole-class check → the teacher only confirms. Students explain WHY."),
    ("Large classes", "Use rows as teams; nominate by number, not by hand-up; use choral drilling to give "
                      "every student speaking time."),
]

ASSESSMENT = [
    ("Continuous (every lesson)", "Homework check, board work, pronunciation spot-check, participation. "
                                  "Recorded in the class register with a simple 3-point scale."),
    ("15-minute tests", "After Units 2, 5, 8, 11 – vocabulary and grammar of the previous units."),
    ("45-minute tests", "In the four Review & Test blocks (after Units 3, 6, 9, 12) – listening, reading, "
                        "language focus and writing."),
    ("Speaking assessment", "In Review blocks: 3-minute pair interview using the unit functions. "
                            "Criteria: fluency, pronunciation, accuracy, task completion (2.5 marks each)."),
    ("Portfolio / project", "One project per unit (poster, survey, mini-book, presentation). Marked on content, "
                            "language, presentation, teamwork."),
]

# Scope & sequence rows are generated from the unit files at build time.
SEMESTERS = {1: (1, 6), 2: (7, 12)}

LESSON_TYPES = [
    "Getting Started",
    "A Closer Look 1",
    "A Closer Look 2",
    "Communication",
    "Skills 1",
    "Skills 2",
    "Looking Back & Project",
]

ICONS = {
    "objectives": "🎯", "vocab": "📕", "grammar": "🔧", "pron": "🔊",
    "listening": "🎧", "speaking": "💬", "reading": "📖", "writing": "✍️",
    "communication": "🌍", "guided": "🧩", "independent": "🚀",
    "review": "🔁", "homework": "🏠", "project": "🛠️",
}
