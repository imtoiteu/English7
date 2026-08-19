"""Extract published transcript + speaker metadata for each source type."""
import sys, re, json
sys.path.insert(0,'.')
import verify as V

NAV = {"Script","Grammar","Quiz","Puzzle","Vocab","Vocabulary","Audio Lessons","Video Lessons",
       "Levels","Search","Lesson Activities","|","Free PDF Worksheet","Comments","Answers",
       "Your browser does not support the audio tag.","Keep Listening"}
STOP = ("Answer the following questions","Learn the words","What is the correct word",
        "Listen to the audio to hear","Got another minute","Keep Listening","Watch More",
        "The more you listen","English Listening Lesson Library","Free Lessons for All Levels",
        "Now it is your turn","Free Materials","Listening Quiz","New Words","Write to us",
        "Words in This Story","_______","See comments","Practice")

def _body(lines, start_after=None):
    out=[]; on = start_after is None
    for l in lines:
        if not on:
            if l == start_after: on=True
            continue
        if any(l.startswith(s) for s in STOP): break
        if l in NAV: continue
        out.append(l)
    return out

SPEAKER = re.compile(r"^[A-Z][A-Za-z.'\u2019 ]{0,20}:\s*\S")
def sg(h):
    """Sound Grammar: ONLY the four conversations. Everything after them on the
    page (grammar points, quiz prompts, promo links) is furniture, not script."""
    lines = V.clean_transcript(h)
    out=[]; on=False
    for l in lines:
        if re.match(r'^Conversation \d', l):
            on=True; out.append(re.split(r'\|', l)[0].strip()); continue
        if not on: continue
        if re.match(r'^Point \d+:', l): break
        if SPEAKER.match(l): out.append(l)
    return out

def ome(h):
    lines = V.clean_transcript(h)
    # transcript = block after the nav row (Script/Quiz/Vocab/Grammar), before the quiz prompt
    idx=None
    for i,l in enumerate(lines):
        if l=="Script":
            j=i
            while j<len(lines) and lines[j] in NAV: j+=1
            idx=j; break
    if idx is None: return []
    return _body(lines[idx:])

def voa(h):
    lines = V.clean_transcript(h)
    spk = re.compile(r"^[A-Z][A-Za-z.'\u2019 ]{1,20}:\s*\S")
    # dialogue begins after the last media-player block
    anchors = [i for i,l in enumerate(lines) if l in ("Pop-out player","Direct link")]
    start = (max(anchors)+1) if anchors else 0
    out=[]
    for l in lines[start:]:
        if any(l.startswith(s) for s in STOP): break
        if l in NAV: continue
        if not out and not spk.match(l): continue
        out.append(l)
    return out

def speaker_meta(h):
    for l in V.clean_transcript(h)[:20]:
        if re.match(r'^[A-Z][a-z]+\s*/\s*[A-Z]', l) and len(l) < 46: return l
    return ""

if __name__=="__main__":
    import mapping as M
    out={}
    for k,d in M.M.items():
        if d['kind']=='RECYCLE': continue
        st,b=V.get(d['url']); h=b.decode('utf-8','replace')
        tx = {"SG":sg,"1ME":ome,"VOA":voa}[d['kind']](h)
        out[k]=dict(kind=d['kind'], title=d['title'], page=d['url'],
                    speaker=speaker_meta(h), transcript=tx,
                    words=len(' '.join(tx).split()))
        print(f"{k:8}{d['kind']:5}{len(tx):4}L {out[k]['words']:5}w {out[k]['speaker'][:22]:24}{' '.join(tx)[:52]}")
    json.dump(out, open('transcripts.json','w'), indent=1)
