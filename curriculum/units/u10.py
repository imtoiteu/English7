# -*- coding: utf-8 -*-
"""UNIT 10 – ENERGY SOURCES  (Periods 70–76)"""
from curriculum.schema import *
from curriculum.audio_sources import AUDIO

UNIT = Unit(
    number=10, title="Energy Sources",
    theme="Kinds of energy, saving energy, renewable sources, the future",
    can_do=["name eight sources of energy and say which are renewable",
            "make predictions about the future with will and won't",
            "ask questions about the future (Will…? What will…?)",
            "read an article about energy and find causes and results",
            "listen to a talk about saving energy and take notes",
            "write a paragraph predicting energy in the future (100–120 words)"],
    grammar_focus=["Future simple: will / won't for predictions",
                   "Questions with will", "because / so for causes and results (recycled)"],
    pron_focus="/tʃ/ (chair) and /dʒ/ (June); the contraction 'll",
    vocab_focus="Energy sources, saving energy, environment verbs",
    project={"name": "Save Energy at School",
             "goal": "Groups audit one part of the school and present a plan to save energy.",
             "steps": ["Choose one area: classrooms, the corridor lights, the fans, the computer "
                       "room, or water.",
                       "Count and measure: how many lights/fans, how many hours a day, "
                       "how many are on when nobody is there?",
                       "Write five suggestions using will: 'If we do X, we will save Y.'",
                       "Make a simple poster with the numbers.",
                       "Present for two minutes to the class (or the head teacher!)."],
             "marking": "Content 3 – Language 3 – Poster/numbers 2 – Presentation 2 (total 10)"})

L1 = Lesson(
    code="U10L1", unit=10, number=1, period=70,
    lesson_type="Getting Started", title="Where does our energy come from?",
    objectives=["name eight sources of energy",
                "say which sources are renewable and which are not",
                "understand a conversation about electricity at home",
                "write three sentences about energy in their house"],
    recycled=["Unit 2 healthy habits; Unit 5 countable/uncountable; Unit 7 because/so"],
    vocab=[V("energy", "n", "/ˈenədʒi/", "năng lượng", "We use a lot of energy every day."),
           V("electricity", "n", "/ɪˌlekˈtrɪsəti/", "điện", "Electricity is expensive in summer."),
           V("coal", "n", "/kəʊl/", "than đá", "Coal is a traditional source of energy."),
           V("solar energy", "n", "/ˈsəʊlə ˈenədʒi/", "năng lượng mặt trời", "Solar energy is free after you buy the panels."),
           V("wind power", "n", "/ˈwɪnd paʊə/", "năng lượng gió", "Wind power is growing in Ninh Thuan."),
           V("hydro power", "n", "/ˈhaɪdrəʊ paʊə/", "thủy điện", "Viet Nam uses a lot of hydro power."),
           V("renewable", "adj", "/rɪˈnjuːəbl/", "tái tạo được", "Sun and wind are renewable."),
           V("save", "v", "/seɪv/", "tiết kiệm", "Turn off the lights to save energy.")],
    phrases=["turn on / turn off", "use energy", "save electricity", "run out of…",
             "be good for the environment"],
    grammar=G("Countable and uncountable energy words (recycled from Unit 5)",
              use=["Most energy words are UNCOUNTABLE: energy, electricity, coal, oil, gas, water. "
                   "No plural, and they take IS.",
                   "But: a solar panel, two wind turbines, three power stations — these are countable.",
                   "Quantities: a lot of energy, a little electricity, too much coal."],
              form=[["Uncountable", "Countable"],
                    ["energy, electricity, coal, oil, gas", "a solar panel, a turbine, a power station"],
                    ["There IS a lot of energy.", "There ARE three turbines."],
                    ["How MUCH electricity?", "How MANY panels?"]],
              examples=["We use too much electricity in the afternoon.",
                        "There are twelve solar panels on the roof of our school."],
              pitfall="*energies*, *electricities*, *How many electricity?* — these words have no "
                      "plural. Recycle the Unit 5 rule.",
              note="Test: can I say 'one energy, two energies'? No → uncountable → much, is, no plural."),
    pron=P("The sounds /tʃ/ (chair) and /dʒ/ (June)",
           "/tʃ/ = 'ch' as in chair, change, cheap, watch. /dʒ/ = 'j' or soft 'g' as in June, energy, "
           "village, change (the second sound!). /tʃ/ has no voice; /dʒ/ buzzes.",
           items=["/tʃ/: chair, cheap, change, watch, kitchen",
                  "/dʒ/: June, energy, village, bridge, generation",
                  "Compare: cheap – jeep | chair – Jane | watch – wage"],
           drill=["The cheap chair is in the kitchen.",
                  "In June the village will change to solar energy."],
           vn_note="Vietnamese has a sound close to /tʃ/ (ch) but not /dʒ/, so 'energy' often becomes "
                   "'enerchy' and 'June' becomes 'chune'. Put a hand on the throat: /dʒ/ must buzz."),
    listening=AUDIO['U10L1'],
    reading=T("Where Viet Nam's electricity comes from",
              ["Twenty years ago, most of Viet Nam's electricity came from two sources: hydro power "
               "from the big rivers, and coal.",
               "Hydro power is renewable — the water comes back with the rain — and it is cheap once "
               "the dam is built. But dams change rivers, move villages and produce much less "
               "electricity in a dry year.",
               "Coal is not renewable: when it is burnt, it is gone. It also produces a lot of smoke, "
               "which is bad for people's lungs and for the climate.",
               "In the last ten years something has changed very fast. Viet Nam now has more solar "
               "power than any other country in South-East Asia. In Ninh Thuan and Binh Thuan, where "
               "the sun is strong and it rains very little, whole valleys are covered with solar "
               "panels. Wind farms are growing along the southern coast too.",
               "The problem with sun and wind is simple: the sun goes down and the wind stops. "
               "So the next big question for Viet Nam is not how to make electricity — it is how to "
               "store it."],
              tasks=[EX("U10.1-R1", "Read and complete the table", "Write the advantages and "
                        "disadvantages.",
                        items=["Source | Renewable? | One advantage | One disadvantage",
                               "Hydro | ___ | ___ | ___", "Coal | ___ | ___ | ___",
                               "Solar | ___ | ___ | ___"],
                        answers=["Hydro | yes | cheap once the dam is built | dams change rivers, "
                                 "move villages, less electricity in a dry year",
                                 "Coal | no | (traditional, reliable) | it is gone when burnt; "
                                 "smoke is bad for lungs and climate",
                                 "Solar | yes | Viet Nam has strong sun; more than any other country "
                                 "in South-East Asia | the sun goes down (storage problem)"],
                        level="M", kind="reading"),
                     EX("U10.1-R2", "Read and answer", "Answer the questions.",
                        items=["1. What were the two main sources twenty years ago?",
                               "2. Which two provinces are mentioned for solar power? Why there?",
                               "3. What is the problem with sun and wind?",
                               "4. What is 'the next big question' for Viet Nam?"],
                        answers=["1. Hydro power and coal.",
                                 "2. Ninh Thuan and Binh Thuan, because the sun is strong and it "
                                 "rains very little.",
                                 "3. The sun goes down and the wind stops.",
                                 "4. How to store electricity."], level="M", kind="reading")]),
    speaking=[EX("U10.1-S1", "Energy survey", "Ask three classmates and complete the table.",
                 items=["How many lights are there in your house? / Do you turn off the computer at "
                        "night? / Does your family have solar panels or a solar water heater?"],
                 answers=["Report: 'Two of my friends have a solar water heater.'"],
                 level="M", kind="speaking")],
    writing=[EX("U10.1-W1", "Sentence writing", "Write three sentences about energy in your house.",
                items=["1. My family uses ______ .", "2. We use most electricity for ______ .",
                       "3. One way we save energy is ______ ."],
                answers=["Model: My family uses electricity and gas. We use most electricity for the "
                         "fan and the fridge. One way we save energy is by drying clothes in the sun."],
                level="M", kind="writing", lines=4)],
    communication={"function": "Talking about a problem at home",
                   "phrases": ["Look at this bill!", "Why is it so high?", "Let's do something.",
                               "Does that really make a difference?", "I'll try.",
                               "Every little helps."],
                   "roleplay": "A parent and a student look at a high electricity bill. "
                               "The parent gives three pieces of advice; the student asks whether "
                               "they really work.",
                   "real_life": "Family conversations about money and energy."},
    guided=[EX("U10.1-G1", "Renewable or not?", "Write R (renewable) or N (not renewable).",
               items=["1. solar energy ___", "2. coal ___", "3. wind power ___", "4. oil ___",
                      "5. hydro power ___", "6. gas ___"],
               answers=["1. R", "2. N", "3. R", "4. N", "5. R", "6. N"], level="E", kind="vocab"),
            EX("U10.1-G2", "much or many?", "Complete the questions.",
               items=["1. How ______ electricity do you use?", "2. How ______ solar panels are there?",
                      "3. How ______ energy does a fan use?", "4. How ______ light bulbs are there "
                      "in your house?", "5. How ______ coal does the power station burn?"],
               answers=["1. much", "2. many", "3. much", "4. many", "5. much"],
               level="M", kind="grammar")],
    independent=[EX("U10.1-I1", "Complete the text", "Use the words in the box.",
                    wordbank=["renewable", "electricity", "save", "solar", "turn off"],
                    items=["Our school uses a lot of (1) ______ . Last year we put twelve (2) ______ "
                           "panels on the roof. Sun is a (3) ______ source of energy, so it never "
                           "runs out. Students must (4) ______ the fans and lights when they leave "
                           "the room. In this way we (5) ______ about two million dong a year."],
                    answers=["1. electricity", "2. solar", "3. renewable", "4. turn off", "5. save"],
                    level="M", kind="vocab"),
                 EX("U10.1-I2", "Energy survey", "Do the survey and report two results.", items=[],
                    answers=["See U10.1-S1."], level="D", kind="speaking")],
    review=["8 energy words", "renewable vs not renewable",
            "energy words are uncountable", "/tʃ/ and /dʒ/"],
    homework=[EX("U10.1-H1", "Vocabulary", "Write the energy word.",
                 items=["1. energy from the sun: ______", "2. energy from moving air: ______",
                        "3. energy from rivers and dams: ______",
                        "4. a black rock we burn: ______",
                        "5. energy that never runs out: ______",
                        "6. what comes through the wires to your house: ______"],
                 answers=["1. solar energy", "2. wind power", "3. hydro power", "4. coal",
                          "5. renewable energy", "6. electricity"], level="E", kind="vocab"),
              EX("U10.1-H2", "Grammar", "Complete with much, many, a lot of or is/are.",
                 items=["1. How ______ electricity does your family use?",
                        "2. There ______ twelve solar panels on the roof.",
                        "3. There ______ a lot of energy in the sun.",
                        "4. How ______ wind turbines are there?",
                        "5. We use too ______ coal."],
                 answers=["1. much", "2. are", "3. is", "4. many", "5. much"],
                 level="M", kind="grammar"),
              EX("U10.1-H3", "Writing", "Write 4 sentences about how your family uses and saves energy.",
                 items=[], answers=["Model: My family uses electricity for lights, fans and the "
                                    "fridge. In summer we use the air conditioner in the evening. "
                                    "We save energy by drying clothes in the sun and by turning off "
                                    "the lights. My grandmother says the fan is enough, but I disagree!"],
                 level="M", kind="writing", lines=5),
              EX("U10.1-H4", "Pronunciation", "Say each pair five times: cheap – jeep, chair – Jane, "
                 "watch – wage. Then: energy, village, June, change.",
                 items=["/dʒ/ must buzz — put your hand on your throat."],
                 answers=["Spot-check in Lesson 2."], level="E", kind="pron")],
    workbook=[EX("U10.1-P1", "Complete the words", "Write the missing letters.",
                 items=["1. e n _ r g y", "2. e l e c t r _ c i t y", "3. r e n _ w a b l e",
                        "4. s _ l a r", "5. h _ d r o   p o w e r"],
                 answers=["1. energy", "2. electricity", "3. renewable", "4. solar", "5. hydro power"],
                 level="E", kind="vocab"),
              EX("U10.1-P2", "Match", "Match the source with the description.",
                 items=["1. solar", "2. wind", "3. hydro", "4. coal", "5. gas",
                        "a. from rivers and dams", "b. a black rock that is burnt",
                        "c. from the sun", "d. burnt for cooking, comes in a tank",
                        "e. from moving air"],
                 answers=["1–c", "2–e", "3–a", "4–b", "5–d"], level="E", kind="vocab"),
              EX("U10.1-P3", "/tʃ/ or /dʒ/?", "Write the sound.",
                 items=["1. chair ___", "2. June ___", "3. energy ___", "4. cheap ___",
                        "5. village ___", "6. watch ___", "7. bridge ___", "8. kitchen ___"],
                 answers=["1. /tʃ/", "2. /dʒ/", "3. /dʒ/", "4. /tʃ/", "5. /dʒ/", "6. /tʃ/",
                          "7. /dʒ/", "8. /tʃ/"], level="M", kind="pron"),
              EX("U10.1-P4", "Correct the mistakes", "One mistake per sentence.",
                 items=["1. How many electricity do you use?", "2. There are a lot of energies in "
                        "the sun.", "3. Solar energy are renewable.",
                        "4. We must turn off lights when we leave.",
                        "5. Coal is renewable because we can buy more."],
                 answers=["1. How much electricity do you use?",
                          "2. There is a lot of energy in the sun.",
                          "3. Solar energy is renewable.",
                          "4. We must turn off the lights when we leave.",
                          "5. Coal is not renewable — when it is burnt, it is gone."],
                 level="D", kind="grammar"),
              EX("U10.1-P5", "Writing", "Write 5 sentences comparing two sources of energy.",
                 items=["Use comparatives from Unit 4 and because/so from Unit 7."],
                 answers=["Model: Solar energy is cleaner than coal because it produces no smoke. "
                          "Coal is cheaper to start, so many countries still use it. Solar panels are "
                          "expensive at the beginning, but the sun costs nothing. However, solar "
                          "energy only works in the day, while a coal power station works all night. "
                          "In my opinion, Viet Nam should use more sun and less coal."],
                 level="D", kind="writing", lines=6)],
    procedure=[ST("Warm-up: Where does it come from?", 5,
                  ["Point at the light, the fan, the phone. Ask: 'Where does the energy come from?' "
                   "Accept Vietnamese; give English."],
                  "Suggest energy sources.", "Whole class", "Slide 2"),
               ST("Presentation: 8 energy words", 9,
                  ["Pictures; elicit and drill with stress: 'EN-er-gy, e-lec-TRI-ci-ty, "
                   "re-NEW-a-ble.",
                   "Two columns on the board: RENEWABLE / NOT RENEWABLE. Sort the sources."],
                  "Repeat; sort the sources.", "Whole class", "Slides 3–5"),
               ST("Pronunciation /tʃ/ /dʒ/", 7,
                  ["Hand on throat: /tʃ/ silent, /dʒ/ buzzes. Minimal pairs game.",
                   "Note 'change' has both sounds!"],
                  "Feel the difference; repeat.", "Whole class", "Slide 6"),
               ST("Listening: the electricity bill", 9,
                  ['Play the recording “Lesson 34: What Will I Do?” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; read in role.'],
                  "Listen and complete.", "Individual → pairs", "Slide 7"),
               ST("Reading + speaking", 10,
                  ["Read 'Where Viet Nam's electricity comes from'; complete the table.",
                   "Then the energy survey in pairs."],
                  "Read, complete, survey.", "Individual → pairs", "Slides 8–10"),
               ST("Wrap-up and homework", 5, ["Class total: how many lights are on in this room "
                                              "right now? Do we need them all? Set H1–H4."],
                  "Count and discuss.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Making energy visible",
                     ["Look up. How many lights are on in this room? Count them. Now: how many do we "
                      "actually need at eleven o'clock in the morning?",
                      "Every light is about 20 watts. Ten lights, five hours a day, two hundred days "
                      "a year… that is real money for our school.",
                      "This unit is not about science. It is about noticing. Once you notice, "
                      "you cannot stop noticing."]),
                  TK("Teaching /dʒ/",
                     ["Say 'ch' — chair. No voice, just air. /tʃ/.",
                      "Now put your hand on your throat and buzz the same shape: /dʒ/. June. Energy. "
                      "Village.",
                      "The word 'energy' is the most important word of this unit, and it has /dʒ/ "
                      "twice? No — once, at the start: EN-er-gy /ˈenədʒi/. The 'g' is /dʒ/. "
                      "Say it five times."])],
    support=["Give picture cards with the words printed.",
             "Provide the renewable/not table half-completed.",
             "Do the sound work with four pairs only."],
    challenge=["Ask for one advantage and one disadvantage of each source.",
               "Ask them to calculate the school's light usage.",
               "Ask them to explain 'renewable' in their own words."],
    assessment=["Names 6 of 8 energy sources", "Sorts renewable/not renewable correctly",
                "Distinguishes /tʃ/ and /dʒ/"],
    board_plan=["LEFT: 8 energy words with stress", "CENTRE: RENEWABLE | NOT RENEWABLE",
                "RIGHT: /tʃ/ | /dʒ/; Homework H1–H4"],
    materials=["Energy pictures", "An old electricity bill if possible", 'Recording: Lesson 34: What Will I Do? — VOA Learning English — Let’s Learn English, Level 1 (4:04)'],
)

L2 = Lesson(
    code="U10L2", unit=10, number=2, period=71,
    lesson_type="A Closer Look 1", title="Saving energy: verbs and collocations",
    objectives=["use ten verbs and phrases about using and saving energy",
                "pronounce /tʃ/ and /dʒ/ correctly in sentences",
                "give five pieces of advice about saving energy",
                "explain a cause and a result"],
    recycled=["U10L1 energy vocabulary; Unit 2 should/shouldn't; Unit 7 must/mustn't and because/so"],
    vocab=[V("turn off / turn on", "v phr", "/tɜːn ɒf/", "tắt / bật", "Turn off the fan when you leave."),
           V("waste", "v/n", "/weɪst/", "lãng phí", "Don't waste water."),
           V("reduce", "v", "/rɪˈdjuːs/", "giảm", "We must reduce our electricity use."),
           V("pollution", "n", "/pəˈluːʃn/", "ô nhiễm", "Coal causes air pollution."),
           V("climate change", "n", "/ˈklaɪmət tʃeɪndʒ/", "biến đổi khí hậu", "Climate change affects farmers."),
           V("bulb", "n", "/bʌlb/", "bóng đèn", "An LED bulb uses much less electricity."),
           V("charge", "v", "/tʃɑːdʒ/", "sạc", "Don't charge your phone all night."),
           V("standby", "n", "/ˈstændbaɪ/", "chế độ chờ", "A TV on standby still uses electricity.")],
    phrases=["turn off the lights", "waste electricity", "reduce pollution", "save money",
             "cause climate change", "use less / more"],
    grammar=G("Cause and result: because / so / cause (recycled and extended)",
              use=["because + cause: We use more electricity in summer BECAUSE it is hot.",
                   "so + result: It is hot, SO we use more electricity.",
                   "X causes Y: Burning coal CAUSES air pollution.",
                   "This means that…: The sun goes down. THIS MEANS THAT we need storage."],
              form=[["Structure", "Example"],
                    ["result because cause", "The bill is high because we use the air conditioner."],
                    ["cause, so result", "It was 39 degrees, so the bill is high."],
                    ["X causes Y", "Coal smoke causes air pollution."],
                    ["This means that…", "Solar panels need sun. This means that they produce nothing "
                     "at night."]],
              examples=["Leaving computers on standby wastes electricity, so our bill is higher "
                        "than it should be.",
                        "Burning coal causes pollution and climate change."],
              pitfall="Still the number one error: *Because … so …* in one sentence. "
                      "Also *It causes to pollution* — 'cause' takes a direct object: "
                      "'It causes pollution'.",
              note="'This means that…' is a very useful chunk for explaining consequences."),
    pron=P("/tʃ/ and /dʒ/ in longer words and sentences",
           "Watch: CHARGE has BOTH sounds (/tʃɑːdʒ/). CHANGE too (/tʃeɪndʒ/). "
           "ENERGY, VILLAGE, BRIDGE end with /dʒ/.",
           items=["charge /tʃɑːdʒ/", "change /tʃeɪndʒ/", "energy /ˈenədʒi/", "village /ˈvɪlɪdʒ/",
                  "kitchen /ˈkɪtʃɪn/"],
           drill=["Don't charge your phone in the kitchen all night.",
                  "Climate change is changing our village."],
           vn_note="Final /dʒ/ (village, bridge, change) is often dropped completely. "
                   "Hold the sound: villa-dge."),
    listening=AUDIO['U10L2'],
    reading=T("Ten minutes that save a million",
              ["A secondary school in Da Nang did a simple experiment. For one week, a teacher "
               "photographed the school at 12.15, when the morning shift had gone home.",
               "The photographs showed 38 lights, 19 fans and 6 computers still on, in rooms with "
               "nobody in them.",
               "The school did not buy anything. It made one rule: the last person out of a room "
               "turns off the lights, the fan and the computer. Each class chose a monitor to check.",
               "After three months, the school compared the bills. It was paying 1.1 million dong a "
               "month less than the year before.",
               "'The interesting thing,' the head teacher said, 'is that nobody worked harder. "
               "Nobody sat in the dark. We simply stopped paying for empty rooms.'",
               "The school used the money for a new water filter and forty pairs of school shoes for "
               "students who needed them."],
              tasks=[EX("U10.2-R1", "Read and answer", "Answer the questions.",
                        items=["1. What did the teacher do for one week?",
                               "2. What did the photographs show?",
                               "3. What rule did the school make?",
                               "4. How much did the school save each month?",
                               "5. What did the school do with the money?"],
                        answers=["1. Photographed the school at 12.15, after the morning shift had "
                                 "gone home.",
                                 "2. 38 lights, 19 fans and 6 computers still on in empty rooms.",
                                 "3. The last person out of a room turns off the lights, the fan and "
                                 "the computer (with a monitor in each class to check).",
                                 "4. 1.1 million dong a month.",
                                 "5. It bought a new water filter and forty pairs of school shoes."],
                        level="M", kind="reading")]),
    speaking=[EX("U10.2-S1", "Give the advice", "Give five pieces of advice about saving energy, "
                 "each with a reason.",
                 items=["Use: 'You should…because…' / 'Don't…, because…' / 'If we…, we will save…'"],
                 answers=["Model: You should turn off the fan when you leave the room, because it "
                          "uses electricity for nobody."], level="M", kind="speaking"),
              EX("U10.2-S2", "Energy detective", "Look around your classroom right now. "
                 "Find three ways to save energy and explain them to your partner.",
                 items=["Look at: lights, fans, windows, the door, the computer, the projector."],
                 answers=["Model: Half the lights are on but the sun is very bright, so we could turn "
                          "off the row near the window."], level="D", kind="speaking")],
    writing=[EX("U10.2-W1", "Cause and result", "Join the sentences with because, so or causes.",
                items=["1. We use the air conditioner a lot. / The bill is high. (so)",
                       "2. The bill is high. / We use the air conditioner a lot. (because)",
                       "3. Burning coal / air pollution (causes)",
                       "4. The sun goes down. / Solar panels produce nothing at night. "
                       "(This means that)"],
                answers=["1. We use the air conditioner a lot, so the bill is high.",
                         "2. The bill is high because we use the air conditioner a lot.",
                         "3. Burning coal causes air pollution.",
                         "4. The sun goes down. This means that solar panels produce nothing at night."],
                level="M", kind="writing")],
    communication={"function": "Persuading somebody to change a habit",
                   "phrases": ["It only takes a second.", "Every little helps.",
                               "Think of the money.", "I know, but…", "Let's try it for a month.",
                               "You'll see the difference."],
                   "roleplay": "You want your family (or your class) to save energy. "
                               "Give three arguments; your partner gives two objections.",
                   "real_life": "Persuading people at home to change a small habit."},
    guided=[EX("U10.2-G1", "Match the verb", "Complete with turn off, waste, reduce, cause, charge, "
               "save.",
               items=["1. Please ______ the lights when you leave.",
                      "2. Don't ______ water — the tap is still running!",
                      "3. LED bulbs ______ our electricity bill.",
                      "4. Burning coal ______ pollution.",
                      "5. Don't ______ your phone all night.",
                      "6. These small actions ______ a lot of money."],
               answers=["1. turn off", "2. waste", "3. reduce", "4. causes", "5. charge", "6. save"],
               level="E", kind="vocab"),
            EX("U10.2-G2", "because or so?", "Complete.",
               items=["1. The bill was high ______ we used the air conditioner.",
                      "2. It was very hot, ______ we used the air conditioner.",
                      "3. We changed the bulbs, ______ the bill is lower now.",
                      "4. Solar panels need sun, ______ they produce nothing at night."],
               answers=["1. because", "2. so", "3. so", "4. so"], level="M", kind="grammar")],
    independent=[EX("U10.2-I1", "Error clinic", "Correct one mistake in each sentence.",
                    items=["1. Because it was hot so we used the fan.",
                           "2. Coal causes to pollution.", "3. Please turn off light.",
                           "4. We must reduce the electricities.",
                           "5. This means solar panels produce nothing at night."],
                    answers=["1. Because it was hot, we used the fan. / It was hot, so we used the fan.",
                             "2. Coal causes pollution.", "3. Please turn off the light.",
                             "4. We must reduce our electricity (use).",
                             "5. This means that solar panels produce nothing at night."],
                    level="D", kind="grammar"),
                 EX("U10.2-I2", "Energy detective", "Do U10.2-S2 and report one idea to the class.",
                    items=[], answers=["See U10.2-S2."], level="D", kind="speaking")],
    review=["10 energy verbs and collocations", "because / so / causes / this means that",
            "/tʃ/ and /dʒ/ including final /dʒ/"],
    homework=[EX("U10.2-H1", "Vocabulary", "Complete with waste, reduce, pollution, climate change, "
                 "bulb, standby.",
                 items=["1. An LED ______ uses much less electricity.",
                        "2. A TV on ______ still uses power.",
                        "3. Burning coal causes air ______ .",
                        "4. We must ______ our energy use.", "5. Don't ______ water.",
                        "6. ______ is a problem for farmers."],
                 answers=["1. bulb", "2. standby", "3. pollution", "4. reduce", "5. waste",
                          "6. Climate change"], level="E", kind="vocab"),
              EX("U10.2-H2", "Grammar", "Join the sentences with because, so, causes or "
                 "this means that.",
                 items=["1. It was 39 degrees. / The bill was very high.",
                        "2. The bill was very high. / It was 39 degrees.",
                        "3. Burning coal / air pollution",
                        "4. LED bulbs use 80% less electricity. / We will save money."],
                 answers=["1. It was 39 degrees, so the bill was very high.",
                          "2. The bill was very high because it was 39 degrees.",
                          "3. Burning coal causes air pollution.",
                          "4. LED bulbs use 80% less electricity. This means that we will save money."],
                 level="M", kind="grammar"),
              EX("U10.2-H3", "Writing", "Write 5 pieces of advice about saving energy at home, "
                 "each with a reason.",
                 items=[], answers=["Model: You should turn off the lights when you leave a room, "
                                    "because empty rooms don't need light. Don't leave the TV on "
                                    "standby, because it uses electricity all night. You should set "
                                    "the air conditioner at 26 degrees, so it works less. "
                                    "Change your old bulbs to LED, because they use 80% less "
                                    "electricity. Dry your clothes in the sun — it is free!"],
                 level="M", kind="writing", lines=7),
              EX("U10.2-H4", "Pronunciation", "Say these five words five times: charge, change, "
                 "energy, village, kitchen.",
                 items=["Do not lose the final sound in charge, change and village."],
                 answers=["Spot-check in Lesson 3."], level="E", kind="pron")],
    workbook=[EX("U10.2-P1", "Match", "Match the two halves.",
                 items=["1. turn off", "2. waste", "3. reduce", "4. cause", "5. charge",
                        "a. pollution", "b. your phone", "c. the lights", "d. water", "e. the bill"],
                 answers=["1–c", "2–d", "3–e", "4–a", "5–b"], level="E", kind="vocab"),
              EX("U10.2-P2", "because / so / causes", "Complete.",
                 items=["1. We used the fan all day, ______ the bill is high.",
                        "2. The bill is high ______ we used the fan all day.",
                        "3. Coal smoke ______ air pollution.",
                        "4. Solar panels work in the day, ______ we need batteries for the night.",
                        "5. He left the computer on ______ he forgot."],
                 answers=["1. so", "2. because", "3. causes", "4. so", "5. because"],
                 level="M", kind="grammar"),
              EX("U10.2-P3", "/tʃ/ or /dʒ/ — or both?", "Write the sounds you hear.",
                 items=["1. charge ___", "2. change ___", "3. bridge ___", "4. chicken ___",
                        "5. energy ___", "6. watch ___"],
                 answers=["1. /tʃ/ … /dʒ/ (both)", "2. /tʃ/ … /dʒ/ (both)", "3. /dʒ/", "4. /tʃ/",
                          "5. /dʒ/", "6. /tʃ/"], level="D", kind="pron"),
              EX("U10.2-P4", "Reading", "Read and answer.",
                 text=["A fan uses about 60 watts. An air conditioner uses about 1,000 watts — "
                       "almost seventeen times more. This does not mean you should never use the air "
                       "conditioner. It means you should use both: set the air conditioner at 26 "
                       "degrees and turn on the fan. The fan moves the cool air, so the room feels "
                       "colder than it is, and the air conditioner works less."],
                 items=["1. How many watts does a fan use?",
                        "2. How much more does an air conditioner use?",
                        "3. What does the writer advise?", "4. Why does using both work?"],
                 answers=["1. About 60 watts.", "2. Almost seventeen times more (about 1,000 watts).",
                          "3. Use both: the air conditioner at 26 degrees plus the fan.",
                          "4. Because the fan moves the cool air, so the room feels colder and the "
                          "air conditioner works less."], level="M", kind="reading"),
              EX("U10.2-P5", "Writing", "Write a paragraph (80–90 words) about how your family could "
                 "save energy.",
                 items=["Three suggestions, each with a reason, and one number if you can."],
                 answers=["Model: My family could save energy in three ways. First, we should change "
                          "the old bulbs in the kitchen and the yard to LED, because LED bulbs use "
                          "about 80% less electricity. Second, we should turn off the TV at the wall "
                          "instead of leaving it on standby all night. Third, we should set the air "
                          "conditioner at 26 degrees and use the fan as well, so the machine works "
                          "less. Last June our bill was 780,000 dong, and I think we could reduce it "
                          "by a fifth. (91 words)"], level="D", kind="writing", lines=10)],
    procedure=[ST("Warm-up: Renewable race", 5,
                  ["Teacher says an energy source; students shout R or N. Recycles Lesson 1."],
                  "Sort the sources.", "Whole class", "Slide 2"),
               ST("Presentation: 10 saving-energy verbs", 9,
                  ["Mime turn off / turn on / charge / waste. Build the collocations on the board."],
                  "Repeat; copy the collocations.", "Whole class", "Slides 3–5"),
               ST("Grammar: cause and result", 8,
                  ["Two boxes: CAUSE → RESULT. Show the four ways to join them.",
                   "Drill with real examples from the classroom."],
                  "Produce cause-result sentences.", "Whole class", "Slides 6–7"),
               ST("Listening: the assembly talk", 10,
                  ['Play the recording “Going to — plans people have made” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.',
                   "Highlight the numbers — they make the argument."],
                  "Listen and complete the notes.", "Individual → pairs", "Slide 8"),
               ST("Speaking: energy detective", 9,
                  ["Students look around the real classroom and find three savings; report to a "
                   "partner, then to the class."],
                  "Observe, discuss, report.", "Pairs", "Slides 9–10"),
               ST("Wrap-up and homework", 4, ["Choose one class rule to try for a week. Set H1–H4."],
                  "Agree a class rule.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Numbers make an argument",
                     ["'We should save energy.' Everybody agrees, and nothing happens.",
                      "'Forty-one lights are on in empty rooms every break time, which costs us four "
                      "and a half million dong a year — thirty library books.' Now something happens.",
                      "In your project, COUNT something. A number that you found yourself is worth "
                      "more than any adjective."]),
                  TK("Because and so — the last warning",
                     ["We met this in Unit 1 and Unit 7. It is still the most common mistake in "
                      "this class.",
                      "In Vietnamese: VÌ trời nóng NÊN chúng tôi bật quạt. Two words, correct.",
                      "In English: choose ONE. 'Because it was hot, we used the fan.' OR "
                      "'It was hot, so we used the fan.'",
                      "If I see 'Because… so…' in your homework, I will send it back unmarked."])],
    support=["Give the collocation list on a desk card.",
             "Provide sentence frames for the advice.",
             "Reduce the error clinic to three sentences."],
    challenge=["Ask them to calculate a saving with real numbers.",
               "Ask for 'This means that…' in their explanations.",
               "Ask them to write a 40-second assembly announcement."],
    assessment=["6 of 6 correct collocations", "Correct use of because/so in 4 of 4 items",
                "Final /dʒ/ audible in 'change' and 'village'"],
    board_plan=["LEFT: energy collocations", "CENTRE: CAUSE → RESULT (because / so / causes / "
                "this means that)", "RIGHT: /tʃ/ | /dʒ/; Homework H1–H4"],
    materials=['Recording: Going to — plans people have made — ELLLO — Sound Grammar (3:02)', "The classroom itself (lights, fans)"],
)

L3 = Lesson(
    code="U10L3", unit=10, number=3, period=72,
    lesson_type="A Closer Look 2", title="The future simple: will and won't",
    objectives=["make predictions about the future with will and won't",
                "ask questions about the future with will",
                "use 'I think… will…' and 'I don't think… will…'",
                "talk about their own future in five sentences"],
    recycled=["U10L1–L2 energy vocabulary, because/so; Unit 6 present continuous for arrangements"],
    vocab=[V("future", "n", "/ˈfjuːtʃə/", "tương lai", "In the future we will use more solar energy."),
           V("predict", "v", "/prɪˈdɪkt/", "dự đoán", "Scientists predict a hotter climate."),
           V("probably", "adv", "/ˈprɒbəbli/", "có lẽ", "It will probably rain tomorrow."),
           V("certainly", "adv", "/ˈsɜːtnli/", "chắc chắn", "Prices will certainly rise."),
           V("run out", "v phr", "/rʌn aʊt/", "cạn kiệt", "Oil will run out one day."),
           V("replace", "v", "/rɪˈpleɪs/", "thay thế", "Solar power will replace coal.")],
    phrases=["I think … will …", "I don't think … will …", "will probably", "won't … at all",
             "in ten years' time"],
    grammar=G("Future simple: will / won't",
              use=["WILL + bare verb for predictions and things we are sure about: "
                   "Solar energy will be cheaper.",
                   "WON'T (= will not) for negative predictions: Coal won't disappear immediately.",
                   "WILL is the same for all subjects — no -s, no 'to'.",
                   "Questions: Will + subject + bare verb? – Yes, it will. / No, it won't.",
                   "Adverbs go between will and the verb: It will PROBABLY rain. "
                   "It will CERTAINLY be hot.",
                   "For negative opinions English prefers 'I don't think it will…' to "
                   "'I think it won't…'."],
              form=[["", "Form", "Example"],
                    ["+", "will + bare verb", "Solar energy will be cheaper."],
                    ["–", "won't + bare verb", "Coal won't disappear immediately."],
                    ["?", "Will + subject + verb?", "Will electric cars be normal? – Yes, they will."],
                    ["adverb", "will + adverb + verb", "It will probably rain."],
                    ["opinion", "I (don't) think … will …", "I don't think oil will last 50 years."]],
              examples=["In twenty years, most houses in Viet Nam will have solar panels.",
                        "I don't think petrol cars will disappear before 2040.",
                        "Will we still use coal in 2050? – Some countries will."],
              pitfall="*She wills go* (no -s), *will to go* (no 'to'), *I think it won't rain* "
                      "(English prefers 'I don't think it will rain').",
              note="'ll is the normal spoken form: I'll, you'll, it'll, we'll. Teach it from the start."),
    pron=P("The contraction 'll and weak 'will'",
           "In speech, 'will' becomes 'll and almost disappears: I'll /aɪl/, we'll /wiːl/, "
           "it'll /ˈɪtl/, they'll /ðeɪl/. 'Won't' is /wəʊnt/ — long and clear.",
           items=["I'll /aɪl/", "we'll /wiːl/", "it'll /ˈɪtl/", "they'll /ðeɪl/",
                  "won't /wəʊnt/ (not 'want' /wɒnt/!)"],
           drill=["I'll turn off the lights. We'll save money.",
                  "It'll probably rain, so they'll stay at home.",
                  "I won't forget. I don't want to forget."],
           vn_note="Two problems: (1) students say the full 'will' every time, which sounds heavy; "
                   "(2) 'won't' and 'want' sound the same. Won't = /wəʊnt/ (long o); "
                   "want = /wɒnt/ (short o)."),
    listening=AUDIO['U10L3'],
    reading=T("Five predictions for 2040",
              ["Nobody can see the future, but here are five things that most scientists agree about.",
               "1. Solar power will be the cheapest electricity in most of the world. In some places "
               "it already is.",
               "2. Petrol cars won't disappear, but they will become a small minority in cities. "
               "Many countries will stop selling new ones.",
               "3. Air conditioning will use much more electricity than today, because the world will "
               "be hotter and more people will be able to afford it. This is a real problem for "
               "hot countries like Viet Nam.",
               "4. Batteries will get much better and much cheaper. Storage, not production, will be "
               "the key.",
               "5. And one prediction that is not about technology at all: the countries that manage "
               "best will be the ones that waste least. A kilowatt you don't use is always the "
               "cheapest kilowatt."],
              tasks=[EX("U10.3-R1", "Read and answer", "Answer the questions.",
                        items=["1. What will be the cheapest electricity?",
                               "2. Will petrol cars disappear? Explain.",
                               "3. Why will air conditioning use more electricity? (two reasons)",
                               "4. What will be 'the key'?",
                               "5. Explain prediction 5 in your own words."],
                        answers=["1. Solar power.",
                                 "2. No, but they will become a small minority in cities, and many "
                                 "countries will stop selling new ones.",
                                 "3. Because the world will be hotter and more people will be able to "
                                 "afford it.",
                                 "4. Storage (batteries), not production.",
                                 "5. The best result comes from using less, not only from making "
                                 "more: saved energy is the cheapest energy."],
                        level="M", kind="reading")]),
    speaking=[EX("U10.3-S1", "Agree or disagree", "Read each prediction and say whether you agree, "
                 "with a reason.",
                 items=["1. In 2040 every house in Viet Nam will have solar panels.",
                        "2. Petrol motorbikes will disappear from Vietnamese cities.",
                        "3. Students won't use paper books in 2040.",
                        "4. People will work four days a week.",
                        "5. Our town will be hotter in 2040."],
                 answers=["Model: I agree. I think every house will have solar panels, because they "
                          "are getting cheaper every year. / I don't think students will stop using "
                          "paper books, because…"], level="M", kind="speaking"),
              EX("U10.3-S2", "My future", "Tell your partner five things about your own future.",
                 items=["Use: I'll…, I won't…, I'll probably…, I don't think I'll…"],
                 answers=["Model: I'll finish Grade 12 in five years. I'll probably study in Hanoi. "
                          "I don't think I'll live in my village all my life, but I'll come back "
                          "every Tet."], level="D", kind="speaking")],
    writing=[EX("U10.3-W1", "will or won't?", "Complete the predictions.",
                items=["1. Solar energy ______ be cheaper. (+)", "2. Coal ______ disappear "
                       "immediately. (–)", "3. I think batteries ______ be much better. (+)",
                       "4. I don't think oil ______ last for ever. (+ after 'don't think')",
                       "5. The world ______ probably be hotter. (+)"],
                answers=["1. will", "2. won't", "3. will", "4. will", "5. will"],
                level="E", kind="writing")],
    communication={"function": "Agreeing and disagreeing about the future",
                   "phrases": ["I think so too.", "I'm not so sure.", "Maybe, but…",
                               "That's optimistic!", "I hope you're right.",
                               "Only time will tell."],
                   "roleplay": "Two students discuss three predictions about their town in 2040. "
                               "Agree on one and disagree on one.",
                   "real_life": "Discussing plans, hopes and worries about the future."},
    guided=[EX("U10.3-G1", "Make predictions", "Write a sentence with will or won't.",
               items=["1. solar panels / cheaper (+)", "2. coal / disappear immediately (–)",
                      "3. electric cars / normal in cities (+)",
                      "4. the world / cooler (–)", "5. batteries / important (+)"],
               answers=["1. Solar panels will be cheaper.",
                        "2. Coal won't disappear immediately.",
                        "3. Electric cars will be normal in cities.",
                        "4. The world won't be cooler.", "5. Batteries will be important."],
               level="E", kind="grammar"),
            EX("U10.3-G2", "Questions with will", "Write the question and a short answer.",
               items=["1. (solar energy / be cheaper?) – Yes", "2. (coal / disappear soon?) – No",
                      "3. (we / use more energy?) – Yes", "4. (petrol cars / disappear?) – No"],
               answers=["1. Will solar energy be cheaper? – Yes, it will.",
                        "2. Will coal disappear soon? – No, it won't.",
                        "3. Will we use more energy? – Yes, we will.",
                        "4. Will petrol cars disappear? – No, they won't."],
               level="M", kind="grammar")],
    independent=[EX("U10.3-I1", "Error clinic", "Correct one mistake in each sentence.",
                    items=["1. She will goes to Hanoi next year.", "2. We will to save energy.",
                           "3. He willn't come.", "4. I think it won't rain tomorrow.",
                           "5. Will you to help me?", "6. It will probably to be hot."],
                    answers=["1. She will go to Hanoi next year.", "2. We will save energy.",
                             "3. He won't come.", "4. I don't think it will rain tomorrow.",
                             "5. Will you help me?", "6. It will probably be hot."],
                    level="D", kind="grammar",
                    note="After will: no 'to', no -s. Negative: won't. For opinions: "
                         "'I don't think … will …'"),
                 EX("U10.3-I2", "Future discussion", "Do U10.3-S1 and report one agreement and one "
                    "disagreement.", items=[], answers=["See U10.3-S1."], level="D", kind="speaking")],
    review=["will / won't + bare verb", "Will + subject + verb?", "will probably / will certainly",
            "I don't think … will …"],
    homework=[EX("U10.3-H1", "Grammar", "Complete with will or won't.",
                 items=["1. Solar energy ______ be cheaper in ten years.",
                        "2. Oil ______ last for ever.",
                        "3. I think electric cars ______ be normal by 2040.",
                        "4. The world ______ get cooler.",
                        "5. Batteries ______ probably be the key.",
                        "6. ______ you help me with my project? – Yes, I ______ ."],
                 answers=["1. will", "2. won't", "3. will", "4. won't", "5. will", "6. Will; will"],
                 level="E", kind="grammar"),
              EX("U10.3-H2", "Grammar", "Rewrite with 'I don't think… will…'.",
                 items=["1. I think petrol cars won't disappear soon. →",
                        "2. I think it won't rain tomorrow. →",
                        "3. I think we won't finish before six. →"],
                 answers=["1. I don't think petrol cars will disappear soon.",
                          "2. I don't think it will rain tomorrow.",
                          "3. I don't think we will finish before six."],
                 level="M", kind="grammar"),
              EX("U10.3-H3", "Writing", "Write 5 predictions about your town or your school in 2040.",
                 items=["Use will, won't, will probably and one 'I don't think… will…'."],
                 answers=["Model: In 2040 my school will probably have solar panels on every roof. "
                          "There won't be any old fans — everything will be new and quiet. "
                          "Students will use tablets instead of heavy books. I don't think teachers "
                          "will disappear, because a machine cannot help a frightened student. "
                          "Our town will certainly be hotter, so the trees we plant now will be "
                          "very important."], level="M", kind="writing", lines=7),
              EX("U10.3-H4", "Pronunciation", "Say these five sentences five times with the "
                 "contraction: I'll help you. We'll save money. It'll be hot. They'll come. "
                 "I won't forget.",
                 items=["Won't = /wəʊnt/ (long), NOT want = /wɒnt/ (short)."],
                 answers=["Spot-check in Lesson 4."], level="M", kind="pron")],
    workbook=[EX("U10.3-P1", "will or won't?", "Complete the predictions.",
                 items=["1. In 2050 people ______ live on the moon. (probably not)",
                        "2. Solar energy ______ be cheaper. (yes)",
                        "3. Petrol cars ______ disappear from cities. (yes)",
                        "4. The world ______ be cooler. (no)",
                        "5. We ______ need batteries. (yes)"],
                 answers=["1. won't", "2. will", "3. will", "4. won't", "5. will"],
                 level="E", kind="grammar"),
              EX("U10.3-P2", "Make questions", "Write the question.",
                 items=["1. ______ ? – Yes, solar panels will be cheaper.",
                        "2. ______ ? – No, coal won't disappear immediately.",
                        "3. ______ ? – I think batteries will be the key.",
                        "4. ______ ? – In about twenty years."],
                 answers=["1. Will solar panels be cheaper?",
                          "2. Will coal disappear immediately?",
                          "3. What will be the key? / What do you think will be the key?",
                          "4. When will it happen?"], level="M", kind="grammar"),
              EX("U10.3-P3", "Adverbs with will", "Put the adverb in the right place.",
                 items=["1. It will be hot tomorrow. (probably)",
                        "2. Prices will rise next year. (certainly)",
                        "3. We will finish before six. (probably not → use won't)",
                        "4. She will come to the meeting. (probably)"],
                 answers=["1. It will probably be hot tomorrow.",
                          "2. Prices will certainly rise next year.",
                          "3. We probably won't finish before six.",
                          "4. She will probably come to the meeting."],
                 level="D", kind="grammar",
                 note="With 'won't', the adverb goes BEFORE: 'probably won't'."),
              EX("U10.3-P4", "Correct the mistakes", "One mistake per sentence.",
                 items=["1. He will goes to university.", "2. They will to help us.",
                        "3. It willn't rain.", "4. I think it won't be cold.",
                        "5. Will she to come tomorrow?"],
                 answers=["1. He will go to university.", "2. They will help us.",
                          "3. It won't rain.", "4. I don't think it will be cold.",
                          "5. Will she come tomorrow?"], level="D", kind="grammar"),
              EX("U10.3-P5", "Writing", "Write 6 predictions about YOUR life in ten years.",
                 items=["Use will, won't, will probably, and one 'I don't think I'll…'."],
                 answers=["Model: In ten years I'll be twenty-three. I'll probably finish university "
                          "in Hanoi or Da Nang. I don't think I'll work in an office, because I "
                          "prefer being outside. I'll certainly still play badminton. My family will "
                          "still live in the same village, and I'll visit them every month. "
                          "I won't forget my English teacher!"], level="D", kind="writing", lines=8)],
    procedure=[ST("Warm-up: Fortune teller", 5,
                  ["Teacher 'predicts' three funny things about students ('You'll be a famous chef!'). "
                   "Elicit the structure."],
                  "Listen and notice 'will'.", "Whole class", "Slide 2"),
               ST("Presentation: will / won't", 12,
                  ["Draw a time line: NOW → 2040. Write predictions on the line.",
                   "Build the form: will + bare verb, same for everybody. Box it: NO -s, NO 'to'.",
                   "Add won't, and the question form. Drill short answers.",
                   "Then the adverbs: will probably / will certainly; and 'I don't think … will …'.",
                   "Teach the contraction 'll from the start."],
                  "Copy the form; produce six predictions.", "Whole class", "Slides 3–7"),
               ST("Guided practice", 8, ["U10.3-G1, G2 and W1; error clinic U10.3-I1."],
                  "Write predictions and questions; correct the errors.", "Pairs",
                  "Student Book p. U10L3"),
               ST("Listening: predictions about 2050", 8,
                  ['Play the recording “Will — predictions and promises” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; do the who-says-what task and the gap-fill.'],
                  "Listen and identify the predictions.", "Individual → pairs", "Slide 8"),
               ST("Speaking: agree or disagree", 9,
                  ["Five predictions on the board; students agree or disagree with a reason, "
                   "then talk about their own future."],
                  "Discuss and predict.", "Pairs", "Slides 9–10"),
               ST("Wrap-up and homework", 3, ["Class prediction: what will our school be like in "
                                              "2040? Three ideas. Set H1–H4."],
                  "Predict; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Will is the easiest tense in English",
                     ["Good news. 'Will' does not change. Not for he, not for she, not for anybody.",
                      "I will. You will. He will. She will. It will. We will. They will. Always WILL.",
                      "And after it, the verb is naked: will GO, will BE, will HELP. No 'to', no -s.",
                      "The only difficult part is the negative: not 'willn't' but WON'T. "
                      "Say it: won't, won't, won't."]),
                  TK("'I don't think it will rain'",
                     ["Listen to two sentences. 'I think it won't rain.' 'I don't think it will rain.'",
                      "Both are understandable, but English speakers almost always choose the second.",
                      "We move the negative to the FIRST verb: I DON'T think… will…",
                      "It sounds more natural and it is worth a mark in the test. Say three: "
                      "I don't think it will rain. I don't think he'll come. I don't think we'll win."])],
    support=["Give a substitution table for predictions.",
             "Colour the 'will + bare verb' box on the board.",
             "Reduce the error clinic to four sentences."],
    challenge=["Add 'might' as a weaker prediction (preview of Unit 11).",
               "Ask for predictions with two adverbs and a reason.",
               "Ask them to interview the teacher about the future."],
    assessment=["5 of 5 correct will/won't", "Forms a will question with a short answer",
                "Uses the contraction 'll in speaking"],
    board_plan=["LEFT: time line NOW → 2040", "CENTRE: will + BARE VERB (no -s, no to) | won't | "
                "Will…? ", "RIGHT: probably / certainly; I don't think … will…; Homework H1–H4"],
    materials=['Recording: Will — predictions and promises — ELLLO — Sound Grammar (3:02)', "Coloured chalk"],
)

L4 = Lesson(
    code="U10L4", unit=10, number=4, period=73,
    lesson_type="Communication", title="Everyday English: making promises and offers with will",
    objectives=["make promises and instant decisions with will",
                "offer help with 'I'll…' and 'Shall I…?'",
                "take part in a 6-turn conversation about a problem",
                "write three promises about saving energy"],
    recycled=["U10L1–L3 energy vocabulary and will; Unit 3 offers; Unit 2 advice"],
    vocab=[V("promise", "n/v", "/ˈprɒmɪs/", "lời hứa; hứa", "I promise I'll turn off the lights."),
           V("decide", "v", "/dɪˈsaɪd/", "quyết định", "We decided to change the bulbs."),
           V("agree", "v", "/əˈɡriː/", "đồng ý", "Everybody agreed to try for a month."),
           V("volunteer", "v", "/ˌvɒlənˈtɪə/", "tình nguyện", "Two students volunteered to be monitors."),
           V("remind", "v", "/rɪˈmaɪnd/", "nhắc nhở", "Please remind me tomorrow."),
           V("forget", "v", "/fəˈɡet/", "quên", "Don't forget to turn off the fan.")],
    phrases=["I'll do it.", "Don't worry, I'll…", "I promise I won't…", "Shall I…?",
             "I'll remind you.", "Don't forget to…"],
    grammar=G("Three more uses of will: promises, instant decisions and offers",
              use=["PROMISE: I'll turn off the lights, I promise. / I won't forget.",
                   "INSTANT DECISION (you decide as you speak): 'The fan is still on.' "
                   "'Oh — I'll turn it off.'",
                   "OFFER: I'll help you. / Shall I close the window?",
                   "Compare with Unit 6: an ARRANGEMENT already made uses the present continuous "
                   "('I'm meeting Nam at four'), but a decision made NOW uses will."],
              form=[["Function", "Language", "Example"],
                    ["promise", "I'll… / I won't…", "I'll be there at seven, I promise."],
                    ["instant decision", "I'll…", "It's raining. I'll take an umbrella."],
                    ["offer", "I'll… / Shall I…?", "I'll carry that for you. / Shall I help?"],
                    ["arrangement (Unit 6)", "am/is/are + V-ing", "I'm meeting Nam at four."]],
              examples=["Don't worry — I'll remind you tomorrow.",
                        "The light is on. I'll turn it off.",
                        "Shall I close the window? It's cold."],
              pitfall="Students use 'will' for arrangements already made: *I will meet Nam at four* "
                      "(they arranged it yesterday). If it is arranged → present continuous. "
                      "If you decide now → will.",
              note="This is a genuinely difficult distinction. Use the test question: "
                   "'Did you decide before now, or this second?'"),
    pron=P("Contractions and stress in offers and promises",
           "'I'll' is one quick sound /aɪl/. In an offer the stress is on the main verb: "
           "I'll HELP you. In a promise the stress can be on 'won't': I WON'T forget.",
           items=["I'll HELP you.", "I'll DO it.", "I WON'T forget.", "Shall I CLOSE the window?"],
           drill=["Don't worry, I'll do it.", "I promise I won't forget.",
                  "Shall I help you with that?"],
           vn_note="Full forms ('I will help you') sound formal or even annoyed in these functions. "
                   "The contraction is the friendly form."),
    listening=AUDIO['U10L4'],
    reading=T("The promise board",
              ["In one school in Hai Duong, there is a large board near the office called "
               "THE PROMISE BOARD.",
               "Each class writes three promises about saving energy on a card and signs it. "
               "The cards stay on the board for the whole year, and anybody can read them.",
               "Class 7A's card says: 'We will turn off the lights and fans at every break. "
               "We won't leave the computer on standby. We will check the classroom before we go home.'",
               "Once a month, the school office writes the electricity bill on the board too.",
               "'A promise on a wall is different from a promise in your head,' the head teacher says. "
               "'Everybody can see it — including the class that wrote it.'",
               "The idea came from a Grade 7 student. When she was asked why she suggested it, "
               "she said: 'Because we are all good at promising and bad at remembering.'"],
              tasks=[EX("U10.4-R1", "Read and answer", "Answer the questions.",
                        items=["1. What is on the board?", "2. How long do the cards stay there?",
                               "3. Write class 7A's three promises.",
                               "4. What else does the office write on the board?",
                               "5. Why did the student suggest the idea?"],
                        answers=["1. Cards with each class's three promises about saving energy, "
                                 "signed by the class.",
                                 "2. The whole year.",
                                 "3. They will turn off the lights and fans at every break; they "
                                 "won't leave the computer on standby; they will check the classroom "
                                 "before they go home.",
                                 "4. The electricity bill, once a month.",
                                 "5. Because 'we are all good at promising and bad at remembering'."],
                        level="M", kind="reading")]),
    speaking=[EX("U10.4-S1", "Offer to help", "Your partner has a problem. Offer help with I'll or "
                 "Shall I…?",
                 items=["1. 'These books are very heavy.'", "2. 'I don't understand this exercise.'",
                        "3. 'The window is open and it's raining.'",
                        "4. 'I've forgotten my pen.'", "5. 'Nobody has turned off the fan.'"],
                 answers=["Model: 1. Shall I take some? / I'll carry half."],
                 level="E", kind="speaking"),
              EX("U10.4-S2", "The class promise", "In groups of four, agree on three promises about "
                 "saving energy in your classroom. Everybody must offer to do one thing.",
                 items=["Language: 'I'll…', 'Shall I…?', 'I promise I won't…', "
                        "'Don't worry, I'll remind you.'"],
                 answers=["Model: We'll turn off the fans at break. I'll be the monitor for our row. "
                          "I promise I won't leave my computer on standby."],
                 level="D", kind="speaking")],
    writing=[EX("U10.4-W1", "Write three promises", "Write three promises about saving energy — "
                "two with will and one with won't.",
                items=[], answers=["Model: I will turn off the light every time I leave my bedroom. "
                                   "I will unplug my phone charger when the phone is full. "
                                   "I won't leave the TV on standby at night."],
                level="M", kind="writing", lines=5)],
    communication={"function": "Offering, promising and reminding",
                   "phrases": ["I'll do it.", "Shall I…?", "Don't worry, I'll…",
                               "I promise I won't…", "I'll remind you.", "Don't forget to…",
                               "Thanks, that's very kind."],
                   "roleplay": "A notices a problem (lights on, window open, litter). "
                               "B offers to fix it and promises to check tomorrow. Then swap.",
                   "real_life": "Offering help and keeping promises — at home, at school, anywhere."},
    guided=[EX("U10.4-G1", "Match the situation with the reply", "Write the letter.",
               items=["1. 'These bags are heavy.'", "2. 'Don't forget the meeting.'",
                      "3. 'The fan is still on.'", "4. 'Nobody wants to be the monitor.'",
                      "a. I'll do it.", "b. I won't forget, I promise.", "c. Shall I carry one?",
                      "d. I'll turn it off."],
               answers=["1–c", "2–b", "3–d", "4–a"], level="E", kind="mixed"),
            EX("U10.4-G2", "will or present continuous?", "Choose the correct form.",
               items=["1. A: The phone is ringing. B: I (answer / 'll answer) it.",
                      "2. I (meet / 'm meeting) Nam at four — we arranged it yesterday.",
                      "3. A: I can't do this exercise. B: I ('ll help / 'm helping) you.",
                      "4. We ('ll visit / 're visiting) the museum on Friday. (the trip is booked)",
                      "5. A: It's cold. B: I ('ll close / 'm closing) the window."],
               answers=["1. 'll answer", "2. 'm meeting", "3. 'll help", "4. 're visiting",
                        "5. 'll close"], level="D", kind="grammar",
               note="Decided NOW → will. Arranged BEFORE → present continuous.")],
    independent=[EX("U10.4-I1", "Complete the conversation", "Write the missing lines.",
                    items=["A: The lights are still on in Room 5.", "B: Oh! ______ (offer to go).",
                           "A: Thanks. And don't forget the poster tomorrow.",
                           "B: ______ (promise).", "A: Do you need help with it?",
                           "B: ______ (accept or refuse politely)."],
                    answers=["B: I'll go and turn them off.", "B: I won't forget, I promise.",
                             "B: Yes, please — shall we do it at break? / No, thanks, I've nearly "
                             "finished."], level="M", kind="mixed"),
                 EX("U10.4-I2", "Class promises", "Do U10.4-S2 and write your group's three promises "
                    "on a card for the class promise board.",
                    items=[], answers=["See U10.4-S2."], level="D", kind="speaking")],
    review=["will for promises, instant decisions and offers", "Shall I…? for offers",
            "will vs present continuous (decided now vs arranged before)"],
    homework=[EX("U10.4-H1", "Everyday English", "Write what you say.",
                 items=["1. Your friend is carrying too much. (offer) ______",
                        "2. Your mother asks you to remember something. (promise) ______",
                        "3. You notice the tap is running. (instant decision) ______",
                        "4. Your teacher needs a volunteer. (offer) ______"],
                 answers=["1. Shall I carry something? / I'll take some.",
                          "2. I won't forget, I promise.",
                          "3. I'll turn it off.", "4. I'll do it."], level="M", kind="mixed"),
              EX("U10.4-H2", "Grammar", "will or present continuous?",
                 items=["1. A: The door is open. B: I ______ (close) it.",
                        "2. I ______ (visit) my grandmother on Sunday — we arranged it last week.",
                        "3. A: I'm thirsty. B: I ______ (get) you some water.",
                        "4. We ______ (have) a test on Friday. (the teacher told us)",
                        "5. A: This bag is heavy. B: I ______ (help) you."],
                 answers=["1. 'll close", "2. 'm visiting", "3. 'll get", "4. 're having",
                          "5. 'll help"], level="D", kind="grammar"),
              EX("U10.4-H3", "Writing", "Write your three energy promises neatly on a card for the "
                 "class promise board.",
                 items=["Two with will, one with won't. Sign your name!"],
                 answers=["See U10.4-W1 model."], level="M", kind="writing", lines=5),
              EX("U10.4-H4", "Speaking", "Practise these five sentences with contractions, "
                 "five times each: I'll do it. I'll help you. I won't forget. Shall I close it? "
                 "Don't worry, I'll remind you.",
                 items=[], answers=["Spot-check in Lesson 5."], level="E", kind="pron")],
    workbook=[EX("U10.4-P1", "Offer, promise or decision?", "Write O, P or D.",
                 items=["1. I'll carry that for you. ___", "2. I won't be late, I promise. ___",
                        "3. (The phone rings) I'll answer it. ___",
                        "4. Shall I open the window? ___", "5. I'll never forget your help. ___"],
                 answers=["1. O", "2. P", "3. D", "4. O", "5. P"], level="E", kind="mixed"),
              EX("U10.4-P2", "Complete with I'll or Shall I", "Write the correct form.",
                 items=["1. ______ take you to the station.", "2. ______ open the window?",
                        "3. ______ help you with your homework.",
                        "4. ______ turn off the computer?", "5. ______ remind you tomorrow."],
                 answers=["1. I'll", "2. Shall I", "3. I'll", "4. Shall I", "5. I'll"],
                 level="E", kind="grammar"),
              EX("U10.4-P3", "will or present continuous?", "Complete.",
                 items=["1. A: Somebody is at the door. B: I ______ (go).",
                        "2. I ______ (play) football with Nam tomorrow — we arranged it.",
                        "3. A: I've lost my pen. B: Don't worry, I ______ (lend) you one.",
                        "4. My class ______ (visit) the power station next Tuesday. (booked)"],
                 answers=["1. 'll go", "2. 'm playing", "3. 'll lend", "4. is visiting"],
                 level="D", kind="grammar"),
              EX("U10.4-P4", "Write a dialogue", "Write a 10-line conversation in which A has three "
                 "problems and B offers help each time.",
                 items=["Include: two 'I'll', one 'Shall I…?', one promise and one 'Don't forget…'."],
                 answers=["Model: A: These boxes are so heavy. B: Shall I take one? A: Thank you. "
                          "And the lights are still on in the hall. B: Don't worry, I'll turn them "
                          "off on the way. A: You're very kind. One more thing — we need the poster "
                          "tomorrow morning. B: I'll bring it, I promise. I'll put it by the door "
                          "tonight. A: Perfect. Don't forget! B: I won't."],
                 level="D", kind="writing", lines=12)],
    procedure=[ST("Warm-up: Prediction chain", 5,
                  ["Each student makes one prediction about next year. Recycles Lesson 3."],
                  "Produce predictions.", "Rows", "Slide 2"),
               ST("Presentation: three new uses of will", 10,
                  ["Act out three situations: drop something (offer), phone rings (decision), "
                   "make a promise.",
                   "Elicit 'I'll…' each time. Write the three functions on the board.",
                   "Contrast with the arrangement: 'I'm meeting Nam at four' — decided yesterday."],
                  "Repeat; copy the three functions.", "Whole class", "Slides 3–6"),
               ST("Listening: four small moments", 8,
                  ['Play the recording “Lesson 36: I Can Fix This!” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; do the O/P task and the gap-fill; read the four exchanges in pairs.'],
                  "Listen, classify, read in role.", "Individual → pairs", "Slide 7"),
               ST("Guided practice", 8, ["U10.4-G1, G2 and I1; two pairs perform I1."],
                  "Match, choose the tense, complete the dialogue.", "Pairs", "Student Book p. U10L4"),
               ST("Speaking: offers and class promises", 10,
                  ["U10.4-S1 (offer to help) round the class, then the group promise task."],
                  "Offer help; agree on three class promises.", "Pairs → fours", "Slides 8–9"),
               ST("Wrap-up and homework", 4, ["Write the class promises on a big card and put it on "
                                              "the wall. Set H1–H4."],
                  "Sign the class promise card.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Will for the decision you make right now",
                     ["(Drop a pile of papers.) Oh no! … What do you say?",
                      "'I'll help you.' You decided one second ago, when you saw the problem. "
                      "That is WILL.",
                      "But if I ask 'What are you doing on Saturday?' and you already arranged it "
                      "with your cousin last week, you say: 'I'm going to my cousin's house.' "
                      "Present continuous.",
                      "The test question: did you decide BEFORE now, or THIS SECOND? "
                      "Before → -ing. This second → will."]),
                  TK("Promises and the promise board",
                     ["A promise inside your head lasts about two hours.",
                      "A promise written on a card, with your name on it, on the wall, lasts a year.",
                      "That is why we are writing our class promises today. Three promises, "
                      "everybody signs.",
                      "And I will write the electricity bill next to it every month — because "
                      "I made a promise too."])],
    support=["Give the three functions with one example each on a card.",
             "Provide picture prompts for the offer activity.",
             "Allow weaker students to choose from three promise sentences."],
    challenge=["Ask them to explain the will / present continuous difference in their own words.",
               "Ask for a 10-line dialogue with all four functions.",
               "Ask them to write promises for the whole school."],
    assessment=["Uses 'I'll' for an instant offer", "4 of 5 correct in the will / continuous task",
                "Produces a clear promise with 'won't'"],
    board_plan=["LEFT: three uses of will (promise / decision / offer)",
                "CENTRE: decided NOW → will | arranged BEFORE → am/is/are + -ing",
                "RIGHT: class promises; Homework H1–H4"],
    materials=['Recording: Lesson 36: I Can Fix This! — VOA Learning English — Let’s Learn English, Level 1 (2:03)', "A large card for the class promises"],
)

L5 = Lesson(
    code="U10L5", unit=10, number=5, period=74,
    lesson_type="Skills 1", title="Reading: A village with electricity + Speaking: Energy debate",
    objectives=["read a 240-word article and answer gist, detail and inference questions",
                "guess new words from context",
                "take part in a short class debate with reasons",
                "agree and disagree politely"],
    recycled=["U10L1–L4: energy vocabulary, will, because/so; Unit 5 opinion language; "
              "Unit 8 although/however"],
    vocab=[V("connect", "v", "/kəˈnekt/", "kết nối, nối điện", "The village was connected in 2018."),
           V("generator", "n", "/ˈdʒenəreɪtə/", "máy phát điện", "They used a noisy diesel generator."),
           V("battery", "n", "/ˈbætri/", "pin, ắc quy", "The batteries store energy for the night."),
           V("install", "v", "/ɪnˈstɔːl/", "lắp đặt", "Workers installed forty solar panels."),
           V("supply", "n/v", "/səˈplaɪ/", "nguồn cung cấp", "The village now has a reliable supply."),
           V("afford", "v", "/əˈfɔːd/", "đủ tiền mua", "Not every family can afford a fridge.")],
    phrases=["be connected to the grid", "store energy", "cost of living", "afford to buy",
             "make a difference"],
    grammar=G("Debate language: opinion, agreement, disagreement",
              use=["Opinion: In my opinion… / I think… / It seems to me that…",
                   "Agreement: I agree with Nam. / That's a good point.",
                   "Polite disagreement: I see what you mean, but… / I'm afraid I disagree, because…",
                   "Concession (Unit 8): Although that is true, …"],
              form=[["Function", "Language"],
                    ["give an opinion", "In my opinion, solar power is the answer."],
                    ["support it", "…because it is free after you buy the panels."],
                    ["agree", "I agree with Mai — and I'd add that…"],
                    ["disagree politely", "I see what you mean, but what about the night?"],
                    ["concede", "Although that is true, batteries are still expensive."]],
              examples=["In my opinion, every school should have solar panels, because we use most "
                        "electricity exactly when the sun is strongest.",
                        "I see what you mean, but who will pay for them?"],
              pitfall="*I disagree you* → 'I disagree WITH you'. *According to me* → 'In my opinion'.",
              note="A debate is judged on REASONS, not on volume. One reason per opinion, always."),
    pron=P("Stress in debate sentences and long words",
           "In a debate, stress the KEY word of your argument: 'It is FREE after you buy the panels.' "
           "Watch: gene'rator, in'stall, su'pply, a'fford, con'nect.",
           items=["'generator (Oooo)", "in'stall (oO)", "su'pply (oO)", "a'fford (oO)",
                  "con'nect (oO)"],
           drill=["In my opinion, / solar power / is the ANSWER, / because it is FREE.",
                  "I see what you MEAN, / but who will PAY for it?"],
           vn_note="Speaking too fast in a debate loses both the stress and the argument. "
                   "Slow down and stress one word per sentence."),
    listening=AUDIO['U10L5'],
    reading=T("The village that got its evenings back",
              ["Until 2018, the village of Ta Van Chu in Lao Cai province had no electricity. "
               "It is 26 kilometres from the nearest town, on the other side of two mountains, "
               "and connecting it to the national grid would have cost more than eleven billion dong.",
               "For years the village used a small diesel generator. It was loud, it smelled, and "
               "diesel had to be carried up the mountain by motorbike. Families could afford to run "
               "it for about two hours a night — long enough to charge phones and light one room.",
               "In 2018 a project installed forty solar panels and a room full of batteries. "
               "The panels charge the batteries in the day; the batteries light the village at night.",
               "The change nobody predicted was not about light. It was about time. Before, children "
               "did their homework between six and eight, or not at all. Now they can study any "
               "evening. Two years after the panels arrived, the number of village children in upper "
               "secondary school had doubled.",
               "There are still problems. In the rainy season, six or seven days can pass with almost "
               "no sun, and the batteries are empty by the fourth day. Batteries also do not last for "
               "ever; the village will need new ones in about eight years, and nobody has yet answered "
               "the question of who will pay for them.",
               "'People think our problem was darkness,' the village leader says. 'Our problem was "
               "that the day ended at six o'clock.'"],
              tasks=[EX("U10.5-R1", "Gist", "Choose the best title.",
                        items=["A. How solar panels work",
                               "B. How electricity changed one mountain village",
                               "C. The cost of diesel in Viet Nam"],
                        answers=["B"], level="E", kind="reading"),
                     EX("U10.5-R2", "Detail", "Answer the questions.",
                        items=["1. How far is the village from the nearest town, and what would "
                               "connecting it have cost?",
                               "2. What were the three problems with the generator?",
                               "3. What was installed in 2018?",
                               "4. What unexpected change happened?",
                               "5. Give two problems that remain."],
                        answers=["1. 26 kilometres; more than eleven billion dong.",
                                 "2. It was loud, it smelled, and diesel had to be carried up the "
                                 "mountain by motorbike (and it only ran about two hours a night).",
                                 "3. Forty solar panels and a room full of batteries.",
                                 "4. Children could study any evening, and in two years the number "
                                 "in upper secondary school doubled.",
                                 "5. In the rainy season the batteries are empty by the fourth day; "
                                 "the batteries will need replacing in about eight years and nobody "
                                 "knows who will pay."], level="M", kind="reading"),
                     EX("U10.5-R3", "Vocabulary from context", "Find a word or phrase that means:",
                        items=["1. the national electricity system (paragraph 1)",
                               "2. to have enough money for (paragraph 2)",
                               "3. put in place and made ready to use (paragraph 3)",
                               "4. become twice as many (paragraph 4)"],
                        answers=["1. the national grid", "2. afford", "3. installed", "4. doubled"],
                        level="M", kind="reading"),
                     EX("U10.5-R4", "Inference", "Answer with your own ideas.",
                        items=["1. Explain the village leader's last sentence.",
                               "2. Why do you think the number of students doubled?",
                               "3. Who should pay for the new batteries in eight years? Give a reason."],
                        answers=["1. The real problem was not the dark but the loss of useful hours: "
                                 "without light, all activity stopped at six.",
                                 "2. Because children could study in the evening, so they could keep "
                                 "up and continue at school.",
                                 "3. Students' own answer with a reason (the government, the village, "
                                 "the project, a mixture)."], level="D", kind="reading")]),
    speaking=[EX("U10.5-S1", "Prepare your argument", "Prepare for the class debate. "
                 "Write two arguments and one answer to the other side.",
                 items=["Motion: 'Every school in our province should have solar panels.'",
                        "My side: FOR / AGAINST", "Argument 1 + reason: ______",
                        "Argument 2 + reason: ______",
                        "The other side will say… and I will answer: ______"],
                 answers=["Notes only. Every argument needs a reason."],
                 level="M", kind="speaking"),
              EX("U10.5-S2", "The debate", "Hold the class debate: three speakers for, three against, "
                 "then open discussion and a vote.",
                 items=["Rules: one minute each; you must use one debate expression; "
                        "no interrupting; the class votes at the end."],
                 answers=["Assessment: content 3, reasons 3, debate language 2, delivery 2."],
                 level="D", kind="speaking")],
    writing=[EX("U10.5-W1", "Write your arguments", "Write your two arguments as full sentences.",
                items=[], answers=["Model: In my opinion, every school should have solar panels, "
                                   "because schools use most of their electricity in the middle of "
                                   "the day, when the sun is strongest. Furthermore, students see "
                                   "the panels every day, so they learn about renewable energy "
                                   "without a lesson."], level="M", kind="writing", lines=6)],
    communication={"function": "Debating politely",
                   "phrases": ["In my opinion,…", "I agree with…", "I see what you mean, but…",
                               "That's a good point.", "Although that is true,…",
                               "Can I say something?", "Let's vote."],
                   "roleplay": "Class debate with a chairperson (a student) who gives turns and "
                               "stops interruptions.",
                   "real_life": "Discussing a real decision in a group without arguing."},
    guided=[EX("U10.5-G1", "True or false", "Read the text again and write T or F.",
               items=["1. The village had no electricity before 2018.",
                      "2. Connecting to the grid would have been cheap.",
                      "3. The generator ran all night.",
                      "4. The number of students in upper secondary school doubled.",
                      "5. The batteries will last for ever."],
               answers=["1. T", "2. F – more than eleven billion dong.",
                        "3. F – about two hours a night.", "4. T",
                        "5. F – new ones will be needed in about eight years."],
               level="E", kind="reading"),
            EX("U10.5-G2", "Debate language", "Complete with the expressions in the box.",
               wordbank=["In my opinion", "I agree with", "I see what you mean, but",
                         "That's a good point", "Although that is true"],
               items=["1. ______ , every school should have panels.",
                      "2. ______ Nam — and I would add one more reason.",
                      "3. ______ who will pay for them?",
                      "4. ______ . I hadn't thought of that.",
                      "5. ______ , the money must come from somewhere."],
               answers=["1. In my opinion", "2. I agree with", "3. I see what you mean, but",
                        "4. That's a good point", "5. Although that is true"],
               level="M", kind="writing")],
    independent=[EX("U10.5-I1", "Retell", "Close the book. Tell your partner the story of Ta Van Chu "
                    "in five sentences.", items=[],
                    answers=["Model: Until 2018 the village of Ta Van Chu had no electricity, because "
                             "connecting it to the grid was too expensive. The village used a noisy "
                             "diesel generator for about two hours a night. In 2018 a project "
                             "installed forty solar panels and batteries. Now children can study in "
                             "the evening, and the number in upper secondary school has doubled. "
                             "However, the batteries will need replacing in eight years."],
                    level="M", kind="speaking"),
                 EX("U10.5-I2", "The debate", "Take part in U10.5-S2.", items=[],
                    answers=["See U10.5-S2."], level="D", kind="speaking")],
    review=["Reading: gist → detail → inference", "Debate language: opinion, agreement, "
            "polite disagreement", "Every argument needs a reason"],
    homework=[EX("U10.5-H1", "Reading", "Answer in full sentences.",
                 items=["1. Why was connecting the village to the grid not possible?",
                        "2. How did the village get diesel?",
                        "3. What happens in the rainy season?",
                        "4. What question has nobody answered yet?"],
                 answers=["1. Because it would have cost more than eleven billion dong (the village "
                          "is 26 km away, behind two mountains).",
                          "2. It was carried up the mountain by motorbike.",
                          "3. Six or seven days can pass with almost no sun, and the batteries are "
                          "empty by the fourth day.",
                          "4. Who will pay for the new batteries in about eight years."],
                 level="M", kind="reading"),
              EX("U10.5-H2", "Vocabulary", "Complete with connect, generator, battery, install, "
                 "supply, afford.",
                 items=["1. The village used a diesel ______ .",
                        "2. Workers came to ______ the panels.",
                        "3. The ______ stores energy for the night.",
                        "4. Not every family can ______ a fridge.",
                        "5. It costs a lot to ______ a village to the grid.",
                        "6. Now the village has a reliable ______ of electricity."],
                 answers=["1. generator", "2. install", "3. battery", "4. afford", "5. connect",
                          "6. supply"], level="E", kind="vocab"),
              EX("U10.5-H3", "Writing", "Write your debate arguments as a paragraph (90–100 words).",
                 items=["Two arguments with reasons and one answer to the other side, using "
                        "'Although…' or 'I see what you mean, but…'."],
                 answers=["See U10.5-W1 model, extended with a counter-argument."],
                 level="D", kind="writing", lines=12),
              EX("U10.5-H4", "Speaking", "Practise your one-minute debate speech three times.",
                 items=["Stress one key word in each sentence."],
                 answers=["Debate in Lesson 6."], level="M", kind="speaking")],
    workbook=[EX("U10.5-P1", "Vocabulary match", "Match the word with the meaning.",
                 items=["1. install", "2. afford", "3. generator", "4. supply", "5. connect",
                        "a. to have enough money for something",
                        "b. a machine that makes electricity", "c. to join to a system",
                        "d. to put something in and make it ready", "e. the amount available"],
                 answers=["1–d", "2–a", "3–b", "4–e", "5–c"], level="E", kind="vocab"),
              EX("U10.5-P2", "Reading", "Read and answer.",
                 text=["A solar water heater is much simpler than a solar panel. It is just a black "
                       "tank on the roof: the sun heats the water directly. There is no electricity "
                       "and there are no batteries. A family heater costs between four and eight "
                       "million dong and lasts about fifteen years. In a hot country like Viet Nam, "
                       "it can provide hot water for eight or nine months of the year without any "
                       "electricity at all."],
                 items=["1. How does a solar water heater work?",
                        "2. How much does one cost and how long does it last?",
                        "3. For how many months a year does it work in Viet Nam?",
                        "4. Why is it simpler than a solar panel?"],
                 answers=["1. It is a black tank on the roof; the sun heats the water directly.",
                          "2. Between four and eight million dong; about fifteen years.",
                          "3. Eight or nine months.",
                          "4. Because it uses no electricity and no batteries."],
                 level="M", kind="reading"),
              EX("U10.5-P3", "Debate practice", "Write one argument FOR and one AGAINST each idea.",
                 items=["1. Every classroom should have air conditioning.",
                        "2. Students should not use phones at school.",
                        "3. Our town should build a wind farm."],
                 answers=["Model: 1. For: students concentrate better when they are not too hot. "
                          "Against: air conditioning uses a huge amount of electricity, and many "
                          "schools cannot afford the bill."],
                 level="D", kind="writing"),
              EX("U10.5-P4", "Writing", "Write a paragraph (90–100 words) answering: 'Should our "
                 "school spend money on solar panels or on new desks?'",
                 items=["Give your opinion, two reasons, one counter-argument and a conclusion."],
                 answers=["Model: In my opinion, our school should buy desks first. I know that solar "
                          "panels save money in the long term, and I agree that they are good for the "
                          "environment. However, three classes in our school still share old desks "
                          "that are too small, and a student who cannot write comfortably cannot learn. "
                          "Panels pay for themselves in six years, but a child is only in Grade 7 "
                          "once. I would buy desks this year and panels next year, when the new "
                          "government programme starts. (95 words)"],
                 level="D", kind="writing", lines=12)],
    procedure=[ST("Warm-up: Prediction ping-pong", 5,
                  ["Teacher gives a topic; students make a will-prediction. Recycles Lesson 3."],
                  "Produce predictions.", "Whole class", "Slide 2"),
               ST("Pre-reading", 6,
                  ["Show a photo of a mountain village at night. Ask: 'What is difficult without "
                   "electricity?' Predict.",
                   "Pre-teach: grid, generator, install, afford. Set the gist task."],
                  "Predict; skim for the title.", "Whole class", "Slides 3–4"),
               ST("While-reading", 13,
                  ["R2 detail individually, pair-check; R3 words in context; R4 inference in pairs."],
                  "Read and answer.", "Individual → pairs", "Slides 5–7"),
               ST("Post-reading: retell", 4, ["Books closed; retell in five sentences."],
                  "Retell.", "Pairs", "Slide 8"),
               ST("Speaking: class debate", 13,
                  ["Play the model debate; students note the arguments and the expressions.",
                   "Divide the class: FOR and AGAINST. 4 minutes to prepare two arguments each.",
                   "Debate: three speakers each side, then open discussion, then a vote."],
                  "Prepare, argue, listen, vote.", "Groups → whole class", "Slides 9–11"),
               ST("Wrap-up and homework", 4, ["Announce the vote result; praise the best reason. "
                                              "Set H1–H4."],
                  "Vote; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("The sentence that makes the text",
                     ["Look at the last line: 'People think our problem was darkness. Our problem was "
                      "that the day ended at six o'clock.'",
                      "That is the whole article in one sentence. Electricity did not only bring "
                      "light — it brought TIME.",
                      "When you read, look for the sentence that says the real point. It is often "
                      "the last one, and it is often somebody speaking."]),
                  TK("How to disagree without arguing",
                     ["In a debate you will disagree. That is the point. But HOW you disagree decides "
                      "whether anybody listens.",
                      "Weak: 'You are wrong.' Nobody changes their mind after that.",
                      "Strong: 'I see what you mean, but who will pay for them?' — you accept their "
                      "point AND you ask a hard question.",
                      "Write both expressions in your notebook. You will need them all your life."])],
    support=["Gloss four words in the margin.",
             "Give two ready-made arguments to choose from.",
             "Let weaker students speak for 30 seconds instead of a minute."],
    challenge=["Ask them to answer the other side's argument directly.",
               "Ask them to chair the debate.",
               "Ask for a written counter-argument in H3."],
    assessment=["4 of 5 detail answers", "Uses two debate expressions",
                "Gives a reason for every opinion"],
    board_plan=["LEFT: 4 new words with stress", "CENTRE: FOR | AGAINST arguments",
                "RIGHT: debate expressions; Homework H1–H4"],
    materials=["Reading text", 'Recording: What will you do this month? — ELLLO — One Minute English (1:00)', "Timer", "Voting slips"],
)

L6 = Lesson(
    code="U10L6", unit=10, number=6, period=75,
    lesson_type="Skills 2", title="Listening: An energy audit + Writing: Energy in 2050",
    objectives=["listen to an audit report and complete a table with numbers",
                "organise a prediction paragraph (situation now – predictions – conclusion)",
                "write 100–120 words about energy in the future",
                "check a partner's work with a checklist"],
    recycled=["U10L1–L5: energy vocabulary, will/won't, because/so, debate language; "
              "all previous writing structures"],
    vocab=[V("audit", "n", "/ˈɔːdɪt/", "kiểm toán, khảo sát", "The class did an energy audit."),
           V("measure", "v", "/ˈmeʒə/", "đo lường", "First, measure how much you use."),
           V("compare", "v", "/kəmˈpeə/", "so sánh", "Compare this month with last month."),
           V("result", "n", "/rɪˈzʌlt/", "kết quả", "The results surprised everybody."),
           V("solution", "n", "/səˈluːʃn/", "giải pháp", "There is no single solution."),
           V("in the long term", "phr", "/ɪn ðə lɒŋ tɜːm/", "về lâu dài", "In the long term, solar will be cheaper.")],
    phrases=["carry out an audit", "the results show that…", "in ten years' time",
             "in the long term", "the biggest change will be…"],
    grammar=G("Prediction paragraph: structure (writing focus)",
              use=["1. THE SITUATION NOW (present simple): Today most of our electricity comes from…",
                   "2. PREDICTIONS (will / won't + probably/certainly): In 2050, solar power will…",
                   "3. A PROBLEM OR A DOUBT (however / although): However, batteries will still be…",
                   "4. CONCLUSION (opinion): In my opinion, the biggest change will be…"],
              form=[["Part", "Tense/language", "Example"],
                    ["Now", "present simple", "Today, about half of our electricity comes from coal."],
                    ["Prediction", "will / won't", "By 2050 solar power will probably be the cheapest."],
                    ["Doubt", "However / Although", "However, we won't solve the storage problem "
                     "quickly."],
                    ["Conclusion", "In my opinion,…", "In my opinion, the biggest change will be how "
                     "we store energy."]],
              examples=["Today most Vietnamese families use electricity for lights and fans. "
                        "In twenty years, they will probably use it for cars as well."],
              pitfall="Students write only predictions and forget the present. A prediction is much "
                      "stronger when it starts from a fact about today.",
              note="One number from today makes the whole paragraph believable."),
    pron=P("Reading numbers and predictions aloud",
           "Practise big numbers: four point five million, eighty per cent, twenty-six degrees. "
           "Stress the number, not the unit: FOUR point FIVE million dong.",
           items=["4.5 million = four point five million", "80% = eighty per cent",
                  "26°C = twenty-six degrees"],
           drill=["The results show that we waste about four point five million dong a year.",
                  "An LED bulb uses eighty per cent less electricity."],
           vn_note="Numbers are where listening and speaking break down most often. "
                   "Practise them aloud every lesson in this unit."),
    listening=AUDIO['U10L6'],
    reading=T("Model paragraph: Energy in 2050",
              ["Today, most of the electricity in Viet Nam comes from hydro power and coal, and only "
               "a small part comes from the sun and the wind. In my own house, we use electricity "
               "mainly for lights, fans and the fridge.",
               "I think this will change completely by 2050. Solar power will almost certainly be the "
               "cheapest kind of electricity, and most houses will have panels on the roof. "
               "Cars and motorbikes will probably be electric, so the air in our cities will be much "
               "cleaner. Coal power stations won't disappear immediately, but they will become "
               "smaller and fewer.",
               "However, one problem won't be solved quickly. The sun goes down every evening, and "
               "batteries are still expensive. Although they are getting better every year, "
               "storing energy will remain the difficult part.",
               "In my opinion, the biggest change won't be how we make electricity. It will be how "
               "much we waste. A country that wastes less needs fewer power stations. (152 words — "
               "yours can be shorter!)"],
              tasks=[EX("U10.6-R1", "Analyse the model", "Answer the questions.",
                        items=["1. What tense is used in paragraph 1, and why?",
                               "2. Find three predictions with 'will'.",
                               "3. Which two adverbs make the predictions softer or stronger?",
                               "4. Which paragraph gives the problem, and which word introduces it?",
                               "5. What is the writer's main opinion?"],
                        answers=["1. The present simple, because it describes the situation NOW.",
                                 "2. e.g. 'Solar power will be the cheapest', 'most houses will have "
                                 "panels', 'cars will probably be electric'.",
                                 "3. 'almost certainly' and 'probably'.",
                                 "4. Paragraph 3, introduced by 'However'.",
                                 "5. That the biggest change will be how much we waste, not how we "
                                 "make electricity."], level="M", kind="reading")]),
    speaking=[EX("U10.6-S1", "Say your predictions", "Tell your partner four predictions before "
                 "you write.",
                 items=["One about your house, one about transport, one about your town, "
                        "one about the world."],
                 answers=["Speaking first improves the writing."], level="M", kind="speaking")],
    writing=[EX("U10.6-W1", "Plan your paragraph", "Complete the plan.",
                items=["1. The situation now (with one number if you can): ______",
                       "2. Prediction 1 (will + probably/certainly): ______",
                       "3. Prediction 2: ______", "4. Prediction 3 (won't): ______",
                       "5. A problem (However / Although): ______",
                       "6. Conclusion (In my opinion, the biggest change will be…): ______"],
                answers=["Check every plan before students write."], level="M", kind="writing", lines=8),
             EX("U10.6-W2", "Write your paragraph", "Write 100–120 words about energy in 2050.",
                items=["Present simple for now; will/won't for the future; one 'However'; "
                       "a clear opinion at the end."],
                answers=["See the model. Marking: content 3, will/won't 3, organisation 2, "
                         "vocabulary 1, length 1."],
                level="D", kind="writing", lines=16),
             EX("U10.6-W3", "Peer check", "Swap and tick the checklist.",
                items=["□ starts with the situation NOW (present simple)",
                       "□ at least three predictions with will", "□ one prediction with won't",
                       "□ one adverb (probably / certainly)", "□ one 'However' or 'Although'",
                       "□ an opinion at the end", "□ 100–120 words"],
                answers=["Write one thing you liked and one to improve."], level="M", kind="writing")],
    communication={"function": "Reporting results and drawing a conclusion",
                   "phrases": ["We measured / counted…", "The results show that…",
                               "In total,…", "Our conclusion is…", "We recommend…"],
                   "roleplay": "Report the results of your energy audit to the class in 60 seconds.",
                   "real_life": "Presenting the results of any survey or measurement."},
    guided=[EX("U10.6-G1", "Now or future?", "Write N (now, present simple) or F (future, will).",
               items=["1. Most of our electricity comes from coal. ___",
                      "2. Solar power will be the cheapest. ___",
                      "3. My family uses electricity for lights and fans. ___",
                      "4. Cars will probably be electric. ___",
                      "5. Batteries are still expensive. ___"],
               answers=["1. N", "2. F", "3. N", "4. F", "5. N"], level="E", kind="grammar"),
            EX("U10.6-G2", "Add the adverbs", "Rewrite with the adverb in brackets.",
               items=["1. Solar power will be the cheapest. (almost certainly)",
                      "2. Cars will be electric. (probably)",
                      "3. Coal won't disappear. (probably → careful with word order!)",
                      "4. The world will be hotter. (certainly)"],
               answers=["1. Solar power will almost certainly be the cheapest.",
                        "2. Cars will probably be electric.",
                        "3. Coal probably won't disappear.",
                        "4. The world will certainly be hotter."],
               level="D", kind="grammar",
               note="With 'will' the adverb goes AFTER; with 'won't' it goes BEFORE.")],
    independent=[EX("U10.6-I1", "Write your paragraph", "Do U10.6-W1 and W2.", items=[],
                    answers=["See the model paragraph."], level="D", kind="writing", lines=16),
                 EX("U10.6-I2", "Report the audit", "Report your group's audit results in 60 seconds.",
                    items=[], answers=["See communication section."], level="M", kind="speaking")],
    review=["Audit listening: numbers and comparisons",
            "Prediction paragraph: now – predictions – problem – opinion",
            "Adverb position with will and won't"],
    homework=[EX("U10.6-H1", "Listening / vocabulary", "Complete from the audit.",
                 items=["1. The school has ______ bulbs, and only ______ are LED.",
                        "2. ______ fans were running in empty rooms at break.",
                        "3. A dripping tap wastes about ______ litres a day.",
                        "4. Changing the bulbs will pay for itself in ______ months."],
                 answers=["1. 186; 32", "2. 23", "3. 30", "4. fourteen"],
                 level="E", kind="listening"),
              EX("U10.6-H2", "Vocabulary", "Complete with audit, measure, compare, results, solution, "
                 "in the long term.",
                 items=["1. First we ______ how much we use.",
                        "2. Then we ______ this month with last month.",
                        "3. The ______ surprised everybody.",
                        "4. There is no single ______ .", "5. We carried out an energy ______ .",
                        "6. ______ , solar power will be cheaper."],
                 answers=["1. measure", "2. compare", "3. results", "4. solution", "5. audit",
                          "6. In the long term"], level="E", kind="vocab"),
              EX("U10.6-H3", "Writing", "Rewrite your paragraph neatly after correction and hand "
                 "it in.",
                 items=["Use the 7-point checklist."],
                 answers=["Marking: content 3, will/won't 3, organisation 2, vocabulary 1, length 1."],
                 level="D", kind="writing", lines=16),
              EX("U10.6-H4", "Speaking", "Practise saying these numbers aloud five times: "
                 "4.5 million, 80 per cent, 26 degrees, 12,000 litres, 154 bulbs.",
                 items=[], answers=["Spot-check in Lesson 7."], level="M", kind="pron")],
    workbook=[EX("U10.6-P1", "Paragraph parts", "Write N (now), P (prediction), D (doubt) or "
                 "O (opinion).",
                 items=["1. Today most of our electricity comes from coal. ___",
                        "2. Solar power will be the cheapest. ___",
                        "3. However, batteries are still expensive. ___",
                        "4. In my opinion, the biggest change will be… ___",
                        "5. Cars will probably be electric. ___"],
                 answers=["1. N", "2. P", "3. D", "4. O", "5. P"], level="E", kind="writing"),
              EX("U10.6-P2", "Complete the paragraph", "Use the words in the box.",
                 wordbank=["comes", "will", "probably", "However", "opinion"],
                 items=["Today most of our electricity (1) ______ from coal and hydro power. "
                        "By 2050 solar power (2) ______ be much cheaper, and most houses will "
                        "(3) ______ have panels. (4) ______ , storing energy will still be difficult. "
                        "In my (5) ______ , the biggest change will be how much we waste."],
                 answers=["1. comes", "2. will", "3. probably", "4. However", "5. opinion"],
                 level="E", kind="writing"),
              EX("U10.6-P3", "Correct the paragraph", "This paragraph has five mistakes. Correct them.",
                 text=["In 2050 solar power will to be cheap. Cars will probably electric. "
                       "Coal willn't disappear. I think it won't be easy to store energy. "
                       "In my opinion the biggest change will how we waste energy."],
                 items=["Write the five corrections."],
                 answers=["1. 'will to be' → 'will be'", "2. 'will probably electric' → "
                          "'will probably be electric'", "3. 'willn't' → 'won't'",
                          "4. 'I think it won't be easy' → 'I don't think it will be easy'",
                          "5. 'will how we waste' → 'will be how we waste'"],
                 level="D", kind="grammar"),
              EX("U10.6-P4", "Writing", "Write a paragraph (100–120 words): 'My town in 2050'.",
                 items=["Situation now – three predictions – one problem – your opinion."],
                 answers=["Model: Today my town has about 20,000 people, two main streets and a great "
                          "many motorbikes. Almost nobody has an electric vehicle. By 2050 I think "
                          "the town will be much bigger, and most motorbikes will certainly be "
                          "electric, so the streets will be far quieter. There will probably be solar "
                          "panels on every school and factory roof. However, the town won't solve "
                          "its water problem quickly: the river is already low in April, and hotter "
                          "summers will make this worse. In my opinion, the most important thing is "
                          "not new technology but planting trees now. (110 words)"],
                 level="D", kind="writing", lines=16)],
    procedure=[ST("Warm-up: Number dictation", 5,
                  ["Read eight numbers (4.5 million, 80%, 26 degrees…); students write them; "
                   "pair-check."],
                  "Listen and write numbers.", "Individual → pairs", "Slide 2"),
               ST("Pre-listening", 5,
                  ["Show the audit table. Pre-teach: audit, measure, dripping tap, pay for itself."],
                  "Predict; copy the table.", "Whole class", "Slides 3–4"),
               ST("Listening", 11,
                  ['Play the recording “The first conditional” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.'],
                  "Listen and complete the audit table.", "Individual → pairs", "Slide 5"),
               ST("Writing: analyse the model", 8,
                  ["Model paragraph on the slide; colour the four parts; note the tense change.",
                   "Do U10.6-G1 and G2 (adverb position)."],
                  "Identify the parts; place the adverbs.", "Whole class → pairs", "Slides 6–7"),
               ST("Writing: plan, say, draft", 12,
                  ["Plan (check every plan); say four predictions aloud; write 100–120 words."],
                  "Plan, say, write.", "Individual → pairs → individual", "Slide 8"),
               ST("Peer check and wrap-up", 4, ["Checklist swap; read one good paragraph. Set H1–H4."],
                  "Peer-check.", "Pairs", "Slides 9–10")],
    teacher_talk=[TK("Start from today",
                     ["Every good prediction starts from a fact about today.",
                      "Weak: 'In 2050 everything will be solar.' Why should I believe you?",
                      "Strong: 'Today only a small part of our electricity comes from the sun. "
                      "By 2050 it will be the cheapest kind.' Now the prediction has a starting point.",
                      "So sentence one is always PRESENT SIMPLE, and if you can, put a number in it."]),
                  TK("Adverb position with won't",
                     ["'It will probably rain.' Adverb after WILL. Easy.",
                      "But: 'It probably won't rain.' Adverb BEFORE won't. Strange but true.",
                      "Say both: will PROBABLY be… / PROBABLY won't be…",
                      "Write both in your notebook, because the test will ask for one of them."])],
    support=["Give the audit table with four numbers filled in.",
             "Provide a paragraph frame with the four parts.",
             "Allow 80–90 words."],
    challenge=["Ask for two 'However' sentences and a counter-prediction.",
               "Ask them to write about the world instead of their town.",
               "Ask for 140 words with three numbers."],
    assessment=["8 of 14 numbers correct in the audit",
                "Paragraph has all four parts and three correct 'will' forms",
                "Correct adverb position in at least one sentence"],
    board_plan=["LEFT: audit table", "CENTRE: paragraph plan (now → predictions → problem → opinion)",
                "RIGHT: will + probably | probably + won't; Homework H1–H4"],
    materials=['Recording: The first conditional — ELLLO — Sound Grammar (3:20)', "Model paragraph slide", "Checklist cards"],
)

L7 = Lesson(
    code="U10L7", unit=10, number=7, period=76,
    lesson_type="Looking Back & Project", title="Unit 10 review and Save Energy at School",
    objectives=["recall the energy vocabulary of Unit 10",
                "use will and won't accurately",
                "correct the six typical mistakes of the unit",
                "present a real energy-saving plan for the school"],
    recycled=["ALL of Unit 10 + Units 1–9"],
    vocab=[V("plan", "n/v", "/plæn/", "kế hoạch", "Here is our three-point plan."),
           V("cost", "n/v", "/kɒst/", "chi phí; tốn", "It costs nothing to turn off a light."),
           V("suggest", "v", "/səˈdʒest/", "đề xuất", "We suggest three changes.")],
    phrases=["Our plan has three parts.", "If we do this, we will save…", "It costs nothing.",
             "We suggest that the school…"],
    grammar=G("Unit 10 grammar in one page",
              use=["will / won't + bare verb for predictions, promises, decisions and offers",
                   "Will + subject + verb? for questions",
                   "will probably / probably won't", "I don't think … will …",
                   "because / so / causes for cause and result"],
              form=[["Structure", "Example", "Common mistake"],
                    ["will + bare verb", "It will be cheaper.", "*It will to be cheaper."],
                    ["no -s", "She will go.", "*She wills go."],
                    ["won't", "It won't disappear.", "*It willn't disappear."],
                    ["adverb", "It will probably rain. / It probably won't rain.",
                     "*It will rain probably."],
                    ["opinion", "I don't think it will rain.", "*I think it won't rain."],
                    ["cause/result", "It was hot, so we used the fan.",
                     "*Because it was hot so we used the fan."]],
              examples=["If we change the bulbs, we will save about four million dong a year, "
                        "so the money will pay for itself in fourteen months."],
              pitfall="Add these six to the classroom wall list."),
    pron=P("Unit 10 sounds review: /tʃ/ /dʒ/, contractions, numbers",
           "Three checks: does 'energy' have /dʒ/? is 'I'll' one quick sound? are the numbers clear?",
           items=["energy, village, change, charge", "I'll, we'll, it'll, won't",
                  "4.5 million, 80 per cent, 26 degrees"],
           drill=["I'll change the bulbs in the village school — it'll save eighty per cent."],
           vn_note="Check all three in the Review 4 block."),
    listening=AUDIO['U10L7'],
    reading=T("The school that pays for its own electricity",
              ["In 2021, a secondary school in Ninh Thuan installed 120 solar panels on the roofs of "
               "three buildings. The cost was 480 million dong, and most of it came from a provincial "
               "programme.",
               "The school uses most of its electricity between eight in the morning and four in the "
               "afternoon — exactly when the sun is strongest. In the first full year, the panels "
               "produced slightly more electricity than the school used.",
               "The bill has not disappeared, because the school still buys electricity at night and "
               "on rainy days. But it has fallen by about 78 per cent, and the school sells a small "
               "amount back to the grid at the weekend, when nobody is there.",
               "The savings pay for two things: 40 new fans, and a science teacher's salary for one "
               "extra afternoon a week.",
               "The head teacher is careful about the numbers. 'People say solar power is free. "
               "It isn't. The sun is free; the panels are not. But over twenty years, it is the "
               "cheapest electricity we will ever buy.'"],
              tasks=[EX("U10.7-R1", "Read and answer", "Answer the questions.",
                        items=["1. How many panels were installed, and what did they cost?",
                               "2. Why is this school a good place for solar panels?",
                               "3. Why has the bill not disappeared completely?",
                               "4. How much has the bill fallen?",
                               "5. Explain the head teacher's last two sentences."],
                        answers=["1. 120 panels; 480 million dong (mostly from a provincial programme).",
                                 "2. Because it uses most electricity between 8 a.m. and 4 p.m., "
                                 "when the sun is strongest.",
                                 "3. Because the school still buys electricity at night and on rainy "
                                 "days.", "4. By about 78 per cent.",
                                 "5. Sunlight costs nothing, but the equipment does; over twenty "
                                 "years, though, it works out cheaper than any other electricity."],
                        level="M", kind="reading")]),
    speaking=[EX("U10.7-S1", "Present your plan", "Present your energy-saving plan for two minutes. "
                 "Everyone speaks.",
                 items=["Frame: 'We looked at… We counted… The results show that… "
                        "We suggest three things. If we do this, we will save… Thank you.'"],
                 answers=["Marking: content 3, language 3, poster/numbers 2, presentation 2."],
                 level="D", kind="speaking")],
    writing=[EX("U10.7-W1", "Write your plan", "Write your group's plan.",
                items=["What we measured and the numbers (2 sentences)",
                       "Three suggestions with 'If we…, we will…'",
                       "One sentence about the cost", "One sentence about the long term"],
                answers=["Model: We counted the fans in our building. At break time, 14 fans were on "
                         "in empty rooms. If every class chooses a monitor, we will save about 90 "
                         "minutes of electricity a day. If we put a sticker on every switch, people "
                         "will remember. If we close the windows when the fans are on, the rooms will "
                         "stay cooler. Two of these ideas cost nothing. In the long term, our school "
                         "will also need solar panels."],
                level="M", kind="writing", lines=10)],
    communication={"function": "Presenting a plan with numbers",
                   "phrases": ["We measured / counted…", "The results show that…",
                               "We suggest three things.", "If we do this, we will save…",
                               "It costs nothing.", "Any questions?"],
                   "roleplay": "Present to the class or, if possible, to the head teacher.",
                   "real_life": "Proposing a real change with evidence."},
    guided=[EX("U10.7-G1", "Vocabulary race", "Write the word.",
               items=["1. energy from the sun: ______", "2. it never runs out: ______",
                      "3. to use something badly and lose it: ______",
                      "4. dirty air and water: ______", "5. a thing that stores electricity: ______",
                      "6. to put equipment in and make it ready: ______"],
               answers=["1. solar energy", "2. renewable", "3. waste", "4. pollution", "5. a battery",
                        "6. install"], level="E", kind="vocab"),
            EX("U10.7-G2", "Error clinic – the six Unit 10 mistakes", "Correct one mistake in each "
               "sentence.",
               items=["1. She will goes to Hanoi.", "2. We will to save energy.",
                      "3. It willn't rain.", "4. I think it won't be cold.",
                      "5. It will rain probably.",
                      "6. Because it was hot so we used the fan."],
               answers=["1. She will go to Hanoi.", "2. We will save energy.", "3. It won't rain.",
                        "4. I don't think it will be cold.", "5. It will probably rain.",
                        "6. It was hot, so we used the fan. / Because it was hot, we used the fan."],
               level="D", kind="grammar")],
    independent=[EX("U10.7-I1", "Mixed review", "Complete the text.",
                    text=["In twenty years, most houses in Viet Nam (1. have) ______ solar panels. "
                          "They (2. be) ______ much cheaper than today. Petrol motorbikes "
                          "(3. not disappear) ______ immediately, but they (4. probably / become) "
                          "______ rare in cities. I (5. not think) ______ we (6. solve) ______ the "
                          "storage problem quickly. However, batteries (7. certainly / improve) "
                          "______ ."],
                    items=["Write the seven answers."],
                    answers=["1. will have", "2. will be", "3. won't disappear",
                             "4. will probably become", "5. don't think", "6. will solve",
                             "7. will certainly improve"], level="D", kind="grammar"),
                 EX("U10.7-I2", "Project work", "Finish your energy plan and rehearse the presentation.",
                    items=[], answers=["Check the numbers and the will-sentences."],
                    level="D", kind="mixed")],
    review=["Energy vocabulary (26 items)", "will / won't for predictions, promises, decisions, offers",
            "Adverb position", "because / so / causes", "Prediction paragraph"],
    homework=[EX("U10.7-H1", "Vocabulary", "Write 10 words from Unit 10 with Vietnamese meanings.",
                 items=[], answers=["Any 10 of the unit's items."], level="E", kind="vocab"),
              EX("U10.7-H2", "Grammar", "Choose the correct answer.",
                 items=["1. Solar energy (will be / will to be) cheaper.",
                        "2. Coal (won't / willn't) disappear immediately.",
                        "3. It (will probably / probably will) rain.",
                        "4. (I think it won't / I don't think it will) be cold.",
                        "5. It was hot, (so / because) we used the fan.",
                        "6. Burning coal (causes / causes to) pollution."],
                 answers=["1. will be", "2. won't", "3. will probably", "4. I don't think it will",
                          "5. so", "6. causes"], level="M", kind="grammar"),
              EX("U10.7-H3", "Writing", "Write a paragraph (110–120 words): 'Energy in my house "
                 "in 2050'.",
                 items=["Situation now – three predictions – one problem – your opinion."],
                 answers=["See U10.6-W2 model."], level="D", kind="writing", lines=16),
              EX("U10.7-H4", "Prepare for Unit 11", "Write five ways of travelling that might exist "
                 "in the future, in English or Vietnamese.",
                 items=[], answers=["Use them to start Unit 11."], level="E", kind="vocab")],
    workbook=[EX("U10.7-P1", "Crossword clues", "Write the word.",
                 items=["1. Energy from the sun. (5)", "2. It never runs out. (9)",
                        "3. Dirty air and water. (9)", "4. It stores electricity. (7)",
                        "5. To use badly and lose. (5)"],
                 answers=["1. solar", "2. renewable", "3. pollution", "4. battery", "5. waste"],
                 level="E", kind="vocab"),
              EX("U10.7-P2", "Mixed grammar", "Put the words in order.",
                 items=["1. cheaper / will / solar / be / energy",
                        "2. disappear / coal / immediately / won't",
                        "3. rain / it / probably / will", "4. think / it / don't / I / cold / will / be",
                        "5. hot / it / so / was / we / the fan / used"],
                 answers=["1. Solar energy will be cheaper.",
                          "2. Coal won't disappear immediately.", "3. It will probably rain.",
                          "4. I don't think it will be cold.",
                          "5. It was hot, so we used the fan."], level="M", kind="grammar"),
              EX("U10.7-P3", "Reading review", "Read and choose.",
                 text=["Viet Nam's solar power grew faster between 2018 and 2021 than almost anywhere "
                       "in the world. The problem was that the electricity grid could not carry it "
                       "all: on some sunny days, solar farms had to be switched off because the wires "
                       "were full. Experts say the next ten years will be less about building panels "
                       "and more about building wires and batteries."],
                 items=["1. The text is mainly about A. how panels work  B. the problem of carrying "
                        "solar electricity  C. the price of electricity",
                        "2. Some solar farms had to be A. sold  B. switched off  C. moved",
                        "3. The next ten years will be about A. panels  B. wires and batteries  "
                        "C. coal"],
                 answers=["1. B", "2. B", "3. B"], level="M", kind="reading"),
              EX("U10.7-P4", "Unit 10 test yourself (10 marks)", "Answer about yourself (2 marks each).",
                 items=["1. Two sources of energy my family uses: ______",
                        "2. One prediction about 2050 with 'will': ______",
                        "3. One prediction with 'won't': ______",
                        "4. One promise about saving energy: ______",
                        "5. One cause-and-result sentence with 'so': ______"],
                 answers=["Model: 1. Electricity and gas. 2. Most houses will have solar panels. "
                          "3. Petrol motorbikes won't disappear from the countryside. "
                          "4. I'll turn off the fan every time I leave my room. "
                          "5. It was 39 degrees last June, so our bill was very high."],
                 level="D", kind="mixed")],
    procedure=[ST("Warm-up: Prediction bingo", 6,
                  ["Students write six predictions; teacher reads similar ones; students cross out "
                   "matches."],
                  "Play bingo with predictions.", "Whole class", "Slide 2"),
               ST("Vocabulary and listening review", 7,
                  ["U10.7-G1 race; then the listening quiz U10.7-L1."],
                  "Write words; complete sentences.", "Pairs", "Slides 3–4"),
               ST("Grammar review + error clinic", 10,
                  ["Grammar table; U10.7-G2 in pairs with explanations; add to the wall list."],
                  "Correct and explain six errors.", "Pairs → whole class", "Slides 5–7"),
               ST("Mixed practice", 6, ["U10.7-I1 gap-fill; fast finishers do Workbook P2."],
                  "Complete the text.", "Individual", "Student Book p. U10L7"),
               ST("Project: Save Energy at School", 12,
                  ["Groups finish their audit poster with real numbers and three suggestions.",
                   "Three groups present; the class chooses the plan to send to the head teacher."],
                  "Finish, present, choose.", "Groups of 4", "Slides 8–10"),
               ST("Wrap-up and homework", 4, ["Agree who will take the plan to the head teacher. "
                                              "Set H1–H4."],
                  "Volunteer; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Take the plan out of the classroom",
                     ["Today's project is not for me. It is for the head teacher.",
                      "That means two things. First, your numbers must be TRUE — count again if you "
                      "are not sure.",
                      "Second, your suggestions must be POSSIBLE. 'Buy solar panels for the whole "
                      "school' is a wish. 'Choose one energy monitor per class' is a plan.",
                      "Who will volunteer to present it? … Good. I'll come with you."]),
                  TK("Final check on will",
                     ["Three rules for the test, and they are all easy.",
                      "One: after will, the verb is naked. No 'to', no -s.",
                      "Two: the negative is WON'T, never 'willn't'.",
                      "Three: for a negative opinion, move the 'not' to the first verb: "
                      "I DON'T THINK it will rain."])],
    support=["Give the error clinic with mistakes underlined.",
             "Provide the plan sentences as a frame.",
             "Assign the 'numbers' role in the presentation."],
    challenge=["Ask them to calculate the yearly saving in dong.",
               "Ask them to present to the head teacher.",
               "Ask for 130 words in H3."],
    assessment=["Unit 10 checklist: 5 of 6 'I can' statements", "Error clinic 5 of 6",
                "Presents a plan with at least two correct 'will' sentences"],
    board_plan=["LEFT: energy vocabulary", "CENTRE: Unit 10 grammar table",
                "RIGHT: project requirements; Homework H1–H4"],
    materials=["Poster paper", 'Recording: Looking Back — listen again (replay — see the lesson page)', "The audit results from Lesson 6"],
)

UNIT.lessons = [L1, L2, L3, L4, L5, L6, L7]

UNIT.revision = [
    EX("R10-1", "Vocabulary", "Complete with a word from Unit 10.",
       items=["1. Energy from the sun is s______ energy.",
              "2. Sun and wind are r______ sources.",
              "3. Please turn ______ the lights when you leave.",
              "4. Burning coal causes air p______ .",
              "5. A b______ stores electricity for the night.",
              "6. An LED b______ uses much less electricity."],
       answers=["1. solar", "2. renewable", "3. off", "4. pollution", "5. battery", "6. bulb"],
       level="E", kind="vocab"),
    EX("R10-2", "Grammar: will / won't", "Complete the predictions.",
       items=["1. Solar energy ______ be cheaper. (+)", "2. Coal ______ disappear soon. (–)",
              "3. ______ electric cars be normal? – Yes, they ______ .",
              "4. It ______ probably rain tomorrow.",
              "5. I ______ think oil will last for ever."],
       answers=["1. will", "2. won't", "3. Will … will", "4. will", "5. don't"],
       level="M", kind="grammar"),
    EX("R10-3", "Grammar: cause and result", "Join the sentences.",
       items=["1. It was 39 degrees. / The bill was high. (so)",
              "2. The bill was high. / We used the air conditioner. (because)",
              "3. Burning coal / air pollution (causes)",
              "4. Solar panels need sun. / They produce nothing at night. (This means that)"],
       answers=["1. It was 39 degrees, so the bill was high.",
                "2. The bill was high because we used the air conditioner.",
                "3. Burning coal causes air pollution.",
                "4. Solar panels need sun. This means that they produce nothing at night."],
       level="M", kind="grammar"),
    EX("R10-4", "Reading", "Read and answer.",
       text=["An average Vietnamese family uses about 200 kWh of electricity a month. "
             "Nearly half of that goes on cooling: fans and air conditioners. Experts say that three "
             "simple changes — setting the air conditioner at 26 degrees, using a fan at the same "
             "time, and closing the doors — can reduce a family's bill by up to a quarter, and they "
             "cost nothing at all."],
       items=["1. How much electricity does an average family use a month?",
              "2. What uses nearly half of it?", "3. Name the three changes.",
              "4. How much can a family save?", "5. How much do the changes cost?"],
       answers=["1. About 200 kWh.", "2. Cooling — fans and air conditioners.",
                "3. Set the air conditioner at 26 degrees; use a fan at the same time; close the doors.",
                "4. Up to a quarter of the bill.", "5. Nothing."], level="M", kind="reading"),
    EX("R10-5", "Writing", "Write a paragraph (100–120 words) about energy in 2050.",
       items=["Situation now – three predictions with will/won't – one problem – your opinion."],
       answers=["See U10.6-W2 model. Marking: content 3, will/won't 3, organisation 2, "
                "vocabulary 1, length 1."], level="D", kind="writing", lines=16),
]
