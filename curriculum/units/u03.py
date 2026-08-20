# -*- coding: utf-8 -*-
"""UNIT 3 – COMMUNITY SERVICE  (Periods 15–21)"""
from curriculum.schema import *
from curriculum.audio_sources import AUDIO

UNIT = Unit(
    number=3, title="Community Service",
    theme="Volunteering, helping other people, doing something good for your area",
    can_do=[
        "name ten community activities (clean up the beach, plant trees, donate books…)",
        "talk about what I did last week / last year using the past simple",
        "pronounce the -ed ending correctly as /t/, /d/ or /ɪd/",
        "read a short article about a volunteer group and answer detail questions",
        "listen to an interview about a clean-up day and complete notes",
        "write a diary entry or a short report about a past activity (70–90 words)",
    ],
    grammar_focus=["Past simple: regular and irregular verbs (+ / – / ?)",
                   "Past time expressions (yesterday, last week, two days ago)"],
    pron_focus="The -ed ending: /t/, /d/ and /ɪd/",
    vocab_focus="Community and volunteering verbs and collocations (raise money, take part in)",
    project={
        "name": "Our Community Service Plan",
        "goal": "Groups plan one real activity for the class and present the plan to the school.",
        "steps": [
            "Choose a problem in your area (litter, lonely old people, children with no books…).",
            "Decide WHAT you will do, WHERE, WHEN and WHO will do each job.",
            "Write the plan on a poster: 5 sentences with will / going to and 3 past examples "
            "of similar work.",
            "Prepare a 2-minute presentation. Everyone speaks.",
            "Vote for one plan and — if possible — really do it!",
        ],
        "marking": "Content 3 – Language 3 – Poster 2 – Presentation 2 (total 10)",
    },
)

L1 = Lesson(
    code="U3L1", unit=3, number=1, period=17,
    lesson_type="Getting Started", title="What can we do for our community?",
    objectives=["name eight community-service activities",
                "understand a short conversation about volunteering",
                "say which activities they have done or would like to do",
                "write three sentences about helping other people"],
    recycled=["Unit 1: present simple, verbs of liking + V-ing; Unit 2: should / shouldn't, imperatives"],
    vocab=[
        V("community", "n", "/kəˈmjuːnəti/", "cộng đồng", "Our community needs a cleaner park."),
        V("volunteer", "n/v", "/ˌvɒlənˈtɪə/", "tình nguyện viên; tình nguyện", "She works as a volunteer at weekends."),
        V("clean up", "v phr", "/kliːn ʌp/", "dọn dẹp", "We cleaned up the beach on Sunday."),
        V("plant trees", "v phr", "/plɑːnt triːz/", "trồng cây", "The students planted 50 trees."),
        V("donate", "v", "/dəʊˈneɪt/", "quyên góp, tặng", "They donated 200 books to the school."),
        V("elderly people", "n", "/ˈeldəli ˈpiːpl/", "người cao tuổi", "We visit elderly people every month."),
        V("orphanage", "n", "/ˈɔːfənɪdʒ/", "trại trẻ mồ côi", "Our club helps a small orphanage."),
        V("litter", "n", "/ˈlɪtə/", "rác", "There is a lot of litter near the lake."),
    ],
    phrases=["take part in an activity", "help out at…", "raise money for…", "do something useful",
             "make a difference"],
    grammar=G("Past simple – first look (recycled and extended)",
              use=["We use the past simple for finished actions in the past.",
                   "Regular verbs add -ed: clean → cleaned, plant → planted.",
                   "Many common verbs are irregular: go → went, do → did, give → gave."],
              form=[["", "Example"],
                    ["Regular", "We cleaned the park last Sunday."],
                    ["Irregular", "We went to the orphanage yesterday."],
                    ["Time words", "yesterday, last week, last month, two days ago, in 2024"]],
              examples=["Our class planted twenty trees last April.",
                        "I helped my neighbour yesterday.",
                        "They gave old books to the library."],
              pitfall="Vietnamese has no verb ending for the past — the time word does the job "
                      "(hôm qua tôi đi). So students say *Yesterday I go*. In English BOTH the time word "
                      "AND the verb change.",
              note="Today only introduce the positive form. The full paradigm comes in Lesson 3."),
    pron=P("The -ed ending (introduction)",
           "-ed has three sounds: /t/ after a quiet sound (helped), /d/ after a voiced sound (cleaned), "
           "/ɪd/ after t or d (planted, needed).",
           items=["/t/: helped, washed, worked", "/d/: cleaned, played, opened",
                  "/ɪd/: planted, painted, needed, visited"],
           drill=["We cleaned the park and planted trees.", "They helped, washed and painted."],
           vn_note="Learners drop -ed completely. Insist on hearing it in every past sentence "
                   "from today until the end of the year."),
    listening=AUDIO['U3L1'],
    reading=T("Small actions, big difference",
              ["You do not need to be rich or old to help your community. Here are three real examples "
               "from students in Viet Nam.",
               "In Hoi An, a group of 25 students cleans the river bank every second Sunday. Last year "
               "they collected more than 400 bags of litter.",
               "In Thai Nguyen, class 7C visits a home for elderly people once a month. The students "
               "sing, read the newspaper aloud and listen to the old people's stories. 'They wait for us "
               "all month,' says Hoa, 13.",
               "In Can Tho, three friends started a small library in their street. They asked their "
               "neighbours for old books, painted a shelf, and now forty children borrow books every week."],
              tasks=[
                  EX("U3.1-R1", "Read and match", "Which town? Write Hoi An, Thai Nguyen or Can Tho.",
                     items=["1. Students collect litter. ______", "2. Students started a library. ______",
                            "3. Students visit old people. ______", "4. Students painted something. ______",
                            "5. Students listen to stories. ______"],
                     answers=["1. Hoi An", "2. Can Tho", "3. Thai Nguyen", "4. Can Tho", "5. Thai Nguyen"],
                     level="E", kind="reading"),
                  EX("U3.1-R2", "Find the numbers", "Complete with a number.",
                     items=["1. ______ students clean the river bank.", "2. They collected ______ bags of litter.",
                            "3. Class 7C visits ______ a month.", "4. ______ children borrow books every week."],
                     answers=["1. 25", "2. more than 400", "3. once", "4. forty"],
                     level="M", kind="reading")]),
    speaking=[EX("U3.1-S1", "Have you ever done it?", "Ask your partner about five activities.",
                 items=["A: Did you clean up your street last year?  B: Yes, I did. / No, I didn't.",
                        "(clean up / plant trees / donate books / visit elderly people / help a neighbour)"],
                 answers=["Then report: 'Nam donated books last year.'"], level="M", kind="speaking")],
    writing=[EX("U3.1-W1", "Sentence writing", "Write three sentences about helping people.",
                items=["1. Last year my class ______ .", "2. I would like to ______ .",
                       "3. In my street, students should ______ ."],
                answers=["Model: Last year my class cleaned up the school garden. I would like to visit "
                         "an orphanage. In my street, students should collect the litter near the market."],
                level="M", kind="writing", lines=4)],
    communication={"function": "Making and responding to suggestions",
                   "phrases": ["I think we should…", "Why don't we…?", "We could…", "That's a good idea.",
                               "I'm not sure. What about…?", "Let's vote."],
                   "roleplay": "Class meeting: in groups of four, suggest three activities for Volunteer "
                               "Day, discuss them and vote for one.",
                   "real_life": "Taking part in a class or club meeting and helping a group decide."},
    guided=[EX("U3.1-G1", "Match the verb and the noun", "Write the correct phrase.",
               items=["1. clean up", "2. plant", "3. donate", "4. visit", "5. collect",
                      "a. trees", "b. books and clothes", "c. the beach", "d. litter",
                      "e. elderly people"],
               answers=["1–c", "2–a", "3–b", "4–e", "5–d"], level="E", kind="vocab"),
            EX("U3.1-G2", "Past or present?", "Write PAST or PRESENT.",
               items=["1. We clean the park every Sunday. ___", "2. We cleaned the park last Sunday. ___",
                      "3. They donate books every year. ___", "4. They donated 200 books in 2024. ___",
                      "5. I help my neighbour on Saturdays. ___"],
               answers=["1. PRESENT", "2. PAST", "3. PRESENT", "4. PAST", "5. PRESENT"],
               level="E", kind="grammar")],
    independent=[EX("U3.1-I1", "Complete with the past simple", "Use the verbs in the box.",
                    wordbank=["cleaned", "planted", "donated", "visited", "helped"],
                    items=["1. Last April our school ______ 50 trees.",
                           "2. We ______ the beach two weeks ago.",
                           "3. My class ______ an orphanage last month.",
                           "4. They ______ 100 books to the library.",
                           "5. I ______ my grandmother yesterday."],
                    answers=["1. planted", "2. cleaned", "3. visited", "4. donated", "5. helped"],
                    level="M", kind="grammar"),
                 EX("U3.1-I2", "Group meeting", "Do the class-meeting role play and vote.",
                    items=[], answers=["See communication section."], level="D", kind="speaking")],
    review=["8 community words", "past simple – positive form", "-ed has three sounds"],
    homework=[
        EX("U3.1-H1", "Vocabulary", "Complete with community, volunteer, litter, orphanage, elderly.",
           items=["1. There is too much ______ in the park.", "2. She is a ______ at the hospital.",
                  "3. We visit ______ people every month.", "4. Our ______ needs a new library.",
                  "5. The ______ has 30 children."],
           answers=["1. litter", "2. volunteer", "3. elderly", "4. community", "5. orphanage"],
           level="E", kind="vocab"),
        EX("U3.1-H2", "Grammar", "Write the past simple form.",
           items=["1. clean → ", "2. plant → ", "3. help → ", "4. visit → ", "5. donate → ",
                  "6. paint → ", "7. collect → ", "8. work → "],
           answers=["1. cleaned", "2. planted", "3. helped", "4. visited", "5. donated", "6. painted",
                    "7. collected", "8. worked"], level="E", kind="grammar"),
        EX("U3.1-H3", "Writing", "Write 4 sentences about something good your class or family did last year.",
           items=["Use past simple and a past time expression in each sentence."],
           answers=["Model: Last summer my family cleaned the road in front of our house. In September "
                    "my class collected old books for a village school. We donated forty books. "
                    "Last month I helped my grandmother in her garden."],
           level="M", kind="writing", lines=5),
        EX("U3.1-H4", "Speaking", "Say these six verbs aloud with a clear -ed: cleaned, planted, helped, "
           "visited, donated, worked.", items=[], answers=["Spot-check in Lesson 2."],
           level="E", kind="pron")],
    workbook=[
        EX("U3.1-P1", "Word building", "Write the missing letters.",
           items=["1. v _ l u n t e e r", "2. c _ m m u n i t y", "3. d _ n a t e", "4. l _ t t e r",
                  "5. _ r p h a n a g e"],
           answers=["1. volunteer", "2. community", "3. donate", "4. litter", "5. orphanage"],
           level="E", kind="vocab"),
        EX("U3.1-P2", "Choose the correct verb", "Circle the correct word.",
           items=["1. (clean / wash) up the beach", "2. (plant / put) trees", "3. (give / donate) books",
                  "4. (take / make) part in an activity", "5. (raise / lift) money for charity"],
           answers=["1. clean", "2. plant", "3. donate", "4. take", "5. raise"], level="E", kind="vocab"),
        EX("U3.1-P3", "Past simple", "Complete with the past simple of the verb in brackets.",
           items=["1. We (clean) ______ the classroom yesterday.",
                  "2. They (plant) ______ trees last April.",
                  "3. She (help) ______ her neighbour last week.",
                  "4. Our class (visit) ______ an orphanage in May.",
                  "5. I (collect) ______ old clothes two days ago."],
           answers=["1. cleaned", "2. planted", "3. helped", "4. visited", "5. collected"],
           level="M", kind="grammar"),
        EX("U3.1-P4", "Correct the mistakes", "One mistake in each sentence.",
           items=["1. Yesterday we clean the park.", "2. Last year my class visit an orphanage.",
                  "3. They donate 100 books last month.", "4. She helps her neighbour two days ago.",
                  "5. We planted trees every year."],
           answers=["1. Yesterday we cleaned the park.", "2. Last year my class visited an orphanage.",
                    "3. They donated 100 books last month.", "4. She helped her neighbour two days ago.",
                    "5. We plant trees every year."],
           level="D", kind="grammar",
           note="No. 5 has a PRESENT time expression, so the verb must be present. Time word and verb "
                "must agree."),
        EX("U3.1-P5", "Writing", "Write 5 sentences about a community activity you would like to do.",
           items=["Use: I would like to… / We could… / It is a good idea because…"],
           answers=["Model: I would like to start a small library in my street. We could ask our "
                    "neighbours for old books. We could paint an old shelf and put it near the tea shop. "
                    "It is a good idea because many children in my street have no books at home. "
                    "I think ten friends would help me."],
           level="D", kind="writing", lines=6)],
    procedure=[
        ST("Warm-up: Good deed brainstorm", 5,
           ["Write HELP OTHER PEOPLE on the board. Students give one idea each in English or Vietnamese; "
            "you write the English."],
           "Give ideas; read the English words.", "Whole class", "Slide 2"),
        ST("Presentation: 8 community words", 10,
           ["Show pictures; elicit, model, drill. Build the verb + noun chunks on the board.",
            "Concept check: 'Is litter good or bad?' 'Where do elderly people live?'"],
           "Repeat and copy the chunks.", "Whole class", "Slides 3–6"),
        ST("Listening: the class meeting", 9,
           ['Play the recording “Lesson 47: How Can I help?” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; then read the script in role.',
            "Highlight three past verbs in the script: cleaned, was, said."],
           "Listen, answer, notice the past verbs.", "Individual → pairs", "Slide 7"),
        ST("Grammar: first look at the past", 8,
           ["Two columns: TODAY / LAST WEEK. Move sentences from one to the other, changing the verb.",
            "Introduce the -ed ending and the three sounds briefly."],
           "Transform present sentences into past ones.", "Whole class", "Slides 8–9"),
        ST("Speaking: Did you…?", 8,
           ["Model 'Did you clean up your street last year?' Drill the short answers.",
            "Pairs ask about five activities; then report one answer."],
           "Ask, answer, report.", "Pairs", "Slide 10"),
        ST("Wrap-up and homework", 5, ["Class vote: which activity would our class like to do?",
                                       "Set H1–H4."],
           "Vote; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[
        TK("Introducing the past simple with a time line",
           ["I draw a line on the board. Here is TODAY. Everything on the left is finished — the past.",
            "Now listen. Every Sunday we clean the park. That is a habit — present.",
            "But LAST Sunday we cleanED the park. Finished. Past. Can you hear the small /d/ at the end?",
            "In Vietnamese, 'hôm qua' is enough and the verb sleeps. In English the verb must WAKE UP "
            "and change too."]),
        TK("Making community service personal",
           ["Put up your hand if you have ever helped a neighbour. … Good, many hands.",
            "You do not need money or a car to help. You need one hour and two hands.",
            "Today we learn the English for what you already do."])],
    support=["Give picture cards with the phrase written under each.",
             "Provide a list of regular verbs with the -ed form already written.",
             "Allow Yes/No answers before full sentences."],
    challenge=["Ask for a reason and a detail: 'We cleaned the beach because tourists left a lot of litter.'",
               "Ask them to find three more community activities in English.",
               "Ask them to chair the group meeting."],
    assessment=["Names 6 of 8 community activities", "Uses -ed in 4 of 5 past sentences",
                "Asks and answers a 'Did you…?' question"],
    board_plan=["LEFT: 8 words + verb chunks", "CENTRE: time line PAST | TODAY; clean → cleaned",
                "RIGHT: suggestion phrases; Homework H1–H4"],
    materials=["Community activity pictures", 'Recording: Lesson 47: How Can I help? — VOA Learning English — Let’s Learn English, Level 1 (3:12)'],
)

L2 = Lesson(
    code="U3L2", unit=3, number=2, period=18,
    lesson_type="A Closer Look 1", title="Volunteering words and the -ed ending",
    objectives=["use eight more volunteering words and collocations",
                "pronounce -ed correctly as /t/, /d/ or /ɪd/ and explain the rule",
                "talk about a past activity using three past verbs",
                "sort verbs into the three -ed sound groups"],
    recycled=["U3L1 community vocabulary and past simple; Unit 2 should/shouldn't; Unit 1 frequency"],
    vocab=[
        V("charity", "n", "/ˈtʃærəti/", "tổ chức từ thiện", "The money goes to a children's charity."),
        V("raise money", "v phr", "/reɪz ˈmʌni/", "gây quỹ", "We raised money by selling cakes."),
        V("homeless", "adj", "/ˈhəʊmləs/", "vô gia cư", "The centre helps homeless people."),
        V("support", "v/n", "/səˈpɔːt/", "hỗ trợ", "Many parents supported our project."),
        V("take care of", "v phr", "/teɪk keə əv/", "chăm sóc", "We take care of the school garden."),
        V("recycle", "v", "/ˌriːˈsaɪkl/", "tái chế", "We recycle paper and plastic bottles."),
        V("environment", "n", "/ɪnˈvaɪrənmənt/", "môi trường", "Planting trees helps the environment."),
        V("kindness", "n", "/ˈkaɪndnəs/", "lòng tốt", "A small act of kindness costs nothing."),
    ],
    phrases=["take care of…", "raise money for…", "give a hand", "act of kindness",
             "make our town cleaner"],
    grammar=G("Regular past simple: spelling rules",
              use=["Most verbs: + ed (help → helped).",
                   "Verbs ending in -e: + d (donate → donated).",
                   "Consonant + y: y → ied (carry → carried, study → studied).",
                   "One short vowel + one consonant: double the consonant (stop → stopped, plan → planned)."],
              form=[["Rule", "Example"],
                    ["+ ed", "clean → cleaned, work → worked"],
                    ["+ d (ends in e)", "donate → donated, recycle → recycled"],
                    ["y → ied", "carry → carried, tidy → tidied"],
                    ["double consonant", "stop → stopped, plan → planned"]],
              examples=["We planned the day carefully and we tidied the whole yard.",
                        "They recycled 200 bottles and carried them to the centre."],
              pitfall="*planed*, *studyed*, *stoped* – the spelling rules are learned by writing, "
                      "not by reading. Give a short spelling test every week.",
              note="Play → played (vowel + y = no change). Only CONSONANT + y becomes -ied."),
    pron=P("The -ed ending: /t/, /d/ and /ɪd/",
           "Put your finger on your throat. If the sound before -ed has NO buzz (p, k, f, s, sh, ch), "
           "say /t/. If it BUZZES (b, g, v, z, m, n, l, r, vowels), say /d/. If the verb already ends "
           "in t or d, you must add a new syllable: /ɪd/.",
           items=["/t/: helped, worked, washed, watched, stopped",
                  "/d/: cleaned, played, opened, recycled, carried",
                  "/ɪd/: planted, painted, visited, donated, needed, wanted"],
           drill=["We worked, cleaned and painted.",
                  "They helped, planted and recycled.",
                  "She visited, donated and carried the books."],
           vn_note="/ɪd/ adds a whole syllable — 'visited' has THREE syllables. Vietnamese learners "
                   "usually say two. Count the syllables on your fingers."),
    listening=AUDIO['U3L2'],
    reading=T("The Green Sunday Club",
              ["The Green Sunday Club started in 2022 with only six students from a school in Da Nang. "
               "Today it has more than ninety members.",
               "Every Sunday morning the members walk along one street and collect plastic bottles, cans "
               "and paper. They wash the bottles, take them to a recycling centre and use the money for "
               "small projects. Last year they bought school bags for twelve children and planted "
               "thirty trees near the market.",
               "'People laughed at us in the first month,' says Duc, the club leader. 'Now the same "
               "people wait for us with their bottles ready. That is the real change.'"],
              tasks=[
                  EX("U3.2-R1", "Read and answer", "Answer the questions.",
                     items=["1. When and where did the club start?", "2. How many members are there now?",
                            "3. What do they do with the bottles?",
                            "4. Name two things they did last year.",
                            "5. How did people react in the first month?"],
                     answers=["1. In 2022, in Da Nang.", "2. More than ninety.",
                              "3. They wash them and take them to a recycling centre.",
                              "4. They bought school bags for twelve children; they planted thirty trees.",
                              "5. They laughed at the club."],
                     level="M", kind="reading")]),
    speaking=[
        EX("U3.2-S1", "Sound sort race", "Say the verb and put it in the right group: /t/, /d/ or /ɪd/.",
           items=["helped, cleaned, visited, worked, played, painted, washed, donated, opened, wanted"],
           answers=["/t/: helped, worked, washed  |  /d/: cleaned, played, opened  |  "
                    "/ɪd/: visited, painted, donated, wanted"], level="M", kind="pron"),
        EX("U3.2-S2", "Tell me what you did", "Tell your partner three things you did last weekend. "
           "At least two verbs must have -ed.",
           items=["A: Last Saturday I helped my mother and I cleaned my room. What about you?"],
           answers=["Monitor for the -ed sound, not only the -ed spelling."],
           level="D", kind="speaking")],
    writing=[EX("U3.2-W1", "Spelling practice", "Write the past simple.",
                items=["1. stop → ", "2. carry → ", "3. recycle → ", "4. plan → ", "5. study → ",
                       "6. play → ", "7. tidy → ", "8. support → "],
                answers=["1. stopped", "2. carried", "3. recycled", "4. planned", "5. studied",
                         "6. played", "7. tidied", "8. supported"], level="E", kind="writing")],
    communication={"function": "Thanking and appreciating people",
                   "phrases": ["Thank you for your help.", "Thanks a lot!", "That's very kind of you.",
                               "You're welcome.", "No problem.", "We couldn't do it without you."],
                   "roleplay": "A helped B carry books to the library. B thanks A in three different "
                               "ways; A responds each time.",
                   "real_life": "Thanking people properly — neighbours, teachers, volunteers."},
    guided=[
        EX("U3.2-G1", "Match", "Match the word with the meaning.",
           items=["1. charity", "2. homeless", "3. recycle", "4. environment", "5. kindness",
                  "a. the natural world around us", "b. having no home",
                  "c. an organisation that helps people", "d. being good to other people",
                  "e. to use something again"],
           answers=["1–c", "2–b", "3–e", "4–a", "5–d"], level="E", kind="vocab"),
        EX("U3.2-G2", "/t/, /d/ or /ɪd/?", "Write the sound of the -ed ending.",
           items=["1. worked ___", "2. cleaned ___", "3. visited ___", "4. washed ___", "5. donated ___",
                  "6. played ___", "7. stopped ___", "8. needed ___"],
           answers=["1. /t/", "2. /d/", "3. /ɪd/", "4. /t/", "5. /ɪd/", "6. /d/", "7. /t/", "8. /ɪd/"],
           level="M", kind="pron")],
    independent=[
        EX("U3.2-I1", "Complete the story", "Write the past simple of the verbs.",
           text=["Last Sunday our club (1. plan) ______ a special day. We (2. collect) ______ old clothes, "
                 "(3. wash) ______ them and (4. carry) ______ them to a centre for homeless people. "
                 "In the afternoon we (5. paint) ______ the front wall and (6. tidy) ______ the garden. "
                 "Everybody (7. work) ______ hard and nobody (8. stop) ______ before five o'clock."],
           items=["Write the eight verbs."],
           answers=["1. planned", "2. collected", "3. washed", "4. carried", "5. painted", "6. tidied",
                    "7. worked", "8. stopped"], level="D", kind="grammar"),
        EX("U3.2-I2", "Speak from the story", "Retell the story in U3.2-I1 to your partner without "
           "looking, using at least five past verbs.",
           items=[], answers=["Model: Last Sunday the club planned a special day. They collected old "
                              "clothes and washed them…"], level="D", kind="speaking")],
    review=["8 volunteering words", "-ed spelling rules", "-ed sounds /t/, /d/, /ɪd/"],
    homework=[
        EX("U3.2-H1", "Vocabulary", "Complete with charity, raise, homeless, recycle, environment.",
           items=["1. We ______ paper and bottles at school.", "2. The money goes to a ______ .",
                  "3. They want to ______ money for the flood victims.",
                  "4. Planting trees is good for the ______ .", "5. The centre helps ______ people."],
           answers=["1. recycle", "2. charity", "3. raise", "4. environment", "5. homeless"],
           level="E", kind="vocab"),
        EX("U3.2-H2", "Spelling", "Write the past simple form.",
           items=["1. plan → ", "2. study → ", "3. donate → ", "4. carry → ", "5. stop → ",
                  "6. play → ", "7. tidy → ", "8. recycle → "],
           answers=["1. planned", "2. studied", "3. donated", "4. carried", "5. stopped", "6. played",
                    "7. tidied", "8. recycled"], level="M", kind="grammar"),
        EX("U3.2-H3", "Pronunciation", "Put the verbs in the correct group: /t/, /d/, /ɪd/.",
           items=["helped, cleaned, wanted, watched, opened, painted, worked, played"],
           answers=["/t/: helped, watched, worked  |  /d/: cleaned, opened, played  |  "
                    "/ɪd/: wanted, painted"], level="M", kind="pron"),
        EX("U3.2-H4", "Writing", "Write 5 sentences about what your class did last term. "
           "Use five different -ed verbs.",
           items=[], answers=["Model: Last term our class cleaned the school yard. We collected old "
                              "newspapers. We recycled them and raised 300,000 dong. We donated the "
                              "money to a children's hospital. Everybody worked together."],
           level="M", kind="writing", lines=6)],
    workbook=[
        EX("U3.2-P1", "Complete the collocations", "Write the missing word.",
           items=["1. ______ money for charity", "2. take ______ of the garden", "3. ______ paper and plastic",
                  "4. an act of ______ ", "5. help the ______ people"],
           answers=["1. raise", "2. care", "3. recycle", "4. kindness", "5. homeless"],
           level="E", kind="vocab"),
        EX("U3.2-P2", "Spelling", "Write the past form and the rule number (1 = +ed, 2 = +d, "
           "3 = y→ied, 4 = double).",
           items=["1. work → ______ (rule ___)", "2. tidy → ______ (rule ___)",
                  "3. recycle → ______ (rule ___)", "4. stop → ______ (rule ___)",
                  "5. carry → ______ (rule ___)", "6. plan → ______ (rule ___)"],
           answers=["1. worked (1)", "2. tidied (3)", "3. recycled (2)", "4. stopped (4)",
                    "5. carried (3)", "6. planned (4)"], level="M", kind="grammar"),
        EX("U3.2-P3", "-ed sounds", "Circle the verb with a DIFFERENT -ed sound.",
           items=["1. helped / washed / cleaned", "2. visited / played / opened",
                  "3. wanted / painted / worked", "4. carried / donated / recycled"],
           answers=["1. cleaned (/d/, others /t/)", "2. visited (/ɪd/, others /d/)",
                    "3. worked (/t/, others /ɪd/)", "4. donated (/ɪd/, others /d/)"],
           level="D", kind="pron"),
        EX("U3.2-P4", "Write the story", "Write 6 sentences about a volunteer day, using these verbs: "
           "plan, collect, wash, carry, paint, work.",
           items=[], answers=["Model: Last month our class planned a volunteer day. We collected old "
                              "clothes from our neighbours. We washed them at school. Then we carried "
                              "them to a centre for homeless people. In the afternoon we painted the "
                              "old wall. Everybody worked hard and we finished at five o'clock."],
           level="D", kind="writing", lines=8)],
    procedure=[
        ST("Warm-up: Past verb chain", 5,
           ["Student 1: 'Yesterday I cleaned my room.' Student 2: 'Yesterday he cleaned his room and "
            "I helped my mother.' Continue along the row."],
           "Repeat and add a past sentence.", "Rows", "Slide 2"),
        ST("Presentation: 8 new words", 8,
           ["Pictures + elicit + drill. Build collocations: RAISE money, TAKE CARE OF, ACT OF kindness."],
           "Repeat and copy.", "Whole class", "Slides 3–5"),
        ST("Pronunciation: the three -ed sounds", 12,
           ["Three columns on the board: /t/ /d/ /ɪd/. Model one verb for each with the throat test.",
            "Explain the rule: no buzz → /t/; buzz → /d/; already t/d → new syllable /ɪd/.",
            "Sound sort race (U3.2-S1). Then choral drill of the three sentences.",
            "Count syllables on fingers: vi-si-ted = 3."],
           "Sort the verbs, drill, count syllables.", "Whole class → teams", "Slides 6–8"),
        ST("Spelling rules", 7,
           ["Four rules on the board with one example each. Students do U3.2-W1 as a race."],
           "Write the past forms.", "Individual → pairs", "Student Book p. U3L2"),
        ST("Reading + speaking", 8,
           ["Read 'The Green Sunday Club' and answer R1. Then U3.2-S2: three things you did last weekend."],
           "Read, answer, then speak with -ed verbs.", "Individual → pairs", "Slides 9–10"),
        ST("Wrap-up and homework", 5,
           ["Rapid-fire: teacher says a verb, class says the past form AND the sound.", "Set H1–H4."],
           "Answer chorally.", "Whole class", "Slide 12")],
    teacher_talk=[
        TK("Teaching the three -ed sounds",
           ["Fingers on your throat. Say /k/ … no buzz. Say /ɡ/ … buzz! Feel the difference?",
            "'Work' ends with /k/ — no buzz. So -ed is quiet too: work-T. Worked.",
            "'Clean' ends with /n/ — buzz. So -ed buzzes: clean-D. Cleaned.",
            "And 'visit' already ends with /t/. You cannot say 'visit-t'! So English adds a whole new "
            "syllable: vi-si-TED. Three syllables. Count with me on your fingers."]),
        TK("Why the ending matters",
           ["Some students say: 'Teacher, nobody hears the small /t/. Why do I need it?'",
            "Listen: 'I clean my room.' — I do it every day. 'I cleanED my room.' — finished, yesterday.",
            "One tiny sound changes the whole meaning. In Vietnamese, the tone changes the word — "
            "you would never drop a tone. In English, do not drop the ending."])],
    support=["Give the verb list with the sound already marked for 4 of the 10 verbs.",
             "Use colour cards: red = /t/, blue = /d/, green = /ɪd/ — students raise a card.",
             "Reduce the spelling test to five verbs."],
    challenge=["Ask them to add three new verbs to each sound column.",
               "Ask for a 6-sentence story using one verb from each spelling rule.",
               "Ask them to explain the /ɪd/ rule to the class."],
    assessment=["7 of 8 correct in the -ed sound task", "6 of 8 correct spellings",
                "Produces audible -ed endings when speaking"],
    board_plan=["LEFT: 8 new words", "CENTRE: /t/ | /d/ | /ɪd/ three columns + 4 spelling rules",
                "RIGHT: thanking phrases; Homework H1–H4"],
    materials=["Colour cards (red/blue/green)", 'Recording: The past simple: -ed verbs — ELLLO — Sound Grammar (2:17)'],
)

L3 = Lesson(
    code="U3L3", unit=3, number=3, period=19,
    lesson_type="A Closer Look 2", title="Past simple: negatives, questions and irregular verbs",
    objectives=["make negative sentences with didn't + bare verb",
                "ask and answer past simple questions (Did you…? What did you…?)",
                "use twelve common irregular verbs in the past",
                "talk about a past experience for one minute"],
    recycled=["U3L1–L2: community vocabulary, regular past simple, -ed sounds"],
    vocab=[
        V("go → went", "v", "/went/", "đã đi", "We went to the orphanage."),
        V("do → did", "v", "/dɪd/", "đã làm", "What did you do last Sunday?"),
        V("give → gave", "v", "/ɡeɪv/", "đã cho", "They gave us some cakes."),
        V("take → took", "v", "/tʊk/", "đã lấy/mang", "We took the books to the library."),
        V("make → made", "v", "/meɪd/", "đã làm/tạo", "She made twenty sandwiches."),
        V("buy → bought", "v", "/bɔːt/", "đã mua", "The club bought school bags."),
        V("teach → taught", "v", "/tɔːt/", "đã dạy", "He taught the children to swim."),
        V("meet → met", "v", "/met/", "đã gặp", "We met the head teacher at nine."),
    ],
    phrases=["What did you do…?", "Where did you go…?", "How many … did you …?",
             "It was + adjective", "We had a great time."],
    grammar=G("Past simple: negative and question forms",
              use=["Negative: didn't + BARE verb. The past is already in 'didn't', so the main verb "
                   "goes back to its simple form.",
                   "Question: Did + subject + BARE verb? Short answers: Yes, I did. / No, I didn't.",
                   "Wh- question: What / Where / When / How many + did + subject + bare verb?",
                   "BUT the verb 'be' is different: was / wasn't, were / weren't (no 'did')."],
              form=[["", "Positive", "Negative", "Question"],
                    ["Regular", "We cleaned the park.", "We didn't clean the park.",
                     "Did you clean the park?"],
                    ["Irregular", "They went to the centre.", "They didn't go to the centre.",
                     "Did they go to the centre?"],
                    ["be", "It was hard.", "It wasn't hard.", "Was it hard?"]],
              examples=["Did you take part in the clean-up day? – Yes, I did.",
                        "We didn't finish before five o'clock.",
                        "What did the club buy with the money? – They bought school bags.",
                        "The weather was hot, but the students weren't tired."],
              pitfall="THE classic error: *Did you went?* / *I didn't went.* After DID or DIDN'T the "
                      "verb has NO past form. Only one word can carry the past — and 'did' has already "
                      "taken the job.",
              note="Board slogan: DID takes the past away from the verb. Write it in a box and point to "
                   "it every time the error appears."),
    pron=P("'did you' in fast speech and stress in questions",
           "In natural speech 'did you' sounds like /dɪdʒə/. The stress falls on the main verb: "
           "'What did you DO?' Students should recognise it, not copy it exactly.",
           items=["What did you do? → /wɒt dɪdʒə duː/", "Did you go? → /dɪdʒə ɡəʊ/",
                  "Where did you go? → /weə dɪdʒə ɡəʊ/"],
           drill=["What did you DO last Sunday?", "Where did you GO?", "Did you EN-joy it?"],
           vn_note="Learners hear only 'did' and miss 'you'. Play the question three times and let them "
                   "hear the joined sound before they see it written."),
    listening=AUDIO['U3L3'],
    reading=T("A letter of thanks",
              ["Dear Class 7A,",
               "Thank you very much for your visit last Saturday. The children talked about it all week!",
               "You didn't only bring books — you brought your time and your voices. The little ones "
               "loved the songs, and Minh, our shyest boy, spoke to a visitor for the first time in "
               "two years.",
               "We counted the books: 214. We put them on the new shelf that your teacher made. "
               "Please come again in December.",
               "With many thanks,",
               "Mrs Nguyen Thi Hoa, Sunflower Children's Home"],
              tasks=[
                  EX("U3.3-R1", "Read and answer", "Answer the questions.",
                     items=["1. When did class 7A visit?", "2. How many books did they bring?",
                            "3. What did the little children love?",
                            "4. What was special about Minh?", "5. Who made the shelf?"],
                     answers=["1. Last Saturday.", "2. 214.", "3. The songs.",
                              "4. He spoke to a visitor for the first time in two years.",
                              "5. Their teacher."], level="M", kind="reading")]),
    speaking=[
        EX("U3.3-S1", "Find someone who… (past)", "Ask 'Did you…?' questions and find a name for each.",
           items=["…went to the countryside last summer.", "…helped a neighbour last week.",
                  "…gave something to a charity.", "…took part in a school activity.",
                  "…made something with their hands."],
           answers=["Report: 'Hoa went to the countryside last summer.'"], level="M", kind="speaking"),
        EX("U3.3-S2", "One-minute memory", "Tell your partner about a day when you helped someone. "
           "Answer these four questions.",
           items=["When was it? / Where did you go? / What did you do? / How did you feel?"],
           answers=["Model: Last Tet I helped my grandmother. I went to her house on the second day. "
                    "I cleaned the yard and made tea for the visitors. I felt tired but very happy."],
           level="D", kind="speaking")],
    writing=[EX("U3.3-W1", "Make it negative, then ask", "Rewrite each sentence as a negative and "
                "then as a question.",
                items=["1. They cleaned the beach.", "2. She went to the orphanage.",
                       "3. We bought new books.", "4. He taught the children."],
                answers=["1. They didn't clean the beach. / Did they clean the beach?",
                         "2. She didn't go to the orphanage. / Did she go to the orphanage?",
                         "3. We didn't buy new books. / Did you buy new books?",
                         "4. He didn't teach the children. / Did he teach the children?"],
                level="M", kind="writing")],
    communication={"function": "Asking about a past experience",
                   "phrases": ["Did you have a good time?", "What did you do?", "Where did you go?",
                               "How was it?", "It was great / hard / tiring but fun.",
                               "Sounds interesting!"],
                   "roleplay": "A came back from a volunteer trip. B asks five past questions. "
                               "Then swap.",
                   "real_life": "Talking about the weekend, a trip or an event — the most common "
                                "conversation in any language."},
    guided=[
        EX("U3.3-G1", "Irregular verbs", "Write the past form.",
           items=["1. go → ", "2. do → ", "3. give → ", "4. take → ", "5. make → ", "6. buy → ",
                  "7. teach → ", "8. meet → ", "9. is/am → ", "10. are → "],
           answers=["1. went", "2. did", "3. gave", "4. took", "5. made", "6. bought", "7. taught",
                    "8. met", "9. was", "10. were"], level="E", kind="grammar"),
        EX("U3.3-G2", "didn't + verb", "Make the sentences negative.",
           items=["1. We went to the market.", "2. She cleaned her room.", "3. They bought a present.",
                  "4. I met the head teacher.", "5. He was tired."],
           answers=["1. We didn't go to the market.", "2. She didn't clean her room.",
                    "3. They didn't buy a present.", "4. I didn't meet the head teacher.",
                    "5. He wasn't tired."], level="M", kind="grammar",
           note="No. 5 uses 'be' → wasn't, NOT 'didn't be'.")],
    independent=[
        EX("U3.3-I1", "Error clinic", "Find and correct one mistake in each sentence.",
           items=["1. Did you went to the beach?", "2. I didn't cleaned my room.",
                  "3. She don't go to school yesterday.", "4. What you did last Sunday?",
                  "5. They was very happy.", "6. Did he bought a book?"],
           answers=["1. Did you go to the beach?", "2. I didn't clean my room.",
                    "3. She didn't go to school yesterday.", "4. What did you do last Sunday?",
                    "5. They were very happy.", "6. Did he buy a book?"],
           level="D", kind="grammar",
           note="Numbers 1, 2 and 6 are the same error: after did/didn't the verb is BARE."),
        EX("U3.3-I2", "Interview", "Do U3.3-S1, then tell the class two answers.",
           items=[], answers=["Watch the question form: Did + subject + bare verb."],
           level="M", kind="speaking")],
    review=["didn't + bare verb", "Did + subject + bare verb?", "12 irregular verbs", "was / were"],
    homework=[
        EX("U3.3-H1", "Grammar", "Complete with the past simple.",
           items=["1. We (go) ______ to the orphanage last Sunday.",
                  "2. They (not buy) ______ new books.",
                  "3. ______ you (meet) ______ the volunteers?",
                  "4. She (teach) ______ the children a song.",
                  "5. It (be) ______ a wonderful day.",
                  "6. The students (not be) ______ tired."],
           answers=["1. went", "2. didn't buy", "3. Did … meet", "4. taught", "5. was", "6. weren't"],
           level="M", kind="grammar"),
        EX("U3.3-H2", "Grammar", "Write the questions for the answers.",
           items=["1. ______ ? – We went to the primary school.",
                  "2. ______ ? – We painted two classrooms.",
                  "3. ______ ? – Yes, I did. It was great.",
                  "4. ______ ? – We raised 600,000 dong."],
           answers=["1. Where did you go?", "2. What did you do?", "3. Did you enjoy it?",
                    "4. How much money did you raise?"], level="D", kind="grammar"),
        EX("U3.3-H3", "Writing", "Write 5 sentences about what you did last weekend. "
           "Include one negative sentence and two irregular verbs.",
           items=[], answers=["Model: Last Saturday I went to my grandmother's house. I helped her in "
                              "the garden and I made lunch. In the afternoon I met my friends near the "
                              "lake. We played football for an hour. I didn't do my homework on Saturday, "
                              "so I studied all Sunday morning."],
           level="M", kind="writing", lines=6),
        EX("U3.3-H4", "Speaking", "Practise asking the five questions from U3.3-S1 aloud. "
           "Remember: 'What did you DO?' — stress the main verb.",
           items=[], answers=["Spot-check in Lesson 4."], level="E", kind="pron")],
    workbook=[
        EX("U3.3-P1", "Irregular verb table", "Complete the table.",
           items=["go – ______ | do – ______ | give – ______ | take – ______",
                  "make – ______ | buy – ______ | teach – ______ | meet – ______",
                  "see – ______ | eat – ______ | write – ______ | come – ______"],
           answers=["went, did, gave, took", "made, bought, taught, met", "saw, ate, wrote, came"],
           level="E", kind="grammar"),
        EX("U3.3-P2", "Positive → negative", "Rewrite.",
           items=["1. He took the books to the library.", "2. We made a poster.",
                  "3. They gave money to the charity.", "4. I saw the volunteers.",
                  "5. She was at the meeting."],
           answers=["1. He didn't take the books to the library.", "2. We didn't make a poster.",
                    "3. They didn't give money to the charity.", "4. I didn't see the volunteers.",
                    "5. She wasn't at the meeting."], level="M", kind="grammar"),
        EX("U3.3-P3", "Write the questions", "Use the words to make past questions.",
           items=["1. what / you / do / yesterday ?", "2. where / your class / go / last month ?",
                  "3. how many books / they / donate ?", "4. you / enjoy / the day ?",
                  "5. why / she / not come ?"],
           answers=["1. What did you do yesterday?", "2. Where did your class go last month?",
                    "3. How many books did they donate?", "4. Did you enjoy the day?",
                    "5. Why didn't she come?"], level="D", kind="grammar"),
        EX("U3.3-P4", "Gap-fill story", "Complete with the past simple.",
           text=["Last December our club (1. go) ______ to a village in the mountains. We (2. take) ______ "
                 "warm clothes and books. The children (3. be) ______ very shy at first, but after an hour "
                 "they (4. sing) ______ with us. We (5. not have) ______ much time, so we (6. not visit) "
                 "______ all the families. Our teacher (7. buy) ______ rice for two families and we "
                 "(8. give) ______ the clothes to the school."],
           items=["Write the eight verbs."],
           answers=["1. went", "2. took", "3. were", "4. sang", "5. didn't have", "6. didn't visit",
                    "7. bought", "8. gave"], level="D", kind="grammar"),
        EX("U3.3-P5", "Writing", "Write a short paragraph (60–70 words) about a school trip or activity "
           "you remember.",
           items=["Include: when, where, what you did (3 things), how you felt."],
           answers=["Model: Last April our class went to Cuc Phuong National Park. We left school at six "
                    "in the morning. We walked in the forest, saw a thousand-year-old tree and ate lunch "
                    "under the trees. In the afternoon we collected the litter that other visitors left. "
                    "I was very tired in the evening, but it was one of the best days of the year."],
           level="D", kind="writing", lines=8)],
    procedure=[
        ST("Warm-up: Irregular verb slam", 5,
           ["Write ten base verbs on the board. Teams race to write the past forms.",
            "Check together; drill the pronunciation of bought /bɔːt/ and taught /tɔːt/."],
           "Race to write past forms.", "Teams", "Slide 2"),
        ST("Presentation: negatives and questions", 12,
           ["Start with a positive sentence: 'We cleaned the park.' Ask: 'How do we say NO?'",
            "Build: We DIDN'T CLEAN the park. Underline 'clean' — no -ed! Explain: did already carries "
            "the past.",
            "Same for the question: DID you CLEAN…? Drill both forms.",
            "Warn about 'be': was / wasn't — no 'did'."],
           "Repeat, copy the table, produce three sentences.", "Whole class", "Slides 3–6"),
        ST("Guided practice", 8,
           ["U3.3-G1 (irregular verbs) then G2 (negatives). Check by nominating students.",
            "Error clinic with U3.3-I1 on the board."],
           "Complete the tasks; correct the six errors.", "Pairs", "Student Book p. U3L3"),
        ST("Listening", 8,
           ['Play the recording “The past simple: irregular verbs” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.',
            "Draw attention to the natural /dɪdʒə/ sound."],
           "Listen and complete; notice 'did you'.", "Individual → pairs", "Slide 7"),
        ST("Speaking", 8,
           ["Find someone who… (past) mingle, then the one-minute memory in pairs."],
           "Ask past questions; tell a personal memory.", "Mingle → pairs", "Slides 8–9"),
        ST("Wrap-up and homework", 4,
           ["Three students report one thing they learned about a classmate.", "Set H1–H4."],
           "Report; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[
        TK("The 'DID takes the past away' rule",
           ["Look at this sentence: We cleanED the park. The -ED carries the past. Good.",
            "Now I make a question: DID you cleaned the park? … Listen. Two past forms — 'did' AND "
            "'cleaned'. That is too much! English only allows ONE.",
            "'Did' is stronger, so it takes the past away from the verb: DID you CLEAN the park?",
            "Same with the negative: I didn't CLEAN. Not 'didn't cleaned'. Say it with me."]),
        TK("Warning about 'be'",
           ["Careful! One verb refuses to work with 'did'. That verb is BE.",
            "We do NOT say 'Did you be happy?' We say: WERE you happy?",
            "And not 'I didn't be tired' but 'I WASN'T tired.'",
            "Be is special. It works alone. Write that in your notebook with a star."])],
    support=["Give the irregular verb list to keep on the desk during all activities.",
             "Colour the bare verb in green in the model sentences.",
             "Let weaker students answer with short answers only in the mingle."],
    challenge=["Ask for Wh- questions with 'How many…?' and 'Why…?'",
               "Ask them to interview the teacher about a past experience.",
               "Ask for a 8-sentence memory with two negatives."],
    assessment=["8 of 10 irregular verbs correct", "No 'did + past verb' errors in written work",
                "Asks two correct past questions in the mingle"],
    board_plan=["LEFT: irregular verb list", "CENTRE: DID takes the past away! + question/negative table",
                "RIGHT: be → was/were (special); Homework H1–H4"],
    materials=["Irregular verb cards", 'Recording: The past simple: irregular verbs — ELLLO — Sound Grammar (2:18)'],
)

L4 = Lesson(
    code="U3L4", unit=3, number=4, period=20,
    lesson_type="Communication", title="Everyday English: offering help and thanking",
    objectives=["offer help and accept or refuse an offer politely",
                "thank someone and respond to thanks",
                "take part in a 6-turn role play about a community activity",
                "interview a classmate about a past experience and report it"],
    recycled=["U3L1–L3: community vocabulary, past simple in all forms, -ed sounds; "
              "Unit 2: sympathy and advice phrases"],
    vocab=[
        V("offer", "v/n", "/ˈɒfə/", "đề nghị giúp", "She offered to carry my bag."),
        V("give someone a hand", "v phr", "/ɡɪv ˈsʌmwʌn ə hænd/", "giúp một tay", "Can you give me a hand?"),
        V("grateful", "adj", "/ˈɡreɪtfl/", "biết ơn", "We are very grateful for your help."),
        V("appreciate", "v", "/əˈpriːʃieɪt/", "trân trọng", "I really appreciate your time."),
        V("carry", "v", "/ˈkæri/", "mang, vác", "They carried the boxes to the truck."),
        V("share", "v", "/ʃeə/", "chia sẻ", "We shared the work between six people."),
    ],
    phrases=["Can I help you?", "Do you need a hand?", "Let me help you with that.",
             "Yes, please. That's very kind.", "No, thanks. I'm fine.", "Thank you so much.",
             "You're welcome. / Don't mention it."],
    grammar=G("Offers with Can I…? / Shall I…? / Would you like…?",
              use=["Can I help you? – the simplest and most common offer.",
                   "Shall I carry that? – slightly more formal, common in Britain.",
                   "Would you like some help? – polite, used with strangers and adults.",
                   "Accepting: Yes, please. That's very kind of you. Refusing: No, thanks. I'm fine."],
              form=[["Offer", "Accept", "Refuse"],
                    ["Can I help you?", "Yes, please.", "No, thanks. I'm fine."],
                    ["Shall I carry that?", "That's very kind of you.", "It's OK, thanks. I can do it."],
                    ["Would you like some help?", "Thank you, I'd love some.", "Thanks, but I'm nearly finished."]],
              examples=["Can I give you a hand with those books? – Yes, please. They're heavy!",
                        "Shall I open the door for you? – That's very kind of you."],
              pitfall="Students say *I help you?* or *You want help?* — direct translations that sound "
                      "abrupt. Teach the three fixed offer forms as chunks.",
              note="After 'Can I' and 'Shall I' the verb is bare: Can I HELP, Shall I CARRY."),
    pron=P("Polite rising intonation in offers",
           "An offer goes UP at the end. A flat or falling offer sounds like an order. "
           "Compare: 'Can I help you? ↗' (kind) vs 'Can I help you. ↘' (cold).",
           items=["Can I help you? ↗", "Shall I carry that? ↗", "Would you like some help? ↗",
                  "Yes, please. ↘", "No, thanks. ↘"],
           drill=["A: Can I help you? ↗  B: Yes, please. That's very kind.",
                  "A: Shall I carry that box? ↗  B: No, thanks. I'm fine."],
           vn_note="Rising intonation carries politeness in English. Model it with an upward hand "
                   "movement and make students copy the gesture."),
    listening=AUDIO['U3L4'],
    reading=T("Thank-you notes on the school board",
              ["'Thank you to class 7A for the 214 books. Our children read every evening now.' "
               "– Sunflower Children's Home",
               "'A big thank you to the students who cleaned the road in front of my shop last Sunday. "
               "I did not ask, and they did not want money. That is real kindness.' – Mr Tam, "
               "the bookshop",
               "'We are very grateful to the Green Sunday Club. In one year they collected 12,000 "
               "plastic bottles from our street.' – The Ward Committee"],
              tasks=[
                  EX("U3.4-R1", "Read and answer", "Answer the questions.",
                     items=["1. Who wrote the first note and why?", "2. What did the students do for Mr Tam?",
                            "3. Did Mr Tam ask them to do it?", "4. How many bottles did the club collect?"],
                     answers=["1. Sunflower Children's Home, to thank class 7A for 214 books.",
                              "2. They cleaned the road in front of his shop.",
                              "3. No, he didn't — and they didn't want money.", "4. 12,000."],
                     level="M", kind="reading")]),
    speaking=[
        EX("U3.4-S1", "Offer and reply", "Look at the situations and make an offer. Your partner "
           "accepts or refuses.",
           items=["1. Your teacher is carrying twenty books.", "2. An old lady drops her bag.",
                  "3. Your friend is cleaning the board alone.", "4. A tourist is looking at a map.",
                  "5. Your mother is cooking for ten guests."],
           answers=["Model: 1. Can I help you with those books, Ms Lan? – Yes, please. That's very kind."],
           level="M", kind="speaking"),
        EX("U3.4-S2", "Volunteer day role play", "A is a volunteer organiser, B is a student who wants "
           "to help. Six turns.",
           items=["Organiser: welcome → say the jobs → answer a question → thank",
                  "Student: offer help → choose a job → ask about the time → say goodbye"],
           answers=["Suggested: A: Good morning, thanks for coming. B: Can I give you a hand? "
                    "A: Yes, please. We need people to carry books or to write labels. "
                    "B: I'd like to carry books. What time do we finish? A: At about four. "
                    "B: Great, see you later. A: Thank you so much!"],
           level="D", kind="speaking")],
    writing=[EX("U3.4-W1", "A thank-you note", "Write a short thank-you note (3–4 sentences) to people "
                "who helped your class.",
                items=["Say what they did, how it helped, and thank them."],
                answers=["Model: Dear parents, Thank you very much for your help on Volunteer Day. "
                         "You carried the heavy boxes and you brought water for everybody. "
                         "Because of you we finished before lunch. We really appreciate it. Class 7A"],
                level="M", kind="writing", lines=5)],
    communication={"function": "Offering help, accepting, refusing and thanking",
                   "phrases": ["Can I help you?", "Do you need a hand?", "Shall I…?",
                               "Yes, please. That's very kind.", "No, thanks. I'm fine.",
                               "Thank you so much.", "You're welcome. / Don't mention it.",
                               "I really appreciate it."],
                   "roleplay": "Chain role play in fours: A offers help to B, B thanks A; then B offers "
                               "help to C, and so on round the group.",
                   "real_life": "Helping a teacher, a neighbour or a stranger, and knowing what to say "
                                "when someone helps you."},
    guided=[
        EX("U3.4-G1", "Offer or thanks?", "Write O (offer), A (accept), R (refuse) or T (thanks).",
           items=["1. Can I give you a hand? ___", "2. Yes, please. ___", "3. No, thanks. I'm fine. ___",
                  "4. I really appreciate it. ___", "5. Shall I carry that? ___",
                  "6. That's very kind of you. ___"],
           answers=["1. O", "2. A", "3. R", "4. T", "5. O", "6. A"], level="E", kind="mixed"),
        EX("U3.4-G2", "Complete the conversation", "Use the words in the box.",
           wordbank=["hand", "please", "kind", "welcome", "Shall"],
           items=["A: Do you need a (1) ______ with those chairs?",
                  "B: Yes, (2) ______ . That's very (3) ______ of you.",
                  "A: (4) ______ I take the big ones?", "B: Thank you so much!",
                  "A: You're (5) ______ ."],
           answers=["1. hand", "2. please", "3. kind", "4. Shall", "5. welcome"],
           level="M", kind="mixed")],
    independent=[
        EX("U3.4-I1", "Interview and report", "Ask a classmate: 'Did you ever help someone? "
           "What did you do? How did they thank you?' Report to the class.",
           items=[], answers=["Model: Last month Nam helped an old man carry rice. The man gave him "
                              "two oranges and said thank you."], level="D", kind="speaking"),
        EX("U3.4-I2", "Role play performance", "Perform U3.4-S2 for another pair with the checklist.",
           items=["Checklist: □ 6 turns □ one offer □ accept/refuse □ a question □ thanks □ polite "
                  "intonation"],
           answers=["Assessment: task 3, fluency 2.5, pronunciation 2.5, accuracy 2."],
           level="D", kind="speaking")],
    review=["Offers: Can I…? / Shall I…? / Do you need a hand?", "Accepting and refusing politely",
            "Thanking and responding"],
    homework=[
        EX("U3.4-H1", "Everyday English", "Write what you say.",
           items=["1. Your teacher is carrying heavy books. (offer) ______",
                  "2. Someone offers to help you but you don't need it. (refuse) ______",
                  "3. A neighbour helped your family. (thank) ______",
                  "4. Your friend says 'Thank you'. (reply) ______"],
           answers=["1. Can I help you with those books? / Shall I carry them?",
                    "2. No, thanks. I'm fine.", "3. Thank you so much. We really appreciate it.",
                    "4. You're welcome. / Don't mention it."], level="M", kind="mixed"),
        EX("U3.4-H2", "Vocabulary", "Complete with offer, grateful, appreciate, carry, share.",
           items=["1. Can you ______ this box for me?", "2. We are very ______ for your help.",
                  "3. I really ______ what you did.", "4. She made a kind ______ .",
                  "5. Let's ______ the work between us."],
           answers=["1. carry", "2. grateful", "3. appreciate", "4. offer", "5. share"],
           level="E", kind="vocab"),
        EX("U3.4-H3", "Writing", "Write your thank-you note from U3.4-W1 neatly.",
           items=[], answers=["See U3.4-W1 model."], level="M", kind="writing", lines=6),
        EX("U3.4-H4", "Speaking", "Practise the three offers with rising intonation five times each.",
           items=["Can I help you? ↗ / Shall I carry that? ↗ / Do you need a hand? ↗"],
           answers=["Spot-check in Lesson 5."], level="E", kind="pron")],
    workbook=[
        EX("U3.4-P1", "Match", "Match the offer with the best reply.",
           items=["1. Can I help you?", "2. Shall I carry that?", "3. Thank you so much.",
                  "4. Do you need a hand?",
                  "a. You're welcome.", "b. No, thanks. It's light.", "c. Yes, please. That's kind.",
                  "d. Yes, please. These boxes are heavy."],
           answers=["1–c", "2–b", "3–a", "4–d"], level="E", kind="mixed"),
        EX("U3.4-P2", "Order the conversation", "Number the lines 1–6.",
           items=["___ You're welcome.", "___ Can I give you a hand with the chairs?",
                  "___ Yes, please. That's very kind of you.", "___ Thank you so much!",
                  "___ Shall I take the heavy ones?", "___ Yes, thank you. They're very heavy."],
           answers=["6, 1, 2, 5, 3, 4 → Can I give you a hand with the chairs? / Yes, please. That's "
                    "very kind of you. / Shall I take the heavy ones? / Yes, thank you. They're very "
                    "heavy. / Thank you so much! / You're welcome."],
           level="M", kind="mixed"),
        EX("U3.4-P3", "Write the offers", "Write a suitable offer for each situation.",
           items=["1. Your grandmother is washing a lot of dishes.",
                  "2. A new student cannot find the classroom.",
                  "3. Your teacher's bag falls and the papers go on the floor.",
                  "4. Your friend has a broken arm and two big books."],
           answers=["1. Shall I help you with the dishes? 2. Can I show you the way? "
                    "3. Let me help you with those papers. 4. Do you need a hand with your books?"],
           level="M", kind="writing"),
        EX("U3.4-P4", "Write a dialogue", "Write a 10-line conversation on Volunteer Day.",
           items=["Include: two offers, one refusal, one question about time, thanks and a reply."],
           answers=["Model: A: Good morning! Thank you for coming. B: Can I give you a hand? "
                    "A: Yes, please. Could you carry these boxes? B: Of course. Shall I take the big "
                    "ones too? A: No, thanks — they are too heavy. The men will take them. "
                    "B: What time do we finish? A: At about four o'clock. B: OK, no problem. "
                    "A: Thank you so much. We really appreciate your help. B: You're welcome!"],
           level="D", kind="writing", lines=12)],
    procedure=[
        ST("Warm-up: Past questions ping-pong", 5,
           ["Students ask each other one past question along the row: 'What did you do yesterday?' "
            "Recycles Lesson 3."],
           "Ask and answer past questions.", "Rows", "Slide 2"),
        ST("Presentation: offers and thanks", 9,
           ["Drop a pile of books on your desk and look helpless. Elicit: 'Can I help you?'",
            "Present the three offer forms and the accept/refuse replies with rising intonation and gesture.",
            "Drill: teacher shows a situation picture, class produces an offer."],
           "Repeat with gesture; produce offers from pictures.", "Whole class", "Slides 3–5"),
        ST("Listening: moving day", 8,
           ['Play the recording “Lesson 41: Teamwork Works Best With a Team” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; read the script in role with four students.',
            "Note the polite refusal Mrs Ha uses ('Thank you, but…')."],
           "Listen, match, complete.", "Individual → pairs", "Slide 6"),
        ST("Guided practice", 7, ["U3.4-G1 and G2 in pairs, then two pairs perform G2."],
           "Complete and perform.", "Pairs", "Student Book p. U3L4"),
        ST("Role play", 11,
           ["Give the role cards. 3 minutes to prepare, then perform to another pair with the checklist.",
            "Two pairs perform for the class; focus feedback on intonation."],
           "Prepare, perform, evaluate another pair.", "Pairs → fours", "Slides 7–9"),
        ST("Wrap-up and homework", 5,
           ["Chain of thanks: each student thanks the next for something real from this week.",
            "Set H1–H4."],
           "Thank a classmate; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[
        TK("Teaching polite offers",
           ["Watch me. (Carry a big pile of books and look tired.) What do you say to me?",
            "'Teacher, I help you'? … I understand, but it sounds like an order, not an offer.",
            "In English we make it a QUESTION and the voice goes UP: Can I help you? ↗",
            "Three chunks for your notebook: Can I help you? / Shall I carry that? / Do you need a hand?"]),
        TK("Refusing without being rude",
           ["Sometimes you don't need help. If you say only 'No', it sounds cold.",
            "Add two things: a thank you, and a reason. 'No, thanks. I'm fine.' 'It's OK, thanks — "
            "it's not heavy.'",
            "Thank you + reason. That is the polite formula in English and in Vietnamese."])],
    support=["Give the offer/reply phrases on a desk card.",
             "Use picture prompts so students do not have to invent the situation.",
             "Allow the role play with the model dialogue visible the first time."],
    challenge=["Ask them to add a follow-up question in every offer.",
               "Ask them to refuse politely with two different reasons.",
               "Ask them to write and perform the chain role play in fours."],
    assessment=["Uses two different offer forms", "Refuses politely with thanks + reason",
                "Rising intonation on offers"],
    board_plan=["LEFT: three offer forms", "CENTRE: accept | refuse replies",
                "RIGHT: thanking phrases; Homework H1–H4"],
    materials=["Situation picture cards", "Role cards", 'Recording: Lesson 41: Teamwork Works Best With a Team — VOA Learning English — Let’s Learn English, Level 1 (3:32)'],
)

L5 = Lesson(
    code="U3L5", unit=3, number=5, period=21,
    lesson_type="Skills 1", title="Reading: Young volunteers + Speaking: Report a past event",
    objectives=["read a 220-word article and answer gist, detail and inference questions",
                "guess the meaning of new words from context",
                "report a past community event in 60–90 seconds",
                "ask a speaker two follow-up questions"],
    recycled=["U3L1–L4: all unit vocabulary, past simple, offers and thanks; Unit 2 opinion language"],
    vocab=[
        V("achievement", "n", "/əˈtʃiːvmənt/", "thành tựu", "Their biggest achievement was the new library."),
        V("local", "adj", "/ˈləʊkl/", "địa phương", "The local people helped us."),
        V("flood", "n", "/flʌd/", "lũ lụt", "The flood damaged twenty houses."),
        V("victim", "n", "/ˈvɪktɪm/", "nạn nhân", "They sent clothes to the flood victims."),
        V("proud of", "adj phr", "/praʊd əv/", "tự hào về", "We are proud of our students."),
        V("difference", "n", "/ˈdɪfrəns/", "sự khác biệt", "Small actions make a big difference."),
    ],
    phrases=["make a difference", "take part in", "be proud of", "thanks to…", "at first… in the end…"],
    grammar=G("Sequencing a past story: first, then, after that, finally",
              use=["Use sequence words so the listener can follow your story.",
                   "First, … / At first, … (the beginning)",
                   "Then, … / After that, … (the middle)",
                   "Finally, … / In the end, … (the end)"],
              form=[["Stage", "Words", "Example"],
                    ["Beginning", "First / At first", "First, we met at the school gate at seven."],
                    ["Middle", "Then / After that / Next", "Then we walked to the beach."],
                    ["End", "Finally / In the end", "Finally, we took a photo together."]],
              examples=["First, we collected the bottles. Then we washed them. Finally, we sold them "
                        "and gave the money to the charity."],
              pitfall="Students write 'and… and… and…'. Sequence words are the easiest way to make "
                      "writing and speaking sound organised.",
              note="'At first' means 'in the beginning, but later it changed': At first it was hard, "
                   "but in the end we finished early."),
    pron=P("Pausing after sequence words",
           "Say the sequence word, then PAUSE for half a second: 'First, / we met at the gate.' "
           "The pause gives the listener time and makes you sound confident.",
           items=["First, / …", "Then, / …", "After that, / …", "Finally, / …"],
           drill=["First, / we collected the bottles. Then, / we washed them. Finally, / we sold them."],
           vn_note="Learners often speak without pauses, so the listener cannot find the structure. "
                   "Mark the pauses in the notes with a slash before speaking."),
    listening=AUDIO['U3L5'],
    reading=T("Young people who made a difference",
              ["Ask most adults about teenagers and they will talk about phones and computer games. "
               "But across Viet Nam, thousands of young people spend their free time helping others. "
               "Here are two of them.",
               "Le Thi Hong Nhung, 14, lives in a small town in Quang Nam. Three years ago, after a "
               "flood, she saw that many children in her street had lost their school books. She asked "
               "her classmates for old books and started a 'book bank' in her family's front room. "
               "At first she had 30 books. Today the book bank has more than 1,200 and eight students "
               "help her every week. 'The books are not mine,' she says. 'They belong to the street.'",
               "Tran Quoc Bao, 15, from Ha Nam, is interested in the environment. Two years ago he "
               "counted the plastic bags in his village market: 4,000 in one morning. He made 200 cloth "
               "bags with his grandmother and gave them free to the sellers. Now most sellers use cloth "
               "bags, and the village committee has copied his idea in two other markets.",
               "Neither of them is rich or famous. They saw one problem, they started small, and they "
               "did not stop."],
              tasks=[
                  EX("U3.5-R1", "Gist", "Read quickly and choose the best title.",
                     items=["A. Two teenagers who solved a problem in their community",
                            "B. Why teenagers use too many phones", "C. How to start a business"],
                     answers=["A"], level="E", kind="reading"),
                  EX("U3.5-R2", "Detail", "Complete the table.",
                     items=["Name | Age | Place | Problem | Action | Result",
                            "Nhung | ___ | ___ | ___ | ___ | ___",
                            "Bao | ___ | ___ | ___ | ___ | ___"],
                     answers=["Nhung | 14 | Quang Nam | children lost their school books after a flood | "
                              "collected old books, started a book bank | more than 1,200 books, "
                              "8 helpers",
                              "Bao | 15 | Ha Nam | 4,000 plastic bags in the market in one morning | "
                              "made 200 cloth bags and gave them free | most sellers use cloth bags; "
                              "two other markets copied the idea"],
                     level="M", kind="reading"),
                  EX("U3.5-R3", "Vocabulary from context", "Find a word or phrase that means:",
                     items=["1. of this area (paragraph 3)", "2. things people own (paragraph 2)",
                            "3. to do the same as someone (paragraph 3)",
                            "4. water that covers the land (paragraph 2)"],
                     answers=["1. village / (the) village committee — accept 'local' from the vocabulary "
                              "box", "2. belong to", "3. copy (has copied)", "4. flood"],
                     level="M", kind="reading"),
                  EX("U3.5-R4", "Inference", "Answer with your own ideas.",
                     items=["1. Why does Nhung say 'The books are not mine'?",
                            "2. Why did Bao count the plastic bags before he did anything?",
                            "3. What is the message of the last paragraph?"],
                     answers=["1. Because she thinks they belong to everyone in the street; she keeps "
                              "them for the community, not for herself.",
                              "2. To find out how big the problem was / to have real numbers to show "
                              "people.",
                              "3. You don't need money or fame — start small with one problem and don't "
                              "give up."], level="D", kind="reading")]),
    speaking=[
        EX("U3.5-S1", "Prepare your report", "Make notes about a real or imagined community event.",
           items=["1. What was it and when? ______", "2. First… ______", "3. Then… ______",
                  "4. Finally… ______", "5. How did you feel? ______"],
           answers=["Notes only. Mark a pause slash after each sequence word."],
           level="M", kind="speaking"),
        EX("U3.5-S2", "Give your report", "Speak for 60–90 seconds in a group of four. "
           "Listeners ask two questions each.",
           items=["Useful language: First, / Then, / After that, / Finally, / It was tiring but…"],
           answers=["Assessment: content 3, sequence words 2, past simple 3, delivery 2."],
           level="D", kind="speaking")],
    writing=[EX("U3.5-W1", "Notes to sentences", "Turn your five notes into five full sentences with "
                "sequence words.",
                items=[], answers=["Model: Last November our class helped a village school. First, we "
                                   "collected old books from every class. Then we packed them into "
                                   "boxes. After that, we travelled to the village by bus. Finally, we "
                                   "put the books on the shelves and played with the children. "
                                   "I felt tired but very proud."],
                level="M", kind="writing", lines=6)],
    communication={"function": "Showing interest and asking follow-up questions",
                   "phrases": ["That's amazing!", "How long did it take?", "How many people helped?",
                               "What was the hardest part?", "Would you do it again?"],
                   "roleplay": "After each report the group must ask at least four questions in total. "
                               "A silent listener loses a point.",
                   "real_life": "Keeping a conversation going by asking about the details of someone's "
                                "story."},
    guided=[
        EX("U3.5-G1", "Sequence words", "Complete the story with First, Then, After that, Finally.",
           items=["1. ______ , we made a plan.", "2. ______ , we collected the books.",
                  "3. ______ , we packed them in boxes.", "4. ______ , we took them to the village."],
           answers=["1. First", "2. Then", "3. After that", "4. Finally"], level="E", kind="writing"),
        EX("U3.5-G2", "True or false", "Read the text again and write T or F.",
           items=["1. Nhung started with 30 books.", "2. She keeps the books in the school library.",
                  "3. Bao counted 4,000 plastic bags in one week.",
                  "4. Bao's grandmother helped him make the bags.",
                  "5. Two other markets copied his idea."],
           answers=["1. T", "2. F – in her family's front room.", "3. F – in one morning.",
                    "4. T", "5. T"], level="M", kind="reading")],
    independent=[
        EX("U3.5-I1", "Retell", "Close the book. Tell your partner about Nhung or Bao in five sentences.",
           items=["Use: name, age, place, problem, action, result."],
           answers=["Model: This is Bao. He is fifteen and he lives in Ha Nam. He counted 4,000 plastic "
                    "bags in the market. He made 200 cloth bags with his grandmother and gave them to "
                    "the sellers. Now most sellers use cloth bags."],
           level="M", kind="speaking"),
        EX("U3.5-I2", "Your report", "Do U3.5-S2 in your group.", items=[],
           answers=["See U3.5-S2."], level="D", kind="speaking")],
    review=["Reading: gist → detail → inference", "Sequence words for a past story",
            "Past simple in connected speech"],
    homework=[
        EX("U3.5-H1", "Reading", "Answer in full sentences.",
           items=["1. What did Nhung see after the flood?", "2. How many books does the book bank have now?",
                  "3. What did Bao do with the 200 cloth bags?",
                  "4. What does the writer say in the last paragraph?"],
           answers=["1. She saw that many children in her street had lost their school books.",
                    "2. More than 1,200.", "3. He gave them free to the sellers in the market.",
                    "4. That they are not rich or famous: they started small and did not stop."],
           level="M", kind="reading"),
        EX("U3.5-H2", "Vocabulary", "Complete with achievement, local, flood, victims, proud.",
           items=["1. The ______ people helped us carry the boxes.",
                  "2. We sent warm clothes to the ______ victims.",
                  "3. Our biggest ______ was the new library.",
                  "4. My parents are ______ of me.", "5. The flood ______ lost everything."],
           answers=["1. local", "2. flood", "3. achievement", "4. proud", "5. victims"],
           level="E", kind="vocab"),
        EX("U3.5-H3", "Writing", "Write your report (70–90 words) with sequence words.",
           items=[], answers=["See U3.5-W1 model."], level="D", kind="writing", lines=10),
        EX("U3.5-H4", "Speaking", "Practise your report three times. Time it: 60–90 seconds.",
           items=["Mark the pauses (/) after First, Then, Finally."],
           answers=["Reports in Lesson 6."], level="M", kind="speaking")],
    workbook=[
        EX("U3.5-P1", "Vocabulary match", "Match the word with the meaning.",
           items=["1. achievement", "2. victim", "3. local", "4. difference", "5. grateful",
                  "a. of this area", "b. a person hurt by something bad", "c. thankful",
                  "d. something good you did", "e. a change that you can see"],
           answers=["1–d", "2–b", "3–a", "4–e", "5–c"], level="E", kind="vocab"),
        EX("U3.5-P2", "Reading", "Read and answer.",
           text=["Last year, the students of class 7B in Vinh started a 'Sunday English Club' for "
                 "primary children in their neighbourhood. Every Sunday morning, six students teach "
                 "simple English words with games and songs. The classes are free. At first only four "
                 "children came. Now there are twenty-eight, and two parents have joined to help. "
                 "'We are not teachers,' says Linh, 13, 'but we remember how hard the first year of "
                 "English was.'"],
           items=["1. Who started the club?", "2. When do the classes take place?",
                  "3. How many children came at first, and how many come now?",
                  "4. Why did they start it?"],
           answers=["1. The students of class 7B in Vinh.", "2. Every Sunday morning.",
                    "3. Four at first; twenty-eight now.",
                    "4. Because they remember how hard the first year of English was."],
           level="M", kind="reading"),
        EX("U3.5-P3", "Sequence words", "Rewrite the story adding First, Then, After that, Finally.",
           items=["We met at school. We walked to the beach. We collected six bags of litter. "
                  "We took a photo together."],
           answers=["First, we met at school. Then we walked to the beach. After that, we collected six "
                    "bags of litter. Finally, we took a photo together."], level="M", kind="writing"),
        EX("U3.5-P4", "Writing", "Write a paragraph (80–90 words) about a community activity you know. "
           "Use four sequence words and six past verbs.",
           items=[], answers=["Model: Last summer the young people in my village cleaned the pond behind "
                              "the pagoda. First, we made a plan with the head of the village. Then, on "
                              "Saturday morning, about thirty people came with buckets and nets. "
                              "We took out the plastic bags and the old bottles. After that, the men "
                              "cut the grass around the water. Finally, we planted six small trees. "
                              "The pond looked completely different, and everybody was proud. (86 words)"],
           level="D", kind="writing", lines=10)],
    procedure=[
        ST("Warm-up: Past questions bingo", 5,
           ["Students write four past activities. Teacher asks 'Did you…?' questions; students cross out."],
           "Answer and cross out.", "Whole class", "Slide 2"),
        ST("Pre-reading", 6,
           ["Show two photos (a book shelf, cloth bags). Predict what the text is about.",
            "Pre-teach: flood, victim, belong to, copy. Set the 60-second gist task."],
           "Predict; skim for the title.", "Whole class", "Slides 3–4"),
        ST("While-reading", 13,
           ["Table task (R2) individually, then pair-check.", "R3 words from context, R4 inference in pairs.",
            "Feedback with the text on screen; underline the evidence for each answer."],
           "Read and complete all three tasks.", "Individual → pairs", "Slides 5–7"),
        ST("Post-reading: retell", 5, ["Books closed; A tells about Nhung, B about Bao."],
           "Retell from memory.", "Pairs", "Slide 8"),
        ST("Speaking: report a past event", 12,
           ["Play the radio report; students order the events and hear the sequence words.",
            "Students make notes (3 min) and give a 60–90-second report in groups of four; "
            "listeners ask two questions each."],
           "Listen, note, report, question.", "Individual → groups of 4", "Slides 9–11"),
        ST("Wrap-up and homework", 4, ["One best report to the class. Set H1–H4."],
           "Listen; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[
        TK("Teaching sequence words",
           ["Listen to two students. Student A: 'We went and we collected and we washed and we sold and "
            "we gave.' … Are you still with me? No. Everything is 'and'.",
            "Student B: 'First, we collected the bottles. Then we washed them. Finally, we sold them.' "
            "Now I can follow, because the words give me signposts.",
            "Four signposts: First / Then / After that / Finally. Use them in every story from today."]),
        TK("Building confidence for reports",
           ["Nobody speaks perfectly for ninety seconds. Not in English, not in Vietnamese.",
            "If you forget a word, say 'the thing for…' and continue. If you stop, look at your notes, "
            "breathe, and start again with 'Then…'.",
            "Your group must ask two questions each. That means they must listen. That is a gift for "
            "the speaker."])],
    support=["Give the table with three cells filled in.",
             "Provide a report skeleton with the sequence words and gaps.",
             "Let weaker students report about the text (Nhung or Bao) instead of their own event."],
    challenge=["Ask for 'At first… but in the end…' in the report.",
               "Ask them to summarise the article in three sentences.",
               "Ask them to be the interviewer and ask four follow-up questions."],
    assessment=["Table task 8 of 12 cells", "Uses at least three sequence words in the report",
                "Past simple accuracy in the report"],
    board_plan=["LEFT: 4 new words", "CENTRE: First / Then / After that / Finally",
                "RIGHT: report plan 1–5; Homework H1–H4"],
    materials=["Reading text", 'Recording: Lesson 29: A Long Time Ago — VOA Learning English — Let’s Learn English, Level 1 (3:20)', "Timer"],
)

L6 = Lesson(
    code="U3L6", unit=3, number=6, period=22,
    lesson_type="Skills 2", title="Listening: A clean-up day + Writing: A diary entry",
    objectives=["listen to a report and complete a table of facts",
                "understand the layout and language of a diary entry",
                "write a diary entry of 80–100 words about a past day",
                "check writing with a checklist and correct a partner's work"],
    recycled=["U3L1–L5: community vocabulary, past simple, sequence words; "
              "Units 1–2: paragraph structure, email layout"],
    vocab=[
        V("diary", "n", "/ˈdaɪəri/", "nhật ký", "I write in my diary every evening."),
        V("exhausted", "adj", "/ɪɡˈzɔːstɪd/", "kiệt sức", "We were exhausted but happy."),
        V("worth it", "adj phr", "/wɜːθ ɪt/", "đáng công", "It was hard work, but it was worth it."),
        V("succeed", "v", "/səkˈsiːd/", "thành công", "We succeeded in cleaning the whole beach."),
        V("organise", "v", "/ˈɔːɡənaɪz/", "tổ chức", "Our teacher organised the trip."),
        V("altogether", "adv", "/ˌɔːltəˈɡeðə/", "tổng cộng", "Altogether we filled 42 bags."),
    ],
    phrases=["I'll never forget…", "The best part was…", "It was tiring, but…",
             "We started at… and finished at…", "Altogether we…"],
    grammar=G("Diary entry: layout and language (writing focus)",
              use=["Start with the DATE (and sometimes the weather / your mood).",
                   "Write in the PAST SIMPLE — a diary is about a finished day.",
                   "Use 'I' and 'we'; a diary is personal and can be informal.",
                   "Order the events with sequence words, and finish with your feeling."],
              form=[["Part", "Example"],
                    ["Date", "Sunday, 12 November"],
                    ["Opening", "Today was one of the busiest days of the year."],
                    ["Events (past simple + sequence)", "First, we met at school at seven. Then…"],
                    ["Details / numbers", "Altogether we collected 42 bags of litter."],
                    ["Feeling / closing", "I was exhausted, but it was worth it. I'll never forget today."]],
              examples=["Saturday, 3 June. Today our class cleaned the beach.",
                        "I was exhausted, but I felt really proud of our class."],
              pitfall="Students write a diary in the present ('Today I go to the beach and I clean'). "
                      "A diary is written in the EVENING about a FINISHED day — past simple.",
              note="Feelings vocabulary: tired, exhausted, proud, happy, surprised, disappointed."),
    pron=P("Linking words together in fast speech",
           "In natural English, a final consonant joins the next vowel: 'picked_up' → /pɪktʌp/, "
           "'cleaned_it' → /kliːndɪt/, 'a lot_of' → /əlɒtəv/.",
           items=["picked up", "cleaned it", "a lot of litter", "filled it up", "worked all day"],
           drill=["We picked up a lot of litter.", "We cleaned it and filled it up.",
                  "We worked all day and finished at four."],
           vn_note="Vietnamese words are separated clearly, so learners speak in blocks. "
                   "Linking is what makes listening hard — practising it also improves listening."),
    listening=AUDIO['U3L6'],
    reading=T("Model diary entry",
              ["Sunday, 12 November",
               "Today was one of the busiest days of the year, but also one of the best.",
               "First, we met at the school gate at half past six. I was still half asleep! Then our "
               "teacher divided us into six groups and we walked to the beach. We started work at seven, "
               "when the air was still cool.",
               "After nine o'clock it became really hot. We picked up bottles, plastic bags, cans and "
               "even an old fishing net. Altogether we filled 42 bags. At eleven the ward committee "
               "arrived with cold water and bread — that was a lovely surprise.",
               "We finished at half past twelve and took a photo together. When I got home I was "
               "exhausted and I slept for two hours.",
               "But this morning I walked past the beach and it was clean and beautiful. It was hard "
               "work, but it was worth it. I'll never forget today."],
              tasks=[
                  EX("U3.6-R1", "Analyse the model", "Answer the questions about the diary entry.",
                     items=["1. What is written on the first line?",
                            "2. Which tense is used almost everywhere?",
                            "3. Find three sequence words.",
                            "4. Which sentence gives numbers?",
                            "5. How does the writer finish the entry?"],
                     answers=["1. The date (Sunday, 12 November).", "2. The past simple.",
                              "3. First, Then, After (nine o'clock) — also 'this morning'.",
                              "4. 'Altogether we filled 42 bags.'",
                              "5. With her feelings: 'It was worth it. I'll never forget today.'"],
                     level="M", kind="reading")]),
    speaking=[EX("U3.6-S1", "Tell it before you write", "Tell your partner your diary story aloud "
                 "in five sentences before writing.",
                 items=["Use: First… Then… After that… Finally… I felt…"],
                 answers=["Speaking first improves the writing. Do not skip this stage."],
                 level="M", kind="speaking")],
    writing=[
        EX("U3.6-W1", "Plan your diary entry", "Complete the plan.",
           items=["Date: ______", "Opening sentence: ______", "Event 1 (First,…): ______",
                  "Event 2 (Then,…): ______", "Event 3 (After that,…): ______",
                  "A number or detail: ______", "Feeling / closing: ______"],
           answers=["Check every plan before students write."], level="M", kind="writing", lines=8),
        EX("U3.6-W2", "Write your diary entry", "Write 80–100 words about a day when you helped "
           "someone or took part in an activity.",
           items=[],
           answers=["Model: Saturday, 8 April. Today my class visited the home for elderly people near "
                    "the market. First, we met at school at eight and walked there together. Then we "
                    "sang three songs — my hands were shaking at the beginning! After that, we sat with "
                    "the old people and listened to their stories. One grandmother told me about the war "
                    "and I nearly cried. Altogether we spent three hours there. We cleaned the yard "
                    "before we left. I was tired, but I felt happy. We will go again in June. (95 words)"],
           level="D", kind="writing", lines=14),
        EX("U3.6-W3", "Peer check", "Swap books and tick the checklist.",
           items=["□ date on the first line", "□ past simple everywhere", "□ at least three sequence words",
                  "□ one number or detail", "□ a feeling at the end", "□ 80–100 words",
                  "□ -ed spelling correct"],
           answers=["Write one thing you liked and one thing to improve."], level="M", kind="writing")],
    communication={"function": "Sharing an experience and reacting to it",
                   "phrases": ["You'll never guess what happened!", "Really? What did you do then?",
                               "That sounds hard!", "How did you feel?", "Good for you!"],
                   "roleplay": "Read your diary entry to your partner as a story. Your partner must "
                               "react three times and ask one question.",
                   "real_life": "Telling a friend about your day; writing a personal journal."},
    guided=[
        EX("U3.6-G1", "Order the diary entry", "Number the sentences 1–6.",
           items=["___ Then we walked to the old people's home.",
                  "___ Saturday, 8 April",
                  "___ I was tired, but I felt very happy.",
                  "___ First, we met at school at eight o'clock.",
                  "___ Today my class did something special.",
                  "___ After that, we sang three songs and listened to their stories."],
           answers=["3, 1, 6, 2, 5(→ position 2 after date? see model), 4 → Correct order: "
                    "Saturday, 8 April / Today my class did something special. / First, we met at school "
                    "at eight o'clock. / Then we walked to the old people's home. / After that, we sang "
                    "three songs and listened to their stories. / I was tired, but I felt very happy."],
           level="E", kind="writing"),
        EX("U3.6-G2", "Past or present?", "Correct the diary sentences.",
           items=["1. Today I go to the beach with my class.", "2. We collect 42 bags of litter.",
                  "3. I am very tired in the evening.", "4. The committee brings us cold water.",
                  "5. It is hard work but it is worth it."],
           answers=["1. Today I went to the beach with my class.", "2. We collected 42 bags of litter.",
                    "3. I was very tired in the evening.", "4. The committee brought us cold water.",
                    "5. It was hard work but it was worth it."],
           level="M", kind="grammar",
           note="A diary describes a finished day → past simple everywhere.")],
    independent=[
        EX("U3.6-I1", "Write your entry", "Do U3.6-W1 and W2.", items=[],
           answers=["See U3.6-W2 model."], level="D", kind="writing", lines=14),
        EX("U3.6-I2", "Read and react", "Read your entry to your partner. Your partner reacts and asks "
           "one question.", items=[], answers=["See communication section."], level="M", kind="speaking")],
    review=["Note-taking with numbers", "Diary layout: date – events in past simple – feeling",
            "Linking in fast speech"],
    homework=[
        EX("U3.6-H1", "Listening / vocabulary", "Complete from the report.",
           items=["1. They met at ______ past six.", "2. ______ students came.",
                  "3. They filled ______ bags.", "4. Hoa felt ______ when she got home.",
                  "5. She said: 'It was hard work, but it was ______ it.'"],
           answers=["1. half", "2. 38", "3. 42", "4. exhausted", "5. worth"],
           level="E", kind="listening"),
        EX("U3.6-H2", "Grammar", "Put the diary into the past simple.",
           text=["Today our club visits the children's hospital. We take 60 books and some toys. "
                 "We read stories and the children sing for us. I am very moved."],
           items=["Rewrite the four sentences in the past."],
           answers=["Today our club visited the children's hospital. We took 60 books and some toys. "
                    "We read (/red/) stories and the children sang for us. I was very moved."],
           level="M", kind="grammar"),
        EX("U3.6-H3", "Writing", "Rewrite your diary entry neatly after correction and hand it in.",
           items=["Use the 7-point checklist."],
           answers=["Mark out of 10: content 3, past simple 3, organisation 2, vocabulary 1, length 1."],
           level="D", kind="writing", lines=14),
        EX("U3.6-H4", "Speaking", "Read your diary entry aloud twice, linking the words: "
           "picked_up, cleaned_it, a lot_of.", items=[], answers=["Spot-check in Lesson 7."],
           level="E", kind="pron")],
    workbook=[
        EX("U3.6-P1", "Diary parts", "Write D (date), O (opening), E (event), F (feeling).",
           items=["1. Sunday, 12 November ___", "2. Today was a busy day. ___",
                  "3. First, we met at the gate. ___", "4. I was exhausted but proud. ___",
                  "5. Then we walked to the beach. ___"],
           answers=["1. D", "2. O", "3. E", "4. F", "5. E"], level="E", kind="writing"),
        EX("U3.6-P2", "Complete the diary", "Use the past simple of the verbs in the box.",
           wordbank=["meet", "walk", "collect", "eat", "feel", "be"],
           items=["Saturday, 5 May. Today (1) ______ a wonderful day. We (2) ______ at the pagoda at "
                  "seven. Then we (3) ______ to the river and (4) ______ ten bags of litter. "
                  "At twelve we (5) ______ lunch under the trees. I (6) ______ tired but very happy."],
           answers=["1. was", "2. met", "3. walked", "4. collected", "5. ate", "6. felt"],
           level="M", kind="grammar"),
        EX("U3.6-P3", "Add the details", "Rewrite each sentence with a number or detail.",
           items=["1. We collected some litter. →", "2. Many students came. →",
                  "3. We worked for a long time. →", "4. We were tired. →"],
           answers=["Model: 1. We collected 42 bags of litter. 2. Altogether 38 students came. "
                    "3. We worked from seven until half past twelve. 4. I was so exhausted that I slept "
                    "for two hours."], level="M", kind="writing"),
        EX("U3.6-P4", "Writing", "Write a diary entry (80–100 words) about the day your class did "
           "something for other people.",
           items=["Date – opening – three events with sequence words – one number – feeling."],
           answers=["See U3.6-W2 model."], level="D", kind="writing", lines=14)],
    procedure=[
        ST("Warm-up: Yesterday chain", 5,
           ["'Yesterday I…' chain round the class; each student repeats the previous sentence in the "
            "third person, then adds their own."],
           "Repeat and add past sentences.", "Rows", "Slide 2"),
        ST("Pre-listening", 5,
           ["Show the table. Pre-teach: exhausted, worth it, ward committee, altogether.",
            "Predict what numbers will appear."],
           "Predict; copy the table.", "Whole class", "Slides 3–4"),
        ST("Listening", 11,
           ['Play the recording “Lesson 28: I Passed It!” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.',
            "Pair-check, then whole-class check with the script on screen."],
           "Listen and complete the table; check.", "Individual → pairs", "Slide 5"),
        ST("Writing: analyse the model diary", 7,
           ["Model diary on the slide. Elicit the five parts and colour them.",
            "Do U3.6-G1 (order) and G2 (past correction)."],
           "Identify the parts; order and correct.", "Whole class → pairs", "Slides 6–7"),
        ST("Writing: plan, say, draft", 12,
           ["Students complete the plan; check every plan. Then they TELL the story to a partner (U3.6-S1).",
            "Write 80–100 words in silence. Monitor and help with vocabulary only."],
           "Plan, tell, write.", "Individual → pairs → individual", "Slide 8"),
        ST("Peer check and wrap-up", 5,
           ["Swap and use the 7-point checklist; read one good entry aloud. Set H1–H4."],
           "Peer-check; listen.", "Pairs", "Slides 9–10")],
    teacher_talk=[
        TK("Why a diary must be in the past",
           ["You write your diary in the evening. The day is FINISHED. It is gone.",
            "So every verb goes into the past: I went, we collected, it was.",
            "If you write 'Today I go to the beach', you are telling me the future or a habit — "
            "not what happened.",
            "Check your entry at the end: put a circle round every verb. Is it past? Good."]),
        TK("Adding detail to make writing come alive",
           ["Two sentences. A: 'We collected some litter.' B: 'Altogether we filled 42 bags — "
            "including one old shoe.'",
            "Which one do you want to read? B, of course. Numbers and small strange details make "
            "writing real.",
            "In your entry I want at least ONE number and ONE small detail that only you know."])],
    support=["Give the table with three answers filled in.",
             "Give a diary frame with sentence starters.",
             "Allow 60–80 words."],
    challenge=["Ask for 110–120 words with direct speech ('One grandmother said, \"…\"').",
               "Ask for two feelings — at the beginning and at the end.",
               "Ask them to write the entry from a parent's or a teacher's point of view."],
    assessment=["6 of 8 items in the listening table", "Diary has date, past simple and a feeling",
                "At least three sequence words used correctly"],
    board_plan=["LEFT: listening table", "CENTRE: the five parts of a diary entry",
                "RIGHT: feelings vocabulary; Homework H1–H4"],
    materials=['Recording: Lesson 28: I Passed It! — VOA Learning English — Let’s Learn English, Level 1 (3:18)', "Model diary on a slide", "Checklist cards"],
)

L7 = Lesson(
    code="U3L7", unit=3, number=7, period=23,
    lesson_type="Looking Back & Project", title="Unit 3 review and Our Community Service Plan",
    objectives=["recall the community vocabulary of Unit 3",
                "use the past simple accurately in all three forms",
                "correct the six typical mistakes of the unit",
                "plan and present a real community service activity"],
    recycled=["ALL of Unit 3 + Units 1–2 (present simple, frequency, should, imperatives, "
              "paragraph and diary writing)"],
    vocab=[V("plan", "n/v", "/plæn/", "kế hoạch; lên kế hoạch", "Here is our plan for Saturday."),
           V("responsible for", "adj phr", "/rɪˈspɒnsəbl fɔː/", "chịu trách nhiệm", "Nam is responsible for the posters."),
           V("in charge of", "phr", "/ɪn tʃɑːdʒ əv/", "phụ trách", "Mai is in charge of the money.")],
    phrases=["We are going to…", "X is responsible for…", "We will need…", "Our plan is to…"],
    grammar=G("Unit 3 grammar in one page",
              use=["Past simple positive: regular + ed / irregular forms",
                   "Negative: didn't + bare verb", "Question: Did + subject + bare verb?",
                   "be: was / were, wasn't / weren't"],
              form=[["Structure", "Example", "Common mistake"],
                    ["regular past", "We cleaned the park.", "*We clean the park yesterday."],
                    ["irregular past", "They went to the village.", "*They goed to the village."],
                    ["didn't + bare verb", "I didn't finish.", "*I didn't finished."],
                    ["Did + bare verb?", "Did you help?", "*Did you helped?"],
                    ["was / were", "It was hot. They were tired.", "*It did be hot."]],
              examples=["Last Sunday our class went to the beach. We collected 42 bags of litter. "
                        "We didn't finish before twelve, but nobody complained."],
              pitfall="Add the Unit 3 errors to the classroom wall list. The 'did + past verb' error "
                      "will return for months — keep pointing at the box."),
    pron=P("Unit 3 sounds review: -ed endings and linking",
           "Three checks: is the -ed there? is it the right sound? do the words link?",
           items=["/t/ helped, worked, washed", "/d/ cleaned, played, carried",
                  "/ɪd/ visited, painted, donated", "picked_up, cleaned_it"],
           drill=["We helped, cleaned and painted, and we picked up a lot of litter."],
           vn_note="Check -ed endings in Review 1 (after this unit) and in every speaking assessment."),
    listening=AUDIO['U3L7'],
    reading=T("What happened after the project",
              ["Three months after class 7A collected 214 books for the Sunflower Children's Home, "
               "something unexpected happened.",
               "The children at the home wrote 214 thank-you letters — one for every book. They sent "
               "them to the school in a big box. The head teacher read three of them at the Monday "
               "assembly and the whole school was silent.",
               "After that, two other classes started their own projects. Class 7B collected warm "
               "clothes and class 8A repaired old bicycles. Altogether, in one term, the school helped "
               "four different places.",
               "'We only wanted to give some books,' said Khang. 'We didn't know it would grow like this.'"],
              tasks=[EX("U3.7-R1", "Read and answer", "Answer the questions.",
                        items=["1. How many letters did the children write? Why that number?",
                               "2. What did the head teacher do?",
                               "3. What did classes 7B and 8A do?",
                               "4. What does Khang mean in the last sentence?"],
                        answers=["1. 214 — one for every book.",
                                 "2. He read three of the letters at the Monday assembly.",
                                 "3. 7B collected warm clothes; 8A repaired old bicycles.",
                                 "4. That a small action grew into something much bigger than they "
                                 "expected."], level="M", kind="reading")]),
    speaking=[EX("U3.7-S1", "Present your plan", "Present your community service plan for two minutes. "
                 "Everyone in the group speaks.",
                 items=["Frame: 'Our plan is to… The problem in our area is… First, we are going to… "
                        "Nam is responsible for… We will need… Thank you for listening.'"],
                 answers=["Marking: content 3, language 3, poster 2, presentation 2."],
                 level="D", kind="speaking")],
    writing=[EX("U3.7-W1", "Write the plan", "Write your group's plan on the poster.",
                items=["What / Where / When / Who does what / What we need (5 sentences)",
                       "Plus 2 sentences about a similar activity that someone did before (past simple)."],
                answers=["Model: Our plan is to clean the pond behind the pagoda on Sunday 15 October. "
                         "Nam and Duy are responsible for the tools. Mai is in charge of the drinks. "
                         "We will need six nets and twenty bags. Last year the young people in the "
                         "village cleaned the same pond and it stayed clean for six months."],
                level="M", kind="writing", lines=8)],
    communication={"function": "Presenting a plan",
                   "phrases": ["Our plan is to…", "We are going to…", "X is responsible for…",
                               "We will need…", "Does anyone have a question?"],
                   "roleplay": "Present the plan to the 'school committee' (the rest of the class), "
                               "who ask two questions each.",
                   "real_life": "Proposing an idea to a group and answering questions about it."},
    guided=[
        EX("U3.7-G1", "Vocabulary race", "Write the word.",
           items=["1. a person who works without money: ______", "2. rubbish on the ground: ______",
                  "3. to use something again: ______", "4. a home for children with no parents: ______",
                  "5. to give money or things: ______", "6. people who lost their homes in a flood: ______"],
           answers=["1. a volunteer", "2. litter", "3. recycle", "4. an orphanage", "5. donate",
                    "6. flood victims"], level="E", kind="vocab"),
        EX("U3.7-G2", "Error clinic – the six Unit 3 mistakes", "Correct one mistake in each sentence.",
           items=["1. Yesterday we clean the park.", "2. They goed to the orphanage.",
                  "3. I didn't finished my work.", "4. Did you went to the meeting?",
                  "5. It did be very hot.", "6. She visit her grandmother last week."],
           answers=["1. Yesterday we cleaned the park.", "2. They went to the orphanage.",
                    "3. I didn't finish my work.", "4. Did you go to the meeting?",
                    "5. It was very hot.", "6. She visited her grandmother last week."],
           level="D", kind="grammar",
           note="Numbers 3 and 4 are the same rule: after did/didn't the verb is bare.")],
    independent=[
        EX("U3.7-I1", "Mixed review", "Complete the text with the past simple.",
           text=["Last term our class (1. want) ______ to do something useful. We (2. make) ______ a plan "
                 "and (3. collect) ______ old books from every class. We (4. not have) ______ enough "
                 "boxes, so our teacher (5. buy) ______ ten. On 20 October we (6. take) ______ 214 books "
                 "to a children's home. The children (7. be) ______ very happy and they (8. write) ______ "
                 "us letters."],
           items=["Write the eight verbs."],
           answers=["1. wanted", "2. made", "3. collected", "4. didn't have", "5. bought", "6. took",
                    "7. were", "8. wrote"], level="M", kind="grammar"),
        EX("U3.7-I2", "Project work", "Make your plan poster and prepare the presentation.",
           items=[], answers=["Check the sentences before they go on the poster."],
           level="D", kind="mixed")],
    review=["Community and volunteering vocabulary (22 items)", "Past simple: all three forms",
            "Irregular verbs (12)", "-ed sounds", "Sequence words", "Diary and report writing"],
    homework=[
        EX("U3.7-H1", "Vocabulary", "Write 10 words from Unit 3 with their Vietnamese meanings.",
           items=[], answers=["Any 10 of the unit's items."], level="E", kind="vocab"),
        EX("U3.7-H2", "Grammar", "Choose the correct answer.",
           items=["1. We (clean / cleaned) the beach last Sunday.",
                  "2. They (didn't go / didn't went) to the meeting.",
                  "3. (Did / Do) you help your neighbour yesterday?",
                  "4. She (buyed / bought) new books.", "5. It (was / were) a hot day.",
                  "6. The students (was / were) very tired."],
           answers=["1. cleaned", "2. didn't go", "3. Did", "4. bought", "5. was", "6. were"],
           level="M", kind="grammar"),
        EX("U3.7-H3", "Writing", "Write a diary entry (90–100 words) about a day you helped someone.",
           items=["Date – opening – three events with sequence words – a number – a feeling."],
           answers=["See U3.6-W2 model."], level="D", kind="writing", lines=14),
        EX("U3.7-H4", "Prepare for Unit 4", "Write the names of five kinds of music or art in "
           "Vietnamese or English.",
           items=[], answers=["Any reasonable answers (nhạc pop, cải lương, hội họa, múa rối nước…). "
                              "Use them to start Unit 4."], level="E", kind="vocab")],
    workbook=[
        EX("U3.7-P1", "Crossword clues", "Write the word.",
           items=["1. Rubbish on the ground. (6)", "2. A person who helps for free. (9)",
                  "3. To give things to people in need. (6)", "4. Water covering the land. (5)",
                  "5. To use again. (7)"],
           answers=["1. litter", "2. volunteer", "3. donate", "4. flood", "5. recycle"],
           level="E", kind="vocab"),
        EX("U3.7-P2", "Mixed grammar", "Put the words in order.",
           items=["1. beach / we / last Sunday / cleaned / the",
                  "2. didn't / they / the meeting / come / to",
                  "3. you / did / what / do / yesterday / ?",
                  "4. were / the students / very / tired",
                  "5. books / 214 / donated / class 7A"],
           answers=["1. We cleaned the beach last Sunday.", "2. They didn't come to the meeting.",
                    "3. What did you do yesterday?", "4. The students were very tired.",
                    "5. Class 7A donated 214 books."], level="M", kind="grammar"),
        EX("U3.7-P3", "Reading review", "Read and choose.",
           text=["Volunteering is good for the people you help — but it is also good for you. Studies "
                 "show that young volunteers make more friends, feel less worried and often do better "
                 "at school. The reason is simple: when you help someone, you feel useful, and a "
                 "person who feels useful has more confidence. You do not need a lot of time. "
                 "Two hours a month is enough to change the way you see yourself."],
           items=["1. The text is mainly about A. how to find a volunteer job  "
                  "B. why volunteering helps the volunteer  C. school marks",
                  "2. Young volunteers often A. sleep more  B. make more friends  C. earn money",
                  "3. The text says ___ a month is enough. A. two hours  B. two days  C. twenty hours"],
           answers=["1. B", "2. B", "3. A"], level="M", kind="reading"),
        EX("U3.7-P4", "Unit 3 test yourself (10 marks)", "Answer about yourself (2 marks each).",
           items=["1. One community activity you did: ______",
                  "2. When and where: ______",
                  "3. One thing you didn't do (negative sentence): ______",
                  "4. A question to ask a volunteer: ______",
                  "5. How you felt: ______"],
           answers=["Model: 1. I helped my neighbour clean her yard. 2. Last Sunday, in my street. "
                    "3. I didn't finish before lunch. 4. How long did you work there? "
                    "5. I was tired but proud."], level="D", kind="mixed")],
    procedure=[
        ST("Warm-up: Irregular verb bingo", 6,
           ["Students write nine past forms in a 3×3 grid. Teacher says the base verb; students cross "
            "out the past form."],
           "Play bingo with irregular verbs.", "Whole class", "Slide 2"),
        ST("Vocabulary and listening review", 7,
           ["U3.7-G1 race, then the listening quiz U3.7-L1."],
           "Write the words; write the past verbs from dictation.", "Pairs", "Slides 3–4"),
        ST("Grammar review + error clinic", 10,
           ["Grammar table on the board; U3.7-G2 in pairs with explanations.",
            "Add the six errors to the wall list."],
           "Correct and explain the six errors.", "Pairs → whole class", "Slides 5–7"),
        ST("Mixed practice", 6, ["U3.7-I1 gap-fill; fast finishers do Workbook P2."],
           "Complete the text.", "Individual", "Student Book p. U3L7"),
        ST("Project: Community Service Plan", 12,
           ["Groups of four: problem → what/where/when → who does what → what we need → two past examples.",
            "Two or three groups present to the 'school committee'; the class votes for one plan.",
            "If possible, arrange to really carry out the winning plan."],
           "Plan, write, present, vote.", "Groups of 4", "Slides 8–10"),
        ST("Wrap-up and homework", 4,
           ["Announce the winning plan and set a date. Set H1–H4 including Unit 4 preparation."],
           "Note the plan and the homework.", "Whole class", "Slide 12")],
    teacher_talk=[
        TK("Making the project real",
           ["This is not only a poster. If we choose a good plan, we will really do it.",
            "So be realistic. 'We will build a school' — beautiful, but impossible for us.",
            "'We will clean the pond behind the pagoda on Sunday morning' — small, clear, possible. "
            "That is a good plan.",
            "Every plan must answer four questions: WHAT, WHERE, WHEN, WHO."]),
        TK("Reviewing the past simple one last time",
           ["Point at the box on the board. Say it with me: DID takes the past away from the verb.",
            "Now look at your own writing from last week. Find one sentence with a past verb. "
            "Check it. Is the -ed there? Is the irregular form right?",
            "You are now your own teacher. That is the goal."])],
    support=["Give the bingo grid with the past forms printed.",
             "Give the error clinic with the mistakes underlined.",
             "Assign one short sentence in the presentation."],
    challenge=["Ask them to write three new error sentences for the class.",
               "Ask them to be the group leader and answer the committee's questions.",
               "Ask for a 120-word diary entry in H3."],
    assessment=["Unit 3 checklist: 5 of 6 'I can' statements", "Error clinic 5 of 6 correct",
                "Speaks 30 seconds in the presentation"],
    board_plan=["LEFT: bingo verbs", "CENTRE: Unit 3 grammar table + DID box",
                "RIGHT: project questions WHAT/WHERE/WHEN/WHO; Homework H1–H4"],
    materials=["Poster paper", "Bingo grids", 'Recording: Looking Back — listen again (replay — see the lesson page)'],
)

UNIT.lessons = [L1, L2, L3, L4, L5, L6, L7]

UNIT.revision = [
    EX("R3-1", "Vocabulary", "Complete with a word from Unit 3.",
       items=["1. A person who works without pay is a v______ .",
              "2. Please don't drop l______ in the park.",
              "3. We r______ paper, glass and plastic.",
              "4. The children live in an o______ .",
              "5. They gave clothes to the flood v______ .",
              "6. Small actions can make a big d______ ."],
       answers=["1. volunteer", "2. litter", "3. recycle", "4. orphanage", "5. victims", "6. difference"],
       level="E", kind="vocab"),
    EX("R3-2", "Grammar: past simple", "Complete with the past simple.",
       items=["1. We (clean) ______ the beach last Sunday.", "2. They (not go) ______ to the meeting.",
              "3. ______ she (donate) ______ the books?", "4. He (buy) ______ ten boxes.",
              "5. The students (be) ______ very tired.", "6. I (not have) ______ enough time."],
       answers=["1. cleaned", "2. didn't go", "3. Did … donate", "4. bought", "5. were", "6. didn't have"],
       level="M", kind="grammar"),
    EX("R3-3", "Pronunciation", "Put the verbs into the correct group: /t/, /d/, /ɪd/.",
       items=["helped, cleaned, visited, washed, played, painted, worked, donated, carried, stopped"],
       answers=["/t/: helped, washed, worked, stopped", "/d/: cleaned, played, carried",
                "/ɪd/: visited, painted, donated"], level="M", kind="pron"),
    EX("R3-4", "Reading", "Read and answer.",
       text=["In 2023 a group of 15 students in Hue started 'Sunday Bicycles'. They collected old, "
             "broken bicycles from their neighbours, repaired them at the weekend and gave them to "
             "children who walked more than five kilometres to school. In the first year they repaired "
             "38 bicycles. 'The hardest part was not the work,' says Duc, the leader. 'It was asking "
             "people for their old bicycles. We were shy at the beginning.'"],
       items=["1. When and where did the group start?", "2. What did they do with the old bicycles?",
              "3. Who received the bicycles?", "4. How many bicycles did they repair in the first year?",
              "5. What was the hardest part, and why?"],
       answers=["1. In 2023, in Hue.", "2. They repaired them at the weekend.",
                "3. Children who walked more than five kilometres to school.", "4. 38.",
                "5. Asking people for their old bicycles, because they were shy at the beginning."],
       level="M", kind="reading"),
    EX("R3-5", "Writing", "Write a diary entry (80–100 words) about a day when your class or family "
       "helped other people.",
       items=["Date – opening – three events with First / Then / Finally – one number – a feeling."],
       answers=["See U3.6-W2 model answer. Marking: content 3, past simple 3, organisation 2, "
                "vocabulary 1, length 1."], level="D", kind="writing", lines=14),
]
