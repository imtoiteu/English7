# -*- coding: utf-8 -*-
"""Write planning/AUDIO_MAPPING_VERIFIED.md from the verified data."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from curriculum import all_lessons
SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verification")
V = {r['key']: r for r in json.load(open(os.path.join(SCRATCH, "final.json")))}

UNIT_TITLES = {1:"Hobbies",2:"Healthy Living",3:"Community Service",4:"Music and Arts",
 5:"Food and Drink",6:"A Visit to a School",7:"Traffic",8:"Films",9:"Festivals Around the World",
 10:"Energy Sources",11:"Travelling in the Future",12:"English-Speaking Countries"}
SRC = {"VOA":"VOA","SG":"ELLLO SG","1ME":"ELLLO 1ME"}

def main():
    ls = {l.code: l for l in all_lessons()}
    out = []
    w = out.append
    w("# Verified 92-Session Audio Mapping — English 7\n")
    w("Every recording below was **opened and machine-verified**, not taken on trust from a title, "
      "snippet or search result. For each one the audio file was downloaded and probed with `ffprobe` "
      "(true length, bitrate, channels), measured with `ffmpeg` (loudness, clipping), transcribed "
      "independently with Whisper ASR, and that machine transcription was compared against the "
      "publisher's transcript. Speech rate is measured **from the audio itself**, not estimated.\n")
    w("Regenerate with `python3 tools/write_mapping_doc.py`; re-check with `python3 tools/check_course.py --net`.\n")
    ok = [r for r in V.values() if r.get('status') == 'OK']
    w("## Summary\n")
    w("| | |\n|---|---|")
    w(f"| Sessions | 92 |")
    w(f"| With an external real-human recording | **80** |")
    w(f"| Looking Back sessions recycling the unit's own audio | 12 |")
    w(f"| Distinct recordings | {len({r['page'] for r in ok})} |")
    w(f"| Speech rate (as heard) | {min(r['wpm_gross'] for r in ok)}–{max(r['wpm_gross'] for r in ok)} wpm |")
    w(f"| Transcript accuracy (ASR vs published) | {min(r['coverage'] for r in ok):.2f}–{max(r['coverage'] for r in ok):.2f} |")
    w(f"| Total verified audio | {sum(r['duration'] for r in ok)/60:.0f} minutes |")
    w("| Synthetic / TTS voices | none |\n")
    w("**Sources.** VOA *Let's Learn English* Level 1 (public domain — may be copied, played and printed "
      "in test papers); ELLLO *Sound Grammar* and *One Minute English* (© elllo productions; ELLLO permits "
      "teachers to download the audio and use it in class or on a class LMS).\n")
    w("British Council LearnEnglish Teens was **dropped**: it is bot-protected and could not be opened to "
      "verify a single recording, and its terms cover personal, non-commercial use only. Randall's ESL "
      "Cyber Listening Lab and the ELLLO Mixer conversations were dropped too — the Mixer audio is served "
      "from SoundCloud/Vimeo with no direct file, so it cannot be verified or reliably played offline.\n")

    for u in range(1, 13):
        w(f"\n### Unit {u} — {UNIT_TITLES[u]}\n")
        w("| # | Session | Recording | Source | Length | wpm | Transcript | Speakers |")
        w("|---|---|---|---|---|---|---|---|")
        for n in range(1, 8):
            code = f"U{u}L{n}"
            l = ls[code]; a = l.listening
            r = V.get(code, {})
            if a.recycled_from:
                w(f"| {l.period} | {code} {l.lesson_type} | *replays {', '.join(a.recycled_from)}* "
                  f"| recycled | — | — | — | — |")
            else:
                w(f"| {l.period} | {code} {l.lesson_type} | [{a.title}]({a.source_page}) "
                  f"| {SRC[r['kind']]} | {a.duration} | {r['wpm_gross']} | {r['coverage']:.2f} "
                  f"| {a.speakers.split('—')[-1].strip()[:44]} |")
    w("\n### Review & Test blocks\n")
    w("| # | Session | Recording | Source | Length | wpm | Transcript |")
    w("|---|---|---|---|---|---|---|")
    for code in ["REV1L1","REV1L2","REV2L1","REV2L2","REV3L1","REV3L2","REV4L1","REV4L2"]:
        l = ls[code]; a = l.listening; r = V[code]
        w(f"| {l.period} | {code} | [{a.title}]({a.source_page}) | {SRC[r['kind']]} "
          f"| {a.duration} | {r['wpm_gross']} | {r['coverage']:.2f} |")
    w("\nAll eight review/test recordings are VOA, i.e. **public domain**, so the audio and its transcript "
      "may legally be embedded in the printed test paper.\n")

    w("\n## What verification changed\n")
    w("| Session | Rejected | Measured reason | Replaced with |")
    w("|---|---|---|---|")
    for row in [
      ("U1L5","ELLLO *Do you play sports?*","only 47 words of speech — too thin for a skills lesson","VOA L17 *Are You Free on Friday?*"),
      ("U3L5","ELLLO *What did you do last night?*","168 wpm — far above the Grade 7 envelope","VOA L29 *A Long Time Ago*"),
      ("U3L6","ELLLO *What did you do over the weekend?*","167 wpm","VOA L28 *I Passed It!*"),
      ("U4L5","ELLLO *Is jazz music interesting?*","only 67 words of speech","VOA L40 *The Woods Are Alive* (a stage audition)"),
      ("U8L5","ELLLO *What is your favourite TV show?*","**content** — it describes *Dexter*, a drama about a serial killer who 'kills bad people', with 'a lot of blood'","VOA L39 *It's Unbelievable!*"),
      ("U10L5","VOA L40 *The Woods Are Alive*","title suggested nature; the recording is a **theatre audition** — wrong unit","ELLLO *What will you do this month?*"),
      ("U10L6","ELLLO *What are your plans for tonight?*","202 wpm — the fastest item tested","ELLLO *The first conditional*"),
      ("U11L6","ELLLO *What is your favourite place?*","202 wpm and −30 dB (too quiet)","VOA L20 *What Can You Do?*"),
      ("U12L5","ELLLO *Where do you live?*","173 wpm","ELLLO *What is your country's geography like?*"),
      ("U12L6","ELLLO *What is different about the city and countryside?*","160 wpm","ELLLO *Where does your family live?*"),
      ("U9L6","(moved) ELLLO *Netherlands geography*","better placed in Unit 12; Unit 9 needs a festival/holiday topic","ELLLO *Who visits you on the holidays?*"),
      ("all VOA","the 64 kbps stream","the 128 kbps master is published alongside it","every VOA item now uses the 128 kbps file"),
    ]:
        w("| " + " | ".join(row) + " |")

    w("\n## Honest limitations\n")
    w("- **I cannot hear.** Everything above is machine verification of the actual audio files — length, "
      "bitrate, loudness, clipping, measured speech rate, and an independent ASR transcription checked "
      "against the publisher's transcript. That is stronger than trusting titles and snippets, and on these "
      "objective criteria stronger than a human ear, but it cannot judge how pleasant a voice sounds.\n")
    w("- **Topic fit is grammar-anchored in Unit 10 (Energy Sources).** No verified real recording in either "
      "corpus is about energy. Those sessions match on *grammar* (will / going to / first conditional), not "
      "subject matter. Unit 8 (Films) is partly the same: U8L1 is a memorial scavenger hunt.\n")
    w("- **Accents are mixed.** VOA is American; ELLLO Sound Grammar is native English; One Minute English "
      "speakers include the UK, USA, Australia, Belize, the Philippines, the Netherlands, Turkey, Ukraine, "
      "Kosovo and El Salvador. That is deliberate for Unit 12, and defensible elsewhere, but the course's "
      "IPA remains British-leaning.\n")
    w("- **Vietnamese content is gone from the listening strand.** Reading, speaking and writing keep Mai, "
      "Nam, Tet and the local context; the recordings are now British/American/international.\n")
    w("- **Internet is needed**, except for VOA, which is public domain and may be downloaded to a school "
      "laptop. ELLLO audio may be downloaded by the teacher for classroom/LMS use under ELLLO's own terms.\n")
    open(os.path.join(ROOT, "planning", "AUDIO_MAPPING_VERIFIED.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("wrote planning/AUDIO_MAPPING_VERIFIED.md")

if __name__ == "__main__":
    main()
