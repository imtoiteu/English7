# Audio hyperlink audit

Generated 2026-08-21 · re-verify with `python3 tools/check_audio_links.py`

Every audio activity in every generated document now offers **two** ways to reach the same
recording:

| | Opens | Works when |
|---|---|---|
| **▶ Play audio** | the local MP3 in `audio/` | you have the project folder |
| **🌐 Listen online** | the publisher's official page for that exact recording | always — including for someone you emailed only the .docx |

Both are always present when both exist. The online link is not a fallback that replaces the
local one; it sits beside it, because a colleague who is sent a single file has no `audio/`
directory and for them the local link is dead while the publisher's page still plays the same
recording. No MP3 is embedded in any document.

---

## Totals

| | |
|---|---|
| DOCX audited | **7** |
| PPTX audited | **92** |
| Listening activities | **92** lessons + **8** diagnostic tasks = **100** |
| **Local links** (▶ Play audio) | **505** |
| **Online links** (🌐 Listen online) | **445** |
| **Total clickable audio links** | **950** |
| Distinct MP3 files referenced | **99** |
| Distinct official source pages | **90** |
| Recordings with no official source URL | **0** |
| Links to a missing local file | **0** |
| Links to a generic homepage | **0** |
| Ambiguous mappings | **0** |
| MP3s embedded in a document | **0** |

## Per document

| Document | ▶ Local | 🌐 Online | Total | Audience |
|---|---|---|---|---|
| `01_Teachers_Coursebook.docx` | 122 | 107 | 229 | Teacher |
| `02_Student_Coursebook.docx` | 119 | 104 | 223 | Student |
| `03_Exercise_and_Practice_Book.docx` | 0 | 0 | 0 | Student — renders no listening activity |
| `04_Homework_Book.docx` | 0 | 0 | 0 | Student — renders no listening activity |
| `05_Teachers_Answer_Key.docx` | 119 | 104 | 223 | Teacher |
| `06_Diagnostic_and_Adaptive_System.docx` | 18 | 18 | 36 | Teacher |
| `07_Diagnostic_Test_Papers.docx` | 8 | 8 | 16 | Student paper, teacher-operated |
| 92 × `output/slides/…/*.pptx` | 119 | 104 | 223 | Teacher, in class |
| **TOTAL** | **505** | **445** | **950** | |

Book 6 carries each diagnostic recording twice by design — once in the task's audio box and
once in the pre-flight check table (which also covers `BRIDGE` and `EXT`, played by the
teacher for trigger T2 and extension E5 but belonging to no paper).

## Why online links are fewer than local ones

505 local versus 445 online is correct, not a gap. ELLLO publishes a multipart recording as
several conversations on **one** page, so four parts share a single official source. Emitting
four identical links would be noise; inventing four separate URLs would be a fabrication.

* **Local links are per part** — every part is individually playable.
* **Online links are per distinct page** — one per real published source.

| Lesson | Local (parts) | Online (distinct pages) | Why |
|---|---|---|---|
| U1L1 | 1 | 1 | single recording |
| U7L3 | 4 | 1 | 4 conversations, 1 ELLLO page |
| U1L7 | 2 | 2 | Looking Back: replays L2 and L3, 2 pages |
| U7L7 | 5 | 2 | Looking Back: L2 + all 4 parts of L3, 2 pages |
| U12L7 | 5 | 2 | Looking Back: L2 + all 4 parts of L3, 2 pages |

## Diagnostic listening tasks

| Task | Q | MP3 (local) | Official source page |
|---|---|---|---|
| **A-L1** | 1–4 | `FD1_1_ab9c2944-eddc-4806-9296-290bfa8c6ff2_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-5-where-are-you/3168971.html> |
| **A-L2** | 1–4 | `FD1_2_442a6a50-693e-411f-8cff-99e40d16614c_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-10/3285228.html> |
| **A-L3** | 1–4 | `FD1_3_4b0918a8-33b1-4b9d-8d88-f54d8a1be9ea_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-27-i-cant-come-in/3457316.html> |
| **B-L1** | 1–4 | `FM1_1_af0324f6-67c5-4c0c-ab42-abb0cd33817c_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-4/3168920.html> |
| **B-L2** | 1–4 | `FM1_2_054d9504-47b3-4cc2-80d1-cb66fff404e4_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-32-welcome-treehouse/3547306.html> |
| **C-L1** | 1–4 | `FF1_1_fe67e651-87d0-4b62-9c68-749b2d3c2f21_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-9-is-it-cold/3261789.html> |
| **C-L2** | 1–4 | `FF1_2_ae6c5055-13ae-485b-995d-b347125ecf10_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-8-are-you-busy/3253185.html> |
| **C-L3** | 1–4 | `FF1_3_7b357de6-9247-45fd-8e49-77197599f6d5_hq.mp3` | <https://learningenglish.voanews.com/a/lets-learn-english-lesson-38-shes-my-best-friend/3591967.html> |

## Online-link verification

All **90** distinct official source pages were fetched and checked twice:

1. **Reachability** — 90/90 returned HTTP 200.
2. **Correspondence** — 90/90 pages were confirmed to actually host the
   exact MP3 filenames attributed to them. A 200 alone would not rule out a soft-404 or a
   page that simply exists but carries different audio.

One URL looks malformed and is not: `…/B1-08-Have-to-Must-Obligation..html` has a double dot,
from a trailing period in the ELLLO slug. It returns 200 and hosts the right recording.

## Verification

```bash
python3 tools/check_audio_links.py    # 23 checks, local and online
python3 tools/fetch_audio.py --verify # all 99 recordings present
```

The suite checks that every listening activity has both link types; that every relative link
resolves to a real file *from that document's own directory*; that every online link is an
exact recorded source page and never a homepage; that each of the 92 decks links exactly its
own lesson's recordings and pages; that nothing embeds an MP3; that every file opens; and —
against a text snapshot taken before any linking — that no existing content changed.

## Declared content change

Book 6's pre-flight table used to truncate filenames to 34 characters, making it useless for
locating a file. It now prints the full name and a Play column. The suite validates that this
is the **only** difference in that document; any other change there still fails.

## Manual-review items

* **Book 7 is a student paper.** Its links are inert on a photocopy, but the digital file lets
  a holder play or open the test audio. Distribute as print or link-free PDF if that matters.
* **Local links assume `output/` and `audio/` stay together.** Move the whole project folder,
  not one part. The online links are unaffected and keep working.
* **A fresh clone has no `audio/`** (gitignored). Until `tools/fetch_audio.py` runs, a rebuild
  emits online links only — which is exactly the recipient scenario this feature exists for.
