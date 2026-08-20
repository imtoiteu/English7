# ENGLISH 7 — A Complete Communicative Course
### Teaching system for Vietnamese Grade 7 students (MOET / *Tiếng Anh 7* framework)

This repository contains a **complete, ready-to-teach English course for one school year**:
2 diagnostic periods + 12 units × 7 lessons + 4 review & test blocks × 2 =
**94 sessions of 45 minutes**.

It is not a fixed textbook. The year opens with a diagnostic that measures what these
students actually know, and the results **change the programme**: which lessons gain a
reinforcement insert, which prerequisites are taught before the unit that assumes them,
and what the strongest students do instead of the independent-practice stage.

Everything is generated from **one source of truth** (`curriculum/`), so the lesson plans,
the student book, the exercises, the homework, the answer key, the diagnostic and the
slides can never drift out of sync. Every exercise has a unique reference (e.g. `U5.3-P4`)
and every test item a unique code (e.g. `A-G3.1`) that is the same in every book.

---

## What to open first

| File | Who uses it | What it contains |
|---|---|---|
| `output/01_Teachers_Coursebook.docx` | Teacher | Full lesson plans: objectives, language content, staged procedure with timing, scripted teacher explanations, board plans, differentiation, assessment, answers |
| `output/02_Student_Coursebook.docx` | Student, in class | Explanations, vocabulary tables with IPA + Vietnamese, grammar, reading texts, listening tasks **and scripts**, speaking activities, writing, review boxes |
| `output/03_Exercise_and_Practice_Book.docx` | Student | Graded practice for every lesson: ★☆☆ Easy → ★★☆ Medium → ★★★ Difficult, plus a pronunciation drill and a speaking prompt in every lesson |
| `output/04_Homework_Book.docx` | Student, at home | 3–4 homework tasks per lesson (20–35 min) + a Revision Set after every unit |
| `output/05_Teachers_Answer_Key.docx` | Teacher | Every answer, model writing answers, suggested speaking answers, and explanations of the typical Vietnamese-learner errors |
| `output/06_Diagnostic_and_Adaptive_System.docx` | Teacher | The diagnostic system: three papers with full answer keys, three rubrics, the scoring framework, band interpretation, the six-strand profile, eight triggers, the decision tree, six bridging lessons and six extension activities |
| `output/07_Diagnostic_Test_Papers.docx` | Student | The three papers exactly as students see them — no answers, no transcripts, photocopiable |
| `output/slides/UnitXX_.../*.pptx` | Teacher, in class | One 16:9 deck per session (~25–35 slides), built directly from the lesson plan |
| `planning/AUDIO_MAPPING_VERIFIED.md` | Teacher, coordinator | The verified 92-session audio mapping: what is played in every session, where it comes from, how fast it is, and under what licence |

---

## Listening: real human recordings, verified

Every listening session uses a **real recording of real people** — no invented scripts, no
text-to-speech. 80 of the 92 sessions play an external recording; the 12 *Looking Back*
sessions replay their own unit's audio for dictation.

| Source | Sessions | Licence |
|---|---|---|
| VOA *Let's Learn English*, Level 1 | 39 | **Public domain** — may be downloaded, played, and printed in test papers |
| ELLLO *Sound Grammar* (A1/A2/B1) | 26 | © elllo productions — teachers may download and use in class or on a class LMS |
| ELLLO *One Minute English* (A1/A2) | 15 | as above |
| VOA *Let's Learn English* — diagnostic only | 10 | **Public domain** — printable inside a test paper |

### The MP3s are not in this repository

`audio/` is gitignored, for two independent reasons: the ELLLO licence grants classroom
use but **not** redistribution, and this repository is public; and 273 MB of MP3 would sit
in the git history forever.

Every recording's source page and direct URL is recorded in `curriculum/audio_sources.py`
and `curriculum/audio_diagnostic.py`, and `planning/AUDIO_INDEX.md` maps each file to its
lesson with duration, speech rate and licence. Download them once into `audio/` using
those URLs and everything resolves — `python3 tools/check_diagnostic.py --probe` will then
confirm each file matches its declared metadata.
| Recycled within the unit | 12 | as the original |

Each recording was **opened and machine-verified**, not trusted from its title: the audio file was
downloaded and probed (`ffprobe`) for true length and bitrate, measured (`ffmpeg`) for loudness and
clipping, transcribed independently with Whisper ASR, and that transcription compared against the
publisher's transcript. Measured results across all 80:

- speech rate **81–141 words per minute** (natural conversation is 150–190)
- transcript accuracy **0.96–1.00**
- longest recording **4:11**, so every one fits a 45-minute lesson
- all 89 audio files and 80 lesson pages return HTTP 200

The teacher's book prints a **🎧 The recording** panel for every session — source, speakers, level,
length, measured speed, lesson-page link, direct audio link, licence, credit line, and anything to
know before pressing play. Run `python3 tools/check_course.py --net` to re-verify everything.

---

## Course design

**Every lesson** contains all thirteen required components — objectives, vocabulary, grammar,
pronunciation, listening, speaking, reading, writing, communication/real-life English,
guided practice, independent practice, review, homework. The *lesson type* decides which
skill is the main focus; the others still appear.

**Every lesson follows the same path:**
`PRESENT → GUIDED PRACTICE → INDEPENDENT PRACTICE → COMMUNICATION`

**Unit structure (7 lessons):**
1. Getting Started · 2. A Closer Look 1 (vocabulary + pronunciation) · 3. A Closer Look 2 (grammar) ·
4. Communication · 5. Skills 1 (reading + speaking) · 6. Skills 2 (listening + writing) ·
7. Looking Back & Project

### Scope and sequence

| Unit | Topic | Main grammar | Pronunciation |
|---|---|---|---|
| 1 | Hobbies | present simple; verbs of liking + V-ing | /ə/ /ɜː/; compound-noun stress |
| 2 | Healthy Living | imperatives; should / shouldn't; too much / too many | /f/ /v/; final /t/ /d/ /k/ |
| 3 | Community Service | past simple (+ / – / ?) | -ed endings /t/ /d/ /ɪd/ |
| 4 | Music and Arts | comparatives and superlatives; as … as | /ʊ/ /uː/ |
| 5 | Food and Drink | countable/uncountable; some/any; much/many | /ɒ/ /ɔː/; weak *of* |
| 6 | A Visit to a School | present simple **vs** present continuous (incl. future arrangements) | -tion /ʃn/ · -sion /ʒn/ + stress |
| 7 | Traffic | must / mustn't; *It is…* (distance) / *It takes…* (time); directions | /aɪ/ /eɪ/; final /t/ |
| 8 | Films | although / but / however; -ed vs -ing adjectives | /ɪ/ /iː/; -teen vs -ty |
| 9 | Festivals Around the World | articles a / an / the / –; question forms | /θ/ /ð/ |
| 10 | Energy Sources | will / won't (predictions, promises, offers) | /tʃ/ /dʒ/; contraction *'ll* |
| 11 | Travelling in the Future | might; possessive pronouns; can | final /l/; 3-syllable stress |
| 12 | English-Speaking Countries | present perfect with ever/never/been to | final clusters /st/ /sk/ /nd/ |

Review & Test blocks come after Units 3, 6, 9 and 12 (2 sessions each: consolidation + a
45-minute progress test with a paired speaking assessment).

---

## Built for Vietnamese learners

The course attacks eight documented difficulties, with a named routine that returns in every unit:

- dropped **final consonants** and **consonant clusters**
- flattened **word stress** and sentence stress
- the missing sounds /θ/ /ð/ /ʃ/ /ʒ/ /v/ /z/
- listening to **connected speech**
- **word-for-word translation** (*I very like it*, *Because … so …*, *by foot*)
- confusion between **similar structures** (present simple vs continuous, much vs many, will vs might)
- missing **verb endings and articles**
- **low speaking confidence** — pair work before whole-class work, fixed sentence frames, thinking time

Listening is now **authentic**: students hear American, British, Australian and international
English at a measured 81–141 wpm rather than a teacher reading a script aloud.

A **wall list of typical errors** grows through the year (six per unit, 72 by June). Each review
block revisits it, and in the final lesson every student diagnoses their own three weak points.

---

## The adaptive system

**Diagnose → identify gaps → adjust teaching → teach → reassess → adjust again.**

| When | What |
|---|---|
| Periods 1–2 | **Paper A**, the initial diagnostic — 80 marks across six strands |
| After period 2 | **Checkpoint 0** — provisional bands from the 60 written marks |
| After period 9 | **Checkpoint 1** — full profile including speaking; the triggers fire and the programme changes |
| Period 48 | **Paper B**, mid-year — re-band, and test every fired trigger for closure |
| Periods 93–94 | **Paper C**, final — growth per strand against September, and the Grade 8 handover |

### What Paper A measures

Listening 12 · Reading 12 · Vocabulary 10 · Grammar 12 · Writing 14 · Speaking 12 ·
Pronunciation 8 = **80**.

Items are calibrated pre-A1 → A2 and weighted towards the floor (67% of Paper A's
objective items sit at or below A1). That is deliberate: a paper that only discriminates
at A2 produces a wall of low scores that all look the same, and the students whose
teaching most needs to change are exactly the ones it cannot tell apart.

Speaking and pronunciation are assessed **rolling** — 22 pairs × 3 minutes does not fit a
20-minute slot, so about six pairs are done in period 2 and the rest in three-minute slots
during Unit 1, finishing by period 9.

### Three bands, and a rule that overrides them

| Band | % of 80 | Programme |
|---|---|---|
| **Foundation** — below Grade 7 level | under 45% | The normal course, **plus** bridging lessons B1–B6 (the Grade 5–6 prerequisites Grade 7 silently assumes). Delivery mode depends on group size: a pre-course block above 40% of the class, whole-class warm-up inserts at 15–40%, targeted homework below that. |
| **Core** — at Grade 7 level | 45–69% | The course as written. No changes beyond whatever fired class-wide. |
| **Extension** — above Grade 7 level | 70%+ | The same lessons, with the extension bank E1–E6 replacing independent practice — different cognitive demand, never more gap-fills. |

Then the **relative-gap rule**: flag any strand 20+ points below that student's own mean.
Two students on 48/80 can need opposite lessons, and the total cannot tell them apart.

### Eight results that change the curriculum

| # | Fires when | The programme changes |
|---|---|---|
| T1 | past simple under 50% correct | B5 required before Unit 3; 8-minute insert in U3L3; cumulative irregular-verb homework |
| T2 | listening 15+ points below reading | pre-listening scaffold and a third play in every Skills 2 lesson; 0.85× first play to Unit 4; `BRIDGE` (88 wpm) as extra input |
| T3 | final-consonant criterion under 1.0/2 | the daily drill doubles to 60 seconds for Units 1–6; B6 taught whole-class; extra `-ed` pass in Unit 3 |
| T4 | vocabulary **and** Unit 1 revision both under 50% | 90-second retrieval quiz opens every lesson on a spacing schedule; cumulative word boxes |
| T5 | third-person -s under 60% | 6-minute insert in U1L3; B2 across the U1 warm-ups; -s corrected even in fluency stages to Unit 4 |
| T6 | 30%+ of the class writing at 4/14 or below | sentence-frame → guided → free ladder on every Skills 2 writing task in Units 1–6 |
| T7 | spread SD over 12 marks | fixed mixed-ability pairs; ★/★★/★★★ becomes the default route, run simultaneously |
| T8 | 25%+ of the class in the Extension band | extension bank from Unit 1; `EXT` (153 wpm) in Skills 2; peer-teaching from Unit 7 |

### How the course actually adapts

`curriculum/class_profile.py` is the hinge, and it is the only file a teacher edits:

```python
DIAGNOSED = True
STRANDS = {"listening": 38, "reading": 57, "vocab": 49, ...}
BANDS   = {"foundation": 16, "core": 22, "extension": 6}
```

```bash
python3 build.py
```

The Teacher's Coursebook then grows an **ADAPTIVE INSERT** box under the procedure of every
lesson a fired trigger names — printed where you will be standing when you need it, not in
an appendix — and a single **STANDING CHANGES** box in the front matter for the changes
that run all year. Book 6 prints this class's own teaching plan instead of a generic one.

Until then `DIAGNOSED = False`, and the course builds exactly as designed.

### What it will not do

It will not stream the class — every student stays in every lesson, and the band changes
what they do inside it. It will not issue a CEFR level. It will not claim Papers A and C
are statistically equated; they are structurally parallel and speed-matched, which
supports "her listening went from 33% to 75%" and not "she improved by 11.4 marks".

### Diagnostic audio

Ten VOA *Let's Learn English* recordings that the 92 teaching sessions never use — a
baseline cannot be built from material students are about to study. All public domain, so
unlike the ELLLO half of the corpus they may legally be printed in a test paper. Verified
with the repository's own harness; see `planning/AUDIO_INDEX.md`.

The corpus spread is deliberate: `BRIDGE` at **88 wpm** is the slowest recording anywhere
in the course and belongs to the Foundation group; `EXT` at **153 wpm** is the fastest and
belongs to the Extension group. The 92 lessons sit between them at 97–131 wpm.

---

## Rebuilding the files

```bash
python3 build.py                            # 7 DOCX books + 92 PPTX decks
python3 tools/check_course.py               # the 92 taught sessions and their audio
python3 tools/check_course.py --net         # …and that every audio URL is still live
python3 tools/check_diagnostic.py           # papers, marks, rubrics, triggers, bands
python3 tools/check_diagnostic.py --probe   # …and re-measures every MP3 with ffprobe
```

The two diagnostic sessions are paper-based and have no slide deck, which is why the count
is 94 sessions and 92 decks.

Requirements: `python-docx`, `python-pptx`.

### Where to edit content

```
curriculum/
  schema.py            dataclasses (Lesson, Ex, Word, Grammar, Pron, Stage, Paper, Trigger…)
  course.py            front matter: philosophy, VN difficulties, routines, assessment plan
  units/u01.py …       one file per unit — all lesson content lives here
  reviews.py           the four review & test blocks
  audio_sources.py     VERIFIED real recordings for the 92 sessions (generated — do not edit)
  diagnostic.py        Papers A, B and C, plus the two diagnostic sessions
  audio_diagnostic.py  the 10 verified recordings the diagnostic uses
  rubrics.py           writing, speaking and pronunciation rubrics
  adaptive.py          bands, triggers, bridging lessons, extension bank, decision tree
  class_profile.py     ← THE ONE FILE A TEACHER EDITS
generators/
  common.py            DOCX styling helpers
  teacher_book.py  student_book.py  workbook.py  homework.py  answer_key.py
  diagnostic_book.py   Book 6 · the teacher's diagnostic pack
  test_papers.py       Book 7 · the photocopiable student papers
  slides.py
tools/
  check_course.py      the 92 taught sessions, their audio and their answer keys
  check_diagnostic.py  the diagnostic and adaptive system
```

Edit a lesson in `curriculum/units/`, run `python3 build.py`, and all eight deliverables
update together. Edit `curriculum/class_profile.py` and rebuild, and the course adapts to
your class.

---

## Assessment built into the course

- **Diagnostic** — Paper A (periods 1–2), Paper B (period 48), Paper C (periods 93–94), on
  three rubrics that never change, so the September and May scores mean the same thing
- **Continuous** — homework, board work, pronunciation spot-checks, participation
- **15-minute tests** after Units 2, 5, 8, 11
- **45-minute progress tests** in the four review blocks (listening · language · reading · writing)
- **Speaking assessment** each block: 3 minutes in pairs — task 3 · fluency 2.5 · pronunciation 2.5 · accuracy 2
- **One project per unit** (poster, campaign, cookbook, gallery, awards, showcase): content 3 · language 3 · design 2 · presentation 2

Marking guides for writing, speaking and projects are printed at the front of the Answer Key.
