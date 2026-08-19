"""Build final.json by reusing verified ASR (matched on page URL) and
re-probing the VOA 128 kbps masters. ASR only where nothing exists yet."""
import sys, json, re, os
sys.path.insert(0,'.')
import verify as V, mapping as M, extract_tx as X
from concurrent.futures import ThreadPoolExecutor

prior = {}
for f in ('phase2.json','cand.json','cand2.json'):
    if not os.path.exists(f): continue
    for r in json.load(open(f)):
        if r.get('status')=='OK' and r.get('page'):
            prior[r['page']] = r

def audio_urls(kind,url,h):
    med=[m for m in V.extract_media(url,h) if 'audiovocab' not in m and '/ANA/' not in m]
    if kind=="VOA":
        hq=[m for m in med if m.endswith('_hq.mp3')]
        pl=[m for m in med if m.endswith('.mp3') and not m.endswith('_hq.mp3')]
        return (hq or pl or med)[:1]
    if kind=="SG":
        main=[m for m in med if 'Audio4x' not in m]
        return main[:1] if main else [m for m in med if 'Audio4x' in m][:4]
    return med[:1]

NEED=[]
def stage1(it):
    k,d=it
    r=dict(key=k,kind=d['kind'],title=d['title'],page=d['url'])
    if d['kind']=='RECYCLE': r['status']='RECYCLE'; return r
    st,b=V.get(d['url']); h=b.decode('utf-8','replace')
    r['page_status']=st
    tx={"SG":X.sg,"1ME":X.ome,"VOA":X.voa}[d['kind']](h)
    r['transcript']=tx; r['speaker']=X.speaker_meta(h)
    urls=audio_urls(d['kind'],d['url'],h)
    parts=[]
    for i,au in enumerate(urls,1):
        fn=re.sub(r'[^A-Za-z0-9._-]','_',f"F{k}_{i}_"+os.path.basename(au))[:120]
        p=V.fetch_audio(au,fn); pr=V.probe(p); lv=V.levels(p)
        parts.append(dict(url=au,dur=pr['duration'],kbps=pr['bitrate_kbps'],sr=pr['sample_rate'],
                          ch=pr['channels'],mean_db=lv.get('mean_db'),max_db=lv.get('max_db'),file=fn))
    r['parts']=parts; r['duration']=round(sum(p['dur'] for p in parts),1)
    p0=prior.get(d['url'])
    if p0 and p0.get('wpm'):
        r.update(wpm=p0['wpm'], wpm_gross=p0['wpm_gross'], coverage=p0['coverage'], asr='reused')
        r['status']='OK'
    else:
        r['status']='NEEDS_ASR'; NEED.append(k)
    return r

with ThreadPoolExecutor(max_workers=6) as ex:
    res=list(ex.map(stage1, M.M.items()))
print("reused:",sum(1 for r in res if r.get('asr')=='reused'),
      " need ASR:",sum(1 for r in res if r['status']=='NEEDS_ASR'),
      " recycle:",sum(1 for r in res if r['status']=='RECYCLE'))
print("to ASR:",[r['key'] for r in res if r['status']=='NEEDS_ASR'])
json.dump(res,open('final_stage1.json','w'),indent=1)
