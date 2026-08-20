# Diagnostic & Adaptive System — design

**Date:** 2026-08-20
**Status:** implemented and verified — `tools/check_diagnostic.py --probe` reports 50 passed / 0 warnings / 0 failures
**Scope:** add a diagnostic/placement assessment and an adaptation layer to the existing
92-session Grade 7 course, without rewriting the existing units.

---

## 1. Problem

The course as built assumes every student starts at the same place. Vietnamese Grade 7
classes do not: a typical class contains students who never consolidated Grade 5–6
English alongside students already reading at A2. The course has no instrument to find
that out and no mechanism to respond to it.

We need: **diagnose → identify gaps → adjust teaching → teach → reassess → adjust again.**

## 2. What we are NOT doing

- Not rewriting Unit 1–12 content. The units are touched only by a mechanical
  `period=N` → `period=N+2` renumber.
- Not replacing the four Review & Test blocks. The mid-year and final diagnostics
  occupy the *test* session of Review 2 and Review 4 (periods 48 and 94), which already
  exist for exactly that purpose.
- Not inventing listening material. Every recording is an existing, published,
  verified real-human recording (see §5).

## 3. Calibration

Grade 7 entry under the MOET framework is consolidated A1 moving to A1+. The course
targets A1+ → A2. The diagnostic therefore spans **pre-A1 → A2**, weighted:

| Band of item | Share | Purpose |
|---|---|---|
| pre-A1 / A1 (Grade 5–6 content) | ~40% | discriminate at the bottom, where teaching decisions actually change |
| A1+ (expected Grade 7 entry) | ~40% | confirm readiness for the normal progression |
| A2 (Grade 7 exit / above) | ~20% | find the ceiling group |

A test that only discriminates at A2 produces a wall of low scores and tells the teacher
nothing about *what* to reteach. Weighting the floor is the single most important
calibration decision in this design.

## 4. Instrument

### 4.1 Paper A — initial diagnostic, 80 marks, 2 × 45'

Periods 1 and 2 of the school year. The year becomes 94 sessions: 92 taught plus these 2.

| Period | Section | Marks | Time |
|---|---|---|---|
| 1 | S1 Listening — 3 graded tasks | 12 | 12' |
| 1 | S2 Reading — 3 graded texts | 12 | 14' |
| 1 | S3 Vocabulary | 10 | 7' |
| 1 | S4 Grammar | 12 | 10' |
| 2 | S5 Writing — sentence-level + paragraph | 14 | 20' |
| 2 | S6 Speaking — paired, 3' | 12 | rolling |
| 2 | S7 Pronunciation — read-aloud card, 45" | 8 | rolling |

**Rolling speaking.** 22 pairs × 3 minutes = 66 minutes; it does not fit a 20-minute
slot. Speaking and pronunciation are therefore assessed *rolling*: ~6 pairs during
Period 2 while the rest write in silence, the remainder in 3-minute slots during the
warm-up and independent-practice stages of U1L1–U1L7. This produces two decision points:

- **Checkpoint 0 (after period 2)** — provisional band from the 60 written marks.
- **Checkpoint 1 (after period 9, end of Unit 1)** — confirmed six-strand profile
  including speaking and pronunciation. All adaptation decisions are taken here.

### 4.2 Paper B — mid-year diagnostic, 46 written marks, 1 × 45' (period 48)

Shorter, same section order, same rubrics. Listening 8 · reading 8 · vocabulary 6 ·
grammar 10 · writing 14 = 46, in 45 minutes. Replaces Progress Test 2 in the Review 2
block. Speaking sampled (2 minutes, one third of the class, rotating so every student is
sampled once across B and C); the sampled oral scores are reported separately and are
**not** added to the 46.

Because the papers have different totals, every comparison between them is made **per
strand as a percentage**, never on raw totals. Paper B's floor is also deliberately
higher than Paper A's — it measures movement on content that has actually been taught,
not placement — so the floor target is 30% of objective items at or below A1 rather than
45%. `tools/check_diagnostic.py` enforces both targets.

### 4.3 Paper C — final diagnostic, 80 marks, periods 93–94 + rolling speaking

Strict parallel form of Paper A: same structure, same mark allocation, same rubrics,
listening matched on words per minute, different content.

Paper A's written sections need 63 minutes, so Paper C's do too — a parallel form cannot
be compressed into one period without changing the instrument. Section 5 (writing, 20
minutes) is therefore sat in the last 20 minutes of period 93, the Review 4 consolidation
session, whose first 25 minutes stay as revision; Sections 1–4 (43 minutes) replace
Progress Test 4 in period 94. Speaking and pronunciation roll through the final fortnight.

Papers A and C are **structurally parallel and speed-matched, not statistically equated**.
That supports "her listening went from 33% to 75%", not "she improved by 11.4 marks".

## 5. Audio

Constraint: authentic, professionally recorded, age-appropriate speakers; no AI-generated
audio; no teacher-recorded audio; matched to target difficulty; same sources as the
course. The course corpus is 89 recordings (VOA Learning English + ELLLO), all already
assigned to the 92 sessions, so the diagnostic needs recordings the students will not
otherwise meet.

Ten previously unused VOA *Let's Learn English* Level 1 episodes were located and
verified with the repository's own harness (`tools/verification/verify.py`): page
fetched, published transcript extracted, audio downloaded, duration/bitrate/sample
rate/channels from `ffprobe`, mean and peak levels from `ffmpeg volumedetect`, speech
rate computed from transcript words over measured duration. `faster_whisper` is not
installed in this environment, so the ASR cross-check that the original 89 received was
not repeated; the VOA published transcript is used as authoritative.

VOA material is **public domain**, which matters here specifically: unlike the ELLLO half
of the corpus, it may legally be printed and distributed inside a test paper.

| Key | VOA lesson | Duration | WPM | Role |
|---|---|---|---|---|
| `D1` part 1 | L5 Where Are You? | 1:01 | 104 | Paper A, A1 floor |
| `D1` part 2 | L10 Come Over to My Place | 1:31 | 108 | Paper A, at level |
| `D1` part 3 | L27 I Can't Come In — excerpt 0:00–1:20 | 1:16 of 3:22 | 140 | Paper A, ceiling |
| `M1` part 1 | L4 What Is It? | 1:29 | 125 | Paper B |
| `M1` part 2 | L32 Welcome to the Treehouse — excerpt 0:00–1:40 | 1:38 of 3:48 | 124 | Paper B |
| `F1` part 1 | L9 Is It Cold? | 2:01 | 104 | Paper C, parallel to D1.1 |
| `F1` part 2 | L8 Are You Busy? | 1:58 | 105 | Paper C, parallel to D1.2 |
| `F1` part 3 | L38 She's My Best Friend — excerpt 0:00–1:20 | 1:20 of 3:31 | 124 | Paper C, parallel to D1.3 |
| `BRIDGE` | L33 Learning America's Sport | 3:48 | **88** | bridging bank — slowest input available |
| `EXT` | L42 I Was Minding My Own Business | 3:01 | **153** | extension bank — fastest, news register |

L33 (88 WPM) and L42 (153 WPM) sit either side of the course's own 97–131 WPM range and
are used deliberately as the remedial and extension poles.

Files are downloaded into `audio/` under the existing naming convention
`F<KEY>_<part>_<source-basename>.mp3` and indexed in `planning/AUDIO_INDEX.md`.

## 6. Interpretation

### 6.1 Bands (on 80 marks)

| Band | Marks | % | Meaning |
|---|---|---|---|
| **Foundation** — below Grade 7 entry | 0–35 | <45% | Grade 5–6 language not consolidated |
| **Core** — at Grade 7 entry | 36–55 | 45–69% | ready for the normal progression |
| **Extension** — above Grade 7 entry | 56–80 | ≥70% | ready for greater cognitive demand |

Paper B (46 written marks) uses the same percentage cut-offs.

### 6.2 Relative-gap rule

Banding on a total hides profile. For each student, compute the mean strand percentage,
then flag any strand **≥20 percentage points below that student's own mean**. A strong
reader with weak listening needs a different intervention from a uniformly weak student,
and the total score cannot distinguish them.

### 6.3 Six-strand profile

Every student gets a profile card across: listening comprehension · reading
comprehension · vocabulary · grammar · writing · speaking, with pronunciation reported
as a sub-score of speaking and separately as a four-criterion pronunciation profile.

## 7. Class-level triggers

Computed from class aggregates at Checkpoint 1, re-evaluated at periods 48 and 94.
Each trigger names a threshold, an interpretation and a prescribed change to the
programme.

| # | Trigger | Fires when | Programme change |
|---|---|---|---|
| T1 | Past simple weak | <50% class-correct on grammar items testing past simple | U3L3 gains an 8-minute reinforcement insert; bridging B5 becomes required before Unit 3; Unit 3 homework switches to cumulative irregular-verb retrieval |
| T2 | Listening gap | class listening % ≥15 points below reading % | every Skills 2 lesson gains a pre-listening scaffold and a third play; first play at 0.85× for Units 1–4; `BRIDGE` (88 WPM) added as extra input |
| T3 | Final sounds weak | pronunciation criterion "final consonants & clusters" mean <1.0/2 | the 30-second final-consonant drill becomes 60 seconds for Units 1–6; Unit 3 `-ed` endings gets a full extra pass |
| T4 | Vocabulary retention low | vocabulary section <50% **and** Unit 1 revision set <50% | 5-item retrieval quiz opens every lesson; word-box homework becomes cumulative, not unit-local |
| T5 | Third-person -s unstable | <60% on present-simple 3rd-person items | U1L3 gains a 6-minute insert; the HE-SHE-IT=S chant runs daily to Unit 4 |
| T6 | Writing below sentence level | ≥30% of class score ≤4/14 on writing | sentence-frame → guided → free scaffold ladder applied to every Skills 2 writing task in Units 1–6 |
| T7 | Wide spread | standard deviation of totals >12 marks | permanent mixed-ability A/B pairing; the existing ★/★★/★★★ workbook columns become the default differentiation route |
| T8 | Extension-heavy class | ≥25% of class in Band 3 | extension bank activated from Unit 1; Extension students default to the ★★★ column |

## 8. Bridging lessons (Foundation band)

Six 45-minute lessons covering the Grade 5–6 prerequisites Grade 7 silently assumes.
Each is also usable as two 20-minute warm-up inserts.

| | Lesson | Prerequisite for |
|---|---|---|
| B1 | *be* + personal pronouns + possessive adjectives | everything |
| B2 | present simple: 3rd-person -s, do/does questions | Unit 1 |
| B3 | there is / there are; a / an / some; plural -s | Units 5, 6 |
| B4 | question words + question word order | Units 1, 9 |
| B5 | past simple: *be*, regular -ed, top-20 irregulars | Unit 3 |
| B6 | sound-to-spelling: final consonants, -ed endings, word stress | Units 2, 3 |

**Delivery mode depends on how large the Foundation band is:**

- \>40% of class → B1–B6 taught as a pre-course block before Unit 1 (adds 6 periods)
- 15–40% → delivered as warm-up inserts inside Units 1–3, whole class
- <15% → targeted homework plus a weekly 10-minute clinic for the named students

## 9. Extension bank (Extension band)

Six activities mapped to unit pairs. The design rule is **different cognitive demand,
not more exercises** — no additional gap-fills.

| | Activity | Units |
|---|---|---|
| E1 | Class survey → data report with frequency adverbs | 1–2 |
| E2 | Opinion paragraph with concession (*although / however*, pre-taught from Unit 8) | 3–4 |
| E3 | 90-second vlog script, recorded, peer-reviewed against a checklist | 5–6 |
| E4 | Structured debate: three arguments plus rebuttal | 7–8 |
| E5 | Research summary from an authentic VOA text, in own words (uses `EXT`, 153 WPM) | 9–10 |
| E6 | Peer-teaching: prepare and teach a 10-minute grammar slot to the Core group | 11–12 |

## 10. Rubrics

- **Writing /14** — task completion 4 · organisation 2 · grammar 3 · vocabulary 3 · mechanics 2
- **Speaking /12** — task completion 3 · fluency & interaction 3 · accuracy 3 · range 3
- **Pronunciation /8** — final consonants & clusters 2 · word stress 2 · target sounds /θ ð ʃ ʒ v z/ 2 · overall intelligibility 2

Every criterion has observable band descriptors and a Vietnamese-learner note naming the
specific L1 interference to expect.

## 11. Code

### New files

| File | Contents |
|---|---|
| `curriculum/audio_diagnostic.py` | `DIAG_AUDIO` dict — the 10 verified recordings with full source/licence metadata. Separate from `audio_sources.py`, which is generated and marked do-not-hand-edit. |
| `curriculum/diagnostic.py` | Papers A, B, C as data; the two diagnostic `Lesson` objects for periods 1–2; administration procedure and teacher script. |
| `curriculum/rubrics.py` | Writing, speaking and pronunciation rubrics as `Rubric`/`Criterion` data. |
| `curriculum/adaptive.py` | Bands, the relative-gap rule, triggers T1–T8, bridging lessons B1–B6, extension bank E1–E6, decision tree. |
| `curriculum/class_profile.py` | The editable class profile. Defaults to `DIAGNOSED = False` so output is unchanged until a real class is tested. |
| `generators/diagnostic_book.py` | Book 6 — `06_Diagnostic_and_Adaptive_System.docx` (teacher pack). |
| `generators/test_papers.py` | Book 7 — `07_Diagnostic_Test_Papers.docx` (clean photocopiable papers, no answers). |

### Schema additions (additive only)

`Item`, `Task`, `Section`, `Paper`, `Criterion`, `Rubric`, `Band`, `Trigger`, `Bridge`,
`Extension` — plus constructor helpers matching the existing `V()`/`G()`/`EX()` style. No
existing dataclass field is changed or removed.

`Trigger` carries two distinct kinds of change, and keeping them apart is what makes the
adapted Coursebook readable:

- `insert_at` — explicit lesson codes that get a full **ADAPTIVE INSERT** box printed
  under the procedure. For a change that happens at a particular moment in a particular
  lesson.
- `standing` — one line describing a change that runs all year (a daily drill, a pairing
  rule, a marking rule), printed **once** in the front matter.

Without that split, a trigger scoped to "every lesson" stamps 94 identical boxes; four
such triggers produced 396 boxes in the first build, which makes the book unreadable and
guarantees the boxes get ignored. The check suite now fails any trigger with more than
twenty inserts, or with neither an insert nor a standing change.

### Edits to existing files

| File | Edit |
|---|---|
| `curriculum/units/u01.py`–`u12.py` | mechanical `period=N` → `period=N+2` |
| `curriculum/reviews.py` | same renumber; Review 2/4 test sessions cross-reference Papers B and C |
| `curriculum/__init__.py` | `load_diagnostic()`, `load_bridging()`; `all_lessons()` prepends the 2 diagnostic sessions |
| `generators/teacher_book.py` | render adaptive inserts where the class profile fires them; add the diagnostic sessions to the lesson-plan sequence |
| `build.py` | build books 6 and 7; report 94 sessions |
| `README.md` | document the adaptive system |
| `planning/AUDIO_INDEX.md` | diagnostic audio section |
| `tools/check_course.py` | expect 94 sessions; validate diagnostic wiring, mark totals and rubric arithmetic |

### Adaptation mechanism

`class_profile.py` holds `DIAGNOSED`, per-strand class percentages, band counts and the
fired trigger list. Generators import it. When `DIAGNOSED is False` the existing books
build byte-identically to today apart from the period renumber. When a teacher fills it
in, `generators/teacher_book.py` stamps an **ADAPTIVE INSERT** box into the affected
lesson plans and Book 6 prints the resulting teaching plan.

## 12. Validation

1. `python3 build.py` completes; 7 DOCX + 94 PPTX decks.
2. `python3 tools/check_course.py` passes with the updated session count.
3. New `tools/check_diagnostic.py`: every section's item count matches its mark
   allocation; every item has an answer; rubric criteria sum to the stated total;
   Paper A and Paper C are structurally parallel; every trigger names an existing
   bridging lesson or extension activity; every diagnostic audio file exists on disk
   and its duration matches the metadata.
4. Period sequence is 1..94 with no gaps or duplicates.
5. Every diagnostic listening answer is verifiably present in the published transcript.
6. Book 7 leaks no answer, transcript, marking note or construct label.
7. No diagnostic recording is reused by any of the 92 teaching sessions.
8. The documented worked example fires exactly the triggers it claims to, and an empty
   profile leaves all eight *undecidable* rather than silently "not fired".
9. `--probe` re-measures every MP3 with ffprobe and compares against the declared
   duration, codec, sample rate and channel count.

## 13. Assumptions

- Class of 40–45, one teacher, no language lab, students may not have phones.
- The teacher can play MP3 audio from a laptop and speaker.
- Vietnamese may be used for test rubric instructions in the Foundation-facing material.
