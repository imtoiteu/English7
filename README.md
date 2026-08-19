# ENGLISH 7 — A Complete Communicative Course
### Teaching system for Vietnamese Grade 7 students (MOET / *Tiếng Anh 7* framework)

This repository contains a **complete, ready-to-teach English course for one school year**:
12 units × 7 lessons + 4 review & test blocks × 2 = **92 teaching sessions of 45 minutes**.

Everything is generated from **one source of truth** (`curriculum/`), so the lesson plans,
the student book, the exercises, the homework, the answer key and the slides can never
drift out of sync. Every exercise has a unique reference (e.g. `U5.3-P4`) that is the same
in all six books.

---

## What to open first

| File | Who uses it | What it contains |
|---|---|---|
| `output/01_Teachers_Coursebook.docx` | Teacher | Full lesson plans: objectives, language content, staged procedure with timing, scripted teacher explanations, board plans, differentiation, assessment, answers |
| `output/02_Student_Coursebook.docx` | Student, in class | Explanations, vocabulary tables with IPA + Vietnamese, grammar, reading texts, listening tasks **and scripts**, speaking activities, writing, review boxes |
| `output/03_Exercise_and_Practice_Book.docx` | Student | Graded practice for every lesson: ★☆☆ Easy → ★★☆ Medium → ★★★ Difficult, plus a pronunciation drill and a speaking prompt in every lesson |
| `output/04_Homework_Book.docx` | Student, at home | 3–4 homework tasks per lesson (20–35 min) + a Revision Set after every unit |
| `output/05_Teachers_Answer_Key.docx` | Teacher | Every answer, model writing answers, suggested speaking answers, and explanations of the typical Vietnamese-learner errors |
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

## Rebuilding the files

```bash
python3 build.py                        # regenerates all 5 DOCX books + every PPTX deck
python3 tools/check_course.py --net     # 14-point check, including that every audio URL is live
```

Requirements: `python-docx`, `python-pptx`.

### Where to edit content

```
curriculum/
  schema.py        dataclasses (Lesson, Ex, Word, Grammar, Pron, Stage…)
  course.py        front matter: philosophy, VN difficulties, routines, assessment plan
  units/u01.py …   one file per unit — all lesson content lives here
  reviews.py       the four review & test blocks
  audio_sources.py VERIFIED real recordings: transcript, tasks, links, licence (generated)
generators/
  common.py        DOCX styling helpers
  teacher_book.py  student_book.py  workbook.py  homework.py  answer_key.py  slides.py
```

Edit a lesson in `curriculum/units/`, run `python3 build.py`, and all six deliverables
update together.

---

## Assessment built into the course

- **Continuous** — homework, board work, pronunciation spot-checks, participation
- **15-minute tests** after Units 2, 5, 8, 11
- **45-minute progress tests** in the four review blocks (listening · language · reading · writing)
- **Speaking assessment** each block: 3 minutes in pairs — task 3 · fluency 2.5 · pronunciation 2.5 · accuracy 2
- **One project per unit** (poster, campaign, cookbook, gallery, awards, showcase): content 3 · language 3 · design 2 · presentation 2

Marking guides for writing, speaking and projects are printed at the front of the Answer Key.
