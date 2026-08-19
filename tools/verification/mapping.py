# Candidate 92-session audio mapping. Every entry is verified by verify_run.py.
# src: VOA | SG (ELLLO Sound Grammar) | 1ME (ELLLO One Minute English) | RECYCLE
VOA = "https://learningenglish.voanews.com/a/"
V = {  # lesson number -> page url
 6:"lets-learn-english-lesson-6-where-is-the-gym/3225958.html",
 17:"are-you-free-on-friday-lets-learn-english/3355785.html",
 20:"lets-learn-english-lesson-20-what-can-you-do/3384429.html",
 28:"lets-learn-english-lesson-28-i-passed-it/3487865.html",
 29:"lets-learn-english-lesson-29-a-long-time-ago/3509519.html",
 39:"lets-learn-english-lesson-39-its-unbelieveable/3598920.html",
 40:"lets-learn-english-lesson-40-the-woods-are-alive/3630341.html",
 7:"lets-learn-english-lesson-7-what-are-you-doing/3240468.html",
 11:"lets-learn-english-lesson-11-this-is-my-neighborhood/3293986.html",
 12:"lets-learn-english-lesson-12-meet-my-family/3301733.html",
 13:"lets-learn-english-lesson-13-happy-birthday-william-shakespeare/3312239.html",
 14:"lets-learn-english-lesson-14-how-about-this/3323771.html",
 15:"lets-learn-english-lesson-15-i-love-people-watching/3343720.html",
 16:"lets-learn-english-lesson-16-where-are-you-from/3355849.html",
 18:"lets-learn-english-lesson-18-she-always-does-that/3357748.html",
 19:"lets-learn-english-lesson-19-when-do-you-start/3357760.html",
 21:"lets-learn-english-lesson-21-can-you-come-to-the-party/3406732.html",
 22:"lets-learn-english-lesson-22/3397314.html",
 23:"lets-learn-english-lesson-23-what-do-you-want/3413753.html",
 24:"lets-learn-english-lesson-24-yesterday-was-amazing/3439164.html",
 25:"lets-learn-english-lesson-25-watch-out/3431138.html",
 26:"lets-learn-english-lesson-26-this-game-is-fun/3457248.html",
 30:"lets-learn-english-lesson-30-rolling-river/3522798.html",
 31:"lets-learn-english-lesson-31-take-me-out-to-the-ball-game/3535235.html",
 34:"lets-learn-english-lesson-34-what-will-i-do/3566043.html",
 35:"lets-learn-english-lesson-35-lets-make-dinner/3571922.html",
 36:"lets-learn-english-lesson-36-i-can-fix-this/3568962.html",
 37:"lets-learn-english-lesson-37-lets-agree-to-disagree/3574029.html",
 41:"lets-learn-english-lesson-41-teamwork/3635015.html",
 43:"lets-learn-english-lesson-43-time-for-plan-b/3666458.html",
 44:"lets-learn-english-lesson-44-making-healthy-choices/3688552.html",
 45:"lesson-45-this-land-is-your-land/3710209.html",
 46:"lets-learn-english-lesson-46-may-i-borrow-that/3723588.html",
 47:"lets-learn-english-lesson-47-how-can-i-help/3737352.html",
 48:"lets-learn-english-lesson-48-have-you-ever/3753664.html",
 49:"lets-learn-english-lesson-49-operation-spy/3763537.html",
 50:"lets-learn-english-lesson-50-back-to-school/3771173.html",
 51:"lets-learn-english-lesson-51-a-good-habit/3773577.html",
 52:"lets-learn-english-lesson-52-taking-chances/3805454.html",
}
VOA_TITLE = {
 6:"Where Is the Gym?",17:"Are You Free on Friday?",20:"What Can You Do?",
 28:"I Passed It!",29:"A Long Time Ago",39:"It's Unbelievable!",40:"The Woods Are Alive",7:"What Are You Doing?",11:"This Is My Neighborhood",12:"Meet My Family",
 13:"Happy Birthday, William Shakespeare!",14:"How About This?",15:"I Love People-Watching!",
 16:"Where Are You From?",18:"She Always Does That",19:"When Do I Start?",
 21:"Can You Come to the Party?",22:"Next Summer...",23:"What Do You Want?",
 24:"Yesterday Was Amazing!",25:"Watch Out!",26:"This Game Is Fun!",30:"Rolling on the River",
 31:"Take Me Out to the Ball Game",34:"What Will I Do?",35:"Let's Make Dinner!",
 36:"I Can Fix This!",37:"Let's Agree to Disagree",41:"Teamwork Works Best With a Team",
 43:"Time for Plan B",44:"Making Healthy Choices",45:"This Land is Your Land",
 46:"May I Borrow That?",47:"How Can I Help?",48:"Have You Ever ...?",49:"Operation Spy!",
 50:"Back to School",51:"A Good Habit",52:"Taking Chances",
}
def voa(n): return VOA + V[n]
def sg(level, slug): return f"https://elllo.org/book/{level}/{slug}.html"
def ome(level, slug):
    ext = "html" if slug.endswith("@html") else "htm"
    slug = slug.replace("@html","")
    return f"https://elllo.org/video/{level}BEG/{slug}.{ext}"

# session key -> (label, source_kind, page_url, title)
M = {}
def add(k, kind, url, title, note=""):
    M[k] = dict(kind=kind, url=url, title=title, note=note)

# ---- Units: L1/L4 = VOA, L2/L3 = Sound Grammar, L5/L6 = One Minute English ----
UNITS = {
 1: dict(l1=15, l4=18, l2=("A1","A1-20-Adverbs-Frequency"), l3=("A2","A2-01-Present-Simple"),
         l5=("VOA",17), l6=("A2","A2-008-NERRY-WHAT-DO-WEEKEND")),
 2: dict(l1=44, l4=51, l2=("A2","A2-23-Much-Many"), l3=("A2","A2-17-Imperatives"),
         l5=("A2","A2-035-HAZAL-WHAT-SNACKS-ARE-HEALTHY"), l6=("A2","A2-017-NERRY-WHAT-FOOD-NOT-HEALTHY")),
 3: dict(l1=47, l4=41, l2=("A2","A2-06-Past-Tense-Ed"), l3=("A2","A2-07-Past-Tense-Irregular"),
         l5=("VOA",29), l6=("VOA",28)),
 4: dict(l1=45, l4=21, l2=("A2","A2-10-Superlatives"), l3=("A2","A2-09-Comparatives"),
         l5=("VOA",40), l6=("SG:A2","A2-19-Expressing-Similarity")),
 5: dict(l1=35, l4=23, l2=("A2","A2-22-Determiner-Nouns"), l3=("A1","A1-25-Any-Some"),
         l5=("A2","A2-022-HAZAL-WHAT-EAT-BREAKFAST"), l6=("A2","A2-045-ROCiO-WHAT-FRUITS-DO-YOU-LIKE")),
 6: dict(l1=50, l4=19, l2=("A2","A2-14-Present-Continuous-Future"), l3=("A2","A2-03-Present-Continuous"),
         l5=("A2","A2-050-NERRY-WHAT-IS-ON-YOUR-SCHEDULE-TODAY"), l6=("A2","A2-036-NERISSA-WHEN-START-AND-FINISH-DAY")),
 7: dict(l1=6, l4=25, l2=("A1","A1-16-Prepositions"), l3=("B1","B1-08-Have-to-Must-Obligation."),
         l5=("A2","A2-015-LESYA-USE-TRAIN-OR-BUS"), l6=("A1","A1-019-NERRY-LIVE-NEAR-TRAIN-STATION")),
 8: dict(l1=26, l4=37, l2=("A2","A2-08-Adjectives"), l3=("A2","A2-13-Connectors"),
         l5=("VOA",39), l6=("VOA",49)),
 9: dict(l1=13, l4=31, l2=("A1","A1-13-Months"), l3=("A1","A1-24-Articles"),
         l5=("A2","A2-043-ELISE-MONTHS"), l6=("A1","A1-024-ELISABETH-WHO-VISITS-HOLIDAYS@html")),
 10:dict(l1=34, l4=36, l2=("A2","A2-05-Going-To"), l3=("A2","A2-04-Will"),
         l5=("A2","A2-025-NATALIE-WILL-WONT"), l6=("SG:B1","B1-10-First-Conditional")),
 11:dict(l1=22, l4=43, l2=("A1","A1-19-Can-Abilities"), l3=("A2","A2-12-May-Might"),
         l5=("A2","A2-047-ELISABETH-WHO-SEE-TONIGHT"), l6=("VOA",20)),
 12:dict(l1=48, l4=16, l2=("A1","A1-18-Nationalities"), l3=("B1","B1-07-Present-Perfect-Experience"),
         l5=("A2","A2-033-ELISE-NETHERLANDS"), l6=("A2","A2-044-NERISSA-WHERE-FAMILY-LIVE")),
}
SG_SLUGS = {"B1-10-First-Conditional","A1-20-Adverbs-Frequency","A2-01-Present-Simple","A2-23-Much-Many","A2-17-Imperatives",
 "A2-06-Past-Tense-Ed","A2-07-Past-Tense-Irregular","A2-10-Superlatives","A2-09-Comparatives",
 "A2-22-Determiner-Nouns","A1-25-Any-Some","A2-14-Present-Continuous-Future","A2-03-Present-Continuous",
 "A1-16-Prepositions","B1-08-Have-to-Must-Obligation.","A2-08-Adjectives","A2-13-Connectors",
 "A1-13-Months","A1-24-Articles","A2-05-Going-To","A2-04-Will","A1-19-Can-Abilities","A2-12-May-Might",
 "A1-18-Nationalities","B1-07-Present-Perfect-Experience","A2-19-Expressing-Similarity"}

for u,d in UNITS.items():
    add(f"U{u}L1","VOA",voa(d['l1']),f"VOA L{d['l1']}: {VOA_TITLE[d['l1']]}")
    for slot in ("l2","l3"):
        lvl,slug = d[slot]
        add(f"U{u}L{slot[1]}","SG",sg(lvl,slug),slug)
    add(f"U{u}L4","VOA",voa(d['l4']),f"VOA L{d['l4']}: {VOA_TITLE[d['l4']]}")
    for slot in ("l5","l6"):
        v = d[slot]
        if v[0]=="VOA":
            add(f"U{u}L{slot[1]}","VOA",voa(v[1]),f"VOA L{v[1]}: {VOA_TITLE[v[1]]}")
        elif v[0].startswith("SG:"):
            add(f"U{u}L{slot[1]}","SG",sg(v[0][3:],v[1]),v[1])
        else:
            add(f"U{u}L{slot[1]}","1ME",ome(v[0],v[1]),v[1])
    add(f"U{u}L7","RECYCLE","","Recycled from this unit")

REVIEWS = {"REV1L1":12,"REV1L2":24,"REV2L1":14,"REV2L2":7,
           "REV3L1":11,"REV3L2":30,"REV4L1":52,"REV4L2":46}
for k,n in REVIEWS.items():
    add(k,"VOA",voa(n),f"VOA L{n}: {VOA_TITLE[n]}")
