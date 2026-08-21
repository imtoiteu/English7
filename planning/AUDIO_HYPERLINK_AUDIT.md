# Audio hyperlink audit

Generated 2026-08-21 · re-verify with `python3 tools/check_audio_links.py`

Every place in this course where somebody has to press play now carries a real, clickable
hyperlink to the exact recording that activity uses. The link points at the local MP3
whenever the file is on disk, and falls back to the publisher's official lesson page for
that same recording only when it is not — never to a generic page, and never to a
different recording because the topic looked similar.

No MP3 is embedded in any document. Linking keeps a slide deck a few hundred KB instead of
carrying megabytes of audio, and keeps one copy of each recording shared by the books, the
slides and the diagnostic papers.

---

## Totals

| | |
|---|---|
| DOCX audited | **7** |
| PPTX audited | **92** |
| Listening activities found | **92** lesson activities + **8** diagnostic tasks = **100** |
| Audio hyperlinks added | **505** clickable links |
| Distinct MP3 files referenced | **99** |
| File references resolved | **129** (multipart and replayed audio counted per part) |
| Links pointing at a missing file | **0** |
| Documents that could not be linked | **0** |
| MP3s embedded in a document | **0** |

## Per document

| Document | Clickable audio links | Audience | What the link says |
|---|---|---|---|
| `01_Teachers_Coursebook.docx` | 122 | Teacher | ▶ Play audio — inside the 🎧 recording panel, beside source, licence and credit |
| `02_Student_Coursebook.docx` | 119 | Student | ▶ Listen — nothing else; no filename, no source, no transcript |
| `03_Exercise_and_Practice_Book.docx` | 0 | Student | — renders no listening activity, so correctly has none |
| `04_Homework_Book.docx` | 0 | Student | — renders no listening activity, so correctly has none |
| `05_Teachers_Answer_Key.docx` | 119 | Teacher | ▶ Play audio, introduced by “To check a listening answer, replay it” |
| `06_Diagnostic_and_Adaptive_System.docx` | 18 | Teacher | ▶ Play audio in each task's audio box, ▶ Play in every pre-flight row |
| `07_Diagnostic_Test_Papers.docx` | 8 | Student paper, teacher-operated | ▶ Play audio (teacher) |
| 92 × `output/slides/…/*.pptx` | 119 | Teacher, in class | A blue **▶ Play audio** button on each Listening slide; one button per part |

## Relative paths

Targets are stored verbatim and resolved by Word/PowerPoint against the document's own
location on disk, so the depth has to match where the file is actually written:

| Document location | Link target |
|---|---|
| `output/BOOK.docx` | `../audio/<file>.mp3` |
| `output/slides/UnitXX_.../DECK.pptx` | `../../../audio/<file>.mp3` |

## Diagnostic listening tasks

| Task | Questions | Audio key | MP3 | Local path | Duration | Speed | Licence |
|---|---|---|---|---|---|---|---|
| **A-L1** | 1–4 | `D1_1` | `FD1_1_ab9c2944-eddc-4806-9296-290bfa8c6ff2_hq.mp3` | `../audio/FD1_1_ab9c2944-eddc-4806-9296-290bfa8c6ff2_hq.mp3` | 1:00 | 104 words per minute | Public domain |
| **A-L2** | 1–4 | `D1_2` | `FD1_2_442a6a50-693e-411f-8cff-99e40d16614c_hq.mp3` | `../audio/FD1_2_442a6a50-693e-411f-8cff-99e40d16614c_hq.mp3` | 1:30 | 108 words per minute | Public domain |
| **A-L3** | 1–4 | `D1_3` | `FD1_3_4b0918a8-33b1-4b9d-8d88-f54d8a1be9ea_hq.mp3` | `../audio/FD1_3_4b0918a8-33b1-4b9d-8d88-f54d8a1be9ea_hq.mp3` | 1:16 | 140 words per minute | Public domain |
| **B-L1** | 1–4 | `M1_1` | `FM1_1_af0324f6-67c5-4c0c-ab42-abb0cd33817c_hq.mp3` | `../audio/FM1_1_af0324f6-67c5-4c0c-ab42-abb0cd33817c_hq.mp3` | 1:29 | 125 words per minute | Public domain |
| **B-L2** | 1–4 | `M1_2` | `FM1_2_054d9504-47b3-4cc2-80d1-cb66fff404e4_hq.mp3` | `../audio/FM1_2_054d9504-47b3-4cc2-80d1-cb66fff404e4_hq.mp3` | 1:38 | 124 words per minute | Public domain |
| **C-L1** | 1–4 | `F1_1` | `FF1_1_fe67e651-87d0-4b62-9c68-749b2d3c2f21_hq.mp3` | `../audio/FF1_1_fe67e651-87d0-4b62-9c68-749b2d3c2f21_hq.mp3` | 2:01 | 104 words per minute | Public domain |
| **C-L2** | 1–4 | `F1_2` | `FF1_2_ae6c5055-13ae-485b-995d-b347125ecf10_hq.mp3` | `../audio/FF1_2_ae6c5055-13ae-485b-995d-b347125ecf10_hq.mp3` | 1:58 | 105 words per minute | Public domain |
| **C-L3** | 1–4 | `F1_3` | `FF1_3_7b357de6-9247-45fd-8e49-77197599f6d5_hq.mp3` | `../audio/FF1_3_7b357de6-9247-45fd-8e49-77197599f6d5_hq.mp3` | 1:20 | 124 words per minute | Public domain |

Both diagnostic books link all eight. `BRIDGE` and `EXT` are also linked in Book 6: they
belong to no paper, but the teacher plays them for trigger T2 (slow input) and extension E5.

## The mapping rule that matters

A file is named `F<lesson code>_<part>_<source basename>.mp3` — **derived** from the recorded
URL, never stored, so it cannot drift. Two cases would produce a broken link if handled naively:

* **Looking Back lessons** carry `recycled_from` and replay their unit's Lesson 2 and Lesson 3
  audio rather than holding a copy. Their links therefore point at the *source* lesson's files —
  `U1L7` links `FU1L2_…` and `FU1L3_…`, because `FU1L7_…` does not exist.
* **Multipart recordings** (U7L3, U10L6, U12L3 are published as four separate conversations)
  resolve to every part, in source order. Nothing is collapsed into one file.

The two combine: `U7L7` and `U12L7` each resolve to **five** files — their Lesson 2 recording
plus all four parts of their Lesson 3 recording.

| Lesson | Files linked |
|---|---|
| U1L7 | 2 |
| U2L7 | 2 |
| U3L7 | 2 |
| U4L7 | 2 |
| U5L7 | 2 |
| U6L7 | 2 |
| U7L3 | 4 |
| U7L7 | 5 |
| U8L7 | 2 |
| U9L7 | 2 |
| U10L6 | 4 |
| U10L7 | 2 |
| U11L7 | 2 |
| U12L3 | 4 |
| U12L7 | 5 |

## Verification

```bash
python3 tools/check_audio_links.py       # 18 checks
python3 tools/fetch_audio.py --verify    # all 99 recordings present and readable
```

The suite checks that every listening activity has a link; that every relative link resolves
to a real file *from that document's own directory*; that each of the 92 decks links exactly
its own lesson's recordings and no others; that no document embeds an MP3; that every file
still opens; and — against a text snapshot taken before any linking — that no existing
content changed.

## Declared content change

One change beyond adding links, and it is deliberate: Book 6's pre-flight check table used to
truncate every filename to 34 characters (`FD1_1_ab9c2944-eddc-4806-9296-290b…`), which made
it useless for locating a file. It now prints the full name and carries a **Play** column. The
verification suite validates that this is the *only* difference in that document; any other
change there still fails.

## Manual-review items

* **Book 7 is a student paper.** Its links say “▶ Play audio (teacher)” and are inert on a
  photocopy, but in the digital file a student with the document could play the recording.
  If that matters for test security, distribute Book 7 as print or PDF-without-links.
* **Word may warn about opening a linked file.** This is normal for any external hyperlink and
  is not a fault in the documents.
* **Links break if `output/` and `audio/` are separated.** The relative path assumes both stay
  in the same project folder. Move the whole folder, not one part of it.
* **A fresh clone has no `audio/`** (it is gitignored). Run `python3 tools/fetch_audio.py`
  first; otherwise the build writes source-page fallback links, which read “▶ Listen online”.
