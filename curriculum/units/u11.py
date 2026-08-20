# -*- coding: utf-8 -*-
"""UNIT 11 – TRAVELLING IN THE FUTURE  (Periods 77–83)"""
from curriculum.schema import *
from curriculum.audio_sources import AUDIO

UNIT = Unit(
    number=11, title="Travelling in the Future",
    theme="Future transport, travel plans, inventions, journeys",
    can_do=["name eight means of transport of the future",
            "use might to talk about possibility, and will for what I am sure about",
            "use possessive pronouns (mine, yours, his, hers, ours, theirs)",
            "read about future transport and separate facts from opinions",
            "listen to travel announcements and note the key information",
            "write a description of a future journey (110–130 words)"],
    grammar_focus=["might / might not for possibility (contrasted with will / won't)",
                   "Possessive pronouns: mine, yours, his, hers, ours, theirs"],
    pron_focus="Final /l/ (will, travel, hotel, people); stress in three-syllable words",
    vocab_focus="Future transport, travel arrangements, invention vocabulary",
    project={"name": "Design the Transport of 2050",
             "goal": "Groups design a vehicle for the future and present it to a panel of 'investors'.",
             "steps": ["Choose a real problem in your town (traffic jams, floods, long journeys, "
                       "pollution).",
                       "Design one vehicle that solves it. Draw it clearly and label six parts.",
                       "Write eight sentences: what it is, how it works, what it will do, "
                       "what it might do, who it is for, and one problem.",
                       "Prepare a 2-minute pitch. Everyone speaks.",
                       "The class acts as investors and votes with 'money' cards."],
             "marking": "Idea 3 – Language 3 – Design 2 – Pitch 2 (total 10)"})

L1 = Lesson(
    code="U11L1", unit=11, number=1, period=79,
    lesson_type="Getting Started", title="How will we travel?",
    objectives=["name eight means of future transport",
                "understand a conversation about a future journey",
                "make simple predictions about transport",
                "write three sentences about how they will travel in the future"],
    recycled=["Unit 7 transport and distance; Unit 10 will/won't"],
    vocab=[V("electric car", "n", "/ɪˈlektrɪk kɑː/", "ô tô điện", "Electric cars are quiet and clean."),
           V("driverless car", "n", "/ˈdraɪvələs kɑː/", "xe tự lái", "A driverless car has no driver."),
           V("high-speed train", "n", "/ˌhaɪ spiːd ˈtreɪn/", "tàu cao tốc", "A high-speed train travels at 300 km/h."),
           V("bullet train", "n", "/ˈbʊlɪt treɪn/", "tàu siêu tốc", "Japan's bullet train opened in 1964."),
           V("flying car", "n", "/ˈflaɪɪŋ kɑː/", "ô tô bay", "Flying cars still only exist in films."),
           V("solar-powered", "adj", "/ˈsəʊlə ˈpaʊəd/", "chạy bằng năng lượng mặt trời", "A solar-powered boat crossed the ocean."),
           V("underground", "n/adj", "/ˌʌndəˈɡraʊnd/", "tàu điện ngầm", "Hanoi is building an underground line."),
           V("invention", "n", "/ɪnˈvenʃn/", "phát minh", "The bicycle is a wonderful invention.")],
    phrases=["travel by…", "in the future", "at 300 kilometres an hour", "it runs on…",
             "it takes … hours to get to…"],
    grammar=G("Predictions about transport (recycling will from Unit 10)",
              use=["will + bare verb for what you are sure about: Electric cars will be normal.",
                   "won't for negative predictions: Flying cars won't be common.",
                   "will probably / probably won't for softer predictions.",
                   "'run on' describes the fuel: It runs on electricity / on solar power."],
              form=[["Structure", "Example"],
                    ["will + verb", "High-speed trains will connect Hanoi and Ho Chi Minh City."],
                    ["won't + verb", "Petrol cars won't disappear immediately."],
                    ["run on + fuel", "It runs on electricity."],
                    ["it takes … to …", "It takes six hours to get to Hue."]],
              examples=["In twenty years, most buses in our city will run on electricity.",
                        "I don't think flying cars will be normal in my lifetime."],
              pitfall="*It runs by electricity* → 'runs ON electricity'. "
                      "*It will takes six hours* → 'will take'.",
              note="Recycle the Unit 7 chunk 'It takes… to…' inside a will sentence: "
                   "'It will take two hours.'"),
    pron=P("Final /l/ (travel, hotel, will, people)",
           "English /l/ at the end of a word is 'dark': the back of the tongue goes up and the tip "
           "touches behind the top teeth. It must be HEARD: traveLLL, hoteLLL, wiLLL, peopLLL.",
           items=["travel, hotel, will, people, school, animal, table, careful"],
           drill=["People will travel by electric car.",
                  "The hotel is careful with its electrical equipment.",
                  "It'll be a beautiful journey."],
           vn_note="Vietnamese has no final /l/, so learners drop it or turn it into /n/: "
                   "'travel' → 'trave', 'hotel' → 'hoten'. Hold the tongue up at the end."),
    listening=AUDIO['U11L1'],
    reading=T("Four ideas that are already real",
              ["People have been predicting flying cars since 1930. They still do not exist. "
               "But four other ideas, which sounded just as strange, are already working somewhere "
               "in the world.",
               "1. SOLAR BOATS. A Swiss boat called PlanetSolar sailed all the way round the world "
               "using only sunlight. It took 584 days.",
               "2. DRIVERLESS BUSES. Small driverless buses already carry passengers in parts of "
               "Japan, China and France — slowly, on short fixed routes.",
               "3. CABLE CARS AS PUBLIC TRANSPORT. In La Paz, Bolivia, cable cars are not for "
               "tourists: they are the city's main public transport, carrying 300,000 people a day "
               "over the mountains.",
               "4. ELECTRIC MOTORBIKES. In Viet Nam, more than a million electric motorbikes and "
               "scooters are already on the roads, mostly ridden by students.",
               "The lesson is simple: the future usually arrives quietly, in a form nobody put in "
               "a film."],
              tasks=[EX("U11.1-R1", "Read and answer", "Answer the questions.",
                        items=["1. How long have people been predicting flying cars?",
                               "2. How long did PlanetSolar take to sail round the world?",
                               "3. Where do driverless buses already carry passengers?",
                               "4. How many people use the cable cars in La Paz every day?",
                               "5. What is 'the lesson' in the last line?"],
                        answers=["1. Since 1930.", "2. 584 days.",
                                 "3. In parts of Japan, China and France.", "4. 300,000.",
                                 "5. That the future usually arrives quietly, in a form nobody "
                                 "imagined in a film."], level="M", kind="reading")]),
    speaking=[EX("U11.1-S1", "How will you travel?", "Ask your partner four questions.",
                 items=["How will you get to school in 2035? / Will you have a car? / "
                        "Will you fly often? / Will Viet Nam have a high-speed train?"],
                 answers=["Report one answer: 'Nam thinks he'll have an electric motorbike.'"],
                 level="M", kind="speaking")],
    writing=[EX("U11.1-W1", "Sentence writing", "Write three predictions about transport.",
                items=["1. In 2040, most people in my town will ______ .",
                       "2. I don't think ______ .", "3. My family will probably ______ ."],
                answers=["Model: In 2040, most people in my town will ride electric motorbikes. "
                         "I don't think we will have an underground railway. My family will probably "
                         "still use the same old bicycle!"], level="M", kind="writing", lines=4)],
    communication={"function": "Imagining and reacting",
                   "phrases": ["Imagine it's 2050…", "Do you really think so?", "Maybe, but…",
                               "That's science fiction!", "I can't imagine that.",
                               "Where would they land?"],
                   "roleplay": "One student describes a future journey; the other reacts with doubt "
                               "and asks three practical questions.",
                   "real_life": "Imagining, and asking practical questions about big ideas."},
    guided=[EX("U11.1-G1", "Match", "Match the transport with the description.",
               items=["1. driverless car", "2. high-speed train", "3. solar-powered boat",
                      "4. underground", "5. electric motorbike",
                      "a. it travels below the city", "b. it has no driver",
                      "c. it runs on sunlight", "d. it costs about 12,000 dong to charge",
                      "e. it travels at 300 km/h"],
               answers=["1–b", "2–e", "3–c", "4–a", "5–d"], level="E", kind="vocab"),
            EX("U11.1-G2", "run on / take", "Complete the sentences.",
               items=["1. This bus ______ electricity.", "2. It ______ two hours to get to Hai Phong.",
                      "3. The boat ______ solar power.",
                      "4. The high-speed train will ______ five hours.",
                      "5. Most motorbikes still ______ petrol."],
               answers=["1. runs on", "2. takes", "3. runs on", "4. take", "5. run on"],
               level="M", kind="grammar")],
    independent=[EX("U11.1-I1", "Complete the text", "Use the words in the box.",
                    wordbank=["invention", "runs on", "underground", "electric", "takes"],
                    items=["The bicycle is a wonderful (1) ______ : it (2) ______ nothing but your "
                           "legs. In Hanoi, the new (3) ______ line (4) ______ about twenty minutes "
                           "from end to end. In the future most buses in the city will be "
                           "(5) ______ ."],
                    answers=["1. invention", "2. runs on", "3. underground", "4. takes",
                             "5. electric"], level="M", kind="vocab"),
                 EX("U11.1-I2", "Future journey", "Do the imagining role play in pairs.", items=[],
                    answers=["See communication section."], level="D", kind="speaking")],
    review=["8 future transport words", "will / won't for transport predictions",
            "run on + fuel; it takes + time", "final /l/"],
    homework=[EX("U11.1-H1", "Vocabulary", "Write the transport word.",
                 items=["1. a car with no driver: ______", "2. a train at 300 km/h: ______",
                        "3. a railway under the city: ______", "4. a boat that uses sunlight: ______",
                        "5. a car that runs on electricity: ______",
                        "6. a new thing that somebody creates: an ______"],
                 answers=["1. a driverless car", "2. a high-speed/bullet train", "3. the underground",
                          "4. a solar-powered boat", "5. an electric car", "6. invention"],
                 level="E", kind="vocab"),
              EX("U11.1-H2", "Grammar", "Complete with will, won't, runs on or takes.",
                 items=["1. This bus ______ electricity.",
                        "2. It ______ two hours to get to the beach.",
                        "3. Flying cars ______ be normal soon. (–)",
                        "4. Electric motorbikes ______ be everywhere. (+)",
                        "5. The new train ______ five hours from Hanoi to Da Nang. (future)"],
                 answers=["1. runs on", "2. takes", "3. won't", "4. will", "5. will take"],
                 level="M", kind="grammar"),
              EX("U11.1-H3", "Writing", "Write 4 sentences about how you and your family will travel "
                 "in twenty years.",
                 items=["Use will, won't and 'probably'."],
                 answers=["Model: In twenty years my family will probably have an electric car. "
                          "I'll still ride a bicycle for short journeys, because our streets are "
                          "narrow. We won't need to go to the city so often, because my father will "
                          "work from home. I don't think we'll ever have a flying car!"],
                 level="M", kind="writing", lines=5),
              EX("U11.1-H4", "Pronunciation", "Say these words five times with a clear final /l/: "
                 "travel, hotel, will, people, school, careful.",
                 items=["Your tongue must touch behind your top teeth at the end."],
                 answers=["Spot-check in Lesson 2."], level="E", kind="pron")],
    workbook=[EX("U11.1-P1", "Complete the words", "Write the missing letters.",
                 items=["1. i n v _ n t i o n", "2. u n d e r g r _ u n d", "3. d r _ v e r l e s s",
                        "4. e l e c t r _ c", "5. h i g h - s p _ e d"],
                 answers=["1. invention", "2. underground", "3. driverless", "4. electric",
                          "5. high-speed"], level="E", kind="vocab"),
              EX("U11.1-P2", "True or false", "Read the text in the Student Book and write T or F.",
                 items=["1. Flying cars already exist.", "2. PlanetSolar sailed round the world.",
                        "3. Driverless buses travel fast on long routes.",
                        "4. Cable cars are the main public transport in La Paz.",
                        "5. Viet Nam has more than a million electric motorbikes."],
                 answers=["1. F", "2. T", "3. F – slowly, on short fixed routes.", "4. T", "5. T"],
                 level="E", kind="reading"),
              EX("U11.1-P3", "Final /l/", "Underline the words with a final /l/ sound and read them "
                 "aloud.",
                 items=["travel · train · hotel · road · people · plane · school · car · careful · "
                        "table"],
                 answers=["travel, hotel, people, school, careful, table"], level="M", kind="pron"),
              EX("U11.1-P4", "Correct the mistakes", "One mistake per sentence.",
                 items=["1. The bus runs by electricity.", "2. It will takes five hours.",
                        "3. Flying cars will normal soon.", "4. I think it won't happen.",
                        "5. This train travel at 300 km/h."],
                 answers=["1. The bus runs on electricity.", "2. It will take five hours.",
                          "3. Flying cars will be normal soon.",
                          "4. I don't think it will happen.",
                          "5. This train travels at 300 km/h."], level="D", kind="grammar"),
              EX("U11.1-P5", "Writing", "Write 5 sentences describing a journey you often make and "
                 "how it will change in the future.",
                 items=[], answers=["Model: Every day I cycle four kilometres to school, and in the "
                                    "rainy season I arrive completely wet. In ten years I think there "
                                    "will be a covered cycle path along the main road. Electric "
                                    "buses will probably run every fifteen minutes. I don't think "
                                    "the journey will be much faster, but it will certainly be drier "
                                    "and quieter. My grandchildren won't believe that we cycled in "
                                    "the rain."], level="D", kind="writing", lines=6)],
    procedure=[ST("Warm-up: Transport time line", 5,
                  ["Draw a line: 1900 – 2000 – 2050. Students place transport words on it "
                   "(bicycle, plane, electric car, flying car). Recycles Unit 7."],
                  "Place the transport on the time line.", "Whole class", "Slide 2"),
               ST("Presentation: 8 future transport words", 9,
                  ["Pictures; elicit and drill. Mark stress: in'VEN-tion, 'UN-der-ground, "
                   "'DRI-ver-less."],
                  "Repeat; copy with stress marks.", "Whole class", "Slides 3–5"),
               ST("Pronunciation: final /l/", 7,
                  ["Model 'travel' with and without the /l/. Students hold the tongue up.",
                   "Word list drill, then the three sentences."],
                  "Feel the tongue position; repeat.", "Whole class", "Slide 6"),
               ST("Listening: a journey in 2050", 9,
                  ['Play the recording “Lesson 22: Next Summer...” twice (three times if the class asks); students do the listening tasks...” twice (three times if the class asks); students do the listening tasks; read the script in role.'],
                  "Listen and complete.", "Individual → pairs", "Slide 7"),
               ST("Reading + speaking", 10,
                  ["Read 'Four ideas that are already real'; answer R1.",
                   "Then the four-question interview about the future."],
                  "Read, answer, interview.", "Individual → pairs", "Slides 8–10"),
               ST("Wrap-up and homework", 5, ["Class vote: which future transport would you most "
                                              "like? Set H1–H4."],
                  "Vote; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("The future arrives quietly",
                     ["Everybody expects flying cars, because films show flying cars.",
                      "But look at the text: solar boats, driverless buses, cable cars as public "
                      "transport, a million electric motorbikes in Viet Nam. Nobody made a film "
                      "about those.",
                      "So when you predict in this unit, do not only imagine spaceships. "
                      "Look at what is already starting."]),
                  TK("Final /l/",
                     ["Say 'travel'. Now stop before the end: 'trave'. That is what many of us say.",
                      "For the /l/, the tip of your tongue must go UP, behind your top teeth, "
                      "and stay there: traveLLL.",
                      "Hold it for two seconds. Now: hoteLLL, schooLLL, peopLLL, wiLLL.",
                      "It feels strange. Do it anyway — it is in hundreds of common words."])],
    support=["Give picture cards with words printed.",
             "Provide the interview questions on a card.",
             "Accept short answers before full sentences."],
    challenge=["Ask for a reason with every prediction.",
               "Ask them to research one real future transport project in Viet Nam.",
               "Ask them to explain why flying cars are difficult."],
    assessment=["Names 6 of 8 transport words", "Makes three correct will/won't predictions",
                "Audible final /l/ in travel and hotel"],
    board_plan=["LEFT: transport time line", "CENTRE: 8 words with stress; run on / it takes",
                "RIGHT: final /l/ words; Homework H1–H4"],
    materials=["Transport pictures", 'Recording: Lesson 22: Next Summer... — VOA Learning English — Let’s Learn English, Level 1 (3:15)'],
)

L2 = Lesson(
    code="U11L2", unit=11, number=2, period=80,
    lesson_type="A Closer Look 1", title="Describing vehicles and inventions",
    objectives=["use ten adjectives and verbs to describe vehicles",
                "pronounce final /l/ and three-syllable words correctly",
                "describe a vehicle in four sentences",
                "explain what a machine does"],
    recycled=["U11L1 transport vocabulary; Unit 4 comparatives; Unit 10 energy words"],
    vocab=[V("comfortable", "adj", "/ˈkʌmftəbl/", "thoải mái", "The seats are very comfortable."),
           V("convenient", "adj", "/kənˈviːniənt/", "tiện lợi", "The station is convenient for our school."),
           V("reliable", "adj", "/rɪˈlaɪəbl/", "đáng tin cậy", "The old bus is slow but reliable."),
           V("affordable", "adj", "/əˈfɔːdəbl/", "vừa túi tiền", "We need affordable transport."),
           V("pollution-free", "adj", "/pəˈluːʃn friː/", "không gây ô nhiễm", "Bicycles are pollution-free."),
           V("passenger", "n", "/ˈpæsɪndʒə/", "hành khách", "It carries twelve passengers."),
           V("fuel", "n", "/ˈfjuːəl/", "nhiên liệu", "What fuel does it use?"),
           V("charge", "v", "/tʃɑːdʒ/", "sạc", "You charge it at home overnight."),
           V("carry", "v", "/ˈkæri/", "chở", "It can carry two people and a bicycle."),
           V("float", "v", "/fləʊt/", "nổi", "In a flood, it floats.")],
    phrases=["carry X passengers", "run on electricity", "charge it overnight",
             "it can + verb", "it is designed for…"],
    grammar=G("Describing what a machine does: can, it is designed for",
              use=["can + bare verb for ability: It can carry two people. It can float.",
                   "can't for what it cannot do: It can't travel more than 60 kilometres.",
                   "'It is designed for…' + noun / V-ing: It is designed for narrow streets. / "
                   "It is designed for carrying heavy loads.",
                   "Adjectives with -able often describe machines: comfortable, reliable, affordable, "
                   "washable."],
              form=[["Function", "Language", "Example"],
                    ["ability", "can + verb", "It can carry four passengers."],
                    ["limit", "can't + verb", "It can't go faster than 45 km/h."],
                    ["purpose", "It is designed for…", "It is designed for flooded streets."],
                    ["fuel", "It runs on…", "It runs on solar power."]],
              examples=["Our vehicle can carry two passengers and it can float in 50 centimetres "
                        "of water.",
                        "It is designed for the narrow lanes in old towns, so it is only one metre "
                        "wide."],
              pitfall="*It can to carry* (no 'to'), *It cans carry* (no -s), "
                      "*It is designed for carry* (→ 'for carrying' or 'to carry').",
              note="'-able' means 'you can do it': afford + able = you can afford it."),
    pron=P("Three- and four-syllable words; final /l/ again",
           "'COM-for-table (3 syllables, not 4!), con-VE-nient, re-LI-a-ble, a-FFOR-da-ble. "
           "All four end with the dark /l/ or a weak syllable.",
           items=["'comfortable /ˈkʌmftəbl/ (3 syllables)", "con'venient (oOoo)",
                  "re'liable (oOoo)", "a'ffordable (oOoo)"],
           drill=["The new bus is comfortable, convenient and affordable.",
                  "A reliable vehicle is more useful than a beautiful one."],
           vn_note="'Comfortable' is the classic trap: it is NOT com-for-ta-ble (4 syllables). "
                   "English says KUMF-ta-bl. Practise it slowly, then fast."),
    listening=AUDIO['U11L2'],
    reading=T("What makes good transport?",
              ["Ask an engineer what makes good public transport and you will not hear the word "
               "'fast' first. You will hear four other words.",
               "RELIABLE. A bus that comes every twenty minutes, always, is more useful than a bus "
               "that sometimes comes in five minutes and sometimes in an hour. People can plan "
               "around 'always'.",
               "AFFORDABLE. If a journey costs more than about ten per cent of a daily wage, "
               "people will walk instead — however comfortable the bus is.",
               "CONVENIENT. A station four hundred metres from your house is used; a station two "
               "kilometres away, with no path, is not.",
               "SAFE. Parents decide how children travel. If a route feels dangerous, a child will "
               "not be allowed to use it, whatever the timetable says.",
               "Speed matters too, of course. But a slow bus that comes every ten minutes beats "
               "a fast one that comes twice a day."],
              tasks=[EX("U11.2-R1", "Read and answer", "Answer the questions.",
                        items=["1. What four words does an engineer say first?",
                               "2. Why is a regular bus better than a sometimes-fast one?",
                               "3. What happens if a journey costs too much?",
                               "4. Why does the writer mention parents?",
                               "5. Explain the last sentence."],
                        answers=["1. Reliable, affordable, convenient, safe.",
                                 "2. Because people can plan around 'always'.",
                                 "3. People will walk instead.",
                                 "4. Because parents decide how children travel, and they will not "
                                 "allow a route that feels dangerous.",
                                 "5. Frequency is more useful than top speed: a slow but frequent "
                                 "service is better than a fast, rare one."], level="M", kind="reading")]),
    speaking=[EX("U11.2-S1", "Describe the vehicle", "Look at a picture card and describe the "
                 "vehicle in four sentences.",
                 items=["What it is / what it can do / what it runs on / who it is for"],
                 answers=["Model: It's a small electric three-wheeler. It can carry two passengers "
                          "and a lot of boxes. It runs on electricity and you charge it overnight. "
                          "It is designed for narrow streets in old towns."],
                 level="M", kind="speaking"),
              EX("U11.2-S2", "Which is best?", "In fours, rank four vehicles for YOUR town using the "
                 "four criteria (reliable, affordable, convenient, safe).",
                 items=["Vehicles: electric bus / cable car / bicycle path / underground"],
                 answers=["Model: For our town the bicycle path is best because it is the most "
                          "affordable and the safest for children, although it is not fast."],
                 level="D", kind="speaking")],
    writing=[EX("U11.2-W1", "Describe an invention", "Write four sentences about a vehicle you know "
                "or imagine.",
                items=["1. What it is: ______", "2. What it can do (2 things): ______",
                       "3. What it runs on: ______", "4. Who it is designed for: ______"],
                answers=["Model: It is a small electric boat. It can carry eight passengers and it "
                         "can travel for six hours. It runs on solar panels on the roof. It is "
                         "designed for tourists in the Mekong Delta, where noisy engines frighten "
                         "the birds."], level="M", kind="writing", lines=6)],
    communication={"function": "Explaining how something works",
                   "phrases": ["It works like this…", "First you…, then it…", "It can…",
                               "The clever part is…", "The problem is…"],
                   "roleplay": "Explain a simple machine (a bicycle, a fan, a lift) to somebody who "
                               "has never seen one.",
                   "real_life": "Explaining a machine or a product clearly."},
    guided=[EX("U11.2-G1", "Which adjective?", "Complete with comfortable, convenient, reliable, "
               "affordable, pollution-free.",
               items=["1. The bus always comes on time — it is very ______ .",
                      "2. The seats are soft and wide: very ______ .",
                      "3. It only costs 5,000 dong, so it is ______ for everybody.",
                      "4. The station is 200 metres from my house, which is very ______ .",
                      "5. A bicycle produces no smoke, so it is ______ ."],
               answers=["1. reliable", "2. comfortable", "3. affordable", "4. convenient",
                        "5. pollution-free"], level="E", kind="vocab"),
            EX("U11.2-G2", "can / can't / is designed for", "Complete the description.",
               items=["1. It ______ carry four passengers.",
                      "2. It ______ travel more than 80 kilometres.  (limit)",
                      "3. It ______ narrow streets.  (purpose)",
                      "4. It ______ float in 50 centimetres of water."],
               answers=["1. can", "2. can't", "3. is designed for", "4. can"],
               level="M", kind="grammar")],
    independent=[EX("U11.2-I1", "Error clinic", "Correct one mistake in each sentence.",
                    items=["1. It can to carry four people.", "2. It cans float.",
                           "3. It is designed for carry heavy boxes.",
                           "4. The bus runs by electricity.", "5. This car is very confortable."],
                    answers=["1. It can carry four people.", "2. It can float.",
                             "3. It is designed for carrying heavy boxes. / …designed to carry…",
                             "4. The bus runs on electricity.",
                             "5. This car is very comfortable."], level="D", kind="grammar"),
                 EX("U11.2-I2", "Rank the vehicles", "Do U11.2-S2 and report your group's choice "
                    "with two reasons.", items=[], answers=["See U11.2-S2."], level="D",
                    kind="speaking")],
    review=["10 vehicle adjectives and verbs", "can / can't + bare verb; is designed for",
            "three-syllable stress and final /l/"],
    homework=[EX("U11.2-H1", "Vocabulary", "Complete with passenger, fuel, charge, carry, float.",
                 items=["1. The bus can ______ forty people.", "2. Every ______ must wear a seat belt.",
                        "3. What ______ does it use?", "4. You ______ it overnight at home.",
                        "5. In a flood, the small boat can ______ ."],
                 answers=["1. carry", "2. passenger", "3. fuel", "4. charge", "5. float"],
                 level="E", kind="vocab"),
              EX("U11.2-H2", "Grammar", "Write four sentences about a vehicle using can, can't, "
                 "runs on and is designed for.",
                 items=[], answers=["Model: Our vehicle can carry two passengers. It can't travel "
                                    "more than 60 kilometres without charging. It runs on "
                                    "electricity. It is designed for students who live in villages "
                                    "far from school."], level="M", kind="grammar"),
              EX("U11.2-H3", "Writing", "Write a description (70–80 words) of the best kind of "
                 "transport for your town.",
                 items=["Use at least three of the four adjectives (reliable, affordable, convenient, "
                        "safe) with reasons."],
                 answers=["Model: In my opinion, the best transport for my town would be a good "
                          "bicycle path along the main road. It would be affordable, because a "
                          "bicycle costs far less than a motorbike. It would be convenient, because "
                          "almost everybody lives within three kilometres of the school. Most "
                          "importantly it would be safe, so parents would allow younger children to "
                          "use it. It wouldn't be fast, but in a town this size that hardly matters. "
                          "(80 words)"], level="D", kind="writing", lines=10),
              EX("U11.2-H4", "Pronunciation", "Say these four words five times: comfortable "
                 "(3 syllables!), convenient, reliable, affordable.",
                 items=[], answers=["Spot-check in Lesson 3."], level="M", kind="pron")],
    workbook=[EX("U11.2-P1", "Match", "Match the adjective with the meaning.",
                 items=["1. reliable", "2. affordable", "3. convenient", "4. comfortable",
                        "5. pollution-free",
                        "a. easy to reach and use", "b. it never breaks down",
                        "c. it produces no smoke", "d. nice to sit in", "e. cheap enough"],
                 answers=["1–b", "2–e", "3–a", "4–d", "5–c"], level="E", kind="vocab"),
              EX("U11.2-P2", "can or can't?", "Complete the description of a small electric van.",
                 items=["1. It ______ carry 500 kilos.", "2. It ______ travel more than 100 km "
                        "on one charge.", "3. It ______ go up steep hills easily.",
                        "4. It ______ park in a very small space.",
                        "5. It ______ be used on the motorway (only 45 km/h)."],
                 answers=["1. can", "2. can't", "3. can (or can't — accept with a reason)",
                          "4. can", "5. can't"], level="M", kind="grammar"),
              EX("U11.2-P3", "Word stress", "Write the stress pattern (Ooo, oOoo…).",
                 items=["1. comfortable ___", "2. convenient ___", "3. reliable ___",
                        "4. affordable ___", "5. passenger ___"],
                 answers=["1. Ooo (KUMF-ta-bl)", "2. oOoo", "3. oOoo", "4. oOoo", "5. Ooo"],
                 level="D", kind="pron"),
              EX("U11.2-P4", "Reading", "Read and answer.",
                 text=["An electric motorbike costs about 30 million dong in Viet Nam — roughly the "
                       "same as a petrol one. The difference is what happens next. A petrol bike "
                       "costs around 40,000 dong a day in fuel for a student who travels 20 "
                       "kilometres. An electric bike costs about 3,000 dong to charge for the same "
                       "distance. Over three years, that is a saving of more than 40 million dong — "
                       "more than the bike itself."],
                 items=["1. How much does each kind of bike cost to buy?",
                        "2. How much does each cost per day for 20 km?",
                        "3. What is the saving over three years?",
                        "4. What does the writer mean by 'more than the bike itself'?"],
                 answers=["1. Both about 30 million dong.", "2. Petrol about 40,000 dong; "
                          "electric about 3,000 dong.", "3. More than 40 million dong.",
                          "4. The fuel saving is bigger than the price of the bike."],
                 level="M", kind="reading"),
              EX("U11.2-P5", "Writing", "Describe an invention you would like to exist (80–90 words).",
                 items=["What it is / what it can do / what it runs on / who it is for / "
                        "one problem."],
                 answers=["Model: I would like somebody to invent a small folding roof for bicycles. "
                          "It would open like an umbrella above the rider, so you could cycle in the "
                          "rain without getting wet. It would need no fuel at all — just your hand to "
                          "open it. It is designed for students in cities like mine, where the rainy "
                          "season lasts four months. The problem is the wind: on a windy day the roof "
                          "would push you sideways. (86 words)"], level="D", kind="writing", lines=10)],
    procedure=[ST("Warm-up: Transport word race", 5,
                  ["Teams write as many transport words as possible in 60 seconds. "
                   "Recycles Unit 7 and Lesson 1."],
                  "Write words in teams.", "Teams", "Slide 2"),
               ST("Presentation: describing vehicles", 10,
                  ["Show a picture of an unusual vehicle. Elicit: what is it? what can it do? "
                   "what does it run on? who is it for?",
                   "Present the four -able adjectives with definitions.",
                   "Drill 'comfortable' as three syllables."],
                  "Repeat; copy the description frame.", "Whole class", "Slides 3–6"),
               ST("Listening: the science fair", 10,
                  ['Play the recording “Can — talking about abilities” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; then the matching task.'],
                  "Listen and complete the notes.", "Individual → pairs", "Slide 7"),
               ST("Reading + guided practice", 8,
                  ["Read 'What makes good transport?'; answer R1. Then U11.2-G1 and G2."],
                  "Read, answer, complete.", "Individual → pairs", "Slide 8"),
               ST("Speaking: describe and rank", 9,
                  ["Picture cards: describe a vehicle in four sentences. Then rank four options "
                   "for your town."],
                  "Describe and rank with reasons.", "Pairs → fours", "Slides 9–10"),
               ST("Wrap-up and homework", 3, ["Error clinic U11.2-I1 orally. Set H1–H4."],
                  "Correct the errors.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Fast is not the most important word",
                     ["If I ask you 'what makes good transport?', most of you say FAST.",
                      "But look at the text: reliable, affordable, convenient, safe. Speed is fifth.",
                      "Think about your own journey. Would you prefer a bus that is very fast twice "
                      "a day, or a slow one every ten minutes?",
                      "Remember this in your project: an idea that is affordable and reliable will "
                      "win more votes than an idea that is only fast."]),
                  TK("Comfortable has three syllables",
                     ["Write it on the board: c-o-m-f-o-r-t-a-b-l-e. Eleven letters. "
                      "How many syllables? Most students say four: com-for-ta-ble.",
                      "English says THREE: KUMF-ta-bl. The 'or' almost disappears.",
                      "Say it slowly: KUMF … ta … bl. Now normal speed: comfortable.",
                      "Same family: vegetable is VEJ-ta-bl, not ve-ge-ta-ble."])],
    support=["Give the description frame on a card.",
             "Provide picture cards with the vocabulary labelled.",
             "Reduce the ranking to two options."],
    challenge=["Ask them to add a disadvantage to every description.",
               "Ask them to rank all four options with reasons.",
               "Ask for the electric vs petrol calculation in P4."],
    assessment=["5 of 5 correct adjectives", "Describes a vehicle in four correct sentences",
                "'Comfortable' with three syllables"],
    board_plan=["LEFT: 10 vehicle words", "CENTRE: description frame (what / can / runs on / "
                "designed for)", "RIGHT: reliable–affordable–convenient–safe; Homework H1–H4"],
    materials=["Vehicle picture cards", 'Recording: Can — talking about abilities — ELLLO — Sound Grammar (2:00)'],
)

L3 = Lesson(
    code="U11L3", unit=11, number=3, period=81,
    lesson_type="A Closer Look 2", title="might for possibility; possessive pronouns",
    objectives=["use might and might not to talk about possibility",
                "choose between will (sure) and might (possible)",
                "use possessive pronouns (mine, yours, his, hers, ours, theirs)",
                "talk about what might happen in the future"],
    recycled=["U11L1–L2 transport vocabulary; Unit 10 will/won't; Unit 6 possessive adjectives"],
    vocab=[V("possible", "adj", "/ˈpɒsəbl/", "có thể", "It's possible, but not certain."),
           V("certain", "adj", "/ˈsɜːtn/", "chắc chắn", "Nothing is certain about the future."),
           V("maybe", "adv", "/ˈmeɪbi/", "có lẽ", "Maybe we'll have flying cars one day."),
           V("perhaps", "adv", "/pəˈhæps/", "có lẽ", "Perhaps it will rain."),
           V("belong to", "v phr", "/bɪˈlɒŋ tuː/", "thuộc về", "This bag belongs to Mai."),
           V("own", "v/adj", "/əʊn/", "sở hữu; riêng", "One day I'll own my own bicycle.")],
    phrases=["It might rain.", "I might not come.", "Whose is this?", "It's mine / yours / hers.",
             "It belongs to…"],
    grammar=G("might / might not; possessive pronouns",
              use=["MIGHT + bare verb = it is POSSIBLE, but I am not sure: It might rain tomorrow.",
                   "MIGHT NOT = it is possible that it will not happen: She might not come.",
                   "Compare: WILL = I am sure. MIGHT = maybe (about 50%).",
                   "Might never changes and never takes 'to' (like will and must).",
                   "POSSESSIVE PRONOUNS replace 'my bag': mine, yours, his, hers, ours, theirs. "
                   "No noun after them!",
                   "Question: Whose is this? / Whose bag is this? – It's mine."],
              form=[["Certainty", "Structure", "Example"],
                    ["sure (100%)", "will / won't", "Electric cars will be normal."],
                    ["possible (50%)", "might / might not", "Flying cars might exist in 2100."],
                    ["Possessive adjective", "+ noun", "This is MY bag."],
                    ["Possessive pronoun", "no noun", "This bag is MINE."],
                    ["Question", "Whose…?", "Whose is this? – It's hers."]],
              examples=["We might have an underground railway in twenty years, but I'm not sure.",
                        "It might not be finished before 2040.",
                        "That's not your helmet — yours is red. This one is mine."],
              pitfall="Two errors: (1) *It might to rain* / *It mights rain* — might never changes; "
                      "(2) *This is mine bag* — a possessive pronoun stands ALONE: "
                      "'This bag is mine' or 'This is my bag'.",
              note="Vietnamese uses 'của tôi' in both positions, so students mix 'my' and 'mine'. "
                   "Rule: noun after it → my. No noun → mine."),
    pron=P("might /maɪt/ and possessive pronouns; final /n/ vs /ŋ/",
           "'Might' has the /aɪ/ from Unit 7 and a clear final /t/. Possessive pronouns end in /z/: "
           "hers /hɜːz/, ours /aʊəz/, theirs /ðeəz/, yours /jɔːz/ — do not lose the /z/!",
           items=["might /maɪt/", "mine /maɪn/", "hers /hɜːz/", "ours /aʊəz/", "theirs /ðeəz/",
                  "yours /jɔːz/"],
           drill=["It might rain, so take mine.",
                  "That bike is hers; ours is over there and theirs is at home."],
           vn_note="The final /z/ in hers, ours, theirs, yours is almost always dropped. "
                   "Hold it: hers-zzz."),
    listening=AUDIO['U11L3'],
    reading=T("Six predictions: how sure are they?",
              ["Scientists are careful people. When they talk about the future, they choose their "
               "words exactly. Here are six statements about transport in 2060, in order from "
               "'certain' to 'possible'.",
               "1. There WILL be more people in cities than today. (Certain — the children are "
               "already born.)",
               "2. Most new cars WILL be electric. (Almost certain — many countries have already "
               "made laws.)",
               "3. Viet Nam WILL have a high-speed railway. (Very likely — it is being built.)",
               "4. Most people MIGHT work from home two days a week. (Possible — it depends on jobs "
               "and on companies.)",
               "5. Small aeroplanes MIGHT be electric. (Possible — batteries are still too heavy.)",
               "6. Flying cars MIGHT exist for ordinary families. (Possible, but not likely — "
               "and where would they land?)",
               "Notice the pattern: 'will' for what has already started; 'might' for what depends on "
               "decisions nobody has made yet."],
              tasks=[EX("U11.3-R1", "Read and answer", "Answer the questions.",
                        items=["1. Why is prediction 1 certain?",
                               "2. Why is prediction 2 almost certain?",
                               "3. What does prediction 4 depend on?",
                               "4. What is the problem with electric aeroplanes?",
                               "5. What is the pattern the writer describes at the end?"],
                        answers=["1. Because the children who will live in those cities are already "
                                 "born.",
                                 "2. Because many countries have already made laws.",
                                 "3. On jobs and on companies.",
                                 "4. Batteries are still too heavy.",
                                 "5. 'Will' is used for what has already started; 'might' for what "
                                 "depends on decisions nobody has made yet."],
                        level="M", kind="reading")]),
    speaking=[EX("U11.3-S1", "Sure or not sure?", "Say each sentence twice: once with will "
                 "(you are sure), once with might (you are not sure).",
                 items=["1. rain tomorrow", "2. our school gets solar panels",
                        "3. I go to university in Hanoi", "4. flying cars exist in 2060",
                        "5. our town builds a bicycle path"],
                 answers=["Model: It will rain tomorrow. / It might rain tomorrow."],
                 level="E", kind="speaking"),
              EX("U11.3-S2", "Whose is it?", "Put five objects on the desk. Ask and answer with "
                 "possessive pronouns.",
                 items=["A: Whose is this pen?  B: It might be Nam's. / It's mine. / "
                        "It isn't mine — mine is blue."],
                 answers=["Insist: no noun after mine, yours, hers."], level="M", kind="speaking")],
    writing=[EX("U11.3-W1", "will or might?", "Complete with will, won't, might or might not.",
                items=["1. The sun ______ rise tomorrow. (certain)",
                       "2. It ______ rain this afternoon. (possible)",
                       "3. I ______ come to the party — I'm not sure yet.",
                       "4. Flying cars ______ be normal in ten years. (certain: no)",
                       "5. Our school ______ get new computers next year. (possible)"],
                answers=["1. will", "2. might", "3. might", "4. won't", "5. might"],
                level="M", kind="writing")],
    communication={"function": "Talking about uncertain plans",
                   "phrases": ["I'm not sure yet.", "It depends on…", "I might…", "Maybe.",
                               "Probably not.", "Let's see."],
                   "roleplay": "A invites B to three events. B is certain about one, unsure about "
                               "one and refuses one.",
                   "real_life": "Answering honestly when you do not know yet."},
    guided=[EX("U11.3-G1", "might or might not?", "Complete the sentences.",
               items=["1. Take an umbrella — it ______ rain.",
                      "2. She ______ come; she has a test tomorrow.",
                      "3. We ______ finish before six, but I doubt it.",
                      "4. He ______ be at home — his light is on.",
                      "5. They ______ know the answer; nobody told them."],
               answers=["1. might", "2. might not", "3. might", "4. might", "5. might not"],
               level="E", kind="grammar"),
            EX("U11.3-G2", "my or mine?", "Complete with the correct word.",
               items=["1. This is ______ bag. (my/mine)", "2. This bag is ______ . (my/mine)",
                      "3. Is this ______ helmet? (your/yours)",
                      "4. That helmet is ______ . (her/hers)",
                      "5. ______ house is bigger than ______ . (our/ours … their/theirs)"],
               answers=["1. my", "2. mine", "3. your", "4. hers", "5. Our … theirs"],
               level="M", kind="grammar")],
    independent=[EX("U11.3-I1", "Error clinic", "Correct one mistake in each sentence.",
                    items=["1. It mights rain tomorrow.", "2. She might to come.",
                           "3. This is mine bag.", "4. That book is her.",
                           "5. Whose is this? – Is my.", "6. They might not to finish."],
                    answers=["1. It might rain tomorrow.", "2. She might come.",
                             "3. This is my bag. / This bag is mine.", "4. That book is hers.",
                             "5. Whose is this? – It's mine.", "6. They might not finish."],
                    level="D", kind="grammar",
                    note="MIGHT never changes and never takes 'to'. Possessive pronouns stand alone."),
                 EX("U11.3-I2", "Uncertain plans", "Ask five classmates about next weekend. "
                    "Note who is sure and who is not.",
                    items=["A: What are you doing on Sunday?  B: I might visit my grandmother, "
                           "but I'm not sure."],
                    answers=["Report: 'Two students are certain; three said might.'"],
                    level="D", kind="speaking")],
    review=["might / might not = possible; will / won't = sure",
            "might never changes and never takes 'to'",
            "possessive pronouns stand alone: mine, yours, his, hers, ours, theirs"],
    homework=[EX("U11.3-H1", "Grammar", "Complete with will, won't, might or might not.",
                 items=["1. I ______ go to the cinema tonight — it depends on my homework.",
                        "2. The sun ______ rise at six tomorrow. (certain)",
                        "3. Flying cars ______ be common in ten years. (certain: no)",
                        "4. It ______ snow in Sa Pa this winter — it sometimes does.",
                        "5. She ______ come to the party; she is ill."],
                 answers=["1. might", "2. will", "3. won't", "4. might", "5. might not"],
                 level="M", kind="grammar"),
              EX("U11.3-H2", "Grammar", "Rewrite using a possessive pronoun.",
                 items=["1. This is my bicycle. → This bicycle is ______ .",
                        "2. That is her helmet. → That helmet is ______ .",
                        "3. These are our books. → These books are ______ .",
                        "4. Is this your bag? → Is this bag ______ ?",
                        "5. That is their house. → That house is ______ ."],
                 answers=["1. mine", "2. hers", "3. ours", "4. yours", "5. theirs"],
                 level="M", kind="grammar"),
              EX("U11.3-H3", "Writing", "Write 5 sentences about next month: two things you are sure "
                 "about (will) and three things that are possible (might).",
                 items=[], answers=["Model: Next month we will have our end-of-term test — the date "
                                    "is already on the wall. My cousin will get married on the "
                                    "fifteenth. I might go to Da Nang with my family, but my father "
                                    "isn't sure about his work. Our class might visit the museum. "
                                    "I might start learning the guitar, if I can borrow one."],
                 level="M", kind="writing", lines=7),
              EX("U11.3-H4", "Pronunciation", "Say these five words five times with a clear final "
                 "/z/: hers, ours, theirs, yours, mine (/n/).",
                 items=[], answers=["Spot-check in Lesson 4."], level="E", kind="pron")],
    workbook=[EX("U11.3-P1", "will or might?", "Choose the correct word.",
                 items=["1. The sun (will / might) rise tomorrow.",
                        "2. It (will / might) rain — the sky is grey.",
                        "3. I'm not sure. I (will / might) come.",
                        "4. Water (will / might) boil at 100 degrees.",
                        "5. Our team (will / might) win — the other team is very good."],
                 answers=["1. will", "2. might", "3. might", "4. will", "5. might"],
                 level="E", kind="grammar"),
              EX("U11.3-P2", "Possessive adjectives and pronouns", "Complete the table.",
                 items=["I – my – ______", "you – ______ – yours", "he – his – ______",
                        "she – ______ – hers", "we – our – ______", "they – ______ – theirs"],
                 answers=["mine", "your", "his", "her", "ours", "their"],
                 level="E", kind="grammar"),
              EX("U11.3-P3", "Complete the dialogue", "Use might, mine, yours, hers or his.",
                 items=["A: Whose helmet is this? Is it (1) ______ ?",
                        "B: No, (2) ______ is blue. It (3) ______ be Nam's.",
                        "A: No, (4) ______ is at home. Maybe it's Mai's.",
                        "B: Yes, it looks like (5) ______ . She (6) ______ come back for it."],
                 answers=["1. yours", "2. mine", "3. might", "4. his", "5. hers", "6. might"],
                 level="M", kind="mixed"),
              EX("U11.3-P4", "Correct the mistakes", "One mistake per sentence.",
                 items=["1. It mights be cold tonight.", "2. She might to arrive late.",
                        "3. This is mine pen.", "4. That bag is her.",
                        "5. Ours house is near the school."],
                 answers=["1. It might be cold tonight.", "2. She might arrive late.",
                          "3. This is my pen. / This pen is mine.", "4. That bag is hers.",
                          "5. Our house is near the school."], level="D", kind="grammar"),
              EX("U11.3-P5", "Writing", "Write 6 predictions about your town in 2060: three with "
                 "will/won't and three with might.",
                 items=["Explain why you are sure or not sure."],
                 answers=["Model: My town will certainly be bigger, because new factories are already "
                          "being built. There will be more electric motorbikes than petrol ones. "
                          "The old market won't disappear — people love it too much. We might get a "
                          "train station, but it depends on the government. The river might be "
                          "cleaner if the factories are careful. And I might still be living here, "
                          "although I don't know yet."], level="D", kind="writing", lines=8)],
    procedure=[ST("Warm-up: Sure or not?", 5,
                  ["Teacher makes ten statements about tomorrow; students show 100% (thumb up) or "
                   "50% (flat hand)."],
                  "Judge the certainty.", "Whole class", "Slide 2"),
               ST("Presentation: might", 10,
                  ["Draw a certainty line: 100% WILL — 50% MIGHT — 0% WON'T.",
                   "Give six sentences and place them on the line with the class.",
                   "Form: might + bare verb, same for everybody, negative = might not.",
                   "Drill: 'It might rain', 'She might not come'."],
                  "Copy the line; produce six sentences.", "Whole class", "Slides 3–5"),
               ST("Presentation: possessive pronouns", 9,
                  ["Collect five objects from students. 'Whose is this?' 'It's mine / hers / his.'",
                   "Build the table: my–mine, your–yours, his–his, her–hers, our–ours, their–theirs.",
                   "Key rule on the board: NOUN after it → my. NO NOUN → mine."],
                  "Repeat; copy the table; play 'Whose is it?'.", "Whole class", "Slides 6–7"),
               ST("Guided practice", 8, ["U11.3-G1, G2, W1; error clinic U11.3-I1."],
                  "Complete and correct.", "Pairs", "Student Book p. U11L3"),
               ST("Listening + speaking", 10,
                  ["Play the three conversations; do both tasks. Then the weekend survey (U11.3-I2)."],
                  "Listen, classify, survey.", "Individual → mingle", "Slides 8–10"),
               ST("Wrap-up and homework", 3, ["Three students report an uncertain plan. Set H1–H4."],
                  "Report; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("The certainty line",
                     ["Draw a line in your notebook. On the left: 0%. In the middle: 50%. "
                      "On the right: 100%.",
                      "100% — I am sure — WILL. 'The sun will rise tomorrow.'",
                      "0% — I am sure it won't — WON'T. 'Our school won't close tomorrow.'",
                      "50% — maybe yes, maybe no — MIGHT. 'It might rain this afternoon.'",
                      "In real life most of the future is 50%. So 'might' is a very honest word — "
                      "and honest English sounds better than confident wrong English."]),
                  TK("my or mine?",
                     ["One simple test. Is there a noun after it? Then use MY, YOUR, HER.",
                      "'This is MY bag.' Bag comes after. My.",
                      "No noun after it? Then MINE, YOURS, HERS.",
                      "'This bag is MINE.' Nothing comes after. Mine.",
                      "In Vietnamese it is 'của tôi' both times, so we must think for one second. "
                      "Noun after → my. Nothing after → mine."])],
    support=["Give the certainty line with three examples in place.",
             "Provide the possessive table half-completed.",
             "Reduce the error clinic to four sentences."],
    challenge=["Add 'may' as a more formal alternative to might.",
               "Ask them to explain why the writer used might in each of the six predictions.",
               "Ask for a paragraph with three wills and three mights."],
    assessment=["5 of 5 correct might/might not", "5 of 5 correct possessive pronouns",
                "Final /z/ audible in hers, ours, theirs"],
    board_plan=["LEFT: certainty line 0% – 50% – 100%",
                "CENTRE: might + BARE VERB (no -s, no to)",
                "RIGHT: my + noun | mine (alone); Homework H1–H4"],
    materials=["Five student objects for the 'Whose is it?' game", 'Recording: May and might — ELLLO — Sound Grammar (3:03)'],
)

L4 = Lesson(
    code="U11L4", unit=11, number=4, period=82,
    lesson_type="Communication", title="Everyday English: travelling and asking for information",
    objectives=["ask for travel information at a station or bus stop",
                "buy a ticket and understand times and platforms",
                "take part in an 8-turn travel role play",
                "write a short message about travel arrangements"],
    recycled=["U11L1–L3 transport vocabulary, might; Unit 7 distance and time; "
              "Unit 5 polite requests"],
    vocab=[V("platform", "n", "/ˈplætfɔːm/", "sân ga", "The train leaves from platform three."),
           V("return ticket", "n", "/rɪˈtɜːn ˈtɪkɪt/", "vé khứ hồi", "A return ticket is cheaper."),
           V("single ticket", "n", "/ˈsɪŋɡl ˈtɪkɪt/", "vé một chiều", "One single to Hai Phong, please."),
           V("depart", "v", "/dɪˈpɑːt/", "khởi hành", "The bus departs at 7.15."),
           V("arrive", "v", "/əˈraɪv/", "đến", "It arrives at 9.40."),
           V("delayed", "adj", "/dɪˈleɪd/", "bị hoãn", "The train is delayed by twenty minutes.")],
    phrases=["What time does the … leave?", "How much is a return to…?", "Which platform?",
             "Is there a bus to…?", "The train is delayed.", "Have a good journey!"],
    grammar=G("Timetable language: present simple for schedules",
              use=["Timetables use the PRESENT SIMPLE, even for the future: "
                   "The train LEAVES at seven. The bus ARRIVES at ten.",
                   "This is the same rule as school timetables in Unit 6.",
                   "Questions: What time does the train leave? When does it arrive? "
                   "How long does the journey take?",
                   "For a change of plan, use will or might: 'It might be late.'"],
              form=[["Function", "Language", "Example"],
                    ["schedule", "present simple", "The bus leaves at 7.15."],
                    ["question", "What time does…?", "What time does the last train leave?"],
                    ["duration", "How long does it take?", "About four hours."],
                    ["problem", "It is delayed / might be late", "The train is delayed by 20 minutes."]],
              examples=["The 7.15 bus arrives in Hai Phong at 9.40, so it takes two hours "
                        "twenty-five minutes.",
                        "Excuse me, which platform does the Hue train leave from?"],
              pitfall="*What time the train leaves?* (missing 'does'), "
                      "*The train will leave at seven* for a fixed timetable "
                      "(use the present simple: 'leaves')."),
    pron=P("Times, numbers and the final /m/ in 'platform'",
           "Practise: seven fifteen, nine forty, half past six, a quarter to eight, platform three. "
           "Keep the -teen / -ty difference clear (Unit 8).",
           items=["7.15 = seven fifteen", "9.40 = nine forty", "platform /ˈplætfɔːm/",
                  "thirteen – thirty, fourteen – forty"],
           drill=["The seven fifteen bus arrives at nine forty.",
                  "The Hue train leaves from platform thirteen — no, platform thirty!"],
           vn_note="Getting on the wrong platform because of thirteen/thirty is a real risk. "
                   "Drill the pair until it is automatic."),
    listening=AUDIO['U11L4'],
    reading=T("A message about a journey",
              ["Hi Nam,",
               "Here are the details for Saturday.",
               "My bus leaves Nam Dinh at 6.45 in the morning and arrives at Giap Bat station in "
               "Hanoi at about 9.15 — but Saturday traffic is bad, so it might be later.",
               "From Giap Bat, take bus number 8 to the Old Quarter. It runs every fifteen minutes "
               "and the journey takes about forty minutes. A ticket is 7,000 dong — have the exact "
               "money if you can.",
               "I'll wait for you at the bookshop on the corner of Hang Bong and Hang Gai. "
               "If I'm late, don't worry — I might be stuck in the traffic. Wait ten minutes, "
               "then call me.",
               "Bring an umbrella. It might rain in the afternoon and everything in the Old Quarter "
               "is outside.",
               "See you on Saturday!",
               "Mai"],
              tasks=[EX("U11.4-R1", "Read and answer", "Answer the questions.",
                        items=["1. What time does Mai's bus leave and arrive?",
                               "2. Why might it be later?",
                               "3. Which bus should Nam take, and how often does it run?",
                               "4. Where exactly will they meet?",
                               "5. What two pieces of advice does Mai give?"],
                        answers=["1. It leaves Nam Dinh at 6.45 and arrives at about 9.15.",
                                 "2. Because Saturday traffic is bad.",
                                 "3. Bus number 8, every fifteen minutes.",
                                 "4. At the bookshop on the corner of Hang Bong and Hang Gai.",
                                 "5. Have the exact money for the ticket; bring an umbrella "
                                 "(and wait ten minutes then call)."], level="M", kind="reading")]),
    speaking=[EX("U11.4-S1", "At the ticket office", "Use the timetable. A is the clerk, B is the "
                 "traveller. Ask about times, price and platform.",
                 items=["Ask: What time does…? When does it arrive? How much is a single/return? "
                        "Which bay/platform?"],
                 answers=["Check that the times and prices are said clearly."],
                 level="M", kind="speaking"),
              EX("U11.4-S2", "A problem journey", "The bus is delayed or cancelled. The traveller "
                 "asks for another way; the clerk suggests one and explains.",
                 items=["Use: 'It's delayed', 'It might not run', 'You could take…', "
                        "'It's longer, but it's certain'."],
                 answers=["Assessment: task 3, fluency 2.5, pronunciation 2.5, accuracy 2."],
                 level="D", kind="speaking")],
    writing=[EX("U11.4-W1", "Write a travel message", "Write a message (60–80 words) to a friend "
                "with the details of a journey.",
                items=["Include: departure and arrival times, which bus/train, how long, where to "
                       "meet, and one 'might' sentence."],
                answers=["See the model message in the reading."],
                level="M", kind="writing", lines=8)],
    communication={"function": "Asking for and giving travel information",
                   "phrases": ["What time does the next bus to … leave?", "When does it arrive?",
                               "How much is a single / return?", "Which platform / bay?",
                               "Is there a later one?", "It's delayed.", "Have a good journey!"],
                   "roleplay": "Ticket office role play in pairs, then a 'problem journey' version.",
                   "real_life": "Travelling alone for the first time — one of the most useful "
                                "English situations there is."},
    guided=[EX("U11.4-G1", "Match", "Match the question with the answer.",
               items=["1. What time does it leave?", "2. When does it arrive?",
                      "3. How much is a return?", "4. Which bay?",
                      "a. Bay four.", "b. At seven fifteen.", "c. 200,000 dong.",
                      "d. About nine forty."],
               answers=["1–b", "2–d", "3–c", "4–a"], level="E", kind="mixed"),
            EX("U11.4-G2", "Timetable questions", "Write the question.",
               items=["1. ______ ? – It leaves at 6.45.", "2. ______ ? – It arrives at 9.15.",
                      "3. ______ ? – About two and a half hours.",
                      "4. ______ ? – 120,000 dong for a single.",
                      "5. ______ ? – From bay six."],
               answers=["1. What time does it leave?", "2. When does it arrive?",
                        "3. How long does it take?", "4. How much is a single (ticket)?",
                        "5. Which bay does it leave from?"], level="M", kind="grammar")],
    independent=[EX("U11.4-I1", "Complete the conversation", "Write the missing lines.",
                    items=["A: Excuse me, ______ does the next bus to Hue leave?",
                           "B: At half past eight, from bay two.",
                           "A: And when ______ it arrive?", "B: At about four in the afternoon.",
                           "A: How much ______ a return?", "B: 480,000 dong.",
                           "A: ______ there a later bus?",
                           "B: Yes, at eleven, but it ______ be full — it's a holiday."],
                    answers=["A: what time", "A: does", "A: is", "A: Is", "B: might"],
                    level="M", kind="mixed"),
                 EX("U11.4-I2", "Problem journey role play", "Do U11.4-S2 with the checklist.",
                    items=["Checklist: □ polite opener □ three questions □ the problem explained "
                           "□ an alternative suggested □ a 'might' sentence □ polite ending"],
                    answers=["See U11.4-S2."], level="D", kind="speaking")],
    review=["Travel questions: what time / when / how much / which platform",
            "Present simple for timetables", "might for uncertain travel"],
    homework=[EX("U11.4-H1", "Vocabulary", "Complete with platform, return, single, departs, "
                 "arrives, delayed.",
                 items=["1. The train ______ at 7.15 and ______ at 9.40.",
                        "2. A ______ ticket is for one journey only.",
                        "3. A ______ ticket is there and back.",
                        "4. The train leaves from ______ three.",
                        "5. The bus is ______ because of the flood."],
                 answers=["1. departs; arrives", "2. single", "3. return", "4. platform",
                          "5. delayed"], level="E", kind="vocab"),
              EX("U11.4-H2", "Grammar", "Write the questions for a journey you want to make.",
                 items=["Write five questions: time of departure, time of arrival, length of "
                        "journey, price of a return, and which platform."],
                 answers=["Model: What time does the train to Hue leave? When does it arrive? "
                          "How long does the journey take? How much is a return ticket? "
                          "Which platform does it leave from?"], level="M", kind="grammar"),
              EX("U11.4-H3", "Writing", "Write your travel message (60–80 words) neatly.",
                 items=["Include one 'might' sentence and one piece of advice."],
                 answers=["See U11.4-W1 / the model message."], level="M", kind="writing", lines=8),
              EX("U11.4-H4", "Speaking", "Practise saying these times five times each: 7.15, 9.40, "
                 "half past six, a quarter to eight, platform 13, platform 30.",
                 items=[], answers=["Spot-check in Lesson 5."], level="M", kind="pron")],
    workbook=[EX("U11.4-P1", "Order the conversation", "Number the lines 1–8.",
                 items=["___ At seven fifteen, from bay four.", "___ Excuse me, what time does the "
                        "next bus to Hai Phong leave?", "___ A return, please.",
                        "___ About nine forty.", "___ And when does it arrive?",
                        "___ 120,000 for a single, 200,000 return.",
                        "___ Thank you. Have a good journey!", "___ How much is it?"],
                 answers=["2, 1, 7, 4, 3, 6, 8, 5"], level="M", kind="mixed"),
              EX("U11.4-P2", "Timetable reading", "Look at the timetable and answer.",
                 text=["NAM DINH → HANOI:  06.45 (arr. 09.15) · 08.30 (arr. 11.00) · "
                       "10.15 (arr. 12.45) · 14.00 (arr. 16.30) · 17.30 (arr. 20.00). "
                       "Single 120,000 · Return 200,000."],
                 items=["1. How long does the journey take?",
                        "2. You must be in Hanoi before midday. Which buses can you take?",
                        "3. How much do two return tickets cost?",
                        "4. What time does the last bus arrive?"],
                 answers=["1. Two and a half hours.", "2. The 06.45 and the 08.30.",
                          "3. 400,000 dong.", "4. At 20.00 (eight in the evening)."],
                 level="M", kind="reading"),
              EX("U11.4-P3", "Present simple or might?", "Complete.",
                 items=["1. The train ______ (leave) at seven — it's on the timetable.",
                        "2. It ______ (be) late; the weather is bad.",
                        "3. The bus ______ (arrive) at 9.40 normally.",
                        "4. The two o'clock ______ (be) full — it's a holiday."],
                 answers=["1. leaves", "2. might be", "3. arrives", "4. might be"],
                 level="D", kind="grammar"),
              EX("U11.4-P4", "Write a message", "Write a message (70–80 words) telling a friend how "
                 "to get from the bus station to your house.",
                 items=["Include: which bus, how often, how long, the fare, where to meet, "
                        "and one 'might'."],
                 answers=["Model: Hi Linh, Take bus number 12 from the station — it runs every twenty "
                          "minutes and the journey takes about half an hour. The fare is 8,000 dong; "
                          "have the exact money. Get off at the market and walk down the small street "
                          "next to the pharmacy. Our house is the third on the left, with a mango "
                          "tree in front. I'll wait at the market at four, but I might be five "
                          "minutes late. See you! Mai (79 words)"],
                 level="D", kind="writing", lines=10)],
    procedure=[ST("Warm-up: Certainty line", 5,
                  ["Teacher says a statement about tomorrow; students say will, might or won't. "
                   "Recycles Lesson 3."],
                  "Judge certainty.", "Whole class", "Slide 2"),
               ST("Presentation: travel language", 9,
                  ["Show a real bus or train timetable. Present the six questions in the order of "
                   "a real transaction.",
                   "Drill times, and the -teen/-ty pair."],
                  "Repeat; copy the questions.", "Whole class", "Slides 3–5"),
               ST("Listening: at the bus station", 10,
                  ['Play the recording “Lesson 43: Time for Plan B” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; then the certain/possible task.',
                   "Read the script in role."],
                  "Listen and complete; read in role.", "Individual → pairs", "Slide 6"),
               ST("Guided practice", 7, ["U11.4-G1, G2 and I1; two pairs perform I1."],
                  "Match, write questions, complete the dialogue.", "Pairs",
                  "Student Book p. U11L4"),
               ST("Role play with timetables", 10,
                  ["Pairs use a printed timetable: buy tickets for three journeys, then the "
                   "'problem journey' version with a delay."],
                  "Ask, answer and solve a travel problem.", "Pairs", "Slides 7–9"),
               ST("Wrap-up and homework", 4, ["One pair performs the problem journey. Set H1–H4."],
                  "Perform/listen.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Timetables use the present simple",
                     ["Strange but true: for the future, timetables use the PRESENT.",
                      "'The train LEAVES at seven tomorrow.' Not 'will leave'.",
                      "Why? Because a timetable is a fact, like a school timetable in Unit 6: "
                      "'We have English on Tuesday.'",
                      "But if something changes — 'It MIGHT be late' — then you use might. "
                      "Fixed fact → present simple. Uncertain → might."]),
                  TK("Thirteen and thirty at the station",
                     ["This is not only a pronunciation exercise. It is a 'do you get on the right "
                      "train' exercise.",
                      "thirTEEN — stress at the END, and the /n/ is clear. THIRty — stress at the "
                      "FRONT, and there is a /t/ sound in the middle.",
                      "If you are not sure, do what English speakers do: ask 'One three or three "
                      "zero?' Nobody thinks you are stupid. Everybody thinks you are careful."])],
    support=["Give the six questions on a desk card.",
             "Provide a simplified timetable with three departures.",
             "Let weaker students be the traveller."],
    challenge=["Ask the clerk to answer without looking at the timetable.",
               "Ask them to handle two problems in one conversation.",
               "Ask for a written travel message of 90 words."],
    assessment=["Asks four correct travel questions", "Reads times and prices accurately",
                "Uses 'might' for an uncertain part of the journey"],
    board_plan=["LEFT: timetable", "CENTRE: six travel questions in transaction order",
                "RIGHT: present simple (fixed) | might (uncertain); Homework H1–H4"],
    materials=["Printed timetables (one per pair)", 'Recording: Lesson 43: Time for Plan B — VOA Learning English — Let’s Learn English, Level 1 (3:39)'],
)

L5 = Lesson(
    code="U11L5", unit=11, number=5, period=83,
    lesson_type="Skills 1", title="Reading: Transport that solves a problem + Speaking: Pitch an idea",
    objectives=["read a 240-word article and answer gist, detail and inference questions",
                "guess new words from context",
                "pitch an invention for 90 seconds",
                "ask two questions about somebody else's idea"],
    recycled=["U11L1–L4: transport vocabulary, will/might, can, possessive pronouns; "
              "Unit 10 debate language"],
    vocab=[V("solve", "v", "/sɒlv/", "giải quyết", "This idea solves a real problem."),
           V("cheap to run", "adj phr", "/tʃiːp tə rʌn/", "rẻ khi vận hành", "It is cheap to run and easy to repair."),
           V("repair", "v", "/rɪˈpeə/", "sửa chữa", "Any mechanic can repair it."),
           V("spare part", "n", "/speə pɑːt/", "phụ tùng", "Spare parts are easy to find."),
           V("practical", "adj", "/ˈpræktɪkl/", "thiết thực", "It is a simple, practical idea."),
           V("prototype", "n", "/ˈprəʊtətaɪp/", "mẫu thử", "They built a prototype from old bicycles.")],
    phrases=["solve a problem", "cheap to run", "easy to repair", "It works because…",
             "The clever part is…"],
    grammar=G("Pitching an idea: language of purpose and benefit",
              use=["Purpose: It is designed to + verb / It is designed for + noun.",
                   "Benefit: This means that… / So students will…",
                   "Possibility: It might also…",
                   "Honesty: The problem is… / It won't work if…"],
              form=[["Function", "Language", "Example"],
                    ["purpose", "It is designed to…", "It is designed to carry two children safely."],
                    ["benefit", "This means that…", "This means that parents will let them travel alone."],
                    ["possibility", "It might also…", "It might also work in the rainy season."],
                    ["honesty", "The problem is…", "The problem is the price of the battery."]],
              examples=["Our vehicle is designed to cross flooded streets, so students won't miss "
                        "school in September. The problem is that it is slow.",
                        "It's cheap to run and easy to repair, which means any village mechanic "
                        "can fix it."],
              pitfall="A pitch with no honesty sounds like an advertisement. Every pitch must include "
                      "one real problem.",
              note="'Which means…' and 'This means that…' are the two chunks that turn a fact into "
                   "a benefit."),
    pron=P("Pitching: pace, stress and pausing",
           "A pitch is slower than normal speech. Stress the benefit word: 'It is CHEAP to run and "
           "EASY to repair.' Pause before the problem: 'The problem is… / the battery.'",
           items=["It's CHEAP to run.", "It's EASY to repair.", "This MEANS that…",
                  "The PROBLEM is…"],
           drill=["Our vehicle is designed to cross flooded streets. / This means that students "
                  "won't miss school. / The problem is / the price."],
           vn_note="Students speed up when they are nervous. Practise the first two sentences until "
                   "they can say them slowly and calmly."),
    listening=AUDIO['U11L5'],
    reading=T("The bicycle ambulance",
              ["In 2005, a nurse in a rural district of northern Viet Nam counted the reasons why "
               "patients arrived at her clinic too late. The commonest reason was not money and not "
               "distance. It was mud.",
               "Between May and October, the road to three villages became impossible for a car. "
               "A motorbike could pass, but a sick person cannot sit on a motorbike for eight "
               "kilometres.",
               "A local mechanic and two teachers built something very simple: a bicycle with a light "
               "metal trailer, big wheels and a mattress. One person cycles; the patient lies down. "
               "It cost about two million dong, mostly from old bicycles.",
               "It is not fast — about twelve kilometres an hour. But it works in mud, it needs no "
               "fuel, and any bicycle mechanic can repair it with spare parts from the market.",
               "In the first two years, the trailer carried 87 patients, including 19 women who were "
               "having babies. Nine other districts have copied the design.",
               "'People wanted to give us an ambulance,' the nurse says. 'A real ambulance would have "
               "been wonderful — for four months a year. We needed something for the other eight.'"],
              tasks=[EX("U11.5-R1", "Gist", "Choose the best title.",
                        items=["A. Why ambulances are expensive",
                               "B. A simple invention that works in mud",
                               "C. Bicycles in Vietnamese villages"],
                        answers=["B"], level="E", kind="reading"),
                     EX("U11.5-R2", "Detail", "Answer the questions.",
                        items=["1. What was the commonest reason for arriving late?",
                               "2. Why is a motorbike not a solution?",
                               "3. What is the bicycle ambulance made of, and what did it cost?",
                               "4. How fast is it, and what are its three advantages?",
                               "5. How many patients did it carry in the first two years?"],
                        answers=["1. Mud.",
                                 "2. Because a sick person cannot sit on a motorbike for eight "
                                 "kilometres.",
                                 "3. A bicycle with a light metal trailer, big wheels and a mattress, "
                                 "mostly from old bicycles; about two million dong.",
                                 "4. About 12 km/h; it works in mud, needs no fuel, and any bicycle "
                                 "mechanic can repair it with market spare parts.",
                                 "5. 87, including 19 women having babies."],
                        level="M", kind="reading"),
                     EX("U11.5-R3", "Vocabulary from context", "Find a word or phrase that means:",
                        items=["1. a small vehicle pulled behind another (paragraph 3)",
                               "2. something soft to lie on (paragraph 3)",
                               "3. pieces used to repair a machine (paragraph 4)",
                               "4. made the same thing (paragraph 5)"],
                        answers=["1. trailer", "2. mattress", "3. spare parts", "4. copied"],
                        level="M", kind="reading"),
                     EX("U11.5-R4", "Inference", "Answer with your own ideas.",
                        items=["1. Explain the nurse's last two sentences.",
                               "2. Why is 'any bicycle mechanic can repair it' so important?",
                               "3. What problem in YOUR area could a simple invention solve?"],
                        answers=["1. A modern ambulance would only be usable in the dry season; "
                                 "they needed something that works during the eight muddy months.",
                                 "2. Because a machine that nobody can repair locally stops working "
                                 "for ever after the first breakdown.",
                                 "3. Students' own answer."], level="D", kind="reading")]),
    speaking=[EX("U11.5-S1", "Prepare your pitch", "Make notes for a 90-second pitch.",
                 items=["1. The problem (with a number if you can) ______",
                        "2. Our idea and what it is ______",
                        "3. What it can do / is designed to do ______",
                        "4. Why it is good (cheap to run? easy to repair?) ______",
                        "5. One honest problem ______"],
                 answers=["Notes only. The problem in point 5 is compulsory."],
                 level="M", kind="speaking"),
              EX("U11.5-S2", "Pitch your idea", "Pitch for 90 seconds in a group of four. "
                 "Listeners ask one question each and give one mark out of five.",
                 items=["Useful language: 'It is designed to…', 'This means that…', "
                        "'It's cheap to run.', 'The problem is…'"],
                 answers=["Assessment: idea 3, language 3, honesty about the problem 2, delivery 2."],
                 level="D", kind="speaking")],
    writing=[EX("U11.5-W1", "Notes to sentences", "Turn your notes into six sentences.",
                items=[], answers=["Model: In our village, the road floods for four months a year and "
                                   "about forty students cannot get to school. Our idea is the Flood "
                                   "Bus: a high truck with a flat floor and simple seats. It is "
                                   "designed to drive through water up to seventy centimetres deep. "
                                   "This means that nobody misses school in September and October. "
                                   "It is cheap to run because it goes slowly and it uses an old "
                                   "engine that any mechanic knows. The problem is that it needs a "
                                   "driver every morning, and we have not solved that yet."],
                level="M", kind="writing", lines=8)],
    communication={"function": "Asking practical questions about an idea",
                   "phrases": ["How much will it cost?", "Who will pay for it?",
                               "What happens if it breaks?", "Has anybody tried it?",
                               "What's the biggest problem?"],
                   "roleplay": "After each pitch, listeners must ask one practical question. "
                               "The presenter must answer honestly.",
                   "real_life": "Asking useful questions instead of only being polite."},
    guided=[EX("U11.5-G1", "True or false", "Read the text again and write T or F.",
               items=["1. The commonest reason for arriving late was money.",
                      "2. The road is impossible for a car from May to October.",
                      "3. The bicycle ambulance cost about twenty million dong.",
                      "4. It travels at about 12 km/h.",
                      "5. Nine other districts have copied it."],
               answers=["1. F – it was mud.", "2. T", "3. F – about two million dong.", "4. T",
                        "5. T"], level="E", kind="reading"),
            EX("U11.5-G2", "Purpose and benefit", "Join the two ideas with 'This means that' "
               "or 'is designed to'.",
               items=["1. The boat crosses in four minutes. / Children don't walk 22 km.",
                      "2. The roof folds like an umbrella. / (purpose: keep students dry)",
                      "3. The motor is the same as a fishing boat motor. / Any mechanic can fix it.",
                      "4. The trailer has big wheels. / (purpose: travel in mud)"],
               answers=["1. The boat crosses in four minutes. This means that children don't walk "
                        "22 kilometres.",
                        "2. The roof is designed to keep students dry.",
                        "3. The motor is the same as a fishing boat motor. This means that any "
                        "mechanic can fix it.",
                        "4. The trailer is designed to travel in mud."],
               level="M", kind="writing")],
    independent=[EX("U11.5-I1", "Retell", "Close the book. Tell your partner the story of the "
                    "bicycle ambulance in five sentences.", items=[],
                    answers=["Model: A nurse found that patients arrived late because of mud, not "
                             "money. A mechanic and two teachers built a bicycle with a trailer and "
                             "a mattress. It cost about two million dong, mostly from old bicycles. "
                             "It is slow but it works in mud and anybody can repair it. In two years "
                             "it carried 87 patients."], level="M", kind="speaking"),
                 EX("U11.5-I2", "Your pitch", "Do U11.5-S2 in your group.", items=[],
                    answers=["See U11.5-S2."], level="D", kind="speaking")],
    review=["Reading: gist → detail → inference", "Pitch structure: problem – idea – purpose – "
            "benefit – honest problem", "is designed to / this means that"],
    homework=[EX("U11.5-H1", "Reading", "Answer in full sentences.",
                 items=["1. Why can't a sick person travel by motorbike?",
                        "2. What are the three advantages of the bicycle ambulance?",
                        "3. How many babies were born thanks to it in the first two years?",
                        "4. Why didn't the nurse want a normal ambulance?"],
                 answers=["1. Because they cannot sit on a motorbike for eight kilometres.",
                          "2. It works in mud, it needs no fuel, and any bicycle mechanic can repair "
                          "it with market spare parts.",
                          "3. 19 women who were having babies were carried.",
                          "4. Because a normal ambulance would only work for about four months a "
                          "year; they needed something for the other eight."],
                 level="M", kind="reading"),
              EX("U11.5-H2", "Vocabulary", "Complete with solve, cheap to run, repair, spare parts, "
                 "practical, prototype.",
                 items=["1. Our idea will ______ a real problem.",
                        "2. It is ______ because it uses sunlight.",
                        "3. Any mechanic can ______ it.",
                        "4. ______ are easy to find at the market.",
                        "5. It is a simple, ______ design.",
                        "6. We built a ______ from two old bicycles."],
                 answers=["1. solve", "2. cheap to run", "3. repair", "4. Spare parts",
                          "5. practical", "6. prototype"], level="E", kind="vocab"),
              EX("U11.5-H3", "Writing", "Write your pitch as a paragraph (100–110 words).",
                 items=["Problem with a number – the idea – purpose – benefit – one honest problem."],
                 answers=["See U11.5-W1 model."], level="D", kind="writing", lines=14),
              EX("U11.5-H4", "Speaking", "Practise your 90-second pitch three times. Speak SLOWLY.",
                 items=["Mark the pause before 'The problem is…'."],
                 answers=["Pitches in Lesson 6."], level="M", kind="speaking")],
    workbook=[EX("U11.5-P1", "Vocabulary match", "Match the word with the meaning.",
                 items=["1. solve", "2. repair", "3. spare part", "4. practical", "5. prototype",
                        "a. the first model you build", "b. to mend something broken",
                        "c. useful in real life", "d. to find an answer to a problem",
                        "e. a piece for mending a machine"],
                 answers=["1–d", "2–b", "3–e", "4–c", "5–a"], level="E", kind="vocab"),
              EX("U11.5-P2", "Reading", "Read and answer.",
                 text=["In Bangladesh, a company sells a bicycle that also pumps water. When the "
                       "bicycle is on its stand, the back wheel turns a small pump, so a farmer can "
                       "water a field by pedalling. It costs about a third of the price of a diesel "
                       "pump and needs no fuel. It is slower, but a farmer with no money for diesel "
                       "does not compare it with a diesel pump. He compares it with carrying water "
                       "in buckets."],
                 items=["1. What can the bicycle do besides carrying people?",
                        "2. How does the pump work?", "3. How does the price compare?",
                        "4. What is the writer's point in the last sentence?"],
                 answers=["1. It pumps water.",
                          "2. When the bicycle is on its stand, the back wheel turns a small pump "
                          "as the farmer pedals.",
                          "3. It costs about a third of the price of a diesel pump.",
                          "4. That the right comparison is not with an expensive machine but with "
                          "what the person actually does now (carrying buckets)."],
                 level="M", kind="reading"),
              EX("U11.5-P3", "Purpose and benefit", "Write one sentence for each idea using "
                 "'is designed to' and one using 'This means that'.",
                 items=["1. a school boat with solar panels", "2. a folding roof for a bicycle",
                        "3. a bicycle with a trailer for patients"],
                 answers=["Model: 1. The boat is designed to cross the river in four minutes. "
                          "This means that children don't have to walk twenty-two kilometres."],
                 level="M", kind="writing"),
              EX("U11.5-P4", "Writing", "Write a pitch (100–110 words) for an invention that would "
                 "solve a problem in your area.",
                 items=["Problem with a number – idea – purpose – benefit – one honest problem."],
                 answers=["See U11.5-W1 model."], level="D", kind="writing", lines=14)],
    procedure=[ST("Warm-up: Problem hunt", 5,
                  ["Ask: 'What is the most annoying transport problem in our area?' "
                   "Collect six problems on the board."],
                  "Name real local problems.", "Whole class", "Slide 2"),
               ST("Pre-reading", 6,
                  ["Show a photo of a muddy road. Ask: 'How would you get a sick person to hospital "
                   "here?' Predict.",
                   "Pre-teach: mud, trailer, mattress, spare parts. Set the gist task."],
                  "Predict; skim for the title.", "Whole class", "Slides 3–4"),
               ST("While-reading", 13,
                  ["R2 detail individually, pair-check; R3 words in context; R4 inference in pairs."],
                  "Read and answer.", "Individual → pairs", "Slides 5–7"),
               ST("Post-reading: retell", 4, ["Books closed; retell in five sentences."],
                  "Retell.", "Pairs", "Slide 8"),
               ST("Speaking: pitch an idea", 13,
                  ["Play the two model pitches; students note the five parts.",
                   "4 minutes to plan; 90-second pitches in groups of four; one question and one "
                   "mark out of five each."],
                  "Listen, plan, pitch, question, score.", "Individual → groups of 4", "Slides 9–11"),
               ST("Wrap-up and homework", 4, ["The best-scoring pitch to the class. Set H1–H4."],
                  "Listen; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("The right comparison",
                     ["The nurse could have said: 'Our bicycle ambulance is much worse than a real "
                      "ambulance.' True — and useless.",
                      "The right comparison is not with the best possible machine. It is with what "
                      "people do NOW: walking eight kilometres in mud.",
                      "When you pitch your idea, do the same. Do not compare it with a spaceship. "
                      "Compare it with today."]),
                  TK("Every pitch needs one honest problem",
                     ["If your pitch has no problem in it, nobody believes you.",
                      "Team two said: 'Our prototype fell over twice.' Did that make their idea "
                      "worse? No — it made me trust them.",
                      "So point five of your notes is compulsory: one real problem, said clearly. "
                      "Then say: 'We are working on it.'"])],
    support=["Gloss four words in the margin.", "Give a pitch skeleton with the five parts.",
             "Let weaker students pitch to one partner only."],
    challenge=["Ask them to answer three practical questions after the pitch.",
               "Ask for a cost estimate with real numbers.",
               "Ask them to compare their idea with what happens now."],
    assessment=["4 of 5 detail answers", "Pitch includes a problem, a purpose and an honest weakness",
                "Speaks slowly for about 90 seconds"],
    board_plan=["LEFT: local transport problems", "CENTRE: pitch plan 1–5",
                "RIGHT: is designed to / this means that / the problem is; Homework H1–H4"],
    materials=["Reading text", 'Recording: Who will you see tonight or tomorrow? — ELLLO — One Minute English (1:10)', "Timer", "Score cards (1–5)"],
)

L6 = Lesson(
    code="U11L6", unit=11, number=6, period=84,
    lesson_type="Skills 2", title="Listening: Travel announcements + Writing: A future journey",
    objectives=["listen to announcements and note the key information",
                "organise a description of a future journey",
                "write 110–130 words describing a journey in the future",
                "check a partner's work with a checklist"],
    recycled=["U11L1–L5: transport vocabulary, will/might, can, travel language; "
              "all previous writing structures"],
    vocab=[V("announcement", "n", "/əˈnaʊnsmənt/", "thông báo", "Listen to the announcement."),
           V("cancel", "v", "/ˈkænsl/", "hủy", "The 8.30 service is cancelled."),
           V("board", "v", "/bɔːd/", "lên (tàu, xe)", "Passengers may now board."),
           V("passenger", "n", "/ˈpæsɪndʒə/", "hành khách", "Passengers for Hue, please go to gate 2."),
           V("luggage", "n", "/ˈlʌɡɪdʒ/", "hành lý", "Please keep your luggage with you."),
           V("on time", "adj phr", "/ɒn taɪm/", "đúng giờ", "The train is running on time.")],
    phrases=["Attention, please.", "The service to … is delayed / cancelled.",
             "Passengers are asked to…", "We apologise for the delay.", "running on time"],
    grammar=G("Describing a future journey (writing focus)",
              use=["1. THE JOURNEY TODAY (present simple): Today the journey takes six hours by bus.",
                   "2. THE FUTURE JOURNEY (will): In 2050 it will take ninety minutes.",
                   "3. DETAILS with might for the parts you are not sure about.",
                   "4. HOW IT WILL FEEL: what you will see, hear and do on the way.",
                   "5. A CONCLUSION: what will be better, and what might be lost."],
              form=[["Part", "Language", "Example"],
                    ["now", "present simple", "Today the bus takes six hours."],
                    ["future", "will", "In 2050 the train will take ninety minutes."],
                    ["uncertain", "might", "There might be a station in my town."],
                    ["experience", "will + senses", "You will see the whole delta through the window."],
                    ["conclusion", "will be better / might be lost",
                     "It will be faster, but we might lose the long conversations on the bus."]],
              examples=["Today my grandmother's village is four hours away. In 2050 the journey will "
                        "probably take one hour, and I might visit her every weekend.",
                        "The journey will be faster, but we might lose something too."],
              pitfall="Students describe only the vehicle. The interesting part is what the journey "
                      "will FEEL like and what it will change.",
              note="The best answers include one thing that might be LOST — that shows real thinking."),
    pron=P("Announcement voice: clear, slow, and complete words",
           "Announcements are slow with a pause after each piece of information. Every final "
           "consonant must be heard: 'The train to HueE… is deLAYED… by twenty minutes.'",
           items=["Attention, please.", "The service to Hue / is delayed / by twenty minutes.",
                  "Passengers are asked to / go to platform three."],
           drill=["Attention, please. / The eight thirty service to Hai Phong / is cancelled. / "
                  "We apologise for the delay."],
           vn_note="Announcements are excellent pronunciation practice: they force slow speech and "
                   "clear final consonants."),
    listening=AUDIO['U11L6'],
    reading=T("Model description: A journey in 2050",
              ["Today, going from my village to my grandmother's house takes four hours. First we "
               "take a motorbike to the main road, then a bus to Thanh Hoa, and then another bus. "
               "In the rainy season it can take six.",
               "I think this journey will be completely different in 2050. There will probably be a "
               "high-speed train through the province, and my town might have a small station. "
               "If it does, the journey will take about fifty minutes instead of four hours.",
               "I imagine sitting by the window with the whole delta going past. The train will be "
               "quiet — no engine noise, because it will run on electricity — and I will be able to "
               "do my homework on the way. My grandmother will still be waiting at the gate, "
               "because some things won't change.",
               "The best thing won't be the speed. It will be that I can visit her on a Saturday and "
               "come home the same evening. However, we might lose something too: on the long bus "
               "journey, my mother tells me family stories for four hours, and nobody looks at a "
               "phone. In fifty minutes there will not be time for that. (196 words — yours can be "
               "shorter!)"],
              tasks=[EX("U11.6-R1", "Analyse the model", "Answer the questions.",
                        items=["1. How long does the journey take today, and how?",
                               "2. Which words show that the writer is not certain?",
                               "3. Find two sentences about how the journey will feel.",
                               "4. What does the writer say is the best thing?",
                               "5. What might be lost? Why is this a good ending?"],
                        answers=["1. Four hours (six in the rainy season): motorbike, bus to Thanh "
                                 "Hoa, then another bus.",
                                 "2. 'probably', 'might have', 'If it does'.",
                                 "3. 'I imagine sitting by the window with the whole delta going "
                                 "past.' / 'The train will be quiet…'",
                                 "4. Not the speed, but being able to visit and come home the same "
                                 "day.",
                                 "5. The four hours of family stories on the bus; it shows real "
                                 "thinking, not only excitement about technology."],
                        level="M", kind="reading")]),
    speaking=[EX("U11.6-S1", "Say your journey", "Tell your partner your journey — today and in "
                 "2050 — in six sentences.",
                 items=["Now → future → how it will feel → what might be lost."],
                 answers=["Speaking first improves the writing."], level="M", kind="speaking")],
    writing=[EX("U11.6-W1", "Plan your description", "Complete the plan.",
                items=["1. A journey I make now (how, how long): ______",
                       "2. How it will be in 2050 (will): ______",
                       "3. One thing I'm not sure about (might): ______",
                       "4. How it will feel (see / hear / do): ______",
                       "5. What will be better: ______",
                       "6. What might be lost: ______"],
                answers=["Check every plan; point 6 is compulsory."], level="M", kind="writing",
                lines=8),
             EX("U11.6-W2", "Write your description", "Write 110–130 words about a journey in "
                "the future.",
                items=["Present simple for now; will for the future; at least one might; "
                       "one sentence about feeling; one thing that might be lost."],
                answers=["See the model. Marking: content 3, will/might 3, organisation 2, "
                         "vocabulary 1, length 1."],
                level="D", kind="writing", lines=18),
             EX("U11.6-W3", "Peer check", "Swap and tick the checklist.",
                items=["□ the journey today (present simple)", "□ at least three 'will' sentences",
                       "□ at least one 'might'", "□ one sentence about how it will feel",
                       "□ one thing that will be better", "□ one thing that might be lost",
                       "□ 110–130 words"],
                answers=["Write one thing you liked and one to improve."], level="M", kind="writing")],
    communication={"function": "Understanding and giving announcements",
                   "phrases": ["Attention, please.", "…is delayed by…", "…is cancelled.",
                               "Passengers are asked to…", "We apologise for the delay."],
                   "roleplay": "Write and read a 30-second station announcement; the class notes the "
                               "information.",
                   "real_life": "Understanding announcements at a station or an airport."},
    guided=[EX("U11.6-G1", "Announcement language", "Complete the announcements.",
               items=["1. ______ , please. The 7.15 service to Hai Phong is now ______ at "
                      "platform two.",
                      "2. The 8.30 service is ______ by forty minutes. We ______ for the delay.",
                      "3. The nine o'clock service to Vinh is ______ .",
                      "4. Passengers ______ asked to keep their ______ with them."],
               answers=["1. Attention; boarding", "2. delayed; apologise", "3. cancelled",
                        "4. are; luggage"], level="E", kind="writing"),
            EX("U11.6-G2", "will or might?", "Complete the description.",
               items=["1. There ______ probably be a high-speed train. (fairly sure)",
                      "2. My town ______ have a station. (not sure)",
                      "3. The journey ______ take fifty minutes. (sure, if there is a station)",
                      "4. We ______ lose the long family conversations. (possible)"],
               answers=["1. will", "2. might", "3. will", "4. might"], level="M", kind="grammar")],
    independent=[EX("U11.6-I1", "Write your description", "Do U11.6-W1 and W2.", items=[],
                    answers=["See the model description."], level="D", kind="writing", lines=18),
                 EX("U11.6-I2", "Make an announcement", "Write and read a 30-second announcement "
                    "for a delayed service. The class notes the information.",
                    items=[], answers=["See communication section."], level="M", kind="speaking")],
    review=["Announcement listening: destination, time, platform, problem",
            "Future journey description: now – future – feeling – what might be lost",
            "will (sure) vs might (possible)"],
    homework=[EX("U11.6-H1", "Listening / vocabulary", "Complete from the announcements.",
                 items=["1. The 7.15 to Hai Phong leaves from platform ______ .",
                        "2. The Lang Son train is delayed by ______ minutes.",
                        "3. The nine o'clock to Vinh is ______ .",
                        "4. The Da Nang train has ______ coaches."],
                 answers=["1. two", "2. forty", "3. cancelled", "4. twelve"],
                 level="E", kind="listening"),
              EX("U11.6-H2", "Vocabulary", "Complete with announcement, cancel, board, passengers, "
                 "luggage, on time.",
                 items=["1. ______ may now ______ at platform two.",
                        "2. Please keep your ______ with you.",
                        "3. They had to ______ the nine o'clock service.",
                        "4. Listen to the ______ .", "5. The train is running ______ ."],
                 answers=["1. Passengers; board", "2. luggage", "3. cancel", "4. announcement",
                          "5. on time"], level="E", kind="vocab"),
              EX("U11.6-H3", "Writing", "Rewrite your description neatly after correction and "
                 "hand it in.",
                 items=["Use the 7-point checklist."],
                 answers=["Marking: content 3, will/might 3, organisation 2, vocabulary 1, length 1."],
                 level="D", kind="writing", lines=18),
              EX("U11.6-H4", "Speaking", "Read one announcement aloud five times, slowly, with a "
                 "pause after each piece of information.",
                 items=[], answers=["Spot-check in Lesson 7."], level="M", kind="pron")],
    workbook=[EX("U11.6-P1", "Announcement or description?", "Write A or D.",
                 items=["1. Attention, please. ___", "2. Today the journey takes four hours. ___",
                        "3. The service is delayed by twenty minutes. ___",
                        "4. In 2050 it will take fifty minutes. ___",
                        "5. Passengers are asked to keep their luggage with them. ___"],
                 answers=["1. A", "2. D", "3. A", "4. D", "5. A"], level="E", kind="writing"),
              EX("U11.6-P2", "Complete the description", "Use the words in the box.",
                 wordbank=["takes", "will", "might", "won't", "However"],
                 items=["Today the journey to my aunt's house (1) ______ three hours by bus. "
                        "In 2050 it (2) ______ probably take one hour by train. My town "
                        "(3) ______ have a station, but I'm not sure. The best thing "
                        "(4) ______ be the speed — it will be the free time. (5) ______ , "
                        "we might lose the long conversations on the bus."],
                 answers=["1. takes", "2. will", "3. might", "4. won't", "5. However"],
                 level="M", kind="writing"),
              EX("U11.6-P3", "Correct the description", "Find and correct five mistakes.",
                 text=["Today the journey take four hours. In 2050 it will takes fifty minutes. "
                       "My town might has a station. The train will quiet because it runs on "
                       "electricity. I think we won't lose nothing."],
                 items=["Write the five corrections."],
                 answers=["1. 'take' → 'takes'", "2. 'will takes' → 'will take'",
                          "3. 'might has' → 'might have'", "4. 'will quiet' → 'will be quiet'",
                          "5. 'won't lose nothing' → 'won't lose anything' / 'will lose nothing'"],
                 level="D", kind="grammar"),
              EX("U11.6-P4", "Writing", "Write a description (110–130 words) of a journey your "
                 "grandparents made when they were young, and the same journey in 2050.",
                 items=["Past – present – future; include one 'might'."],
                 answers=["Model: When my grandmother was thirteen, she walked eleven kilometres to "
                          "school and back, and in the rainy season she often did not go at all. "
                          "Today my sister makes the same journey in twenty minutes on an electric "
                          "bicycle, and she complains when it rains. In 2050 I think there will be a "
                          "covered cycle path all the way, and small electric buses every ten minutes. "
                          "There might even be a station in the village, although I doubt it. "
                          "The journey will be safe, dry and quick. However, my grandmother says that "
                          "she learned the names of every tree on that road, and my sister does not "
                          "know one. (124 words)"], level="D", kind="writing", lines=18)],
    procedure=[ST("Warm-up: Announcement dictation", 5,
                  ["Read one announcement at normal speed; students note destination, time, platform "
                   "and problem."],
                  "Listen and note.", "Individual → pairs", "Slide 2"),
               ST("Pre-listening", 5,
                  ["Show the table. Pre-teach: board, delayed, cancelled, refund, coach, luggage."],
                  "Predict; copy the table.", "Whole class", "Slides 3–4"),
               ST("Listening", 11,
                  ["Play the recording “Lesson 20: What Can You Do?” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; complete the table; then the 'what should you do' questions."],
                  "Listen and complete.", "Individual → pairs", "Slide 5"),
               ST("Writing: analyse the model", 8,
                  ["Model description on the slide; colour the parts; find the 'might' and the "
                   "'what might be lost' sentence. Do U11.6-G2."],
                  "Identify the parts; practise will/might.", "Whole class → pairs", "Slides 6–7"),
               ST("Writing: plan, say, draft", 12,
                  ["Plan (check every plan, especially point 6); say it aloud; write 110–130 words."],
                  "Plan, say, write.", "Individual → pairs → individual", "Slide 8"),
               ST("Peer check and wrap-up", 4, ["Checklist swap; read one good description. "
                                                "Set H1–H4."],
                  "Peer-check.", "Pairs", "Slides 9–10")],
    teacher_talk=[TK("What might be lost",
                     ["Most writing about the future is only excited: faster, cleaner, better.",
                      "The model description does something braver. It says: 'On the four-hour bus "
                      "journey my mother tells me family stories. In fifty minutes there will not be "
                      "time for that.'",
                      "That one sentence is worth ten sentences about technology, because it shows "
                      "you are thinking, not dreaming.",
                      "So point six of your plan is compulsory: what might be lost?"]),
                  TK("Announcements as pronunciation practice",
                     ["Announcements are slow, loud and complete. Every ending is there: "
                      "delayED, cancelLED, platforM.",
                      "That is exactly what we need to practise.",
                      "So when you read your announcement, do not be shy. Stand up. Slow down. "
                      "Pause after each piece of information. Be the voice in the station."])],
    support=["Give the announcement table with four answers filled in.",
             "Provide a description frame with the six parts.",
             "Allow 90–100 words."],
    challenge=["Ask for two 'might' sentences and two things that might be lost.",
               "Ask them to write and perform a station announcement with a problem.",
               "Ask for 150 words including a grandparent's journey."],
    assessment=["10 of 16 items in the announcement table",
                "Description includes now, future, feeling and a possible loss",
                "Correct will/might distinction"],
    board_plan=["LEFT: announcement table", "CENTRE: description plan 1–6",
                "RIGHT: will (sure) | might (possible); Homework H1–H4"],
    materials=['Recording: Lesson 20: What Can You Do? — VOA Learning English — Let’s Learn English, Level 1 (3:39)', "Model description slide", "Checklist cards"],
)

L7 = Lesson(
    code="U11L7", unit=11, number=7, period=85,
    lesson_type="Looking Back & Project", title="Unit 11 review and Design the Transport of 2050",
    objectives=["recall the transport vocabulary of Unit 11",
                "use might and possessive pronouns accurately",
                "correct the six typical mistakes of the unit",
                "design and pitch a vehicle for the future"],
    recycled=["ALL of Unit 11 + Units 1–10"],
    vocab=[V("design", "n/v", "/dɪˈzaɪn/", "thiết kế", "Here is our design."),
           V("investor", "n", "/ɪnˈvestə/", "nhà đầu tư", "The class acts as investors."),
           V("pitch", "n/v", "/pɪtʃ/", "bài thuyết trình chào hàng", "Each group has a 2-minute pitch.")],
    phrases=["Our design solves…", "It is designed to…", "This means that…",
             "The problem is…", "Would you invest in it?"],
    grammar=G("Unit 11 grammar in one page",
              use=["might / might not = possible (50%); will / won't = sure",
                   "might never changes and never takes 'to'",
                   "possessive pronouns stand alone: mine, yours, his, hers, ours, theirs",
                   "can / can't for what a machine can do",
                   "present simple for timetables"],
              form=[["Structure", "Example", "Common mistake"],
                    ["might + bare verb", "It might rain.", "*It mights rain / might to rain."],
                    ["might not", "She might not come.", "*She might don't come."],
                    ["possessive pronoun", "This bag is mine.", "*This is mine bag."],
                    ["possessive adjective", "This is my bag.", "*This is mine bag."],
                    ["can + bare verb", "It can carry four people.", "*It can to carry."],
                    ["timetable", "The train leaves at seven.", "*The train will leave at seven "
                     "(fixed timetable)."]],
              examples=["Our vehicle can carry six passengers and it might also work in a flood, "
                        "although we are not sure. This design is ours; theirs is the one with "
                        "the solar roof."],
              pitfall="Add these six to the classroom wall list."),
    pron=P("Unit 11 sounds review: final /l/, final /z/, three-syllable stress",
           "Three checks: can I hear the /l/ in travel? the /z/ in hers? is 'comfortable' three "
           "syllables?",
           items=["travel, hotel, people, school", "hers, ours, theirs, yours",
                  "comfortable, convenient, reliable"],
           drill=["Their hotel is more comfortable than ours, but ours is more convenient."],
           vn_note="Check all three in the Review 4 block."),
    listening=AUDIO['U11L7'],
    reading=T("The competition that built a bus stop",
              ["Two years ago, a school in Quang Ngai held a competition: design something that would "
               "make the journey to school better. Twenty-six teams entered.",
               "Most designs were vehicles — flying bicycles, solar cars, a boat with wheels. "
               "The winning idea was none of these. It was a bus stop.",
               "The team had noticed something simple: 140 students waited every morning at a place "
               "with no shelter, no seat and no light. In the rain they stood under the trees; "
               "in the dark, drivers could not see them.",
               "Their design was a small roof, two benches, a solar light and a board with the bus "
               "times. It cost 14 million dong. The commune paid half; parents paid the rest.",
               "'Everybody wants to invent the future,' the teacher said afterwards. 'These students "
               "looked at what was already broken.'"],
              tasks=[EX("U11.7-R1", "Read and answer", "Answer the questions.",
                        items=["1. What was the competition?", "2. How many teams entered?",
                               "3. What had the winning team noticed?",
                               "4. What four things were in their design, and what did it cost?",
                               "5. Explain the teacher's last sentence."],
                        answers=["1. Design something that would make the journey to school better.",
                                 "2. Twenty-six.",
                                 "3. That 140 students waited every morning with no shelter, no seat "
                                 "and no light.",
                                 "4. A small roof, two benches, a solar light and a board with the "
                                 "bus times; 14 million dong.",
                                 "5. Most people try to invent something new, but the best ideas "
                                 "often come from fixing what is already wrong."],
                        level="M", kind="reading")]),
    speaking=[EX("U11.7-S1", "Pitch to the investors", "Pitch your design for two minutes. "
                 "Everyone speaks. The class votes with 'money' cards.",
                 items=["Frame: 'The problem is… Our design is… It can… It is designed to… "
                        "This means that… The problem is… Would you invest?'"],
                 answers=["Marking: idea 3, language 3, design 2, pitch 2."],
                 level="D", kind="speaking")],
    writing=[EX("U11.7-W1", "Design sheet", "Write the eight sentences for your design.",
                items=["1–2: the problem (with a number)", "3: what it is",
                       "4–5: what it can do (can)", "6: what it will do (will)",
                       "7: what it might do (might)", "8: one honest problem"],
                answers=["Model: In our village 40 students cross the river to school. In September "
                         "the ferry stops for two weeks. Our design is a floating footbridge made "
                         "from plastic barrels and bamboo. It can carry twenty people at a time and "
                         "it can rise with the water. It will cost about 60 million dong. "
                         "It might also help the market sellers in the morning. The problem is that "
                         "somebody must check the ropes every week."],
                level="M", kind="writing", lines=12)],
    communication={"function": "Pitching and evaluating",
                   "phrases": ["Would you invest in it?", "How much will it cost?",
                               "What happens if…?", "I'd invest, because…",
                               "I'm not convinced, because…"],
                   "roleplay": "Investor panel: each group pitches; the class asks one question "
                               "and votes.",
                   "real_life": "Presenting an idea and answering hard questions."},
    guided=[EX("U11.7-G1", "Vocabulary race", "Write the word.",
               items=["1. a car with no driver: ______", "2. a railway under a city: ______",
                      "3. a person travelling on a bus: ______", "4. easy to reach and use: ______",
                      "5. it never breaks down: ______", "6. the first model you build: ______"],
               answers=["1. a driverless car", "2. the underground", "3. a passenger",
                        "4. convenient", "5. reliable", "6. a prototype"], level="E", kind="vocab"),
            EX("U11.7-G2", "Error clinic – the six Unit 11 mistakes", "Correct one mistake in each "
               "sentence.",
               items=["1. It mights rain tomorrow.", "2. She might to come.",
                      "3. This is mine bag.", "4. That helmet is her.",
                      "5. It can to carry four people.",
                      "6. The train will leave at seven every morning. (fixed timetable)"],
               answers=["1. It might rain tomorrow.", "2. She might come.",
                        "3. This is my bag. / This bag is mine.", "4. That helmet is hers.",
                        "5. It can carry four people.",
                        "6. The train leaves at seven every morning."], level="D", kind="grammar")],
    independent=[EX("U11.7-I1", "Mixed review", "Complete the text.",
                    text=["Our village is fifteen kilometres from the town, and the bus "
                          "(1. leave) ______ at six every morning. In 2050 I think there "
                          "(2. be) ______ an electric bus every twenty minutes. There "
                          "(3. might/be) ______ a small station too, but I'm not sure. "
                          "The new bus (4. can) ______ carry forty passengers. My father says his old "
                          "bicycle is better than any bus; (5. my/mine) ______ is broken, so I "
                          "disagree!"],
                    items=["Write the five answers."],
                    answers=["1. leaves", "2. will be", "3. might be", "4. can", "5. mine"],
                    level="M", kind="grammar"),
                 EX("U11.7-I2", "Project work", "Finish your design and rehearse the pitch.",
                    items=[], answers=["Check might/will and can before the pitch."],
                    level="D", kind="mixed")],
    review=["Transport vocabulary (26 items)", "might / might not", "possessive pronouns",
            "can for machines", "present simple for timetables", "Future journey description"],
    homework=[EX("U11.7-H1", "Vocabulary", "Write 10 words from Unit 11 with Vietnamese meanings.",
                 items=[], answers=["Any 10 of the unit's items."], level="E", kind="vocab"),
              EX("U11.7-H2", "Grammar", "Choose the correct answer.",
                 items=["1. It (will / might) rain — I'm not sure.",
                        "2. The sun (will / might) rise tomorrow.",
                        "3. This bag is (my / mine).", "4. That is (her / hers) helmet.",
                        "5. It (can / cans) carry six passengers.",
                        "6. The train (leaves / will leave) at seven every day."],
                 answers=["1. might", "2. will", "3. mine", "4. her", "5. can", "6. leaves"],
                 level="M", kind="grammar"),
              EX("U11.7-H3", "Writing", "Write a description (110–130 words) of a journey you make, "
                 "as it will be in 2050.",
                 items=["Now – future – feeling – what might be lost."],
                 answers=["See U11.6-W2 model."], level="D", kind="writing", lines=18),
              EX("U11.7-H4", "Prepare for Unit 12", "Write the names of five English-speaking "
                 "countries and one fact about each.",
                 items=[], answers=["Use them to start Unit 12."], level="E", kind="vocab")],
    workbook=[EX("U11.7-P1", "Crossword clues", "Write the word.",
                 items=["1. A person travelling on a bus. (9)", "2. Easy to reach and use. (10)",
                        "3. It never breaks down. (8)", "4. The first model. (9)",
                        "5. A railway under the city. (11)"],
                 answers=["1. passenger", "2. convenient", "3. reliable", "4. prototype",
                          "5. underground"], level="E", kind="vocab"),
              EX("U11.7-P2", "Mixed grammar", "Put the words in order.",
                 items=["1. rain / might / it / tomorrow", "2. is / bag / mine / this",
                        "3. carry / can / it / passengers / six",
                        "4. at / leaves / seven / the train",
                        "5. hers / that / is / helmet"],
                 answers=["1. It might rain tomorrow.", "2. This bag is mine.",
                          "3. It can carry six passengers.", "4. The train leaves at seven.",
                          "5. That helmet is hers."], level="M", kind="grammar"),
              EX("U11.7-P3", "Reading review", "Read and choose.",
                 text=["Hanoi's first underground line opened in 2021 after twelve years of "
                       "construction. In its first full year it carried about 7.5 million "
                       "passengers. Critics said the line was too short and took too long to build. "
                       "Supporters answered that every city's first line is the hardest, and that "
                       "the second and third lines will be faster and cheaper because the engineers "
                       "have learned."],
                 items=["1. When did the line open, and how long did it take?",
                        "2. How many passengers in the first full year?",
                        "3. What do supporters say about the next lines?"],
                 answers=["1. In 2021, after twelve years.", "2. About 7.5 million.",
                          "3. That they will be faster and cheaper because the engineers have "
                          "learned."], level="M", kind="reading"),
              EX("U11.7-P4", "Unit 11 test yourself (10 marks)", "Answer about yourself (2 marks each).",
                 items=["1. One thing that WILL happen next year: ______",
                        "2. One thing that MIGHT happen: ______",
                        "3. A sentence with a possessive pronoun: ______",
                        "4. What a vehicle you know CAN do: ______",
                        "5. A timetable sentence (present simple): ______"],
                 answers=["Model: 1. I will be in Grade 8 next year. 2. My family might buy an "
                          "electric motorbike. 3. That blue bicycle is mine. 4. Our school bus can "
                          "carry forty students. 5. The bus leaves the village at half past six."],
                 level="D", kind="mixed")],
    procedure=[ST("Warm-up: Whose is it?", 6,
                  ["Collect six objects; play 'Whose is this?' with possessive pronouns. "
                   "Recycles Lesson 3."],
                  "Answer with possessive pronouns.", "Whole class", "Slide 2"),
               ST("Vocabulary and listening review", 7,
                  ["U11.7-G1 race; then the listening quiz U11.7-L1."],
                  "Write words; complete sentences.", "Pairs", "Slides 3–4"),
               ST("Grammar review + error clinic", 10,
                  ["Grammar table; U11.7-G2 in pairs with explanations; add to the wall list."],
                  "Correct and explain six errors.", "Pairs → whole class", "Slides 5–7"),
               ST("Mixed practice", 6, ["U11.7-I1 gap-fill; fast finishers do Workbook P2."],
                  "Complete the text.", "Individual", "Student Book p. U11L7"),
               ST("Project: Design the Transport of 2050", 12,
                  ["Groups finish the drawing and the eight sentences; rehearse the two-minute pitch.",
                   "Three or four groups pitch; the class asks one question each and votes with "
                   "'money' cards."],
                  "Finish, pitch, question, vote.", "Groups of 4", "Slides 8–10"),
               ST("Wrap-up and homework", 4, ["Announce which design attracted most 'investment'. "
                                              "Set H1–H4."],
                  "Vote; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Look at what is already broken",
                     ["Read the last line of today's text again: 'Everybody wants to invent the "
                      "future. These students looked at what was already broken.'",
                      "The winning idea was a bus stop. Not a flying car — a roof, two benches and "
                      "a light.",
                      "So before you pitch, ask yourself one question: does my idea fix something "
                      "that is really wrong here, this year? If yes, the investors will listen."]),
                  TK("Might and mine — the last check",
                     ["Two small words, two easy marks.",
                      "MIGHT never changes and never takes 'to'. It might rain. She might come.",
                      "MINE stands alone. 'This bag is mine.' If a noun follows, use MY: "
                      "'This is my bag.'",
                      "Say both pairs with me, twice. Then find them in your project sentences."])],
    support=["Give the error clinic with mistakes underlined.",
             "Provide the eight design sentences as a frame.",
             "Assign the drawing role plus two sentences."],
    challenge=["Ask them to answer three investor questions.",
               "Ask for a cost estimate and who would pay.",
               "Ask for 140 words in H3."],
    assessment=["Unit 11 checklist: 5 of 6 'I can' statements", "Error clinic 5 of 6",
                "Pitches with at least one might and one can sentence"],
    board_plan=["LEFT: transport vocabulary", "CENTRE: Unit 11 grammar table",
                "RIGHT: pitch requirements; Homework H1–H4"],
    materials=["Poster paper, coloured pens", "'Money' cards for voting", 'Recording: Looking Back — listen again (replay — see the lesson page)'],
)

UNIT.lessons = [L1, L2, L3, L4, L5, L6, L7]

UNIT.revision = [
    EX("R11-1", "Vocabulary", "Complete with a word from Unit 11.",
       items=["1. A car with no driver is a d______ car.",
              "2. The u______ is a railway below the city.",
              "3. A p______ is a person travelling on a bus or train.",
              "4. The bus is r______ : it always comes on time.",
              "5. The station is close, so it is very c______ .",
              "6. Any mechanic can r______ it."],
       answers=["1. driverless", "2. underground", "3. passenger", "4. reliable", "5. convenient",
                "6. repair"], level="E", kind="vocab"),
    EX("R11-2", "Grammar: will or might?", "Complete the sentences.",
       items=["1. The sun ______ rise tomorrow. (sure)",
              "2. It ______ rain this afternoon. (possible)",
              "3. I ______ come to the party — I'm not sure.",
              "4. Flying cars ______ be common in ten years. (sure: no)",
              "5. Our town ______ get a new station, but nobody knows."],
       answers=["1. will", "2. might", "3. might", "4. won't", "5. might"],
       level="M", kind="grammar"),
    EX("R11-3", "Grammar: possessive pronouns and can", "Complete.",
       items=["1. This bag is ______ . (I)", "2. That helmet is ______ . (she)",
              "3. Is this ______ ? (you)", "4. Our house is bigger than ______ . (they)",
              "5. It ______ carry six passengers.", "6. It ______ travel more than 60 km. (limit)"],
       answers=["1. mine", "2. hers", "3. yours", "4. theirs", "5. can", "6. can't"],
       level="M", kind="grammar"),
    EX("R11-4", "Reading", "Read and answer.",
       text=["Electric buses are quiet and produce no smoke, which makes them ideal for city centres. "
             "However, they are expensive to buy: about twice the price of a diesel bus. "
             "They are much cheaper to run, so over ten years the total cost is similar or lower. "
             "The real problem for many Vietnamese cities is not the buses but the charging: "
             "a large fleet needs a depot with high-power chargers, and building one takes land, "
             "money and time."],
       items=["1. Give two advantages of electric buses.",
              "2. How much more do they cost to buy?",
              "3. Why is the total cost similar over ten years?",
              "4. What is 'the real problem'?", "5. What three things does a charging depot need?"],
       answers=["1. They are quiet and produce no smoke.", "2. About twice the price of a diesel bus.",
                "3. Because they are much cheaper to run.", "4. The charging, not the buses.",
                "5. Land, money and time."], level="M", kind="reading"),
    EX("R11-5", "Writing", "Write a description (110–130 words) of a journey you make, as it will be "
       "in 2050.",
       items=["The journey now – the future with will – one 'might' – how it will feel – "
              "one thing that might be lost."],
       answers=["See U11.6-W2 model. Marking: content 3, will/might 3, organisation 2, "
                "vocabulary 1, length 1."], level="D", kind="writing", lines=18),
]
