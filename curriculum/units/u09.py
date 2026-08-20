# -*- coding: utf-8 -*-
"""UNIT 9 – FESTIVALS AROUND THE WORLD  (Periods 61–67)"""
from curriculum.schema import *
from curriculum.audio_sources import AUDIO

UNIT = Unit(
    number=9, title="Festivals Around the World",
    theme="Vietnamese and international festivals, customs, celebrations",
    can_do=["name eight festivals and say when and where they happen",
            "describe what people do at a festival",
            "use a, an, the and no article correctly",
            "ask a range of questions about a festival",
            "read about a festival in another country and compare it with a Vietnamese one",
            "write a description of a festival (100–120 words)"],
    grammar_focus=["Articles: a / an / the / no article",
                   "Question forms review (Wh- and yes/no)"],
    pron_focus="The sounds /θ/ (think) and /ð/ (this)",
    vocab_focus="Festivals, customs and celebration verbs",
    project={"name": "Festival Fair",
             "goal": "Groups present one festival — Vietnamese or foreign — at a class festival fair.",
             "steps": ["Choose a festival that is NOT Tet (too easy!).",
                       "Find or draw four pictures.",
                       "Write six sentences: when and where, what people do (three), what people eat, "
                       "and why it matters.",
                       "Prepare five questions for your visitors, with answers on the back.",
                       "Half the class presents while the other half visits; then swap."],
             "marking": "Content 3 – Language 3 – Display 2 – Presenting/answering 2 (total 10)"})

L1 = Lesson(
    code="U9L1", unit=9, number=1, period=63,
    lesson_type="Getting Started", title="Festivals near and far",
    objectives=["name eight festivals and say when they happen",
                "understand a conversation about a festival",
                "describe what people do at a festival",
                "write three sentences about a festival they know"],
    recycled=["Unit 6 prepositions of time (in/on/at); Unit 3 past simple; Unit 4 superlatives"],
    vocab=[V("festival", "n", "/ˈfestɪvl/", "lễ hội", "The Mid-Autumn Festival is in September."),
           V("celebrate", "v", "/ˈselɪbreɪt/", "kỷ niệm, ăn mừng", "We celebrate Tet with our family."),
           V("lantern", "n", "/ˈlæntən/", "đèn lồng", "Children carry lanterns in the street."),
           V("parade", "n", "/pəˈreɪd/", "cuộc diễu hành", "There is a parade through the town."),
           V("firework", "n", "/ˈfaɪəwɜːk/", "pháo hoa", "The fireworks start at midnight."),
           V("costume", "n", "/ˈkɒstjuːm/", "trang phục", "People wear colourful costumes."),
           V("custom", "n", "/ˈkʌstəm/", "phong tục", "It is a custom to give lucky money."),
           V("decorate", "v", "/ˈdekəreɪt/", "trang trí", "We decorate the house with flowers.")],
    phrases=["It takes place in…", "People celebrate by + V-ing", "It is a custom to…",
             "on the fifteenth day of…", "wish somebody a happy…"],
    grammar=G("Describing a festival: takes place / celebrate / custom",
              use=["WHEN: It takes place in September / on the 15th day of the 8th lunar month.",
                   "WHERE: It is celebrated all over Viet Nam / in the north.",
                   "WHAT PEOPLE DO: People make lanterns, eat mooncakes and watch lion dances.",
                   "WHY: It is a custom to… / People believe that…"],
              form=[["Function", "Language", "Example"],
                    ["when", "It takes place in / on…", "It takes place in April."],
                    ["where", "It is celebrated in…", "It is celebrated all over the country."],
                    ["activities", "People + present simple", "People wear special costumes."],
                    ["custom", "It is a custom to + verb", "It is a custom to give lucky money."]],
              examples=["The Mid-Autumn Festival takes place on the 15th day of the 8th lunar month.",
                        "People celebrate by making lanterns and eating mooncakes."],
              pitfall="*It is happened in September* and *People celebrate Tet by eat banh chung* — "
                      "the correct forms are 'It takes place' and 'by + V-ing'.",
              note="'Celebrate by + V-ing' is a very useful chunk for the whole unit."),
    pron=P("The sounds /θ/ (think) and /ð/ (this)",
           "Put the tip of your tongue between your teeth. /θ/ has no voice — just air: think, three, "
           "thank. /ð/ buzzes: this, that, the, they, mother.",
           items=["/θ/: think, three, thank, month, birthday, north",
                  "/ð/: this, that, the, they, mother, weather",
                  "Compare: think – this | thin – then | three – the"],
           drill=["Thank you for the three lanterns.",
                  "This festival is in the third month.",
                  "They think this is the best month of the year."],
           vn_note="Vietnamese has no /θ/ or /ð/, so learners say 't' or 'd': 'think' → 'tink', "
                   "'this' → 'dis'. The tongue MUST come out between the teeth. Use a mirror."),
    listening=AUDIO['U9L1'],
    reading=T("Four festivals, four countries",
              ["HOLI (India, March). People throw coloured powder and water at each other. "
               "By the end of the day everybody is pink, green and blue — and nobody minds.",
               "LA TOMATINA (Spain, August). For one hour, 20,000 people throw tomatoes in the streets "
               "of a small town. The town uses 150,000 kilos of tomatoes and then cleans everything "
               "with water from fire engines.",
               "HANAMI (Japan, late March or April). Families sit under the cherry trees to look at "
               "the flowers, eat and talk. The flowers last about one week, so people check the "
               "weather forecast every day.",
               "MID-AUTUMN FESTIVAL (Viet Nam, September). Children carry lanterns, lion dancers go "
               "from house to house, and families eat mooncakes under the full moon."],
              tasks=[EX("U9.1-R1", "Read and match", "Which festival?",
                        items=["1. People throw food. ______", "2. People look at flowers. ______",
                               "3. People throw coloured powder. ______",
                               "4. Children carry lanterns. ______",
                               "5. It lasts only one hour. ______"],
                        answers=["1. La Tomatina", "2. Hanami", "3. Holi", "4. Mid-Autumn Festival",
                                 "5. La Tomatina"], level="E", kind="reading"),
                     EX("U9.1-R2", "Read and answer", "Answer the questions.",
                        items=["1. When does Holi take place?",
                               "2. How many kilos of tomatoes are used at La Tomatina?",
                               "3. How long do the cherry flowers last?",
                               "4. Why do Japanese people check the weather forecast?"],
                        answers=["1. In March.", "2. 150,000 kilos.", "3. About one week.",
                                 "4. Because the flowers last only about a week, so they must choose "
                                 "the right day."], level="M", kind="reading")]),
    speaking=[EX("U9.1-S1", "Festival quiz", "In pairs, ask and answer about the four festivals.",
                 items=["A: When does Holi take place?  B: In March. A: What do people do?  "
                        "B: They throw coloured powder."],
                 answers=["Then ask about a Vietnamese festival your partner knows."],
                 level="M", kind="speaking")],
    writing=[EX("U9.1-W1", "Sentence writing", "Write three sentences about a festival you know.",
                items=["1. ______ takes place in ______ .", "2. People celebrate by ______ .",
                       "3. It is a custom to ______ ."],
                answers=["Model: The Hung Kings Festival takes place in April. People celebrate by "
                         "visiting the temple and offering banh chung. It is a custom to climb the "
                         "mountain with your family."], level="M", kind="writing", lines=4)],
    communication={"function": "Explaining your culture to a visitor",
                   "phrases": ["Have you heard of…?", "It's a bit like…", "You must try it.",
                               "It's difficult to explain, but…", "Come and see it yourself!"],
                   "roleplay": "A foreign student asks you about a Vietnamese festival. Answer four "
                               "questions and invite them.",
                   "real_life": "Explaining Vietnamese customs to a foreign visitor."},
    guided=[EX("U9.1-G1", "Match", "Match the word with the meaning.",
               items=["1. lantern", "2. parade", "3. costume", "4. custom", "5. decorate",
                      "a. special clothes for a festival", "b. a light you carry",
                      "c. to make something look beautiful", "d. a traditional way of doing things",
                      "e. people walking through the streets together"],
               answers=["1–b", "2–e", "3–a", "4–d", "5–c"], level="E", kind="vocab"),
            EX("U9.1-G2", "celebrate by + V-ing", "Complete the sentences.",
               items=["1. People celebrate Tet by ______ (visit) their relatives.",
                      "2. Children celebrate the Mid-Autumn Festival by ______ (carry) lanterns.",
                      "3. Families celebrate by ______ (eat) special food.",
                      "4. In Spain people celebrate by ______ (throw) tomatoes."],
               answers=["1. visiting", "2. carrying", "3. eating", "4. throwing"],
               level="M", kind="grammar")],
    independent=[EX("U9.1-I1", "Complete the description", "Use the words in the box.",
                    wordbank=["takes place", "celebrate", "custom", "decorate", "costumes"],
                    items=["The Hue Festival (1) ______ every two years in April. People (2) ______ "
                           "with music, dance and boat races on the Perfume River. Performers wear "
                           "traditional (3) ______ , and the city (4) ______ the streets with lights. "
                           "It is a (5) ______ to invite artists from other countries."],
                    answers=["1. takes place", "2. celebrate", "3. costumes", "4. decorates",
                             "5. custom"], level="M", kind="vocab"),
                 EX("U9.1-I2", "Explain a festival", "Do the visitor role play in pairs.", items=[],
                    answers=["See communication section."], level="D", kind="speaking")],
    review=["8 festival words", "takes place / celebrate by + V-ing / it is a custom to",
            "/θ/ and /ð/"],
    homework=[EX("U9.1-H1", "Vocabulary", "Write the word.",
                 items=["1. a light children carry at Trung Thu: ______",
                        "2. special clothes for a festival: ______",
                        "3. people walking through the streets together: ______",
                        "4. a traditional way of doing something: ______",
                        "5. lights in the sky at midnight: ______",
                        "6. to make a room beautiful: ______"],
                 answers=["1. a lantern", "2. a costume", "3. a parade", "4. a custom",
                          "5. fireworks", "6. decorate"], level="E", kind="vocab"),
              EX("U9.1-H2", "Grammar", "Complete with the correct form.",
                 items=["1. Tet (take) ______ place in January or February.",
                        "2. People celebrate by (give) ______ lucky money.",
                        "3. It is a custom (visit) ______ your grandparents.",
                        "4. Families (decorate) ______ their houses with peach flowers.",
                        "5. Children celebrate by (carry) ______ lanterns."],
                 answers=["1. takes", "2. giving", "3. to visit", "4. decorate", "5. carrying"],
                 level="M", kind="grammar"),
              EX("U9.1-H3", "Writing", "Write 4 sentences about your favourite festival.",
                 items=["When / where / what people do / why you like it."],
                 answers=["Model: My favourite festival is Tet. It takes place in late January or "
                          "February. People clean and decorate their houses, cook banh chung and "
                          "visit their relatives. I like it because the whole family comes home, "
                          "even my uncle who works in Korea."], level="M", kind="writing", lines=5),
              EX("U9.1-H4", "Pronunciation", "Say these words five times with your tongue between "
                 "your teeth: think, three, thank, this, that, they.",
                 items=["Use a mirror — you should SEE the tongue."],
                 answers=["Spot-check in Lesson 2."], level="E", kind="pron")],
    workbook=[EX("U9.1-P1", "Complete the words", "Write the missing letters.",
                 items=["1. f _ s t i v a l", "2. l _ n t e r n", "3. p a r _ d e",
                        "4. c _ s t u m e", "5. c _ s t o m", "6. d e c _ r a t e"],
                 answers=["1. festival", "2. lantern", "3. parade", "4. costume", "5. custom",
                          "6. decorate"], level="E", kind="vocab"),
              EX("U9.1-P2", "Which festival?", "Write the country.",
                 items=["1. Holi: ______", "2. La Tomatina: ______", "3. Hanami: ______",
                        "4. Mid-Autumn Festival: ______"],
                 answers=["1. India", "2. Spain", "3. Japan", "4. Viet Nam"],
                 level="E", kind="reading"),
              EX("U9.1-P3", "/θ/ or /ð/?", "Write the sound.",
                 items=["1. think ___", "2. this ___", "3. three ___", "4. mother ___",
                        "5. birthday ___", "6. they ___", "7. month ___", "8. weather ___"],
                 answers=["1. /θ/", "2. /ð/", "3. /θ/", "4. /ð/", "5. /θ/", "6. /ð/", "7. /θ/",
                          "8. /ð/"], level="M", kind="pron"),
              EX("U9.1-P4", "Correct the mistakes", "One mistake per sentence.",
                 items=["1. Tet is happened in February.",
                        "2. People celebrate by eat special food.",
                        "3. It is a custom giving lucky money.",
                        "4. The festival take place in April.",
                        "5. Children carrying lanterns in the street."],
                 answers=["1. Tet takes place in February.",
                          "2. People celebrate by eating special food.",
                          "3. It is a custom to give lucky money.",
                          "4. The festival takes place in April.",
                          "5. Children carry lanterns in the street."], level="D", kind="grammar"),
              EX("U9.1-P5", "Writing", "Write 5 sentences about a festival in your province or village.",
                 items=["When / where / activities / food / why people love it."],
                 answers=["Model: In my village we have a temple festival in the second lunar month. "
                          "It takes place in the yard of the old temple near the river. People carry "
                          "flags, play traditional drums and hold a cooking competition. "
                          "Everybody eats sticky rice and boiled chicken. Old people say the festival "
                          "keeps the village together, because everybody comes home for it."],
                 level="D", kind="writing", lines=6)],
    procedure=[ST("Warm-up: Festival brainstorm", 5,
                  ["Write FESTIVAL on the board. Students give names (Vietnamese and foreign); "
                   "you write the English."],
                  "Give festival names.", "Whole class", "Slide 2"),
               ST("Presentation: 8 festival words", 9,
                  ["Pictures; elicit and drill with stress: 'FES-ti-val, 'LAN-tern, pa-RADE, "
                   "'COS-tume, 'CUS-tom.",
                   "Build the description frame: takes place / celebrate by V-ing / it is a custom to."],
                  "Repeat; copy the frame.", "Whole class", "Slides 3–5"),
               ST("Pronunciation /θ/ /ð/", 8,
                  ["Model with a mirror or by exaggerating. Students put a finger in front of their "
                   "mouth and must touch the tongue with it.",
                   "Sort words into two columns; drill the three sentences."],
                  "Feel the tongue; sort and repeat.", "Whole class", "Slides 6–7"),
               ST("Listening: Mid-Autumn Festival", 9,
                  ['Play the recording “Lesson 13: Happy Birthday, William Shakespeare!” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; read the script in role.'],
                  "Listen and complete.", "Individual → pairs", "Slide 8"),
               ST("Reading + speaking", 9,
                  ["Read 'Four festivals'; do R1 and R2. Then the festival quiz in pairs."],
                  "Read, answer, ask and answer.", "Individual → pairs", "Slides 9–10"),
               ST("Wrap-up and homework", 5, ["Class vote: which foreign festival would you most like "
                                              "to see? Set H1–H4."],
                  "Vote; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Teaching /θ/ and /ð/",
                     ["This is the hardest pair of sounds in English for Vietnamese speakers — "
                      "and the most famous.",
                      "Put your tongue between your teeth. Yes, really — it must come OUT. "
                      "Now blow: /θ/. Think, three, thank.",
                      "Now the same position, but add your voice: /ð/. This, that, they. Feel the buzz.",
                      "If your tongue stays behind your teeth, 'think' becomes 'tink' and 'they' "
                      "becomes 'day'. Everybody: tongue out. Think. This. Again."]),
                  TK("Celebrate BY + V-ing",
                     ["How do people celebrate Tet? With one useful chunk you can answer any "
                      "festival question.",
                      "People celebrate BY + verb-ING. By visiting. By eating. By giving.",
                      "Not 'by visit', not 'by to visit'. BY + ING.",
                      "Say four with me: by visiting, by eating, by singing, by dancing."])],
    support=["Give picture cards for the eight words.",
             "Provide the description frame on a desk card.",
             "Do the sound sort with six words only."],
    challenge=["Ask for four sentences about a festival with all the frames.",
               "Ask them to compare two festivals with Unit 4 comparatives.",
               "Ask them to explain a Vietnamese custom to a 'foreign visitor'."],
    assessment=["Names 6 of 8 festival words", "Uses 'celebrate by + V-ing' correctly",
                "Tongue visible for /θ/ and /ð/"],
    board_plan=["LEFT: 8 words with stress", "CENTRE: takes place / celebrate by V-ing / custom to",
                "RIGHT: /θ/ | /ð/ columns; Homework H1–H4"],
    materials=["Festival pictures", "Small mirrors if possible", 'Recording: Lesson 13: Happy Birthday, William Shakespeare! — VOA Learning English — Let’s Learn English, Level 1 (2:10)'],
)

L2 = Lesson(
    code="U9L2", unit=9, number=2, period=64,
    lesson_type="A Closer Look 1", title="Festival activities and the sounds /θ/ and /ð/",
    objectives=["use eight verbs and phrases for festival activities",
                "pronounce /θ/ and /ð/ correctly in words and sentences",
                "describe what happens at a festival in sequence",
                "ask three questions about a festival"],
    recycled=["U9L1 festival vocabulary; Unit 3 sequence words; Unit 6 present simple"],
    vocab=[V("take part in", "v phr", "/teɪk pɑːt ɪn/", "tham gia", "Thousands take part in the parade."),
           V("perform", "v", "/pəˈfɔːm/", "biểu diễn", "Dancers perform in the square."),
           V("offer", "v", "/ˈɒfə/", "dâng, cúng", "People offer fruit and flowers at the temple."),
           V("gather", "v", "/ˈɡæðə/", "tụ họp", "Families gather at the grandparents' house."),
           V("light", "v", "/laɪt/", "thắp sáng", "At eight o'clock they light the lanterns."),
           V("worship", "v", "/ˈwɜːʃɪp/", "thờ cúng", "People worship their ancestors."),
           V("ancestor", "n", "/ˈænsestə/", "tổ tiên", "We remember our ancestors at Tet."),
           V("harvest", "n", "/ˈhɑːvɪst/", "vụ mùa thu hoạch", "The festival celebrates the harvest.")],
    phrases=["take part in a parade", "gather at…", "light the lanterns", "worship the ancestors",
             "give thanks for the harvest"],
    grammar=G("Describing a festival in sequence (recycling Unit 3)",
              use=["Use the present simple for what happens every year.",
                   "Use sequence words: First, Then, After that, In the evening, Finally.",
                   "Use time phrases: at midnight, on the first morning, for three days.",
                   "Passive-like meaning without the passive: 'The streets are full of…' / "
                   "'There are lion dances in every street.'"],
              form=[["Stage", "Language", "Example"],
                    ["before", "A few days before, people…", "A few days before, people clean the house."],
                    ["first day", "On the first morning, …", "On the first morning, families gather."],
                    ["evening", "In the evening, …", "In the evening, children light lanterns."],
                    ["end", "Finally / At the end, …", "Finally, everybody watches the fireworks."]],
              examples=["A few days before Tet, families clean and decorate their houses. "
                        "On the first morning, they visit their grandparents. In the evening, "
                        "everybody gathers for a big meal."],
              pitfall="Students switch between present and past when describing a yearly festival. "
                      "Choose the PRESENT SIMPLE and keep it all the way through.",
              note="A festival description is a 'timetable' — always present simple, like a timetable."),
    pron=P("/θ/ and /ð/ in sentences; 'the' before vowels",
           "/θ/ think, three, month. /ð/ this, they, the, gather, weather. "
           "Note: 'the' is /ðə/ before a consonant and /ði/ before a vowel: the moon /ðə/, "
           "the eighth /ði/.",
           items=["/θ/: think, three, thank, month, birthday, thousands",
                  "/ð/: this, that, they, the, gather, together, weather",
                  "the moon /ðə muːn/ – the eighth /ði eɪtθ/"],
           drill=["They gather together on the third day of the month.",
                  "Thousands of people think this is the best festival.",
                  "The eighth month and the third day."],
           vn_note="Also watch the final /θ/ in 'month', 'fourth', 'eighth' — it is very hard and "
                   "very often dropped."),
    listening=AUDIO['U9L2'],
    reading=T("Thanksgiving in the United States",
              ["Thanksgiving takes place on the fourth Thursday of November. It is not a religious "
               "festival and it is not about presents: it is about food and family.",
               "The story goes back to 1621, when English settlers and Native Americans shared a meal "
               "after the harvest. Today, families travel long distances to be together — the days "
               "around Thanksgiving are the busiest travel days of the whole American year.",
               "The meal is almost always the same: turkey, potatoes, vegetables and pumpkin pie. "
               "Many families go round the table and each person says one thing they are thankful for.",
               "Vietnamese students often notice how similar this is to a Vietnamese family meal at "
               "Tet or at the death anniversary of an ancestor: the same idea of gathering, the same "
               "special food, the same feeling that being together matters more than the food."],
              tasks=[EX("U9.2-R1", "Read and answer", "Answer the questions.",
                        items=["1. When exactly does Thanksgiving take place?",
                               "2. What happened in 1621?",
                               "3. Why are those days the busiest travel days?",
                               "4. What do many families do around the table?",
                               "5. What similarity does the writer point out?"],
                        answers=["1. On the fourth Thursday of November.",
                                 "2. English settlers and Native Americans shared a meal after the "
                                 "harvest.",
                                 "3. Because families travel long distances to be together.",
                                 "4. Each person says one thing they are thankful for.",
                                 "5. That it is similar to a Vietnamese family meal at Tet or at an "
                                 "ancestor's death anniversary — gathering, special food, and being "
                                 "together mattering most."], level="M", kind="reading")]),
    speaking=[EX("U9.2-S1", "Describe the day", "Describe a festival day in order using First, "
                 "Then, In the afternoon, In the evening.",
                 items=["Choose: Tet / the Mid-Autumn Festival / a local temple festival."],
                 answers=["Model: A few days before Tet we clean the house. On the first morning we "
                          "visit my grandparents. Then we give lucky money to the children. "
                          "In the evening the whole family eats together."],
                 level="M", kind="speaking"),
              EX("U9.2-S2", "Festival interview", "Ask your partner five questions about a festival "
                 "they know.",
                 items=["When? Where? What do people do? What do people eat? Why do you like it?"],
                 answers=["Then report one answer to the class."], level="D", kind="speaking")],
    writing=[EX("U9.2-W1", "Sequence the description", "Put the sentences in order and add sequence "
                "words.",
                items=["a. families eat a big meal together",
                       "b. people clean and decorate the house",
                       "c. children receive lucky money",
                       "d. everybody visits the grandparents"],
                answers=["Model: A few days before, people clean and decorate the house. "
                         "On the first morning, everybody visits the grandparents. Then children "
                         "receive lucky money. In the evening, families eat a big meal together."],
                level="M", kind="writing")],
    communication={"function": "Asking about customs politely",
                   "phrases": ["Can I ask you something about…?", "Why do people…?",
                               "What does it mean?", "Is it the same everywhere?",
                               "That's interesting — we do something similar."],
                   "roleplay": "A foreign student asks about three Vietnamese customs; you explain "
                               "and ask about one custom in their country.",
                   "real_life": "Talking about culture with someone from another country."},
    guided=[EX("U9.2-G1", "Match the verb", "Complete with take part in, perform, offer, gather, "
               "light, worship.",
               items=["1. People ______ fruit and flowers at the temple.",
                      "2. Families ______ at the grandparents' house.",
                      "3. Dancers ______ in the square.", "4. Thousands ______ the parade.",
                      "5. At eight they ______ the lanterns.",
                      "6. People ______ their ancestors."],
               answers=["1. offer", "2. gather", "3. perform", "4. take part in", "5. light",
                        "6. worship"], level="E", kind="vocab"),
            EX("U9.2-G2", "/θ/ or /ð/?", "Sort the words.",
               wordbank=["think", "this", "three", "they", "month", "gather", "birthday", "the"],
               items=["/θ/ (no voice): ______", "/ð/ (voice, buzz): ______"],
               answers=["/θ/: think, three, month, birthday", "/ð/: this, they, gather, the"],
               level="M", kind="pron")],
    independent=[EX("U9.2-I1", "Complete the festival description", "Use the correct form.",
                    text=["The Hung Kings Festival (1. take) ______ place on the tenth day of the "
                          "third lunar month. A few days before, people (2. clean) ______ the temples. "
                          "On the morning of the festival, thousands of people (3. gather) ______ at "
                          "the foot of the mountain and (4. climb) ______ to the temples. "
                          "They (5. offer) ______ banh chung and flowers and (6. worship) ______ the "
                          "Hung Kings. In the afternoon there (7. be) ______ traditional games and "
                          "singing."],
                    items=["Write the seven verbs."],
                    answers=["1. takes", "2. clean", "3. gather", "4. climb", "5. offer", "6. worship",
                             "7. are"], level="M", kind="grammar"),
                 EX("U9.2-I2", "Festival interview", "Do U9.2-S2 and report one answer.", items=[],
                    answers=["See U9.2-S2."], level="D", kind="speaking")],
    review=["8 festival activity verbs", "Present simple + sequence words for a festival",
            "/θ/ and /ð/ in words and sentences"],
    homework=[EX("U9.2-H1", "Vocabulary", "Complete with take part in, perform, offer, gather, "
                 "worship, harvest.",
                 items=["1. Many people ______ the competition.", "2. We ______ our ancestors at Tet.",
                        "3. The festival gives thanks for the ______ .",
                        "4. Families ______ for a big meal.", "5. Musicians ______ on a boat.",
                        "6. People ______ fruit at the temple."],
                 answers=["1. take part in", "2. worship", "3. harvest", "4. gather", "5. perform",
                          "6. offer"], level="E", kind="vocab"),
              EX("U9.2-H2", "Grammar", "Write four sentences about a festival using First, Then, "
                 "In the afternoon, In the evening.",
                 items=[], answers=["Model: First, families clean and decorate the house. "
                                    "Then everybody visits the grandparents. In the afternoon children "
                                    "receive lucky money. In the evening the family eats together."],
                 level="M", kind="grammar"),
              EX("U9.2-H3", "Writing", "Write 5 sentences describing what happens at a festival "
                 "in your area.",
                 items=["Present simple only; at least three sequence words."],
                 answers=["Model: Our village festival takes place in the second lunar month. "
                          "A few days before, the men repair the temple gate. On the morning of the "
                          "festival, everybody gathers at the temple and the old men carry the flags. "
                          "Then there is a procession round the village. In the afternoon there are "
                          "games and in the evening everybody eats together."],
                 level="M", kind="writing", lines=6),
              EX("U9.2-H4", "Pronunciation", "Say these sentences five times: 'They gather together "
                 "on the third day of the month.' 'Thousands think this is the best festival.'",
                 items=["Tongue between the teeth!"], answers=["Spot-check in Lesson 3."],
                 level="M", kind="pron")],
    workbook=[EX("U9.2-P1", "Match", "Match the verb with the noun.",
                 items=["1. light", "2. worship", "3. take part in", "4. offer", "5. perform",
                        "a. a dance", "b. the lanterns", "c. fruit and flowers", "d. the parade",
                        "e. the ancestors"],
                 answers=["1–b", "2–e", "3–d", "4–c", "5–a"], level="E", kind="vocab"),
              EX("U9.2-P2", "Sequence words", "Complete the description.",
                 wordbank=["A few days before", "On the first morning", "Then", "In the evening",
                           "Finally"],
                 items=["1. ______ , people clean the house.", "2. ______ , families visit the "
                        "grandparents.", "3. ______ , children receive lucky money.",
                        "4. ______ , everybody eats a big meal.",
                        "5. ______ , the children go outside to play."],
                 answers=["1. A few days before", "2. On the first morning", "3. Then",
                          "4. In the evening", "5. Finally"], level="E", kind="writing"),
              EX("U9.2-P3", "/θ/ or /ð/?", "Write the sound and then read the sentence aloud.",
                 items=["1. The third day ___ ___", "2. They think so ___ ___",
                        "3. My mother's birthday ___ ___", "4. Three months ___ ___"],
                 answers=["1. the /ð/, third /θ/", "2. They /ð/, think /θ/",
                          "3. mother /ð/, birthday /θ/", "4. Three /θ/, months /θ/"],
                 level="D", kind="pron"),
              EX("U9.2-P4", "Reading", "Read and answer.",
                 text=["The Whale Festival is held in the fishing villages of central Viet Nam. "
                       "Fishermen believe that whales protect boats in a storm, so when a whale dies, "
                       "the village buries it and builds a small temple. Once a year, before the "
                       "fishing season, the whole village gathers at the temple, offers food and asks "
                       "for a safe year. Then there are boat races, and every family eats together on "
                       "the beach."],
                 items=["1. Where does this festival take place?", "2. Why do fishermen respect whales?",
                        "3. When exactly is the festival held?", "4. Name two activities."],
                 answers=["1. In the fishing villages of central Viet Nam.",
                          "2. Because they believe whales protect boats in a storm.",
                          "3. Once a year, before the fishing season.",
                          "4. Offering food at the temple, asking for a safe year, boat races, "
                          "eating together on the beach (any two)."], level="M", kind="reading"),
              EX("U9.2-P5", "Writing", "Write a description (80–90 words) of one day of a festival, "
                 "in order.",
                 items=["Use the present simple and five sequence words."],
                 answers=["Model: The Mid-Autumn Festival is a day for children. A few days before, "
                          "shops fill with lanterns and mooncakes, and children make their own "
                          "lanterns at school. On the day itself, families buy fruit and cakes and "
                          "arrange them on a tray. In the early evening, lion dancers go from house to "
                          "house and the drums are very loud. Then, when the moon rises, children walk "
                          "through the streets with their lanterns. Finally, families sit outside, "
                          "eat mooncakes and look at the moon. (92 words)"],
                 level="D", kind="writing", lines=10)],
    procedure=[ST("Warm-up: /θ/ /ð/ minimal pairs", 5,
                  ["Teacher says a word; students point left (/θ/) or right (/ð/). Recycles Lesson 1."],
                  "Identify the sounds.", "Whole class", "Slide 2"),
               ST("Presentation: 8 activity verbs", 9,
                  ["Pictures of festival activities; elicit and drill the verb + noun chunks."],
                  "Repeat; copy the chunks.", "Whole class", "Slides 3–5"),
               ST("Presentation: sequence in the present", 8,
                  ["Build a festival timeline on the board: a few days before → morning → afternoon → "
                   "evening.",
                   "Insist on the PRESENT SIMPLE all the way through."],
                  "Copy the timeline; produce four sentences.", "Whole class", "Slides 6–7"),
               ST("Listening: the Lim Festival", 10,
                  ['Play the recording “Months of the year” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.'],
                  "Listen and complete the notes.", "Individual → pairs", "Slide 8"),
               ST("Speaking: describe and interview", 9,
                  ["U9.2-S1 in pairs, then the five-question interview."],
                  "Describe and interview.", "Pairs", "Slides 9–10"),
               ST("Wrap-up and homework", 4, ["Two students report an interview answer. Set H1–H4."],
                  "Report; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("One tense all the way through",
                     ["A festival happens every year. So we describe it in the PRESENT SIMPLE, "
                      "like a timetable.",
                      "'People clean the house. Families gather. Children receive lucky money.'",
                      "The mistake is to start in the present and slip into the past: "
                      "'People clean the house and then they visited…' — no!",
                      "Choose the present, and check every verb at the end."]),
                  TK("Final /θ/ in month, fourth, eighth",
                     ["The hardest sound in English is not at the beginning of a word — it is at "
                      "the END.",
                      "'Month.' /mʌnθ/. Tongue out, blow. Not 'mon', not 'mont'.",
                      "'The fourth day of the eighth month.' Say it slowly. Now again.",
                      "This appears in every date, so it is worth two minutes every lesson."])],
    support=["Give the festival timeline with two stages completed.",
             "Do the sound sort with six words.",
             "Provide the interview questions on a card."],
    challenge=["Ask for a full-day description with six sequence words.",
               "Ask them to compare a Vietnamese and a foreign festival.",
               "Ask them to explain why a custom exists."],
    assessment=["6 of 8 verb chunks correct", "Keeps the present simple throughout a description",
                "Audible /θ/ in 'month' and 'third'"],
    board_plan=["LEFT: 8 activity verbs", "CENTRE: festival timeline (before / morning / afternoon / "
                "evening)", "RIGHT: /θ/ | /ð/; Homework H1–H4"],
    materials=["Festival activity pictures", 'Recording: Months of the year — ELLLO — Sound Grammar (2:01)'],
)

L3 = Lesson(
    code="U9L3", unit=9, number=3, period=65,
    lesson_type="A Closer Look 2", title="Articles: a, an, the and no article",
    objectives=["use a and an correctly with singular countable nouns",
                "use the for something specific or already mentioned",
                "use no article for general plural and uncountable nouns",
                "correct the six commonest article mistakes"],
    recycled=["U9L1–L2 festival vocabulary; Unit 5 countable and uncountable nouns"],
    vocab=[V("tradition", "n", "/trəˈdɪʃn/", "truyền thống", "It is an old tradition."),
           V("ceremony", "n", "/ˈserəməni/", "buổi lễ", "The ceremony starts at eight."),
           V("procession", "n", "/prəˈseʃn/", "đám rước", "The procession goes round the village."),
           V("temple", "n", "/ˈtempl/", "đền, chùa", "There is a temple on the hill."),
           V("altar", "n", "/ˈɔːltə/", "bàn thờ", "Fruit is placed on the altar."),
           V("incense", "n", "/ˈɪnsens/", "hương, nhang", "The smell of incense fills the temple.")],
    phrases=["for the first time", "at the temple", "in the evening", "once a year",
             "all over the country"],
    grammar=G("Articles: a / an / the / no article",
              use=["A / AN: one thing, not specific, the first time you mention it. "
                   "A = before a consonant sound; AN = before a vowel sound (a lantern, an altar).",
                   "THE: (1) we both know which one; (2) you already mentioned it; "
                   "(3) there is only one (the moon, the sun); (4) with superlatives (the biggest).",
                   "NO ARTICLE: plural nouns in general (Festivals are important) and uncountable "
                   "nouns in general (Rice is our main food).",
                   "Also no article with most countries, cities and days: Viet Nam, Hanoi, Monday."],
              form=[["Use", "Example"],
                    ["a / an — first mention", "I bought a lantern. / She wore an ao dai."],
                    ["the — second mention", "The lantern was red."],
                    ["the — only one", "the moon, the sun, the Mekong"],
                    ["the — superlative", "the biggest festival in the country"],
                    ["no article — general plural", "Children love festivals."],
                    ["no article — uncountable", "Rice is important in Viet Nam."]],
              examples=["There is a temple on the hill. The temple is 300 years old.",
                        "At Tet, people give lucky money to children.",
                        "The moon is biggest on the fifteenth day."],
              pitfall="Vietnamese has NO articles, so students either leave them out "
                      "(*I saw temple*) or add 'the' everywhere (*I like the festivals*). "
                      "The two rules that fix most errors: first mention = a/an; "
                      "general plural = no article.",
              note="Say 'AN' before a vowel SOUND, not a vowel letter: an hour (silent h), "
                   "a university (/juː/)."),
    pron=P("Weak articles: a /ə/, an /ən/, the /ðə/ or /ði/",
           "Articles are NEVER stressed. a = /ə/, an = /ən/, the = /ðə/ (before consonants) or "
           "/ði/ (before vowels). They almost disappear in fast speech.",
           items=["a lantern /ə ˈlæntən/", "an altar /ən ˈɔːltə/", "the temple /ðə ˈtempl/",
                  "the eighth /ði eɪtθ/"],
           drill=["I saw a lantern and an altar at the temple.",
                  "The moon on the fifteenth is the biggest of the year."],
           vn_note="Because articles are weak, learners do not HEAR them — which is why they do not "
                   "write them. Dictation of short phrases is the best cure."),
    listening=AUDIO['U9L3'],
    reading=T("A letter about a first Tet",
              ["Dear Grandma,",
               "I have just spent my first Tet in Viet Nam and I want to tell you about it.",
               "Three days before, my host family cleaned the whole house. They bought a peach tree "
               "for the living room — the tree was taller than me! They also made banh chung, "
               "a square cake made of rice, pork and beans. It takes twelve hours to cook.",
               "On the first morning, the family visited the grandparents. The grandmother gave "
               "lucky money to all the children in red envelopes. I got one too, although I am "
               "seventeen and much too old!",
               "The most surprising thing was the silence in the streets. In Viet Nam, cities are "
               "usually very noisy. But on the first day of Tet, everybody is at home with the family, "
               "so the streets are empty. It was strange and beautiful.",
               "Love, Anna"],
              tasks=[EX("U9.3-R1", "Read and answer", "Answer the questions.",
                        items=["1. What did the family buy for the living room?",
                               "2. What is banh chung made of and how long does it take to cook?",
                               "3. What did the grandmother give the children?",
                               "4. What surprised Anna most, and why?"],
                        answers=["1. A peach tree.",
                                 "2. Rice, pork and beans; it takes twelve hours to cook.",
                                 "3. Lucky money in red envelopes.",
                                 "4. The silence in the streets, because everybody was at home with "
                                 "their family."], level="M", kind="reading"),
                     EX("U9.3-R2", "Find the articles", "Find in the letter:",
                        items=["1. two examples of 'a' with a first mention",
                               "2. one example of 'the' with a second mention",
                               "3. one general plural with no article",
                               "4. one superlative with 'the'"],
                        answers=["1. 'a peach tree', 'a square cake', 'a red envelope' (any two)",
                                 "2. 'the tree was taller than me'",
                                 "3. 'cities are usually very noisy'",
                                 "4. 'The most surprising thing'"], level="D", kind="reading")]),
    speaking=[EX("U9.3-S1", "Describe the picture", "Describe a festival picture. Your partner "
                 "listens for article mistakes.",
                 items=["Use: 'There is a…', 'The … is…', 'People are…'"],
                 answers=["Peer-monitoring for articles is very effective at this level."],
                 level="M", kind="speaking"),
              EX("U9.3-S2", "First time in Viet Nam", "A is a foreign visitor at a festival, "
                 "B explains what they can see. Six exchanges.",
                 items=["A: What's that? B: It's a lantern. The lantern is for children."],
                 answers=["Model: A: What are those? B: They're incense sticks. People light the "
                          "incense at the altar."], level="D", kind="speaking")],
    writing=[EX("U9.3-W1", "a, an, the or –?", "Complete the sentences.",
                items=["1. I saw ______ lantern in the shop. ______ lantern was red.",
                       "2. ______ children love festivals.", "3. She wore ______ ao dai.",
                       "4. ______ moon is very bright tonight.",
                       "5. Tet is ______ most important festival in Viet Nam.",
                       "6. We eat ______ rice every day."],
                answers=["1. a; The", "2. – ", "3. an", "4. The", "5. the", "6. –"],
                level="M", kind="writing")],
    communication={"function": "Explaining an object or a custom to a visitor",
                   "phrases": ["It's a…", "It's used for…", "It means…", "We use it at…",
                               "It's a bit like a…"],
                   "roleplay": "Show and tell: describe one festival object (a lantern, a red "
                               "envelope, incense) to a visitor in three sentences.",
                   "real_life": "Explaining Vietnamese objects and customs to a foreign friend."},
    guided=[EX("U9.3-G1", "a or an?", "Complete.",
               items=["1. ______ lantern", "2. ______ altar", "3. ______ costume", "4. ______ envelope",
                      "5. ______ hour", "6. ______ university", "7. ______ ancestor", "8. ______ parade"],
               answers=["1. a", "2. an", "3. a", "4. an", "5. an (silent h)", "6. a (/juː/)",
                        "7. an", "8. a"], level="E", kind="grammar",
               note="It is the SOUND that matters, not the letter: an hour, a university."),
            EX("U9.3-G2", "the or no article?", "Complete.",
               items=["1. ______ festivals are important in Viet Nam.",
                      "2. ______ festival in my village is in March.",
                      "3. ______ rice is our main food.",
                      "4. ______ rice on the altar is for the ancestors.",
                      "5. ______ Mekong is the longest river in the south."],
               answers=["1. – ", "2. The", "3. – ", "4. The", "5. The"],
               level="M", kind="grammar")],
    independent=[EX("U9.3-I1", "Error clinic", "Correct one mistake in each sentence.",
                    items=["1. I saw temple on the hill.", "2. She wore a ao dai.",
                          "3. The children love the festivals.", "4. Tet is most important festival.",
                          "5. We eat the rice every day.", "6. There is a moon in the sky tonight."],
                    answers=["1. I saw a temple on the hill.", "2. She wore an ao dai.",
                             "3. Children love festivals.",
                             "4. Tet is the most important festival.",
                             "5. We eat rice every day.", "6. There is the moon / The moon is in the "
                             "sky tonight."],
                    level="D", kind="grammar",
                    note="Rule 1: first mention = a/an. Rule 2: general plural or uncountable = "
                         "no article. Rule 3: only one of them in the world = the."),
                 EX("U9.3-I2", "Visitor role play", "Do U9.3-S2 with a partner; your partner counts "
                    "your article mistakes.", items=[], answers=["See U9.3-S2."],
                    level="D", kind="speaking")],
    review=["a/an for first mention", "the for something specific or unique",
            "no article for general plurals and uncountables"],
    homework=[EX("U9.3-H1", "Grammar", "Complete with a, an, the or – .",
                 items=["1. There is ______ temple near my house.",
                        "2. ______ temple is very old.", "3. ______ children get lucky money at Tet.",
                        "4. She is wearing ______ ao dai.", "5. ______ sun goes down at six.",
                        "6. We eat ______ mooncakes at the Mid-Autumn Festival.",
                        "7. It is ______ biggest festival in the country.",
                        "8. ______ incense smells wonderful."],
                 answers=["1. a", "2. The", "3. – ", "4. an", "5. The", "6. – ", "7. the", "8. –"],
                 level="M", kind="grammar"),
              EX("U9.3-H2", "Grammar", "Correct the mistakes (one per sentence).",
                 items=["1. I bought lantern for my sister.", "2. She wore a ao dai.",
                        "3. I love the Vietnamese food.", "4. Tet is most important festival.",
                        "5. We went to temple on Sunday."],
                 answers=["1. I bought a lantern for my sister.", "2. She wore an ao dai.",
                          "3. I love Vietnamese food.", "4. Tet is the most important festival.",
                          "5. We went to the temple on Sunday."], level="D", kind="grammar"),
              EX("U9.3-H3", "Writing", "Write 5 sentences about a festival, using a/an twice, "
                 "the twice and no article once.",
                 items=["Underline the articles."],
                 answers=["Model: In my village there is a small temple near the river. "
                          "The temple is more than two hundred years old. Every spring there is a "
                          "festival there. Children love festivals because they get sweets and money. "
                          "The best part is the boat race on the last afternoon."],
                 level="M", kind="writing", lines=6),
              EX("U9.3-H4", "Pronunciation", "Say these five phrases quickly, with weak articles: "
                 "a lantern, an altar, the temple, the eighth, an hour.",
                 items=[], answers=["Spot-check in Lesson 4."], level="E", kind="pron")],
    workbook=[EX("U9.3-P1", "a or an?", "Complete.",
                 items=["1. ___ apple", "2. ___ lantern", "3. ___ egg", "4. ___ costume",
                        "5. ___ orange", "6. ___ hour", "7. ___ umbrella", "8. ___ university"],
                 answers=["1. an", "2. a", "3. an", "4. a", "5. an", "6. an", "7. an", "8. a"],
                 level="E", kind="grammar"),
              EX("U9.3-P2", "the or – ?", "Complete.",
                 items=["1. ___ Tet is in February.", "2. ___ moon is very bright.",
                        "3. ___ students like festivals.", "4. ___ students in my class like music.",
                        "5. ___ Viet Nam has many festivals.", "6. ___ Mekong Delta is in the south."],
                 answers=["1. – ", "2. The", "3. – ", "4. The", "5. – ", "6. The"],
                 level="M", kind="grammar"),
              EX("U9.3-P3", "Complete the text", "Write a, an, the or – .",
                 text=["Last year I went to (1) ___ festival in (2) ___ small village near Hue. "
                       "(3) ___ festival takes place once (4) ___ year. In (5) ___ morning there was "
                       "(6) ___ procession, and in (7) ___ afternoon there were games. "
                       "(8) ___ people were very friendly."],
                 items=["Write the eight answers."],
                 answers=["1. a", "2. a", "3. The", "4. a", "5. the", "6. a", "7. the", "8. The"],
                 level="D", kind="grammar"),
              EX("U9.3-P4", "Find and correct", "There are six article mistakes in this paragraph.",
                 text=["I love the festivals. Last month I went to festival in my village. "
                       "There was a procession and an ceremony at temple. People offered the fruit "
                       "and incense. The moon was very bright. It was best day of the year."],
                 items=["Write the six corrections."],
                 answers=["1. 'the festivals' → 'festivals'", "2. 'to festival' → 'to a festival'",
                          "3. 'an ceremony' → 'a ceremony'", "4. 'at temple' → 'at the temple'",
                          "5. 'the fruit' → 'fruit'", "6. 'best day' → 'the best day'"],
                 level="D", kind="grammar"),
              EX("U9.3-P5", "Writing", "Write 6 sentences about a place you visited, using at least "
                 "six articles correctly.",
                 items=[], answers=["Model: Last summer I visited a small island near Nha Trang. "
                                    "The island has only one village and a very old temple. "
                                    "We took a boat from the harbour. The boat was slow but the sea "
                                    "was beautiful. People on the island are fishermen. It was the "
                                    "quietest place I have ever seen."], level="D", kind="writing",
                 lines=8)],
    procedure=[ST("Warm-up: Festival word race", 5,
                  ["Teams write as many festival words as they can in 60 seconds. Recycles Lessons 1–2."],
                  "Write words in teams.", "Teams", "Slide 2"),
               ST("Presentation: a / an", 8,
                  ["Hold up objects: a pen, an apple, an envelope. Elicit the rule: vowel SOUND = an.",
                   "Trap examples: an hour, a university. Explain: it is the sound, not the letter."],
                  "Repeat; produce ten a/an phrases.", "Whole class", "Slides 3–4"),
               ST("Presentation: the / no article", 12,
                  ["Story on the board: 'I saw A temple. THE temple was old.' Draw an arrow from "
                   "'a' to 'the' — first mention, second mention.",
                   "Add: only one in the world (the moon, the sun) and superlatives (the biggest).",
                   "Then the no-article rule with general plurals and uncountables: "
                   "'Children love festivals.' 'Rice is our main food.'",
                   "Warn about the Vietnamese habit of adding 'the' to everything."],
                  "Copy the four rules with one example each.", "Whole class", "Slides 5–8"),
               ST("Guided practice", 8, ["U9.3-G1, G2, W1 and the error clinic U9.3-I1."],
                  "Complete and correct.", "Pairs", "Student Book p. U9L3"),
               ST("Listening: dictation of articles", 7,
                  ['Play the recording “Articles: a / an / the” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; students write the missing articles. This trains the ear for weak forms.'],
                  "Listen and write the articles.", "Individual → pairs", "Slide 9"),
               ST("Wrap-up and homework", 5, ["Speaking with peer article-monitoring (U9.3-S1). "
                                              "Set H1–H4."],
                  "Describe and monitor.", "Pairs", "Slide 12")],
    teacher_talk=[TK("Why articles are so hard for us",
                     ["Vietnamese has no articles. 'Tôi thấy ngôi đền' — no 'a', no 'the'.",
                      "So two things happen: we forget them completely, or we put 'the' everywhere.",
                      "Two rules will fix eighty per cent of your mistakes.",
                      "Rule one: the FIRST time you mention something, use A or AN. "
                      "Rule two: when you talk about things in general — plural or uncountable — "
                      "use NOTHING. 'Children love festivals.' 'Rice is our food.'"]),
                  TK("First mention, second mention",
                     ["Listen to this little story. 'Yesterday I saw A dog. THE dog was black.'",
                      "First time: A dog — you don't know which one. Second time: THE dog — now we "
                      "both know which dog.",
                      "It is like introducing a friend. First: 'This is a friend of mine.' "
                      "After that: 'The friend I told you about.'",
                      "Draw the arrow in your notebook: a → the."])],
    support=["Give the four rules on a desk card with one example each.",
             "Colour-code: a/an = blue, the = red, no article = green.",
             "Reduce the error clinic to four sentences."],
    challenge=["Add 'the' with rivers, seas and mountain ranges (the Mekong, the Truong Son).",
               "Ask them to find and explain five articles in a reading text.",
               "Ask them to write a paragraph and mark every article rule used."],
    assessment=["8 of 8 correct a/an", "5 of 6 correct the / no article",
                "Fewer than 3 article errors in a short spoken description"],
    board_plan=["LEFT: a → the (first mention / second mention)",
                "CENTRE: 4 rules: a/an · the (specific, unique, superlative) · no article (general)",
                "RIGHT: error clinic; Homework H1–H4"],
    materials=["Real objects for a/an", "Coloured chalk", 'Recording: Articles: a / an / the — ELLLO — Sound Grammar (2:26)'],
)

L4 = Lesson(
    code="U9L4", unit=9, number=4, period=66,
    lesson_type="Communication", title="Everyday English: asking about a festival",
    objectives=["ask a range of questions about a festival",
                "answer questions about a Vietnamese festival",
                "take part in an 8-turn cultural exchange conversation",
                "write five good questions and answers"],
    recycled=["U9L1–L3: festival vocabulary, articles; Unit 6 question forms; Unit 3 past simple"],
    vocab=[V("public holiday", "n", "/ˌpʌblɪk ˈhɒlədeɪ/", "ngày nghỉ lễ", "Tet is a public holiday."),
           V("lunar calendar", "n", "/ˈluːnə ˈkælɪndə/", "âm lịch", "The date follows the lunar calendar."),
           V("relative", "n", "/ˈrelətɪv/", "họ hàng", "We visit our relatives at Tet."),
           V("lucky money", "n", "/ˈlʌki ˈmʌni/", "tiền lì xì", "Children receive lucky money."),
           V("greeting", "n", "/ˈɡriːtɪŋ/", "lời chúc", "The usual greeting is 'Chuc mung nam moi'."),
           V("superstition", "n", "/ˌsuːpəˈstɪʃn/", "điều mê tín", "There are many superstitions at Tet.")],
    phrases=["Can I ask you about…?", "What exactly is…?", "Why do people…?",
             "What does it mean?", "Is it the same in your country?"],
    grammar=G("Question forms for asking about culture (review and extend)",
              use=["Yes/no: Do you get a holiday? Is it a public holiday?",
                   "Wh-: When is it? Where do people go? What do they eat? Why do they do that?",
                   "How + adjective/adverb: How long does it last? How often is it? "
                   "How many days do you get?",
                   "'What exactly is…?' asks for a definition. 'What does it mean?' asks for meaning."],
              form=[["Question type", "Example", "Answer"],
                    ["yes/no", "Is Tet a public holiday?", "Yes, it is — for several days."],
                    ["Wh-", "Why do people clean the house?", "To sweep away the bad luck of last year."],
                    ["How long", "How long does it last?", "Officially five days."],
                    ["definition", "What exactly is banh chung?", "It's a square rice cake with pork "
                     "and beans."]],
              examples=["How many days of holiday do you get? – Usually five to seven.",
                        "Why do people give lucky money? – Because it brings good luck for the year."],
              pitfall="*How long does it lasts?* and *Why people clean the house?* — remember the "
                      "auxiliary: does it LAST, why DO people clean.",
              note="Recycle from Unit 6: after 'do/does' the verb is bare."),
    pron=P("Question intonation and the /θ/ /ð/ sounds in questions",
           "Yes/no questions rise; Wh- questions fall. Watch the sounds in 'What's the third day?' "
           "and 'Do they think…?'",
           items=["Is it a public holiday? ↗", "How long does it last? ↘",
                  "What does it mean? ↘", "Do they think it's important? ↗"],
           drill=["Is Tet a public holiday? ↗ – Yes, it is.",
                  "Why do people clean the house? ↘ – To sweep away bad luck."],
           vn_note="Combining two difficulties (intonation + /θ/ /ð/) in one drill is efficient — "
                   "but slow down."),
    listening=AUDIO['U9L4'],
    reading=T("Five questions foreigners ask about Tet",
              ["1. 'Is it like Christmas?' A little — family, food, presents for children — but Tet "
               "is not religious in the same way, and the date changes every year.",
               "2. 'Why is everything closed?' Because almost everybody goes home to their family. "
               "For three or four days, cities become empty and villages become full.",
               "3. 'How much lucky money should I give?' A small amount is fine. The envelope matters "
               "more than the money.",
               "4. 'Can I visit a Vietnamese family?' Yes — but the first visitor on the first morning "
               "is special, so wait until the second day unless you are invited.",
               "5. 'What should I say?' 'Chuc mung nam moi' — Happy New Year. Add a wish: "
               "health for old people, good marks for students, money for everybody else."],
              tasks=[EX("U9.4-R1", "Read and answer", "Answer the questions.",
                        items=["1. Give one similarity and one difference between Tet and Christmas.",
                               "2. Why does everything close?",
                               "3. How much lucky money should a visitor give?",
                               "4. When should a visitor come, and why?",
                               "5. What wish is suitable for an old person? And for a student?"],
                        answers=["1. Similar: family, food, presents for children. Different: "
                                 "Tet is not religious in the same way and the date changes.",
                                 "2. Because almost everybody goes home to their family.",
                                 "3. A small amount — the envelope matters more.",
                                 "4. From the second day, because the first visitor on the first "
                                 "morning is special.",
                                 "5. Health for old people; good marks for students."],
                        level="M", kind="reading")]),
    speaking=[EX("U9.4-S1", "Question bank", "Write five questions about a festival, then ask your "
                 "partner.",
                 items=["Include: one yes/no, two Wh-, one 'How long/many', one 'Why…?'"],
                 answers=["Model: Is it a public holiday? When exactly is it? What do people eat? "
                          "How long does it last? Why do people do that?"],
                 level="M", kind="speaking"),
              EX("U9.4-S2", "Cultural exchange role play", "A is a foreign student, B is Vietnamese. "
                 "A asks about a Vietnamese festival; B answers and asks one question back. "
                 "Eight turns.",
                 items=["Checklist: □ polite opener □ four questions □ one 'Why?' □ one reaction "
                        "□ one question back □ polite ending"],
                 answers=["Assessment: task 3, fluency 2.5, pronunciation 2.5, accuracy 2."],
                 level="D", kind="speaking")],
    writing=[EX("U9.4-W1", "Questions and answers", "Write five questions a foreign visitor might ask "
                "about a Vietnamese festival, with your answers.",
                items=[], answers=["Model: Q: When exactly is the Mid-Autumn Festival? "
                                   "A: On the fifteenth day of the eighth lunar month, usually in "
                                   "September. Q: Why do children carry lanterns? A: Because the "
                                   "festival celebrates the full moon, and the lanterns are like small "
                                   "moons."],
                level="M", kind="writing", lines=10)],
    communication={"function": "Cultural exchange: asking and explaining",
                   "phrases": ["Can I ask you about…?", "What exactly is…?", "Why do people…?",
                               "That's interesting!", "Is it the same in your country?",
                               "Thanks for explaining."],
                   "roleplay": "Speed cultural exchange: three-minute conversations with three "
                               "different partners.",
                   "real_life": "Talking about your culture with someone from another country — "
                                "one of the most likely real uses of English."},
    guided=[EX("U9.4-G1", "Make the questions", "Write the question.",
               items=["1. (when / Tet / be?) ______", "2. (how long / the holiday / last?) ______",
                      "3. (why / people / clean the house?) ______",
                      "4. (what / children / receive?) ______",
                      "5. (be / it / a public holiday?) ______"],
               answers=["1. When is Tet?", "2. How long does the holiday last?",
                        "3. Why do people clean the house?", "4. What do children receive?",
                        "5. Is it a public holiday?"], level="M", kind="grammar"),
            EX("U9.4-G2", "Match", "Match the question with the answer.",
               items=["1. How long does it last?", "2. What exactly is banh chung?",
                      "3. Why do people give lucky money?", "4. Is it a public holiday?",
                      "a. It's a square rice cake with pork and beans.",
                      "b. Yes, for several days.", "c. Officially five days.",
                      "d. Because it is a wish for a good year."],
               answers=["1–c", "2–a", "3–d", "4–b"], level="E", kind="mixed")],
    independent=[EX("U9.4-I1", "Complete the interview", "Write the missing questions.",
                    items=["A: ______ ? B: It's in September, on the fifteenth day of the eighth "
                           "lunar month.",
                           "A: ______ ? B: Children carry lanterns and families eat mooncakes.",
                           "A: ______ ? B: Because it celebrates the full moon.",
                           "A: ______ ? B: No, it isn't a public holiday — we still go to school.",
                           "A: ______ ? B: About one night, but the shops start selling cakes a month "
                           "before."],
                    answers=["1. When is the Mid-Autumn Festival? / When exactly is it?",
                             "2. What do people do?", "3. Why do people celebrate it?",
                             "4. Is it a public holiday?", "5. How long does it last?"],
                    level="M", kind="mixed"),
                 EX("U9.4-I2", "Speed cultural exchange", "Do U9.4-S2 with three different partners.",
                    items=[], answers=["See U9.4-S2."], level="D", kind="speaking")],
    review=["Question forms about culture", "What exactly is…? / Why do people…?",
            "Yes/no ↗ and Wh- ↘ intonation"],
    homework=[EX("U9.4-H1", "Vocabulary", "Complete with public holiday, lunar calendar, relatives, "
                 "lucky money, greeting, superstition.",
                 items=["1. Tet follows the ______ .", "2. Children receive ______ in red envelopes.",
                        "3. We visit our ______ during Tet.", "4. Tet is a ______ .",
                        "5. 'Chuc mung nam moi' is the usual ______ .",
                        "6. Not cleaning on the first day is a ______ ."],
                 answers=["1. lunar calendar", "2. lucky money", "3. relatives", "4. public holiday",
                          "5. greeting", "6. superstition"], level="E", kind="vocab"),
              EX("U9.4-H2", "Grammar", "Write the questions.",
                 items=["1. ______ ? – It's in September.", "2. ______ ? – It lasts three days.",
                        "3. ______ ? – Because it celebrates the harvest.",
                        "4. ______ ? – Yes, it's a public holiday.",
                        "5. ______ ? – People eat sticky rice and chicken."],
                 answers=["1. When is it?", "2. How long does it last?", "3. Why do people celebrate "
                          "it?", "4. Is it a public holiday?", "5. What do people eat?"],
                 level="M", kind="grammar"),
              EX("U9.4-H3", "Writing", "Write your five questions and answers (U9.4-W1) neatly.",
                 items=[], answers=["See U9.4-W1 model."], level="M", kind="writing", lines=10),
              EX("U9.4-H4", "Speaking", "Practise answering the five questions about Tet aloud, "
                 "three times.", items=["Remember the falling voice on Wh- questions."],
                 answers=["Spot-check in Lesson 5."], level="M", kind="speaking")],
    workbook=[EX("U9.4-P1", "Correct the questions", "One mistake per question.",
                 items=["1. How long does it lasts?", "2. Why people clean the house?",
                        "3. What means this word?", "4. When is happen the festival?",
                        "5. Is it public holiday?"],
                 answers=["1. How long does it last?", "2. Why do people clean the house?",
                          "3. What does this word mean?", "4. When does the festival take place?",
                          "5. Is it a public holiday?"], level="D", kind="grammar"),
              EX("U9.4-P2", "Question words", "Complete with When, Where, What, Why, How long.",
                 items=["1. ______ is the festival? – In April.",
                        "2. ______ does it take place? – In Phu Tho.",
                        "3. ______ do people do? – They climb the mountain.",
                        "4. ______ do they do that? – To worship the Hung Kings.",
                        "5. ______ does it last? – Three days."],
                 answers=["1. When", "2. Where", "3. What", "4. Why", "5. How long"],
                 level="E", kind="grammar"),
              EX("U9.4-P3", "Reading", "Read and answer.",
                 text=["In many countries, people ask 'How much lucky money should I give?' "
                       "In Viet Nam, the answer surprises visitors: the amount is not important, "
                       "but the number is. Even numbers are usually preferred, and the number 8 is "
                       "considered lucky. New, clean notes are important too — many people go to the "
                       "bank before Tet to change old notes for new ones. The queue at the bank in "
                       "the last week before Tet can take two hours."],
                 items=["1. What is more important than the amount?",
                        "2. Which number is considered lucky?",
                        "3. Why do people go to the bank before Tet?",
                        "4. How long can the queue take?"],
                 answers=["1. The number (and that the notes are new and clean).", "2. Eight.",
                          "3. To change old notes for new ones.", "4. Two hours."],
                 level="M", kind="reading"),
              EX("U9.4-P4", "Write a dialogue", "Write a 12-line conversation between a foreign "
                 "visitor and a Vietnamese student about a festival.",
                 items=["Include six questions, one 'Why?', one reaction and a question back."],
                 answers=["Model: A: Can I ask you about the Mid-Autumn Festival? B: Of course. "
                          "A: When exactly is it? B: On the fifteenth day of the eighth lunar month. "
                          "A: What do people do? B: Children carry lanterns and there are lion dances. "
                          "A: Why lanterns? B: Because the festival celebrates the full moon — "
                          "the lanterns are like small moons. A: That's beautiful. Is it a public "
                          "holiday? B: No, we still go to school! Do you have a festival for children "
                          "in your country? A: We have Halloween, but it's quite different. "
                          "B: You must tell me about it!"], level="D", kind="writing", lines=14)],
    procedure=[ST("Warm-up: Article race", 5,
                  ["Teacher says a noun phrase without the article; students shout a/an/the/–. "
                   "Recycles Lesson 3."],
                  "Supply the correct article.", "Whole class", "Slide 2"),
               ST("Presentation: cultural questions", 9,
                  ["Build the four question types with festival examples.",
                   "Teach 'What exactly is…?' and 'What does it mean?' as fixed chunks.",
                   "Drill the intonation with gestures."],
                  "Repeat; copy the question bank.", "Whole class", "Slides 3–5"),
               ST("Listening: the foreign teacher", 10,
                  ['Play the recording “Lesson 31: Take Me Out to the Ball Game” twice (three times if the class asks); students do the listening tasks; students do the listening tasks. Read the script in role.'],
                  "Listen, complete, read in role.", "Individual → pairs", "Slide 6"),
               ST("Guided practice", 7, ["U9.4-G1, G2 and I1; two pairs perform I1."],
                  "Write and match questions.", "Pairs", "Student Book p. U9L4"),
               ST("Speed cultural exchange", 10,
                  ["Two rows facing each other; three minutes per pair, then rotate. Three rounds.",
                   "Each student must ask four questions and answer four."],
                  "Ask and answer with three partners.", "Pairs (rotating)", "Slides 7–9"),
               ST("Wrap-up and homework", 4, ["Report: 'What did you learn from a classmate?' "
                                              "Set H1–H4."],
                  "Report; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Why explaining your own culture is hard",
                     ["Here is a strange thing: it is harder to explain YOUR culture than to learn "
                      "about another one.",
                      "Why? Because you have never had to. You have done it a hundred times without "
                      "thinking.",
                      "'Why do you clean the house before Tet?' — stop and think. There IS a reason.",
                      "Today you will practise explaining things you have always known. "
                      "That is real communication."]),
                  TK("Question accuracy",
                     ["'How long does it lasts?' — one word too many. After DOES, the verb is naked: "
                      "does it LAST.",
                      "'Why people clean the house?' — one word missing. Why DO people clean.",
                      "Two rules from Unit 6 come back: use the auxiliary, and keep the verb bare.",
                      "Check your five questions before you ask them."])],
    support=["Give the question bank on a card.",
             "Allow weaker students to read their questions in the first round.",
             "Provide model answers about Tet."],
    challenge=["Ask them to answer 'why' questions with two reasons.",
               "Ask them to explain a superstition and what people believe.",
               "Ask them to ask about a festival in the partner's imagined country."],
    assessment=["Forms 4 of 5 questions correctly", "Explains one custom clearly with a reason",
                "Correct question intonation"],
    board_plan=["LEFT: question bank (yes/no, Wh-, How long, What exactly)",
                "CENTRE: sample answers about Tet", "RIGHT: ↗ ↘ ; Homework H1–H4"],
    materials=["Question cards", 'Recording: Lesson 31: Take Me Out to the Ball Game — VOA Learning English — Let’s Learn English, Level 1 (3:30)'],
)

L5 = Lesson(
    code="U9L5", unit=9, number=5, period=67,
    lesson_type="Skills 1", title="Reading: An unusual festival + Speaking: Present a festival",
    objectives=["read a 240-word article and answer gist, detail and inference questions",
                "guess new words from context",
                "present a festival for 90 seconds using a five-point plan",
                "ask two follow-up questions"],
    recycled=["U9L1–L4: festival vocabulary, articles, question forms; Unit 3 sequence words; "
              "Unit 4 comparatives"],
    vocab=[V("origin", "n", "/ˈɒrɪdʒɪn/", "nguồn gốc", "Nobody is sure about the origin of the festival."),
           V("legend", "n", "/ˈledʒənd/", "truyền thuyết", "There is a legend about a dragon."),
           V("attract", "v", "/əˈtrækt/", "thu hút", "It attracts thousands of visitors."),
           V("tourist", "n", "/ˈtʊərɪst/", "khách du lịch", "Tourists come from all over the world."),
           V("preserve", "v", "/prɪˈzɜːv/", "giữ gìn, bảo tồn", "Festivals help to preserve traditions."),
           V("generation", "n", "/ˌdʒenəˈreɪʃn/", "thế hệ", "The custom passes from generation to generation.")],
    phrases=["pass from generation to generation", "date back to…", "attract visitors",
             "keep a tradition alive", "It is believed that…"],
    grammar=G("Talking about origins: dates and 'It is believed that…'",
              use=["dates back to + year/period: The festival dates back to the 15th century.",
                   "It is believed that + sentence: It is believed that the fire brings good luck.",
                   "According to legend, + sentence: According to legend, a dragon lived in the lake.",
                   "These three chunks make a presentation sound much more advanced."],
              form=[["Chunk", "Example"],
                    ["date back to", "The festival dates back to 1470."],
                    ["It is believed that…", "It is believed that the water gives health."],
                    ["According to legend,…", "According to legend, a giant fish saved the village."],
                    ["pass from generation to generation", "The songs pass from generation to generation."]],
              examples=["The Fire Festival dates back more than 300 years. According to legend, "
                        "the fire protected the village from a tiger."],
              pitfall="Students say *It is believe that…* — the correct form is 'It is believeD that'. "
                      "Teach it as a fixed phrase.",
              note="These are chunks, not grammar to analyse. Learn them whole."),
    pron=P("Stress in long words; /θ/ /ð/ in a presentation",
           "'ORigin, 'LEgend, at'TRACT, 'TOUrist, pre'SERVE, gene'RAtion. Keep the /θ/ and /ð/ clear "
           "while you speak at normal speed.",
           items=["'origin (Ooo)", "'legend (Oo)", "at'tract (oO)", "gene'ration (ooOo)",
                  "pre'serve (oO)"],
           drill=["According to legend, the festival dates back three hundred years.",
                  "It attracts thousands of tourists and preserves an old tradition."],
           vn_note="In a presentation, students often speed up and lose both the stress and the "
                   "/θ/ /ð/. Slow down: 90 seconds is long enough for about 120 words."),
    listening=AUDIO['U9L5'],
    reading=T("The festival where nobody sleeps",
              ["In the mountains of Ha Giang, on the twenty-seventh day of the third lunar month, "
               "a market opens that is not really a market at all.",
               "The Khau Vai Love Market dates back more than a hundred years. According to legend, "
               "a young man and a young woman from two different groups fell in love, but their "
               "families would not allow them to marry. They agreed to meet once a year, on the same "
               "day, at Khau Vai.",
               "Today, thousands of people walk for hours over the mountains to be there. Some come "
               "to sell cloth and food, and many young people come to meet somebody. But the heart of "
               "the market is older people: men and women who loved each other long ago, married "
               "other people, and now meet once a year to talk for one night.",
               "Their husbands and wives usually know, and usually come too. Nobody is angry. "
               "The custom is understood.",
               "The festival attracts more and more tourists, and this worries some people. "
               "'When there are cameras, people stop talking,' one old woman said. "
               "'This night was never for photographs.'",
               "Others say that visitors bring money to a very poor area, and that money keeps the "
               "road open and the school full. Both are right, and nobody has solved it yet."],
              tasks=[EX("U9.5-R1", "Gist", "Choose the best title.",
                        items=["A. Shopping in the mountains",
                               "B. A festival where old friends meet once a year",
                               "C. How to travel in Ha Giang"],
                        answers=["B"], level="E", kind="reading"),
                     EX("U9.5-R2", "Detail", "Answer the questions.",
                        items=["1. When and where does the market take place?",
                               "2. What does the legend say?",
                               "3. Who is at the heart of the market?",
                               "4. How do the husbands and wives react?",
                               "5. Give one argument for and one against the tourists."],
                        answers=["1. On the 27th day of the third lunar month, at Khau Vai in "
                                 "Ha Giang.",
                                 "2. A young man and woman from different groups fell in love but "
                                 "could not marry, so they agreed to meet once a year.",
                                 "3. Older people who loved each other long ago and married other "
                                 "people.",
                                 "4. They usually know, usually come too, and nobody is angry.",
                                 "5. For: visitors bring money to a poor area, which keeps the road "
                                 "open and the school full. Against: with cameras, people stop "
                                 "talking — the night was never for photographs."],
                        level="M", kind="reading"),
                     EX("U9.5-R3", "Vocabulary from context", "Find a word or phrase that means:",
                        items=["1. began a long time ago (paragraph 2)",
                               "2. a very old story that may not be true (paragraph 2)",
                               "3. brings people to a place (paragraph 5)",
                               "4. found an answer to a problem (paragraph 6)"],
                        answers=["1. dates back", "2. legend", "3. attracts", "4. solved"],
                        level="M", kind="reading"),
                     EX("U9.5-R4", "Inference", "Answer with your own ideas.",
                        items=["1. Why do you think nobody is angry?",
                               "2. What does the old woman mean by 'This night was never for "
                               "photographs'?",
                               "3. Should tourists be allowed to come? Give your opinion and a reason."],
                        answers=["1. Because the custom is old and understood by everybody in the "
                                 "community; it is about memory, not about breaking a marriage.",
                                 "2. That the meeting is private and emotional, and cameras change "
                                 "how people behave.",
                                 "3. Students' own answer with a reason (accept both sides)."],
                        level="D", kind="reading")]),
    speaking=[EX("U9.5-S1", "Prepare your presentation", "Make notes for a 90-second presentation "
                 "of a festival.",
                 items=["1. Name, when and where ______", "2. History / legend ______",
                        "3. What people do (three things) ______", "4. Food and music ______",
                        "5. Why it matters (and one problem if there is one) ______"],
                 answers=["Notes only."], level="M", kind="speaking"),
              EX("U9.5-S2", "Present your festival", "Speak for 90 seconds in a group of four. "
                 "Listeners ask one question each.",
                 items=["Useful chunks: 'It takes place…', 'It dates back to…', "
                        "'According to legend,…', 'People celebrate by…', 'It is important because…'"],
                 answers=["Assessment: content 3, chunks and articles 3, delivery 2, questions 2."],
                 level="D", kind="speaking")],
    writing=[EX("U9.5-W1", "Notes to sentences", "Turn your notes into six sentences.",
                items=[], answers=["Model: The Whale Festival takes place in the fishing villages of "
                                   "Khanh Hoa, before the fishing season begins. It dates back "
                                   "hundreds of years. According to legend, a whale once saved a boat "
                                   "in a storm, so fishermen believe whales protect them. On the day, "
                                   "the whole village gathers at the whale temple, offers food and "
                                   "asks for a safe year. Then there are boat races, and every family "
                                   "eats together on the beach. It is important because it keeps the "
                                   "village together."], level="M", kind="writing", lines=8)],
    communication={"function": "Handling a difficult question",
                   "phrases": ["That's a good question.", "I'm not completely sure, but…",
                               "Some people think… while others…", "It depends who you ask.",
                               "I'll find out and tell you."],
                   "roleplay": "After each presentation, one listener must ask a difficult question "
                               "('Is it good for the animals?', 'Do young people still care?').",
                   "real_life": "Answering honestly when you do not know something."},
    guided=[EX("U9.5-G1", "True or false", "Read the text again and write T or F.",
               items=["1. The Khau Vai market is mainly for buying and selling.",
                      "2. The legend is about two people who could not marry.",
                      "3. Only young people come.",
                      "4. Husbands and wives are usually angry.",
                      "5. Tourists bring money to a poor area."],
               answers=["1. F – it is not really a market at all.", "2. T",
                        "3. F – older people are at the heart of it.", "4. F – nobody is angry.",
                        "5. T"], level="E", kind="reading"),
            EX("U9.5-G2", "Useful chunks", "Complete the sentences.",
               items=["1. The festival ______ back more than 300 years.",
                      "2. ______ to legend, a dragon lived in the lake.",
                      "3. It ______ believed that the water gives health.",
                      "4. The songs pass from ______ to ______ .",
                      "5. The festival ______ thousands of visitors."],
               answers=["1. dates", "2. According", "3. is", "4. generation; generation",
                        "5. attracts"], level="M", kind="writing")],
    independent=[EX("U9.5-I1", "Retell", "Close the book. Tell your partner about the Khau Vai Love "
                    "Market in five sentences.", items=[],
                    answers=["Model: The Khau Vai Love Market is in Ha Giang, on the 27th day of the "
                             "third lunar month. According to legend, two young people could not "
                             "marry, so they agreed to meet once a year. Today thousands of people "
                             "walk over the mountains to be there. Older people meet the person they "
                             "loved long ago and talk for one night. Their families understand, "
                             "and nobody is angry."], level="M", kind="speaking"),
                 EX("U9.5-I2", "Your presentation", "Do U9.5-S2 in your group.", items=[],
                    answers=["See U9.5-S2."], level="D", kind="speaking")],
    review=["Reading: gist → detail → inference", "Chunks: dates back to / according to legend / "
            "it is believed that", "Presenting a festival in five points"],
    homework=[EX("U9.5-H1", "Reading", "Answer in full sentences.",
                 items=["1. How old is the Khau Vai Love Market?",
                        "2. Why do some people come to sell things?",
                        "3. What worries some people about the tourists?",
                        "4. What is the argument in favour of tourists?"],
                 answers=["1. More than a hundred years old.",
                          "2. To sell cloth and food to the thousands of visitors.",
                          "3. That with cameras, people stop talking — the night was never for "
                          "photographs.",
                          "4. Visitors bring money to a very poor area, which keeps the road open and "
                          "the school full."], level="M", kind="reading"),
              EX("U9.5-H2", "Vocabulary", "Complete with origin, legend, attract, tourists, preserve, "
                 "generation.",
                 items=["1. Nobody knows the ______ of this custom.",
                        "2. According to ______ , a dragon lived here.",
                        "3. The festival ______ thousands of visitors.",
                        "4. Many ______ come from other countries.",
                        "5. Festivals help to ______ our traditions.",
                        "6. The songs pass from one ______ to the next."],
                 answers=["1. origin", "2. legend", "3. attracts", "4. tourists", "5. preserve",
                          "6. generation"], level="E", kind="vocab"),
              EX("U9.5-H3", "Writing", "Write your festival presentation as a paragraph (100–110 "
                 "words).",
                 items=["Five points; at least two chunks from this lesson; check your articles."],
                 answers=["See U9.5-W1 model."], level="D", kind="writing", lines=14),
              EX("U9.5-H4", "Speaking", "Practise your presentation three times. Time it: 90 seconds.",
                 items=[], answers=["Presentations in Lesson 6."], level="M", kind="speaking")],
    workbook=[EX("U9.5-P1", "Vocabulary match", "Match the word with the meaning.",
                 items=["1. origin", "2. legend", "3. preserve", "4. generation", "5. attract",
                        "a. all the people born at about the same time",
                        "b. to bring people to a place", "c. where something began",
                        "d. to keep something for the future", "e. a very old story"],
                 answers=["1–c", "2–e", "3–d", "4–a", "5–b"], level="E", kind="vocab"),
              EX("U9.5-P2", "Reading", "Read and answer.",
                 text=["The Ok Om Bok Festival is celebrated by the Khmer people in the south of "
                       "Viet Nam, in the tenth lunar month. People give thanks to the moon for the "
                       "harvest. The most famous part is the ngo boat race: long wooden boats with "
                       "up to fifty rowers race on the river, and the noise of the drums can be heard "
                       "kilometres away. In the evening, families put green rice, coconut and banana "
                       "on a tray and an old person feeds a little to each child while asking what "
                       "they wish for."],
                 items=["1. Who celebrates this festival and when?", "2. Why do people give thanks?",
                        "3. How many rowers can a ngo boat have?",
                        "4. What happens in the evening?"],
                 answers=["1. The Khmer people in the south of Viet Nam, in the tenth lunar month.",
                          "2. To thank the moon for the harvest.", "3. Up to fifty.",
                          "4. Families prepare a tray of green rice, coconut and banana, and an old "
                          "person feeds a little to each child and asks what they wish for."],
                 level="M", kind="reading"),
              EX("U9.5-P3", "Useful chunks", "Rewrite the sentences using the chunk in brackets.",
                 items=["1. The festival is very old — about 400 years. (dates back)",
                        "2. People think the fire brings good luck. (It is believed that)",
                        "3. There is a story that a fish saved the village. (According to legend)",
                        "4. Grandparents teach the songs to their grandchildren. "
                        "(pass from generation to generation)"],
                 answers=["1. The festival dates back about 400 years.",
                          "2. It is believed that the fire brings good luck.",
                          "3. According to legend, a fish saved the village.",
                          "4. The songs pass from generation to generation."],
                 level="D", kind="writing"),
              EX("U9.5-P4", "Writing", "Write a description (100–110 words) of a festival you would "
                 "like to see, in Viet Nam or abroad.",
                 items=["Five points: name/when/where – history – activities – food – why you want "
                        "to see it."],
                 answers=["Model: I would love to see the Lantern Festival in Hoi An. It takes place "
                          "on the fourteenth day of every lunar month, in the old town. On that night "
                          "all the electric lights are turned off, and the streets are lit only by "
                          "silk lanterns. The custom dates back hundreds of years, when Hoi An was a "
                          "busy trading port. People float small paper lanterns with candles on the "
                          "river and make a wish. There is traditional music and street food "
                          "everywhere. I want to see it because I have only seen photographs, and "
                          "everybody says photographs are not enough. (108 words)"],
                 level="D", kind="writing", lines=14)],
    procedure=[ST("Warm-up: Festival questions", 5,
                  ["Students ask each other three festival questions along the row. "
                   "Recycles Lesson 4."],
                  "Ask and answer.", "Rows", "Slide 2"),
               ST("Pre-reading", 6,
                  ["Show a photo of a mountain market. Ask: 'What do people buy at a market? "
                   "What if a market is NOT for buying?' Predict.",
                   "Pre-teach: legend, dates back, attract, solve. Set the gist task."],
                  "Predict; skim for the title.", "Whole class", "Slides 3–4"),
               ST("While-reading", 13,
                  ["R2 detail individually, pair-check; R3 words in context; R4 inference in pairs.",
                   "For R4 question 3, take a class vote and hear two arguments from each side."],
                  "Read, answer, discuss.", "Individual → pairs", "Slides 5–7"),
               ST("Post-reading: retell", 4, ["Books closed; retell in five sentences."],
                  "Retell.", "Pairs", "Slide 8"),
               ST("Speaking: present a festival", 13,
                  ["Play the model presentation; students find the five points.",
                   "3 minutes to plan; 90-second presentations in groups of four; "
                   "one question each, including one difficult question."],
                  "Listen, plan, present, question.", "Individual → groups of 4", "Slides 9–11"),
               ST("Wrap-up and homework", 4, ["Best presentation to the class. Set H1–H4."],
                  "Listen; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("A festival with a difficult question inside it",
                     ["Most texts about festivals are only beautiful. This one is honest.",
                      "Tourists bring money to a poor area — good. Tourists bring cameras, and people "
                      "stop talking — bad.",
                      "Both are true at the same time. That is real life, and it is also good English "
                      "practice: 'Some people think… while others…'",
                      "In your presentation, if your festival has a difficult question, say it. "
                      "It makes your talk much more interesting."]),
                  TK("Answering a question you cannot answer",
                     ["Somebody will ask you a question you cannot answer. That happens to everybody, "
                      "in every language.",
                      "Do not panic and do not switch to Vietnamese. Say: 'That's a good question. "
                      "I'm not completely sure, but I think…'",
                      "Or: 'I'll find out and tell you tomorrow.' Both are perfect English and "
                      "perfectly honest."])],
    support=["Gloss four words in the margin.", "Give a presentation skeleton with the five points "
             "and starters.", "Let weaker students present to one partner only."],
    challenge=["Ask them to include one 'Some people think… while others…' sentence.",
               "Ask them to summarise the article in three sentences.",
               "Ask them to answer two difficult questions."],
    assessment=["4 of 5 detail answers", "Uses two chunks from the lesson in the presentation",
                "Presentation covers all five points in about 90 seconds"],
    board_plan=["LEFT: 4 new words with stress", "CENTRE: presentation plan 1–5",
                "RIGHT: dates back to / according to legend / it is believed that; Homework H1–H4"],
    materials=["Photos of festivals", 'Recording: What are monthly events in your area? — ELLLO — One Minute English (1:27)', "Timer"],
)

L6 = Lesson(
    code="U9L6", unit=9, number=6, period=68,
    lesson_type="Skills 2", title="Listening: A festival report + Writing: Describe a festival",
    objectives=["listen to a report and complete a fact file",
                "organise a festival description in four paragraphs",
                "write a description of 100–120 words",
                "check a partner's work with a checklist"],
    recycled=["U9L1–L5: festival vocabulary, articles, sequence, chunks; "
              "Units 1–8 all writing structures"],
    vocab=[V("fact file", "n", "/ˈfækt faɪl/", "bảng thông tin", "Complete the fact file."),
           V("colourful", "adj", "/ˈkʌləfl/", "sặc sỡ", "The costumes are very colourful."),
           V("crowded", "adj", "/ˈkraʊdɪd/", "đông đúc", "The streets are crowded all night."),
           V("noisy", "adj", "/ˈnɔɪzi/", "ồn ào", "It is noisy but everybody is happy."),
           V("atmosphere", "n", "/ˈætməsfɪə/", "không khí", "The atmosphere is wonderful."),
           V("unforgettable", "adj", "/ˌʌnfəˈɡetəbl/", "không thể quên", "It was an unforgettable night.")],
    phrases=["The atmosphere is…", "The streets are full of…", "You can smell / hear / see…",
             "I will never forget…"],
    grammar=G("Festival description: four paragraphs (writing focus)",
              use=["Paragraph 1 — FACTS: name, when, where, how long.",
                   "Paragraph 2 — HISTORY: dates back to / according to legend.",
                   "Paragraph 3 — WHAT HAPPENS: sequence words + present simple + food and music.",
                   "Paragraph 4 — FEELING: the atmosphere, and why it matters to people.",
                   "Use the senses in paragraph 4: what you see, hear and smell."],
              form=[["Paragraph", "Content", "Useful language"],
                    ["1 Facts", "name, when, where", "…takes place in… It lasts…"],
                    ["2 History", "origin, legend", "It dates back to… According to legend,…"],
                    ["3 Events", "what people do", "First,… Then,… In the evening,…"],
                    ["4 Feeling", "atmosphere, importance", "The atmosphere is… It matters because…"]],
              examples=["The streets are crowded and noisy, and you can smell grilled meat everywhere.",
                        "For me, the best moment is when all the lanterns are lit at the same time."],
              pitfall="Students write only paragraph 3 (a list of activities). The FEELING paragraph "
                      "is what makes a description worth reading.",
              note="Encourage one sentence with the senses: 'You can hear the drums from the "
                   "other side of the village.'"),
    pron=P("Reading a description aloud with feeling",
           "Group your words, pause at the commas, and let your voice rise a little on the "
           "exciting parts. A description read flatly sounds like a timetable.",
           items=["The streets / are crowded and noisy, / and you can smell grilled meat / everywhere.",
                  "I will NEVER forget / the moment / when all the lanterns / were lit."],
           drill=["The atmosphere is wonderful. / You can hear the drums / from the other side of the "
                  "village."],
           vn_note="Reading your own writing aloud with feeling also helps you find the sentences "
                   "that are too long."),
    listening=AUDIO['U9L6'],
    reading=T("Model description",
              ["THE HOI AN LANTERN FESTIVAL",
               "The Lantern Festival takes place in the old town of Hoi An on the fourteenth day of "
               "every lunar month — the night before the full moon. It lasts about four hours, "
               "from six until ten in the evening.",
               "Hoi An has made silk lanterns for centuries, but the festival as we know it began "
               "only in 1998, when the town decided to protect its old buildings and attract "
               "visitors. It is believed that lanterns bring good luck to a house.",
               "At six o'clock, all the electric lights in the old town are turned off and the "
               "lanterns are lit. There are no motorbikes: everybody walks. Musicians play "
               "traditional music on the corners, and people play bai choi, which is half singing "
               "and half cards. On the river, visitors buy small paper lanterns with candles, "
               "make a wish and put them on the water.",
               "The atmosphere is difficult to describe. The streets are crowded and noisy, "
               "but the river is silent, and there are thousands of small lights moving slowly in "
               "the dark. For me, the best moment is at nine o'clock, when the tourists go back to "
               "their hotels and the town belongs to Hoi An again. I will never forget it. "
               "(200 words — yours can be shorter!)"],
              tasks=[EX("U9.6-R1", "Analyse the model", "Answer the questions.",
                        items=["1. What is in each of the four paragraphs?",
                               "2. Find the two 'history' chunks in paragraph 2.",
                               "3. Which sequence markers are used in paragraph 3?",
                               "4. Find two sentences using the senses.",
                               "5. Why is the last sentence effective?"],
                        answers=["1. P1 facts; P2 history; P3 what happens; P4 atmosphere and feeling.",
                                 "2. 'began only in 1998' (date) and 'It is believed that…'.",
                                 "3. 'At six o'clock', 'On the river'.",
                                 "4. 'The streets are crowded and noisy', 'there are thousands of "
                                 "small lights moving slowly in the dark'.",
                                 "5. It is short and personal after a long description."],
                        level="M", kind="reading")]),
    speaking=[EX("U9.6-S1", "Say your description", "Tell your partner your four paragraphs in "
                 "six sentences before you write.",
                 items=["Facts → history → what happens → feeling."],
                 answers=["Speaking first improves the writing."], level="M", kind="speaking")],
    writing=[EX("U9.6-W1", "Plan your description", "Complete the plan.",
                items=["P1 Facts (name, when, where, how long): ______",
                       "P2 History (dates back / legend): ______",
                       "P3 What happens (three things in order + food/music): ______",
                       "P4 Atmosphere and why it matters (one sense sentence): ______"],
                answers=["Check every plan before students write."], level="M", kind="writing", lines=9),
             EX("U9.6-W2", "Write your description", "Write 100–120 words about a festival "
                "(four paragraphs).",
                items=["Use the present simple, sequence words, one history chunk and one sense "
                       "sentence."],
                answers=["Model: The Mid-Autumn Festival takes place on the fifteenth day of the "
                         "eighth lunar month, all over Viet Nam. It lasts one night, but the "
                         "preparations start weeks before. The festival dates back more than a "
                         "thousand years, to a time when farmers celebrated the harvest and the full "
                         "moon. It is believed that the moon is at its most beautiful on that night. "
                         "In the days before, shops fill with lanterns and mooncakes. On the evening "
                         "itself, lion dancers go from house to house, and children walk through the "
                         "streets carrying lanterns. Families sit outside and eat mooncakes together. "
                         "The atmosphere is noisy and happy: you can hear drums from every direction "
                         "and see hundreds of small lights moving in the dark. For me it is the "
                         "warmest night of the year. (137 words)"],
                level="D", kind="writing", lines=18),
             EX("U9.6-W3", "Peer check", "Swap and tick the checklist.",
                items=["□ four paragraphs", "□ facts: when, where, how long",
                       "□ one history chunk", "□ three activities in order",
                       "□ one sentence using the senses", "□ articles checked (a/an/the/–)",
                       "□ 100–120 words"],
                answers=["Write one thing you liked and one to improve."], level="M", kind="writing")],
    communication={"function": "Sharing a personal memory",
                   "phrases": ["I'll never forget…", "The best moment was…", "It reminds me of…",
                               "You have to be there.", "Photographs don't show it."],
                   "roleplay": "Tell your partner about the best festival night you remember, "
                               "in one minute.",
                   "real_life": "Telling a personal story about a place or an event."},
    guided=[EX("U9.6-G1", "Which paragraph?", "Write P1, P2, P3 or P4.",
               items=["1. It takes place in April. ___", "2. According to legend, a dragon… ___",
                      "3. First, families clean the house. ___",
                      "4. The atmosphere is wonderful. ___",
                      "5. It lasts three days. ___", "6. I will never forget it. ___"],
               answers=["1. P1", "2. P2", "3. P3", "4. P4", "5. P1", "6. P4"],
               level="E", kind="writing"),
            EX("U9.6-G2", "Use the senses", "Rewrite the sentences with a sense verb "
               "(see / hear / smell).",
               items=["1. There is a lot of noise. →", "2. There is grilled meat everywhere. →",
                      "3. There are many lights on the river. →"],
               answers=["Model: 1. You can hear drums from every direction. "
                        "2. You can smell grilled meat everywhere. "
                        "3. You can see hundreds of small lights on the river."],
               level="M", kind="writing")],
    independent=[EX("U9.6-I1", "Write your description", "Do U9.6-W1 and W2.", items=[],
                    answers=["See U9.6-W2 model."], level="D", kind="writing", lines=18),
                 EX("U9.6-I2", "Read and react", "Read your description to your partner. "
                    "Your partner says which sentence they liked best and why.",
                    items=[], answers=["Peer feedback on content, not only on errors."],
                    level="M", kind="speaking")],
    review=["Fact-file listening", "Four-paragraph festival description",
            "Using the senses to describe atmosphere"],
    homework=[EX("U9.6-H1", "Listening / vocabulary", "Complete from the report.",
                 items=["1. The festival is on the ______ day of every lunar month.",
                        "2. It lasts from ______ to ______ .",
                        "3. The modern festival began in ______ .",
                        "4. A paper lantern costs about ______ dong.",
                        "5. About ______ people come on a normal full moon."],
                 answers=["1. fourteenth", "2. six; ten", "3. 1998", "4. 10,000", "5. 4,000"],
                 level="E", kind="listening"),
              EX("U9.6-H2", "Vocabulary", "Complete with colourful, crowded, noisy, atmosphere, "
                 "unforgettable.",
                 items=["1. The streets are ______ on festival nights.",
                        "2. The costumes are very ______ .", "3. It is ______ , but everybody is happy.",
                        "4. The ______ is wonderful.", "5. It was an ______ evening."],
                 answers=["1. crowded", "2. colourful", "3. noisy", "4. atmosphere",
                          "5. unforgettable"], level="E", kind="vocab"),
              EX("U9.6-H3", "Writing", "Rewrite your description neatly after correction. "
                 "Add a picture for the class festival book.",
                 items=["Use the 7-point checklist."],
                 answers=["Marking: content 3, organisation 2, language 3, articles 1, length 1."],
                 level="D", kind="writing", lines=18),
              EX("U9.6-H4", "Speaking", "Read your description aloud twice with feeling, "
                 "pausing at the commas.",
                 items=[], answers=["Spot-check in Lesson 7."], level="E", kind="pron")],
    workbook=[EX("U9.6-P1", "Paragraph plan", "Put the sentences into the right paragraph (1–4).",
                 items=["a. It takes place in the third lunar month.",
                        "b. According to legend, a giant fish saved the village.",
                        "c. In the morning there is a procession to the temple.",
                        "d. The atmosphere is quiet and serious.",
                        "e. It lasts two days.", "f. Then families eat together on the beach."],
                 answers=["P1: a, e", "P2: b", "P3: c, f", "P4: d"], level="E", kind="writing"),
              EX("U9.6-P2", "Complete the description", "Use the words in the box.",
                 wordbank=["takes place", "dates back", "First", "atmosphere", "never forget"],
                 items=["The Fire Festival (1) ______ in February. It (2) ______ more than 200 years. "
                        "(3) ______ , the men build a large fire in the village square. "
                        "The (4) ______ is exciting and a little frightening. I will "
                        "(5) ______ the moment when the fire was lit."],
                 answers=["1. takes place", "2. dates back", "3. First", "4. atmosphere",
                          "5. never forget"], level="E", kind="writing"),
              EX("U9.6-P3", "Improve the description", "This paragraph is only a list. "
                 "Rewrite it with an atmosphere sentence and one sense sentence.",
                 text=["People clean the house. They cook food. They visit relatives. "
                       "Children get money. It is good."],
                 items=["Write your improved version (4–5 sentences)."],
                 answers=["Model: A few days before Tet, families clean the house from top to bottom "
                          "and cook banh chung. On the first morning, everybody visits their "
                          "relatives, and children receive lucky money in red envelopes. "
                          "The atmosphere in the streets is completely different from a normal day: "
                          "the shops are shut and you can smell incense from every house. "
                          "For me it is the best week of the year."],
                 level="D", kind="writing"),
              EX("U9.6-P4", "Writing", "Write a description (100–120 words) of a festival in "
                 "another country that you would like to attend.",
                 items=["Four paragraphs; check your articles carefully."],
                 answers=["See U9.5-P4 model for the style."], level="D", kind="writing", lines=18)],
    procedure=[ST("Warm-up: Fact-file dictation", 5,
                  ["Read six festival facts; students note them in a mini fact file."],
                  "Listen and note.", "Individual → pairs", "Slide 2"),
               ST("Pre-listening", 5,
                  ["Show the fact file. Pre-teach: turn off, silk lantern, bai choi, protect."],
                  "Predict; copy the fact file.", "Whole class", "Slides 3–4"),
               ST("Listening", 11,
                  ['Play the recording “Who visits you on the holidays?” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.'],
                  "Listen and complete the fact file.", "Individual → pairs", "Slide 5"),
               ST("Writing: analyse the model", 8,
                  ["Model description on the slide; colour the four paragraphs; find the sense "
                   "sentences. Do U9.6-G1 and G2."],
                  "Identify the paragraphs; write sense sentences.", "Whole class → pairs",
                  "Slides 6–7"),
               ST("Writing: plan, say, draft", 12,
                  ["Plan (check every plan); say it aloud; write 100–120 words."],
                  "Plan, say, write.", "Individual → pairs → individual", "Slide 8"),
               ST("Peer check and wrap-up", 4, ["Checklist swap; read one good description. "
                                                "Set H1–H4."],
                  "Peer-check.", "Pairs", "Slides 9–10")],
    teacher_talk=[TK("The paragraph everybody forgets",
                     ["Most students write three paragraphs: when, history, what happens. All correct, "
                      "all a little boring.",
                      "The fourth paragraph is where the marks are: THE FEELING. What does it look "
                      "like, sound like, smell like? Why does it matter to people?",
                      "'You can hear drums from every direction.' One sentence like that is worth "
                      "five sentences of facts.",
                      "Every description must have at least one sense sentence. Write it in your plan "
                      "BEFORE you write the rest."]),
                  TK("Checking articles in your own writing",
                     ["Before you hand this in, do one special check: circle every noun.",
                      "Ask: is this the first time I mention it? Then A or AN. Is it specific? THE. "
                      "Is it general and plural? Nothing.",
                      "Two minutes of circling will save you half a mark in the test — and it is "
                      "the mistake we make most."])],
    support=["Give the fact file with three answers filled in.",
             "Provide a four-paragraph frame with starters.",
             "Allow 80–90 words."],
    challenge=["Ask for two sense sentences and one 'Some people think… while others…'.",
               "Ask them to write about a festival they have never seen (research at home).",
               "Ask for 140 words."],
    assessment=["8 of 12 items in the fact file", "Description has four paragraphs and one sense "
                "sentence", "Fewer than four article errors"],
    board_plan=["LEFT: fact file", "CENTRE: four-paragraph plan",
                "RIGHT: senses — see / hear / smell; Homework H1–H4"],
    materials=['Recording: Who visits you on the holidays? — ELLLO — One Minute English (1:08)', "Model description slide", "Checklist cards"],
)

L7 = Lesson(
    code="U9L7", unit=9, number=7, period=69,
    lesson_type="Looking Back & Project", title="Unit 9 review and the Festival Fair",
    objectives=["recall the festival vocabulary of Unit 9",
                "use articles and question forms accurately",
                "correct the six typical mistakes of the unit",
                "present a festival stand and answer visitors' questions"],
    recycled=["ALL of Unit 9 + Units 1–8"],
    vocab=[V("stand", "n", "/stænd/", "gian trưng bày", "Each group has a stand."),
           V("visitor", "n", "/ˈvɪzɪtə/", "khách tham quan", "Visitors ask questions at each stand."),
           V("quiz", "n", "/kwɪz/", "câu đố", "We prepared a five-question quiz.")],
    phrases=["Welcome to our stand.", "Would you like to know about…?", "Any questions?",
             "Thank you for visiting."],
    grammar=G("Unit 9 grammar in one page",
              use=["a/an for first mention (a lantern, an altar)",
                   "the for something specific, unique or superlative",
                   "no article for general plurals and uncountables",
                   "Question forms: yes/no, Wh-, How long, What exactly"],
              form=[["Structure", "Example", "Common mistake"],
                    ["a/an first mention", "I saw a temple.", "*I saw temple."],
                    ["an + vowel sound", "an ao dai, an hour", "*a ao dai"],
                    ["the + specific", "The temple is old.", "*Temple is old."],
                    ["no article general", "Children love festivals.", "*The children love the festivals."],
                    ["question with do", "Why do people clean?", "*Why people clean?"],
                    ["celebrate by + V-ing", "They celebrate by singing.", "*by sing"]],
              examples=["At Tet, children receive lucky money in a red envelope. The envelope is more "
                        "important than the money."],
              pitfall="Add these six to the classroom wall list."),
    pron=P("Unit 9 sounds review: /θ/ /ð/ and weak articles",
           "Three checks: is the tongue between the teeth? is the final /θ/ in 'month' audible? "
           "are the articles weak?",
           items=["think – this", "month, fourth, eighth", "a lantern, an altar, the temple"],
           drill=["They think this is the third month, and the festival is on the eighth."],
           vn_note="Check all three in the Review 3 block."),
    listening=AUDIO['U9L7'],
    reading=T("The festival that came back",
              ["For nearly fifty years, the village of Dong Ky did not hold its firework festival. "
               "The old men remembered it; the young people had only heard about it.",
               "Then, in the 1990s, three old men decided to write down everything they could "
               "remember: the songs, the order of the procession, even the exact words the leader "
               "says before the fire is lit. It took them two years.",
               "The first new festival was small and, everybody agrees, not very good. The second was "
               "better. Today it attracts thousands of visitors and the village makes and sells "
               "traditional furniture all year because of the people who first came for the festival.",
               "'A tradition does not die when the old people die,' one of the three men said before "
               "he died in 2011. 'It dies when nobody writes it down.'"],
              tasks=[EX("U9.7-R1", "Read and answer", "Answer the questions.",
                        items=["1. How long did the village not hold the festival?",
                               "2. What did the three old men do, and how long did it take?",
                               "3. What was the first new festival like?",
                               "4. What is the economic result today?",
                               "5. Explain the last sentence in your own words."],
                        answers=["1. Nearly fifty years.",
                                 "2. They wrote down everything they could remember about the "
                                 "festival; it took two years.",
                                 "3. Small and not very good.",
                                 "4. The village sells traditional furniture all year because of "
                                 "visitors who first came for the festival.",
                                 "5. A tradition survives if it is recorded; it is lost when nobody "
                                 "writes it down for the next generation."],
                        level="M", kind="reading")]),
    speaking=[EX("U9.7-S1", "Festival Fair", "Present your stand for two minutes and answer visitors' "
                 "questions.",
                 items=["Frame: 'Welcome to our stand. This is… It takes place… People celebrate by… "
                        "It is important because… Any questions?'"],
                 answers=["Marking: content 3, language 3, display 2, presenting/answering 2."],
                 level="D", kind="speaking")],
    writing=[EX("U9.7-W1", "Stand text and quiz", "Write your six sentences and your five quiz "
                "questions with answers.",
                items=["Six sentences: when/where, three activities, food, why it matters.",
                       "Five quiz questions for visitors, with answers on the back."],
                answers=["Model quiz: 1. When does the Lim Festival take place? (13th day of the "
                         "first lunar month) 2. What is it famous for? (Quan Ho singing) "
                         "3. Do the singers use instruments? (No)"],
                level="M", kind="writing", lines=12)],
    communication={"function": "Hosting a stand and answering questions",
                   "phrases": ["Welcome to our stand.", "Would you like to know about…?",
                               "That's a good question.", "Try our quiz!", "Thank you for visiting."],
                   "roleplay": "Half the class hosts while the other half visits; then swap.",
                   "real_life": "Presenting information at a fair, an exhibition or an open day."},
    guided=[EX("U9.7-G1", "Vocabulary race", "Write the word.",
               items=["1. a light children carry: ______", "2. people walking together in the "
                      "street: ______", "3. special clothes: ______",
                      "4. a traditional way of doing something: ______",
                      "5. a very old story: ______", "6. people who visit a country: ______"],
               answers=["1. a lantern", "2. a parade/procession", "3. a costume", "4. a custom",
                        "5. a legend", "6. tourists"], level="E", kind="vocab"),
            EX("U9.7-G2", "Error clinic – the six Unit 9 mistakes", "Correct one mistake in each "
               "sentence.",
               items=["1. I saw temple on the hill.", "2. She wore a ao dai.",
                      "3. The children love the festivals.", "4. Tet is most important festival.",
                      "5. Why people clean the house?",
                      "6. People celebrate by eat special food."],
               answers=["1. I saw a temple on the hill.", "2. She wore an ao dai.",
                        "3. Children love festivals.", "4. Tet is the most important festival.",
                        "5. Why do people clean the house?",
                        "6. People celebrate by eating special food."], level="D", kind="grammar")],
    independent=[EX("U9.7-I1", "Mixed review", "Complete the text with one word in each gap.",
                    text=["Last spring I went to (1) ______ festival in (2) ______ small village near "
                          "Hue. (3) ______ festival takes place once (4) ______ year, in April. "
                          "In (5) ______ morning there was a procession to the temple, where people "
                          "offered (6) ______ fruit and incense. (7) ______ do they do that? "
                          "Because it is a custom to thank the ancestors."],
                    items=["Write the seven words."],
                    answers=["1. a", "2. a", "3. The", "4. a", "5. the", "6. – (no article)",
                             "7. Why"], level="M", kind="grammar"),
                 EX("U9.7-I2", "Project work", "Finish your stand and practise answering questions.",
                    items=[], answers=["Check the articles before display."], level="D", kind="mixed")],
    review=["Festival vocabulary (26 items)", "Articles a/an/the/–", "Question forms",
            "celebrate by + V-ing", "Four-paragraph description", "/θ/ and /ð/"],
    homework=[EX("U9.7-H1", "Vocabulary", "Write 10 words from Unit 9 with Vietnamese meanings.",
                 items=[], answers=["Any 10 of the unit's items."], level="E", kind="vocab"),
              EX("U9.7-H2", "Grammar", "Choose the correct answer.",
                 items=["1. I saw (a / the) temple on the hill for the first time.",
                        "2. She wore (a / an) ao dai.",
                        "3. (The children / Children) love festivals.",
                        "4. Tet is (a / the) most important festival.",
                        "5. Why (do people / people do) clean the house?",
                        "6. They celebrate by (sing / singing)."],
                 answers=["1. a", "2. an", "3. Children", "4. the", "5. do people", "6. singing"],
                 level="M", kind="grammar"),
              EX("U9.7-H3", "Writing", "Write a description (110–120 words) of a festival for the "
                 "class festival book.",
                 items=["Four paragraphs; one sense sentence; check the articles."],
                 answers=["See U9.6-W2 model."], level="D", kind="writing", lines=18),
              EX("U9.7-H4", "Prepare for Unit 10", "Write five sources of energy you know "
                 "(electricity, solar…), in English or Vietnamese.",
                 items=[], answers=["Use them to start Unit 10."], level="E", kind="vocab")],
    workbook=[EX("U9.7-P1", "Crossword clues", "Write the word.",
                 items=["1. A light you carry. (7)", "2. Special clothes. (7)",
                        "3. A very old story. (6)", "4. To keep something for the future. (8)",
                        "5. People who visit a country. (8)"],
                 answers=["1. lantern", "2. costume", "3. legend", "4. preserve", "5. tourists"],
                 level="E", kind="vocab"),
              EX("U9.7-P2", "Mixed grammar", "Put the words in order.",
                 items=["1. place / the / takes / in / festival / April",
                        "2. by / people / lanterns / celebrate / carrying",
                        "3. why / clean / do / people / the house / ?",
                        "4. saw / a / I / temple / on the hill",
                        "5. love / children / festivals"],
                 answers=["1. The festival takes place in April.",
                          "2. People celebrate by carrying lanterns.",
                          "3. Why do people clean the house?", "4. I saw a temple on the hill.",
                          "5. Children love festivals."], level="M", kind="grammar"),
              EX("U9.7-P3", "Reading review", "Read and choose.",
                 text=["UNESCO has recognised several Vietnamese cultural traditions, including "
                       "Quan Ho singing, the Hung Kings worship and the gong culture of the Central "
                       "Highlands. Recognition does not bring much money, but it does bring attention "
                       "— and attention brings students. In Bac Ninh, the number of young people "
                       "learning Quan Ho has more than doubled since 2009, when it was recognised."],
                 items=["1. The text is mainly about A. UNESCO money  B. recognition of Vietnamese "
                        "traditions  C. Bac Ninh province",
                        "2. Recognition mainly brings A. money  B. attention  C. tourists",
                        "3. Since 2009, young Quan Ho learners have A. halved  B. stayed the same  "
                        "C. more than doubled"],
                 answers=["1. B", "2. B", "3. C"], level="M", kind="reading"),
              EX("U9.7-P4", "Unit 9 test yourself (10 marks)", "Answer about yourself (2 marks each).",
                 items=["1. My favourite festival is ______ . It takes place ______ .",
                        "2. People celebrate by ______ .",
                        "3. One custom: it is a custom to ______ .",
                        "4. A question a foreign visitor might ask: ______",
                        "5. One sentence with a, an, the and no article: ______"],
                 answers=["Model: 1. My favourite festival is Tet. It takes place in late January or "
                          "February. 2. People celebrate by visiting their relatives and eating banh "
                          "chung. 3. It is a custom to give lucky money to children. "
                          "4. How long does the holiday last? 5. I bought a lantern at the market and "
                          "the lantern is now in my room, because children love lanterns."],
                 level="D", kind="mixed")],
    procedure=[ST("Warm-up: Article bingo", 6,
                  ["Students write nine nouns; teacher reads phrases; students cross out if the "
                   "article is correct."],
                  "Play bingo with articles.", "Whole class", "Slide 2"),
               ST("Vocabulary and listening review", 7,
                  ["U9.7-G1 race; then the listening quiz U9.7-L1."],
                  "Write words; complete sentences.", "Pairs", "Slides 3–4"),
               ST("Grammar review + error clinic", 10,
                  ["Grammar table; U9.7-G2 in pairs with explanations; add to the wall list."],
                  "Correct and explain six errors.", "Pairs → whole class", "Slides 5–7"),
               ST("Mixed practice", 6, ["U9.7-I1 gap-fill; fast finishers do Workbook P2."],
                  "Complete the text.", "Individual", "Student Book p. U9L7"),
               ST("Project: Festival Fair", 12,
                  ["Groups set up their stands with pictures, six sentences and a five-question quiz.",
                   "Half the class hosts for five minutes while the other half visits; then swap.",
                   "Visitors must ask two questions and try one quiz."],
                  "Host and visit the stands.", "Groups of 4", "Slides 8–10"),
               ST("Wrap-up and homework", 4, ["Vote for the best stand and the best quiz question. "
                                              "Set H1–H4."],
                  "Vote; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Running the Festival Fair",
                     ["Groups 1–3, you are HOSTS first. Stand at your table.",
                      "Groups 4–6, you are VISITORS. Visit two stands, ask two questions at each, "
                      "and try the quiz.",
                      "Hosts: do not read your poster to the visitors. Talk to them. Look at them.",
                      "When I clap, swap. Everybody hosts and everybody visits."]),
                  TK("The last word on articles",
                     ["Look at the wall list. Two of the six errors are articles.",
                      "Before you hand in ANY writing for the rest of this year, do the circle check: "
                      "circle every noun, ask a / the / nothing.",
                      "It takes two minutes and it is the cheapest half-mark in the exam."])],
    support=["Give the error clinic with mistakes underlined.",
             "Provide the six stand sentences as a frame.",
             "Assign the quiz-master role (reading prepared questions)."],
    challenge=["Ask them to answer visitors' questions without notes.",
               "Ask them to prepare two difficult quiz questions.",
               "Ask for 130 words in H3."],
    assessment=["Unit 9 checklist: 5 of 6 'I can' statements", "Error clinic 5 of 6",
                "Hosts the stand and answers two questions"],
    board_plan=["LEFT: festival vocabulary", "CENTRE: Unit 9 grammar table (articles + questions)",
                "RIGHT: fair instructions; Homework H1–H4"],
    materials=["Poster paper, pictures, tape", "Quiz cards", 'Recording: Looking Back — listen again (replay — see the lesson page)'],
)

UNIT.lessons = [L1, L2, L3, L4, L5, L6, L7]

UNIT.revision = [
    EX("R9-1", "Vocabulary", "Complete with a word from Unit 9.",
       items=["1. Children carry a l______ at the Mid-Autumn Festival.",
              "2. People wear traditional c______ .",
              "3. It is a c______ to give lucky money.",
              "4. According to l______ , a dragon lived in the lake.",
              "5. The festival a______ thousands of visitors.",
              "6. Festivals help to p______ our traditions."],
       answers=["1. lantern", "2. costumes", "3. custom", "4. legend", "5. attracts", "6. preserve"],
       level="E", kind="vocab"),
    EX("R9-2", "Grammar: articles", "Complete with a, an, the or – .",
       items=["1. I saw ______ temple on the hill. ______ temple was very old.",
              "2. She wore ______ ao dai.", "3. ______ children love festivals.",
              "4. Tet is ______ most important festival in Viet Nam.",
              "5. We eat ______ rice every day.", "6. ______ moon is very bright tonight."],
       answers=["1. a; The", "2. an", "3. – ", "4. the", "5. – ", "6. The"],
       level="M", kind="grammar"),
    EX("R9-3", "Grammar: questions and chunks", "Write the question or complete the sentence.",
       items=["1. ______ ? – It takes place in April.",
              "2. ______ ? – It lasts three days.",
              "3. ______ ? – Because it is a custom to thank the ancestors.",
              "4. People celebrate ______ (by / carry) lanterns.",
              "5. The festival ______ back more than 300 years."],
       answers=["1. When does it take place?", "2. How long does it last?",
                "3. Why do people do that?", "4. by carrying", "5. dates"],
       level="M", kind="grammar"),
    EX("R9-4", "Reading", "Read and answer.",
       text=["The Perfume Pagoda Festival is the longest festival in Viet Nam: it lasts three months, "
             "from the sixth day of the first lunar month until the end of the third. More than a "
             "million people come. Most take a small boat along the Yen stream and then climb for "
             "two hours to the main cave. Older visitors can now use a cable car, which opened in "
             "2006. Some people say the cable car has spoiled the journey; others say it has allowed "
             "their grandmothers to reach the top for the first time."],
       items=["1. How long does the festival last, and when does it start?",
              "2. How many people come?", "3. How do most people travel?",
              "4. When did the cable car open?",
              "5. Give one argument for and one against the cable car."],
       answers=["1. Three months, from the sixth day of the first lunar month until the end of the "
                "third.", "2. More than a million.",
                "3. By small boat along the Yen stream, then a two-hour climb.", "4. In 2006.",
                "5. Against: it has spoiled the journey. For: it has allowed older people to reach "
                "the top for the first time."], level="M", kind="reading"),
    EX("R9-5", "Writing", "Write a description of a festival (100–120 words) in four paragraphs.",
       items=["Facts – history – what happens – atmosphere and why it matters."],
       answers=["See U9.6-W2 model. Marking: content 3, organisation 2, language 3, articles 1, "
                "length 1."], level="D", kind="writing", lines=18),
]
