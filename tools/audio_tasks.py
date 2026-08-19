# -*- coding: utf-8 -*-
"""Build listening tasks that are ANCHORED IN THE REAL TRANSCRIPT.

Every answer is checked against the transcript before it is emitted, so the
answer key cannot disagree with what the students actually hear.
"""
import re, random

SPK = re.compile(r"^([A-Z][A-Za-z.'’ ]{0,20}):\s*(.+)$")
NUMWORD = {"one":"three","two":"five","three":"seven","four":"nine","five":"two",
           "six":"eight","seven":"four","eight":"six","nine":"three","ten":"twelve",
           "eleven":"fifteen","twelve":"twenty","twenty":"thirty","thirty":"fifty"}
DAYSWAP = {"Monday":"Thursday","Tuesday":"Friday","Wednesday":"Sunday","Thursday":"Monday",
           "Friday":"Tuesday","Saturday":"Wednesday","Sunday":"Saturday"}
MONSWAP = {"January":"August","February":"October","March":"November","April":"September",
           "May":"December","June":"February","July":"March","August":"January",
           "September":"April","October":"June","November":"May","December":"July"}


def sentences(transcript):
    """(speaker, sentence) pairs from the published transcript."""
    out = []
    for line in transcript:
        line = line.strip()
        if not line or line.lower().startswith("conversation"):
            continue
        m = SPK.match(line)
        spk, body = (m.group(1), m.group(2)) if m else ("", line)
        for s in re.split(r'(?<=[.!?])\s+', body):
            s = s.strip()
            if 4 <= len(s.split()) <= 22 and not s.startswith('*'):
                out.append((spk, s))
    return out


def _swap(sent):
    """Return (false_sentence, true_fact) by changing exactly one fact, or None.

    Only facts that can be swapped without breaking the grammar are touched:
    weekdays, months, digits, and number words that are not sentence-initial
    and not part of a phrase like "one of the ...".
    """
    for table in (DAYSWAP, MONSWAP):
        for k, v in table.items():
            if re.search(rf'\b{k}\b', sent):
                return re.sub(rf'\b{k}\b', v, sent, count=1), k
    m = re.search(r'(?<![\w.])(\d{1,4})\b', sent)
    if m:
        n = int(m.group(1))
        new_n = str(n + 3 if n < 100 else n + 10)
        return sent[:m.start(1)] + new_n + sent[m.end(1):], m.group(1)
    for k, v in NUMWORD.items():
        for m in re.finditer(rf'\b{k}\b', sent, re.I):
            if m.start() == 0:                       # never rewrite the first word
                continue
            if sent[m.end():m.end() + 4].lower().startswith(' of'):
                continue                             # "one of the ..." must stay
            return sent[:m.start()] + v + sent[m.end():], k
    return None


def main_idea(code, gist, other_gists, rng):
    """MCQ on the global meaning. Distractors come from other units, so they are false."""
    opts = [gist] + rng.sample(other_gists, 2)
    rng.shuffle(opts)
    letters = "ABC"
    correct = letters[opts.index(gist)]
    body = "   ".join(f"{letters[i]}. {o}" for i, o in enumerate(opts))
    return (["1. What is the recording mainly about?", f"   {body}"],
            [f"1. {correct} — {gist}"])


def true_false(sents, rng, used=None, n=5):
    """3 true + 2 false statements, every fact taken from the recording."""
    used = used if used is not None else set()
    full = " ".join(s for _, s in sents).lower()
    cands = [s for _, s in sents if len(s.split()) >= 6 and s not in used]
    if len(cands) < 4:
        return None
    rng.shuffle(cands)
    items, answers = [], []
    falses = []
    for s in cands:
        sw = _swap(s)
        if sw and sw[0].lower() not in full:
            falses.append((s, sw[0], sw[1]))
        if len(falses) >= 2:
            break
    if len(falses) < 2:
        return None
    trues = [s for s in cands if all(s != f[0] for f in falses)][:3]
    if len(trues) < 3:
        return None
    rows = [(t, True, None) for t in trues] + [(f[1], False, f[2]) for f in falses]
    rng.shuffle(rows)
    for _t in trues: used.add(_t)
    for _f in falses: used.add(_f[0])
    for i, (text, is_true, fact) in enumerate(rows, 1):
        items.append(f"{i}. {text}")
        answers.append(f"{i}. T" if is_true else f"{i}. F — the recording says “{fact}”.")
    return items, answers


def notice_form(sents, focus, rng, used=None, n=5):
    """Gap-fill on the target language, using real lines only.

    A focus entry may be a plain word or a regex written as "re:<pattern>".
    The same target word may be asked at most twice - repetition of the target
    form is the point of a grammar lesson, but five identical gaps are not.
    """
    used = used if used is not None else set()
    picked, items, answers = [], [], []
    counts = {}
    pats = []
    for f in focus:
        if f.startswith("re:"):
            pats.append((f, re.compile(f[3:], re.I)))
        else:
            pats.append((f.lower(), re.compile(rf'\b{re.escape(f)}\b', re.I)))
    for spk, s_ in sents:
        if len(picked) >= n:
            break
        if len(s_.split()) < 5 or s_ in used:
            continue
        if any(s_ == p for p, _ in picked):
            continue
        for key, pat in pats:
            m = pat.search(s_)
            if not m:
                continue
            word = s_[m.start():m.end()]
            if counts.get(word.lower(), 0) >= 2:
                continue                      # already asked for twice
            gapped = s_[:m.start()] + "_____" + s_[m.end():]
            picked.append((s_, (gapped, word, spk)))
            counts[word.lower()] = counts.get(word.lower(), 0) + 1
            break
    if len(picked) < 3:
        return None
    for _s, _ in picked:
        used.add(_s)
    for i, (_, (gapped, word, spk)) in enumerate(picked, 1):
        lead = f"{spk}: " if spk else ""
        items.append(f"{i}. {lead}{gapped}")
        answers.append(f"{i}. {word}")
    return items, answers


def which_conversation(transcript, rng, used, n=5):
    """Sound Grammar pages hold four separate conversations: ask which one."""
    blocks, cur = [], None
    for line in transcript:
        if re.match(r'^Conversation (\d)', line):
            cur = int(re.match(r'^Conversation (\d)', line).group(1))
            continue
        if cur is None:
            continue
        m = SPK.match(line.strip())
        if not m:
            continue
        body = m.group(2).strip()
        if 5 <= len(body.split()) <= 20 and body not in used:
            blocks.append((cur, body))
    if len({c for c, _ in blocks}) < 3:
        return None
    rng.shuffle(blocks)
    picked, seen = [], set()
    for c, b in blocks:                       # spread across conversations
        if c in seen and len(picked) < len({x for x, _ in blocks}):
            continue
        seen.add(c); picked.append((c, b))
        if len(picked) >= n:
            break
    if len(picked) < 3:
        return None
    items = [f"{i}. {b}" for i, (_, b) in enumerate(picked, 1)]
    answers = [f"{i}. Conversation {c}" for i, (c, _) in enumerate(picked, 1)]
    for _, b in picked:
        used.add(b)
    return items, answers


def ordering(sents, rng, used, n=5):
    """Put real lines back into the order they are heard."""
    seq = [s for _, s in sents if 5 <= len(s.split()) <= 20 and s not in used]
    if len(seq) < 4:
        return None
    start = rng.randrange(0, max(1, len(seq) - n))
    chosen = seq[start:start + n]
    if len(chosen) < 4:
        return None
    order = list(range(len(chosen)))
    shuffled = order[:]
    rng.shuffle(shuffled)
    items, answers = [], []
    for pos, idx in enumerate(shuffled, 1):
        items.append(f"{chr(96+pos)}. {chosen[idx]}")
    for pos, idx in enumerate(shuffled, 1):
        answers.append(f"{chr(96+pos)} = {order.index(idx) + 1}")
    for c in chosen:
        used.add(c)
    return items, ["Order heard: " + ", ".join(
        f"{chr(96+p)}" for p in sorted(range(1, len(shuffled) + 1),
                                       key=lambda q: shuffled[q - 1]))] + answers


def build(code, transcript, gist, focus, other_gists):
    """Return list of (suffix, title, instruction, items, answers, level, note).

    Task sentences are kept disjoint so one task never gives away another.
    """
    rng = random.Random(code)          # deterministic
    sents = sentences(transcript)
    used = set()
    out = []

    it, an = main_idea(code, gist, other_gists, rng)
    out.append(("L1", "Listen for the main idea",
                "Listen once. Choose the best answer.", it, an, "E",
                "Students do not need every word — only the overall topic."))

    # --- notice the target language first, and reserve those lines ---
    nf = notice_form(sents, focus, rng, used=used)

    # --- a detail task, from whichever provably-correct type fits ---
    detail = None
    tf = true_false(sents, rng, used=used)
    if tf:
        detail = ("Listen for details", "Listen again. Write T (true) or F (false).",
                  tf[0], tf[1],
                  "Every statement is taken from the recording; the false ones change one fact.")
    if detail is None:
        wc = which_conversation(transcript, rng, used)
        if wc:
            detail = ("Which conversation?",
                      "Listen again. Write the number of the conversation (1-4) you hear each line in.",
                      wc[0], wc[1], "All lines are exactly as spoken on the recording.")
    if detail is None:
        od = ordering(sents, rng, used)
        if od:
            detail = ("Listen for the order",
                      "Listen again. Number the lines 1-5 in the order you hear them.",
                      od[0], od[1], "The lines are exactly as spoken; only the order is changed.")
    if detail:
        out.append(("L2", detail[0], detail[1], detail[2], detail[3], "M", detail[4]))

    if nf:
        out.append(("L3", "Notice the language",
                    "Listen once more and write the missing word.", nf[0], nf[1], "M",
                    "The gapped words are the target language of this lesson."))
    return out
