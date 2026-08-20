# -*- coding: utf-8 -*-
"""UNIT 12 – ENGLISH-SPEAKING COUNTRIES  (Periods 84–90)"""
from curriculum.schema import *
from curriculum.audio_sources import AUDIO

UNIT = Unit(
    number=12, title="English-Speaking Countries",
    theme="Countries where English is spoken, their people, places and customs; English as a world language",
    can_do=["name six English-speaking countries and one famous place in each",
            "talk about experiences with the present perfect (Have you ever…?)",
            "use been to and never for experiences",
            "read about a country and complete a fact file",
            "listen to a student describing life abroad and take notes",
            "write a fact file or an email about a country (110–130 words)"],
    grammar_focus=["Present perfect with ever / never (introduction)",
                   "have/has been to", "Superlatives (recycled from Unit 4)"],
    pron_focus="Final consonant clusters /st/, /sk/, /sp/, /nd/; sentence intonation review",
    vocab_focus="Countries, nationalities, landmarks, cultural facts",
    project={"name": "Country Corner — end-of-year showcase",
             "goal": "Groups create a corner about one English-speaking country and host visitors "
                     "(including students from other classes if possible).",
             "steps": ["Choose one country: the UK, the USA, Canada, Australia, New Zealand, "
                       "Ireland, Singapore or India.",
                       "Make a fact file poster: population, capital, language(s), one famous place, "
                       "one famous person, one food, one custom.",
                       "Write eight sentences, including two superlatives and one present perfect.",
                       "Prepare five quiz questions with answers on the back.",
                       "Host your corner; then visit the others and answer their quizzes."],
             "marking": "Content 3 – Language 3 – Poster 2 – Hosting 2 (total 10)"})

L1 = Lesson(
    code="U12L1", unit=12, number=1, period=86,
    lesson_type="Getting Started", title="Where is English spoken?",
    objectives=["name six English-speaking countries and their nationalities",
                "understand a conversation about a country",
                "give one fact about each country",
                "write three sentences about a country they would like to visit"],
    recycled=["Unit 4 superlatives; Unit 9 country and culture words; Unit 10 will"],
    vocab=[V("the United Kingdom (the UK)", "n", "/ðə juːˌnaɪtɪd ˈkɪŋdəm/", "Vương quốc Anh", "The UK has four parts."),
           V("the United States (the USA)", "n", "/ðə juːˌnaɪtɪd ˈsteɪts/", "Hoa Kỳ", "The USA has fifty states."),
           V("Australia", "n", "/ɒˈstreɪliə/", "Úc", "Australia is a country and a continent."),
           V("Canada", "n", "/ˈkænədə/", "Ca-na-đa", "Canada has two official languages."),
           V("New Zealand", "n", "/ˌnjuː ˈziːlənd/", "Niu Di-lân", "New Zealand has more sheep than people."),
           V("Singapore", "n", "/ˌsɪŋəˈpɔː/", "Xin-ga-po", "Singapore has four official languages."),
           V("nationality", "n", "/ˌnæʃəˈnæləti/", "quốc tịch", "What nationality is she?"),
           V("official language", "n", "/əˈfɪʃl ˈlæŋɡwɪdʒ/", "ngôn ngữ chính thức", "English is an official language there.")],
    phrases=["English is spoken in…", "the capital of…", "What nationality…?",
             "It's famous for…", "I'd love to visit…"],
    grammar=G("Countries, nationalities and 'be famous for' (recycled)",
              use=["Country → nationality: England → English; Australia → Australian; "
                   "Canada → Canadian; Viet Nam → Vietnamese; Singapore → Singaporean.",
                   "Nationalities always begin with a CAPITAL letter.",
                   "'The' is used with some countries: the UK, the USA, the Philippines. "
                   "Most others take no article: Australia, Canada, Viet Nam.",
                   "be famous for + noun / V-ing: Australia is famous for its beaches."],
              form=[["Country", "Nationality", "Example"],
                    ["the UK", "British", "She is British."],
                    ["the USA", "American", "He is American."],
                    ["Australia", "Australian", "They are Australian."],
                    ["Canada", "Canadian", "My teacher is Canadian."],
                    ["New Zealand", "a New Zealander", "He's a New Zealander."],
                    ["Viet Nam", "Vietnamese", "We are Vietnamese."]],
              examples=["English is spoken in more than sixty countries.",
                        "Canada is famous for its lakes and its ice hockey.",
                        "The capital of Australia is Canberra, not Sydney."],
              pitfall="*I am vietnamese* (no capital letter), *She is from the Canada* "
                      "(no 'the' with Canada), *He is a British* (British is an adjective here: "
                      "'He is British').",
              note="Recycle Unit 9 articles: the UK and the USA always take 'the'."),
    pron=P("Final consonant clusters /st/, /sk/, /sp/, /nd/",
           "English often ends words with two or three consonants together: fir-ST, a-SK, "
           "cri-SP, la-ND, world. Do not add a vowel and do not drop the last sound.",
           items=["/st/: first, most, last, west, tourist", "/sk/: ask, desk, task",
                  "/sp/: crisp, wasp", "/nd/: land, island, England, second"],
           drill=["The first tourist asked about the island.",
                  "England is the second-largest country in the UK.",
                  "Most of the west coast is desert."],
           vn_note="Vietnamese syllables never end with two consonants, so 'first' becomes 'fir' "
                   "and 'island' becomes 'ai-lan'. Say the word slowly, then add speed: fir-st, "
                   "first."),
    listening=AUDIO['U12L1'],
    reading=T("Six countries, six surprises",
              ["THE UK is not one country but four: England, Scotland, Wales and Northern Ireland. "
               "They play football as four separate teams.",
               "THE USA has no official language at national level. English is used everywhere, "
               "but no law makes it official.",
               "CANADA has two official languages, English and French. In Quebec, most people speak "
               "French first.",
               "AUSTRALIA is about twenty-three times larger than Viet Nam, but it has only about a "
               "quarter of the population.",
               "NEW ZEALAND has three official languages: English, Maori and New Zealand Sign "
               "Language — the only country in the world with an official sign language.",
               "SINGAPORE is smaller than Phu Quoc island, and it has four official languages. "
               "Most students there learn two languages at school from the age of six."],
              tasks=[EX("U12.1-R1", "Read and match", "Which country?",
                        items=["1. It is really four countries. ______",
                               "2. It has no official language. ______",
                               "3. It has an official sign language. ______",
                               "4. It is much bigger than Viet Nam but has fewer people. ______",
                               "5. It is smaller than Phu Quoc. ______"],
                        answers=["1. the UK", "2. the USA", "3. New Zealand", "4. Australia",
                                 "5. Singapore"], level="E", kind="reading"),
                     EX("U12.1-R2", "Read and answer", "Answer the questions.",
                        items=["1. Name the four parts of the UK.",
                               "2. What are Canada's two official languages?",
                               "3. How much larger is Australia than Viet Nam?",
                               "4. From what age do Singaporean students learn two languages?"],
                        answers=["1. England, Scotland, Wales and Northern Ireland.",
                                 "2. English and French.", "3. About twenty-three times.",
                                 "4. From the age of six."], level="M", kind="reading")]),
    speaking=[EX("U12.1-S1", "Country quiz", "In pairs, make five quiz questions about the six "
                 "countries and test another pair.",
                 items=["Use: Which country…? What is the capital of…? How many…?"],
                 answers=["Model: Which country has three official languages? – New Zealand."],
                 level="M", kind="speaking")],
    writing=[EX("U12.1-W1", "Sentence writing", "Write three sentences about a country you would "
                "like to visit.",
                items=["1. I'd love to visit ______ .", "2. It is famous for ______ .",
                       "3. I want to go there because ______ ."],
                answers=["Model: I'd love to visit New Zealand. It is famous for its mountains and "
                         "its sheep. I want to go there because I have seen photographs of the "
                         "south island and it looks like another planet."],
                level="M", kind="writing", lines=4)],
    communication={"function": "Correcting politely and giving information",
                   "phrases": ["Actually, it's…", "That's a common mistake.",
                               "I thought so too, but…", "Are you sure?", "Let me check."],
                   "roleplay": "A gives three 'facts' about a country; two are wrong. "
                               "B corrects them politely.",
                   "real_life": "Correcting somebody without being rude."},
    guided=[EX("U12.1-G1", "Country → nationality", "Write the nationality.",
               items=["1. the UK → ", "2. the USA → ", "3. Australia → ", "4. Canada → ",
                      "5. Viet Nam → ", "6. Singapore → "],
               answers=["1. British", "2. American", "3. Australian", "4. Canadian", "5. Vietnamese",
                        "6. Singaporean"], level="E", kind="vocab"),
            EX("U12.1-G2", "the or no article?", "Complete.",
               items=["1. ______ UK", "2. ______ Australia", "3. ______ USA", "4. ______ Canada",
                      "5. ______ Philippines", "6. ______ New Zealand"],
               answers=["1. the", "2. – ", "3. the", "4. – ", "5. the", "6. –"],
               level="M", kind="grammar")],
    independent=[EX("U12.1-I1", "Complete the facts", "Use the words in the box.",
                    wordbank=["capital", "official", "nationality", "population", "famous"],
                    items=["1. Canberra is the ______ of Australia.",
                           "2. English is an ______ language in more than sixty countries.",
                           "3. What ______ is she? — She's Canadian.",
                           "4. Australia has a small ______ for such a large country.",
                           "5. New Zealand is ______ for its mountains."],
                    answers=["1. capital", "2. official", "3. nationality", "4. population",
                             "5. famous"], level="M", kind="vocab"),
                 EX("U12.1-I2", "Country quiz", "Do U12.1-S1 with another pair.", items=[],
                    answers=["See U12.1-S1."], level="D", kind="speaking")],
    review=["6 English-speaking countries and nationalities", "the UK / the USA (with 'the')",
            "final clusters /st/, /sk/, /nd/"],
    homework=[EX("U12.1-H1", "Vocabulary", "Write the country.",
                 items=["1. Its capital is Canberra: ______", "2. It has four official languages "
                        "and is very small: ______", "3. It is really four countries: ______",
                        "4. It is the second largest country in the world: ______",
                        "5. It has more sheep than people: ______"],
                 answers=["1. Australia", "2. Singapore", "3. the UK", "4. Canada",
                          "5. New Zealand"], level="E", kind="vocab"),
              EX("U12.1-H2", "Grammar", "Write the nationality and add 'the' where necessary.",
                 items=["1. She comes from ______ UK. She is ______ .",
                        "2. He comes from ______ Australia. He is ______ .",
                        "3. They come from ______ USA. They are ______ .",
                        "4. I come from ______ Viet Nam. I am ______ ."],
                 answers=["1. the; British", "2. – ; Australian", "3. the; American",
                          "4. – ; Vietnamese"], level="M", kind="grammar"),
              EX("U12.1-H3", "Writing", "Write 4 sentences about an English-speaking country: "
                 "capital, language(s), one famous place, one fact that surprised you.",
                 items=[], answers=["Model: The capital of Canada is Ottawa, not Toronto. "
                                    "Canada has two official languages, English and French. "
                                    "It is famous for Niagara Falls and for ice hockey. "
                                    "What surprised me is that it is the second largest country in "
                                    "the world but has fewer people than Viet Nam."],
                 level="M", kind="writing", lines=5),
              EX("U12.1-H4", "Pronunciation", "Say these words five times, keeping both final "
                 "consonants: first, most, ask, desk, island, England.",
                 items=[], answers=["Spot-check in Lesson 2."], level="M", kind="pron")],
    workbook=[EX("U12.1-P1", "Complete the words", "Write the missing letters.",
                 items=["1. A _ s t r a l i a", "2. C a n _ d a", "3. S i n g a p _ r e",
                        "4. n a t i o n _ l i t y", "5. o f f _ c i a l"],
                 answers=["1. Australia", "2. Canada", "3. Singapore", "4. nationality",
                          "5. official"], level="E", kind="vocab"),
              EX("U12.1-P2", "Capitals quiz", "Match the country with its capital.",
                 items=["1. Australia", "2. Canada", "3. New Zealand", "4. the UK", "5. the USA",
                        "a. Ottawa", "b. London", "c. Canberra", "d. Washington D.C.",
                        "e. Wellington"],
                 answers=["1–c", "2–a", "3–e", "4–b", "5–d"], level="M", kind="vocab"),
              EX("U12.1-P3", "Final clusters", "Read the words aloud and tick the ones you find "
                 "difficult. Then practise them ten times.",
                 items=["first · most · asked · desk · island · England · second · west · "
                        "tourist · world"],
                 answers=["No fixed answer — the teacher listens and marks the two hardest for "
                          "each student."], level="M", kind="pron"),
              EX("U12.1-P4", "Correct the mistakes", "One mistake per sentence.",
                 items=["1. She is from the Canada.", "2. I am vietnamese.",
                        "3. He is a British.", "4. The capital of Australia is Sydney.",
                        "5. English is official language in many countries."],
                 answers=["1. She is from Canada.", "2. I am Vietnamese.", "3. He is British.",
                          "4. The capital of Australia is Canberra.",
                          "5. English is an official language in many countries."],
                 level="D", kind="grammar"),
              EX("U12.1-P5", "Writing", "Write 5 sentences about Viet Nam for a foreign student.",
                 items=["Capital, population, language, one famous place, one custom."],
                 answers=["Model: The capital of Viet Nam is Hanoi, although Ho Chi Minh City is "
                          "bigger. About one hundred million people live here. The official language "
                          "is Vietnamese, and many students also learn English. Ha Long Bay is our "
                          "most famous place. At Tet, families clean their houses and give lucky "
                          "money to children."], level="D", kind="writing", lines=6)],
    procedure=[ST("Warm-up: World map", 5,
                  ["Show a world map. Students name countries where English is spoken; "
                   "mark them on the map."],
                  "Name countries.", "Whole class", "Slide 2"),
               ST("Presentation: 6 countries + nationalities", 10,
                  ["Flags and names; drill with stress: Aus'TRA-lia, 'CA-na-da, Singa'PORE.",
                   "Build the country → nationality table. Highlight capital letters and 'the'."],
                  "Repeat; copy the table.", "Whole class", "Slides 3–6"),
               ST("Pronunciation: final clusters", 7,
                  ["Model 'first' slowly: fir–st. Students say it in two parts, then join it.",
                   "Word list drill, then the three sentences."],
                  "Break and rejoin the clusters.", "Whole class", "Slide 7"),
               ST("Listening: the quiz", 8,
                  ['Play the recording “Lesson 48: Have You Ever ...?” twice (three times if the class asks); students do the listening tasks...?” twice (three times if the class asks); students do the listening tasks; note the answers and the final facts.'],
                  "Listen and answer.", "Individual → pairs", "Slide 8"),
               ST("Reading + speaking", 10,
                  ["Read 'Six countries, six surprises'; do R1 and R2.",
                   "Then pairs write five quiz questions and test another pair."],
                  "Read, answer, quiz.", "Individual → pairs", "Slides 9–10"),
               ST("Wrap-up and homework", 5, ["Class vote: which country would you most like to "
                                              "visit? Set H1–H4."],
                  "Vote; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Most English speakers learned it",
                     ["Here is the most important fact in this unit. About one and a half billion "
                      "people speak English. Only four hundred million learned it as babies.",
                      "That means the great majority of English speakers in the world are people "
                      "like you: they studied it at school.",
                      "So when you speak English to a Japanese engineer or a Brazilian doctor, "
                      "you are both learners. Nobody is judging your grammar.",
                      "English does not belong to England any more. It belongs to everybody who "
                      "uses it — including you."]),
                  TK("Final clusters: break and rejoin",
                     ["Say 'first'. Many of us say 'fir'. The /st/ disappears.",
                      "Break it into two parts: fir … st. Say the /st/ alone: sssst.",
                      "Now join them slowly: fir–st. Faster: first. Perfect.",
                      "Do the same with asked (ask–t), island (ai–land), second (se–cond). "
                      "Break, then rejoin."])],
    support=["Give the country/nationality table half-completed.",
             "Use flags and a map for support.",
             "Practise four clusters instead of eight."],
    challenge=["Ask for three extra English-speaking countries (Ireland, India, South Africa).",
               "Ask them to write five quiz questions with superlatives.",
               "Ask them to explain why the USA has no official language."],
    assessment=["Names 5 of 6 countries and nationalities", "Uses 'the' correctly with the UK/USA",
                "Says 'first', 'island', 'asked' with both consonants"],
    board_plan=["LEFT: world map with countries marked",
                "CENTRE: country → nationality table (+ the UK / the USA)",
                "RIGHT: /st/ /sk/ /nd/ clusters; Homework H1–H4"],
    materials=["World map", "Flags or pictures", 'Recording: Lesson 48: Have You Ever ...? — VOA Learning English — Let’s Learn English, Level 1 (3:37)'],
)

L2 = Lesson(
    code="U12L2", unit=12, number=2, period=87,
    lesson_type="A Closer Look 1", title="Landmarks and cultural facts",
    objectives=["name eight landmarks and say where they are",
                "use superlatives to compare countries",
                "pronounce final consonant clusters correctly",
                "give three facts about a country"],
    recycled=["U12L1 countries and nationalities; Unit 4 superlatives; Unit 9 culture words"],
    vocab=[V("landmark", "n", "/ˈlændmɑːk/", "địa danh nổi tiếng", "The Opera House is a famous landmark."),
           V("population", "n", "/ˌpɒpjuˈleɪʃn/", "dân số", "The population is about 26 million."),
           V("continent", "n", "/ˈkɒntɪnənt/", "lục địa", "Australia is a country and a continent."),
           V("desert", "n", "/ˈdezət/", "sa mạc", "Most of central Australia is desert."),
           V("island", "n", "/ˈaɪlənd/", "hòn đảo", "New Zealand has two main islands."),
           V("waterfall", "n", "/ˈwɔːtəfɔːl/", "thác nước", "Niagara Falls is on the border."),
           V("bridge", "n", "/brɪdʒ/", "cây cầu", "The Golden Gate Bridge is in San Francisco."),
           V("skyscraper", "n", "/ˈskaɪskreɪpə/", "tòa nhà chọc trời", "New York is full of skyscrapers.")],
    phrases=["It is located in…", "It was built in…", "It is the biggest … in the world",
             "It attracts … visitors a year"],
    grammar=G("Superlatives for facts (recycled from Unit 4)",
              use=["the + -est / the most + adjective, for the number one in a group.",
                   "Add the group: the largest country IN THE WORLD, the tallest building "
                   "IN AUSTRALIA.",
                   "Common irregulars: good → the best; bad → the worst; far → the furthest.",
                   "'one of the + superlative + plural noun': one of the most visited places "
                   "in the world."],
              form=[["Structure", "Example"],
                    ["the + -est", "Russia is the largest country in the world."],
                    ["the most + adj", "It is the most visited landmark in Australia."],
                    ["irregular", "It is the best-known bridge in America."],
                    ["one of the…", "Niagara is one of the most famous waterfalls in the world."]],
              examples=["Sydney Opera House is one of the most photographed buildings in the world.",
                        "Canada is the second largest country in the world."],
              pitfall="*the most biggest* (never both), *the largest of the world* "
                      "(→ IN the world), *one of the most famous waterfall* (→ waterfallS).",
              note="After 'one of the most…' the noun is always PLURAL."),
    pron=P("More final clusters: /sk/, /st/, /ks/, /dʒ/",
           "skyscraper begins with /sk/ and 'ask', 'desk' end with it. 'Bridge' ends with /dʒ/. "
           "Watch 'landmark' (/nd/ + /m/) and 'island' (silent s!).",
           items=["/sk/: skyscraper, ask, desk", "/st/: tourist, most, west",
                  "/dʒ/: bridge, village, large", "island /ˈaɪlənd/ — the S is SILENT"],
           drill=["The tourist asked about the largest bridge.",
                  "Most skyscrapers in the west are on the island."],
           vn_note="'Island' is a famous trap: the s is silent — /ˈaɪlənd/, not /ˈɪslənd/."),
    listening=AUDIO['U12L2'],
    reading=T("Australia in numbers",
              ["AREA: 7.7 million square kilometres — about twenty-three times the size of Viet Nam, "
               "and the sixth largest country in the world.",
               "POPULATION: about 26 million — a quarter of Viet Nam's, in twenty-three times the "
               "space. Most Australians live within fifty kilometres of the coast, because the "
               "centre is desert.",
               "CAPITAL: Canberra. Sydney and Melbourne are both much bigger, and they argued about "
               "which should be the capital, so a new city was built between them in 1913.",
               "LANGUAGES: English, plus more than a hundred and fifty Aboriginal languages still "
               "spoken today, out of about 250 before 1788.",
               "ANIMALS: about 80% of Australia's animals are found nowhere else in the world.",
               "ONE SURPRISE: Australia is the driest inhabited continent on Earth, but it is also "
               "one of the world's largest food exporters."],
              tasks=[EX("U12.2-R1", "Read and complete the fact file", "Write the information.",
                        items=["Area: ______ km² (______ times Viet Nam)",
                               "Population: about ______ million",
                               "Capital: ______ ; why: ______",
                               "Languages: ______ plus ______ Aboriginal languages",
                               "Animals: ______ % found nowhere else"],
                        answers=["7.7 million; twenty-three", "26",
                                 "Canberra; Sydney and Melbourne argued, so a new city was built "
                                 "between them in 1913",
                                 "English; more than 150", "80"], level="M", kind="reading"),
                     EX("U12.2-R2", "Superlative sentences", "Write three superlative sentences from "
                        "the text.",
                        items=["1. (size in the world) ______", "2. (driest) ______",
                               "3. (food exporters) ______"],
                        answers=["1. Australia is the sixth largest country in the world.",
                                 "2. It is the driest inhabited continent on Earth.",
                                 "3. It is one of the world's largest food exporters."],
                        level="D", kind="reading")]),
    speaking=[EX("U12.2-S1", "Landmark descriptions", "Describe a landmark without saying its name. "
                 "Your partner guesses.",
                 items=["Say: which country, what kind of place, one number, why it is famous."],
                 answers=["Model: It's in Australia. It's a building near the water. "
                          "Its roof has a million tiles. It looks like sails. → Sydney Opera House."],
                 level="M", kind="speaking"),
              EX("U12.2-S2", "Compare two countries", "Compare Viet Nam with an English-speaking "
                 "country using three superlatives or comparatives.",
                 items=["Ideas: size, population, weather, food, famous places."],
                 answers=["Model: Australia is much bigger than Viet Nam, but Viet Nam has four "
                          "times more people. Ha Long Bay is the most famous place in Viet Nam, "
                          "and the Opera House is probably the most famous in Australia."],
                 level="D", kind="speaking")],
    writing=[EX("U12.2-W1", "Superlative facts", "Write five superlative sentences.",
                items=["1. (Russia / large country / world) ______",
                       "2. (Australia / dry inhabited continent) ______",
                       "3. (Canada / second large country) ______",
                       "4. (Ha Long Bay / famous place / Viet Nam) ______",
                       "5. (one of / photographed buildings / world / Sydney Opera House) ______"],
                answers=["1. Russia is the largest country in the world.",
                         "2. Australia is the driest inhabited continent.",
                         "3. Canada is the second largest country in the world.",
                         "4. Ha Long Bay is the most famous place in Viet Nam.",
                         "5. The Sydney Opera House is one of the most photographed buildings in "
                         "the world."], level="M", kind="writing")],
    communication={"function": "Sharing surprising facts",
                   "phrases": ["Did you know that…?", "I didn't know that!", "Are you serious?",
                               "That can't be true!", "It is, actually."],
                   "roleplay": "Fact exchange: tell your partner three facts, one of which is false. "
                               "Your partner must find the false one.",
                   "real_life": "Sharing information and checking whether it is true."},
    guided=[EX("U12.2-G1", "Match the landmark and the country", "Write the letter.",
               items=["1. Sydney Opera House", "2. Niagara Falls", "3. Big Ben",
                      "4. Golden Gate Bridge", "5. Milford Sound",
                      "a. the UK", "b. New Zealand", "c. Australia", "d. the USA",
                      "e. Canada / the USA border"],
               answers=["1–c", "2–e", "3–a", "4–d", "5–b"], level="E", kind="vocab"),
            EX("U12.2-G2", "Superlative forms", "Write the superlative.",
               items=["1. large → ", "2. dry → ", "3. famous → ", "4. good → ", "5. big → ",
                      "6. beautiful → "],
               answers=["1. the largest", "2. the driest", "3. the most famous", "4. the best",
                        "5. the biggest", "6. the most beautiful"], level="E", kind="grammar")],
    independent=[EX("U12.2-I1", "Error clinic", "Correct one mistake in each sentence.",
                    items=["1. Russia is the most biggest country.",
                           "2. It is the largest country of the world.",
                           "3. It is one of the most famous waterfall in the world.",
                           "4. Australia is more bigger than Viet Nam.",
                           "5. It is the goodest place to visit."],
                    answers=["1. Russia is the biggest country.",
                             "2. It is the largest country in the world.",
                             "3. It is one of the most famous waterfalls in the world.",
                             "4. Australia is much bigger than Viet Nam.",
                             "5. It is the best place to visit."], level="D", kind="grammar"),
                 EX("U12.2-I2", "Fact exchange", "Do the three-facts game (one false) with a partner.",
                    items=[], answers=["See communication section."], level="D", kind="speaking")],
    review=["8 landmark and geography words", "Superlatives with 'in the world'",
            "one of the most + plural noun", "final clusters and silent s in 'island'"],
    homework=[EX("U12.2-H1", "Vocabulary", "Complete with landmark, population, continent, desert, "
                 "island, waterfall.",
                 items=["1. Australia is a country and a ______ .",
                        "2. Niagara is a famous ______ .", "3. New Zealand has two main ______ s.",
                        "4. The centre of Australia is ______ .",
                        "5. The ______ of Singapore is about six million.",
                        "6. The Opera House is Sydney's most famous ______ ."],
                 answers=["1. continent", "2. waterfall", "3. island", "4. desert", "5. population",
                          "6. landmark"], level="E", kind="vocab"),
              EX("U12.2-H2", "Grammar", "Complete with the superlative.",
                 items=["1. Russia is (large) ______ country in the world.",
                        "2. Australia is (dry) ______ inhabited continent.",
                        "3. Ha Long Bay is (famous) ______ place in Viet Nam.",
                        "4. It is one of (visited) ______ landmarks in the world.",
                        "5. That was (good) ______ trip of my life."],
                 answers=["1. the largest", "2. the driest", "3. the most famous",
                          "4. the most visited", "5. the best"], level="M", kind="grammar"),
              EX("U12.2-H3", "Writing", "Write 5 facts about an English-speaking country, "
                 "including two superlatives.",
                 items=[], answers=["Model: Canada is the second largest country in the world, but "
                                    "it has fewer people than Viet Nam. Its capital is Ottawa, "
                                    "not Toronto. It has two official languages, English and French. "
                                    "Niagara Falls, on the border with the USA, is one of the most "
                                    "visited waterfalls in the world. Canada is also famous for ice "
                                    "hockey and maple syrup."], level="M", kind="writing", lines=6),
              EX("U12.2-H4", "Pronunciation", "Say these words five times: island (silent s!), "
                 "skyscraper, tourist, bridge, asked, landmark.",
                 items=[], answers=["Spot-check in Lesson 3."], level="M", kind="pron")],
    workbook=[EX("U12.2-P1", "Match", "Match the word with the meaning.",
                 items=["1. landmark", "2. continent", "3. desert", "4. population", "5. skyscraper",
                        "a. a very tall building", "b. the number of people",
                        "c. a very dry place with little rain", "d. a famous place people recognise",
                        "e. one of the seven big land areas of the world"],
                 answers=["1–d", "2–e", "3–c", "4–b", "5–a"], level="E", kind="vocab"),
              EX("U12.2-P2", "Superlatives", "Complete the sentences.",
                 items=["1. The Nile is ______ (long) river in the world.",
                        "2. Everest is ______ (high) mountain.",
                        "3. Singapore is one of ______ (small) countries in Asia.",
                        "4. That is ______ (bad) film I have ever seen.",
                        "5. Ha Long Bay is one of ______ (beautiful) places in Viet Nam."],
                 answers=["1. the longest", "2. the highest", "3. the smallest",
                          "4. the worst", "5. the most beautiful"], level="M", kind="grammar"),
              EX("U12.2-P3", "Reading", "Read and answer.",
                 text=["New Zealand has about five million people and about twenty-five million sheep "
                       "— five sheep for every person. The country is made of two main islands, "
                       "North and South, plus about six hundred small ones. Its Maori name is "
                       "Aotearoa, which means 'the land of the long white cloud'. New Zealand was "
                       "one of the last large places on Earth to be settled by people: humans arrived "
                       "only about 700 years ago."],
                 items=["1. How many people and sheep are there?",
                        "2. How many islands does the country have?",
                        "3. What does Aotearoa mean?",
                        "4. When did people first arrive?"],
                 answers=["1. About five million people and twenty-five million sheep.",
                          "2. Two main islands plus about six hundred small ones.",
                          "3. 'The land of the long white cloud'.", "4. About 700 years ago."],
                 level="M", kind="reading"),
              EX("U12.2-P4", "Writing", "Write a short fact file (80–90 words) about a country you "
                 "know well.",
                 items=["Area, population, capital, languages, one landmark, one surprising fact. "
                        "Include two superlatives."],
                 answers=["Model: Singapore is one of the smallest countries in the world: only "
                          "730 square kilometres, less than Phu Quoc island. About six million "
                          "people live there, so it is also one of the most crowded places on Earth. "
                          "The capital is the city itself. There are four official languages: "
                          "English, Malay, Mandarin and Tamil. Its most famous landmark is Marina Bay "
                          "Sands, a hotel with a swimming pool on the roof. What surprised me most is "
                          "that Singapore has no natural water and buys most of it. (89 words)"],
                 level="D", kind="writing", lines=10)],
    procedure=[ST("Warm-up: Nationality quick-fire", 5,
                  ["Teacher says a country; students say the nationality. Recycles Lesson 1."],
                  "Give nationalities.", "Whole class", "Slide 2"),
               ST("Presentation: landmarks and geography", 9,
                  ["Show pictures of eight landmarks; elicit and drill. Mark stress: 'LAND-mark, "
                   "popu'LA-tion, 'SKY-scra-per.",
                   "Point out the silent s in 'island'."],
                  "Repeat; copy with stress marks.", "Whole class", "Slides 3–5"),
               ST("Grammar: superlatives revisited", 8,
                  ["Recycle Unit 4: the -est / the most. Add 'in the world' and "
                   "'one of the most … + plural'.",
                   "Error warning: never 'the most biggest'; never 'of the world'."],
                  "Produce five superlative facts.", "Whole class", "Slides 6–7"),
               ST("Listening: landmark quiz", 9,
                  ['Play the recording “Languages and nationalities” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.'],
                  "Listen and complete.", "Individual → pairs", "Slide 8"),
               ST("Reading + speaking", 10,
                  ["Read 'Australia in numbers'; complete the fact file and write superlatives.",
                   "Then the guess-the-landmark game."],
                  "Read, write, describe and guess.", "Individual → pairs", "Slides 9–10"),
               ST("Wrap-up and homework", 4, ["Three students give a surprising fact. Set H1–H4."],
                  "Share facts.", "Whole class", "Slide 12")],
    teacher_talk=[TK("'In the world', not 'of the world'",
                     ["In Vietnamese we say 'lớn nhất thế giới' — the group comes straight after.",
                      "In English we need a preposition, and the preposition is IN.",
                      "'The largest country IN the world.' 'The best student IN our class.' "
                      "'The most famous place IN Viet Nam.'",
                      "Never 'of the world'. Say the three examples with me."]),
                  TK("One of the most … + PLURAL",
                     ["'It is one of the most famous waterfall in the world.' Can you hear the "
                      "mistake?",
                      "'One of' means it belongs to a GROUP. A group needs a plural: waterfallS.",
                      "One of the most famous waterfallS. One of the best studentS. "
                      "One of the biggest citieS.",
                      "This is worth half a mark in the test and it is very easy to remember: "
                      "one of the … + S."])],
    support=["Give landmark pictures with the names printed.",
             "Provide the superlative table from Unit 4.",
             "Reduce the fact file to four items."],
    challenge=["Ask for 'one of the most…' in three sentences.",
               "Ask them to research one more landmark at home.",
               "Ask them to compare Viet Nam and Australia in five sentences."],
    assessment=["Names 6 of 8 landmarks/geography words", "4 of 5 correct superlatives",
                "'Island' pronounced with a silent s"],
    board_plan=["LEFT: 8 landmark words with stress", "CENTRE: the + -est / the most … IN the world; "
                "one of the most … + plural", "RIGHT: final clusters; Homework H1–H4"],
    materials=["Landmark pictures", "World map", 'Recording: Languages and nationalities — ELLLO — Sound Grammar (1:36)'],
)

L3 = Lesson(
    code="U12L3", unit=12, number=3, period=88,
    lesson_type="A Closer Look 2", title="Present perfect: Have you ever…?",
    objectives=["form the present perfect with have/has + past participle",
                "ask and answer 'Have you ever…?' with ever and never",
                "use 'have been to' for experiences",
                "talk about their experiences in a class survey"],
    recycled=["U12L1–L2 country vocabulary; Unit 3 past simple and irregular verbs"],
    vocab=[V("experience", "n", "/ɪkˈspɪəriəns/", "trải nghiệm", "It was a wonderful experience."),
           V("abroad", "adv", "/əˈbrɔːd/", "ở nước ngoài", "Have you ever been abroad?"),
           V("foreigner", "n", "/ˈfɒrənə/", "người nước ngoài", "I talked to a foreigner yesterday."),
           V("try", "v", "/traɪ/", "thử", "Have you ever tried Indian food?"),
           V("meet", "v", "/miːt/", "gặp", "I have met people from six countries."),
           V("visit", "v", "/ˈvɪzɪt/", "thăm", "She has visited Australia twice.")],
    phrases=["Have you ever…?", "I have never…", "I've been to…", "Yes, I have. / No, I haven't.",
             "How many times…?"],
    grammar=G("Present perfect with ever and never (introduction)",
              use=["We use the present perfect to talk about EXPERIENCES in your life up to now. "
                   "The time is not important — only whether it happened.",
                   "Form: have / has + PAST PARTICIPLE (the third form: go–went–GONE, "
                   "see–saw–SEEN, eat–ate–EATEN). Regular verbs: -ed (visit → visited).",
                   "Question with EVER (= at any time in your life): Have you ever eaten sushi?",
                   "Negative with NEVER (never = not + ever, so do NOT add 'not'): "
                   "I have never eaten sushi.",
                   "'BEEN TO' means you went and came back: I've been to Hanoi twice.",
                   "IMPORTANT: if you say WHEN (yesterday, last year, in 2020), you must use the "
                   "PAST SIMPLE: I went to Hanoi last year."],
              form=[["", "Form", "Example"],
                    ["+", "have/has + past participle", "I have visited Hue. / She has visited Hue."],
                    ["–", "have/has never…", "I have never visited Hue."],
                    ["?", "Have/Has + subject + ever…?", "Have you ever visited Hue?"],
                    ["short answers", "Yes, I have. / No, I haven't.", "Has she? – Yes, she has."],
                    ["been to", "have been to + place", "I've been to Da Nang three times."],
                    ["with a past time", "past simple!", "I went to Da Nang last summer."]],
              examples=["Have you ever met a foreigner? – Yes, I have. I've met two.",
                        "She has never been abroad, but she has talked to visitors at her father's "
                        "shop.",
                        "I've seen the sea twice. I saw it for the first time in 2022."],
              pitfall="Three big errors: (1) *I have never not been* (never already means not); "
                      "(2) *I have been to Hanoi last year* (with a past time word use the past "
                      "simple: I WENT); (3) using the past simple instead: "
                      "*Did you ever eat sushi?* is possible in American English, but this course "
                      "teaches 'Have you ever eaten…?'",
              note="Vietnamese uses 'đã từng' for exactly this meaning — that is a very useful "
                   "translation for the concept."),
    pron=P("Contractions and the weak 'have'",
           "I've /aɪv/, you've /juːv/, we've /wiːv/, they've /ðeɪv/, he's /hiːz/ (= he has). "
           "In questions 'have' is weak: /həv juː ˈevə/.",
           items=["I've been to…", "she's visited…", "Have you ever…? /həv juː ˈevə/",
                  "Yes, I have. (strong) / No, I haven't."],
           drill=["Have you ever been abroad? – No, I haven't.",
                  "I've never met an Australian, but I've talked to a Canadian."],
           vn_note="In the short answer 'Yes, I HAVE' the word is strong and clear. "
                   "In the question it almost disappears. Drill both."),
    listening=AUDIO['U12L3'],
    reading=T("Three students, three experiences",
              ["HOA, 13, Nam Dinh: 'I have never been abroad and I have never met a foreigner in my "
               "town. But I have watched about four hundred hours of English videos, and last month "
               "I understood a whole film without subtitles for the first time. That was my "
               "experience.'",
               "DUC, 14, Da Nang: 'I've spoken English to tourists many times, because my mother "
               "sells drinks near the beach. I've helped people from Russia, Korea, France and "
               "Australia. My grammar is bad, but I have never had a conversation that failed.'",
               "LINH, 13, Can Tho: 'I've written to a girl in the Philippines since September. "
               "We've sent each other 26 emails. She has never been to Viet Nam and I have never "
               "been to her country, but I know what her bedroom looks like and she knows my "
               "grandmother's name.'",
               "Three different lives — and none of them has been on a plane."],
              tasks=[EX("U12.3-R1", "Read and answer", "Answer the questions.",
                        items=["1. What has Hoa never done? What has she done?",
                               "2. Why has Duc spoken to many tourists?",
                               "3. What does Duc say about his grammar?",
                               "4. How many emails have Linh and her friend sent?",
                               "5. What is the point of the last sentence?"],
                        answers=["1. She has never been abroad or met a foreigner in her town; "
                                 "she has watched about 400 hours of English videos and understood "
                                 "a whole film without subtitles.",
                                 "2. Because his mother sells drinks near the beach.",
                                 "3. That it is bad, but he has never had a conversation that failed.",
                                 "4. 26.",
                                 "5. That you do not need to travel to have real English experiences."],
                        level="M", kind="reading"),
                     EX("U12.3-R2", "Find the grammar", "Find in the text:",
                        items=["1. two sentences with 'never'", "2. two sentences with 'have/has + "
                               "past participle' in the positive",
                               "3. one past simple sentence and say why it is past simple"],
                        answers=["1. 'I have never been abroad', 'I have never met a foreigner', "
                                 "'I have never had a conversation that failed', 'She has never been "
                                 "to Viet Nam' (any two)",
                                 "2. 'I have watched about four hundred hours', 'I've spoken English "
                                 "to tourists many times', 'We've sent each other 26 emails' (any two)",
                                 "3. 'last month I understood a whole film' — because it says WHEN "
                                 "(last month)."], level="D", kind="reading")]),
    speaking=[EX("U12.3-S1", "Find someone who has…", "Ask 'Have you ever…?' and find a name for each.",
                 items=["1. …been to another province.", "2. …spoken English to a foreigner.",
                        "3. …eaten food from another country.", "4. …written an email in English.",
                        "5. …watched a film without subtitles.", "6. …been on a plane."],
                 answers=["Report with the third person: 'Nam has been on a plane.'"],
                 level="M", kind="speaking"),
              EX("U12.3-S2", "Tell me more", "Choose one 'yes' answer from the survey and ask three "
                 "follow-up questions in the PAST SIMPLE.",
                 items=["A: Have you ever been to Hanoi? B: Yes, I have. "
                        "A: When did you go? B: Last summer. A: What did you do?"],
                 answers=["This is the key skill: present perfect to open, past simple for details."],
                 level="D", kind="speaking")],
    writing=[EX("U12.3-W1", "Present perfect or past simple?", "Complete the sentences.",
                items=["1. I ______ (be) to Hanoi three times.",
                       "2. I ______ (go) to Hanoi last summer.",
                       "3. ______ you ever ______ (eat) sushi?",
                       "4. She ______ (never / meet) a foreigner.",
                       "5. We ______ (watch) an English film yesterday.",
                       "6. He ______ (write) six emails since September."],
                answers=["1. have been", "2. went", "3. Have … eaten", "4. has never met",
                         "5. watched", "6. has written"], level="D", kind="writing")],
    communication={"function": "Talking about experiences",
                   "phrases": ["Have you ever…?", "Yes, I have. / No, I haven't.",
                               "Really? What was it like?", "When did you go?",
                               "I've never done that.", "I'd love to try it."],
                   "roleplay": "Two students compare experiences; each must ask three "
                               "'Have you ever…?' questions and three past simple follow-ups.",
                   "real_life": "The commonest 'getting to know you' conversation in English."},
    guided=[EX("U12.3-G1", "Past participles", "Write the past participle.",
               items=["1. be → ", "2. go → ", "3. see → ", "4. eat → ", "5. meet → ",
                      "6. write → ", "7. visit → ", "8. try → "],
               answers=["1. been", "2. gone/been", "3. seen", "4. eaten", "5. met", "6. written",
                        "7. visited", "8. tried"], level="E", kind="grammar",
               note="'Been' = went and came back. 'Gone' = went and is still there."),
            EX("U12.3-G2", "Make questions and answers", "Write the question and a short answer.",
               items=["1. (you / ever / be / abroad?) – No", "2. (she / ever / try / Korean food?) – Yes",
                      "3. (they / ever / meet / a foreigner?) – Yes",
                      "4. (he / ever / write / an email in English?) – No"],
               answers=["1. Have you ever been abroad? – No, I haven't.",
                        "2. Has she ever tried Korean food? – Yes, she has.",
                        "3. Have they ever met a foreigner? – Yes, they have.",
                        "4. Has he ever written an email in English? – No, he hasn't."],
               level="M", kind="grammar")],
    independent=[EX("U12.3-I1", "Error clinic", "Correct one mistake in each sentence.",
                    items=["1. I have never not been abroad.",
                           "2. I have been to Hanoi last year.",
                           "3. Have you ever went to Hue?",
                           "4. She have visited Australia.",
                           "5. I have ate sushi twice.",
                           "6. Did you ever been to Da Nang?"],
                    answers=["1. I have never been abroad.", "2. I went to Hanoi last year.",
                             "3. Have you ever been to Hue?", "4. She has visited Australia.",
                             "5. I have eaten sushi twice.",
                             "6. Have you ever been to Da Nang?"],
                    level="D", kind="grammar",
                    note="Rule: WHEN you say the time → past simple. No time given → present perfect."),
                 EX("U12.3-I2", "Class survey", "Do U12.3-S1 and report three results with he/she "
                    "has…", items=[], answers=["See U12.3-S1."], level="D", kind="speaking")],
    review=["have/has + past participle for experiences", "ever in questions, never in negatives",
            "been to = went and came back", "with a past time word → past simple"],
    homework=[EX("U12.3-H1", "Grammar", "Write the past participle.",
                 items=["1. be → ", "2. see → ", "3. eat → ", "4. write → ", "5. meet → ",
                        "6. take → ", "7. do → ", "8. have → "],
                 answers=["1. been", "2. seen", "3. eaten", "4. written", "5. met", "6. taken",
                          "7. done", "8. had"], level="E", kind="grammar"),
              EX("U12.3-H2", "Grammar", "Present perfect or past simple?",
                 items=["1. I ______ (never / be) to Australia.",
                        "2. We ______ (visit) Hue in 2023.",
                        "3. ______ you ever ______ (meet) a foreigner?",
                        "4. She ______ (write) three emails this week.",
                        "5. He ______ (see) the sea for the first time last summer.",
                        "6. They ______ (try) Indian food twice."],
                 answers=["1. have never been", "2. visited", "3. Have … met", "4. has written",
                          "5. saw", "6. have tried"], level="D", kind="grammar"),
              EX("U12.3-H3", "Writing", "Write 5 sentences about your experiences: three with the "
                 "present perfect and two with the past simple.",
                 items=["Use ever, never and at least one 'been to'."],
                 answers=["Model: I have never been abroad, but I have been to five provinces in "
                          "Viet Nam. I have spoken English to a foreigner once: a Korean tourist "
                          "asked me the way last April. I have never eaten Indian food, although I "
                          "would like to try it. Last summer I saw the sea for the first time. "
                          "I have watched more than fifty films in English."],
                 level="M", kind="writing", lines=7),
              EX("U12.3-H4", "Pronunciation", "Say these five sentences five times with contractions: "
                 "I've been there. She's visited Hue. We've never met. Have you ever tried it? "
                 "Yes, I have.",
                 items=[], answers=["Spot-check in Lesson 4."], level="M", kind="pron")],
    workbook=[EX("U12.3-P1", "Past participles", "Complete the table.",
                 items=["go – went – ______", "see – saw – ______", "eat – ate – ______",
                        "write – wrote – ______", "meet – met – ______", "be – was/were – ______",
                        "take – took – ______", "do – did – ______"],
                 answers=["gone/been", "seen", "eaten", "written", "met", "been", "taken", "done"],
                 level="E", kind="grammar"),
              EX("U12.3-P2", "ever or never?", "Complete the sentences.",
                 items=["1. Have you ______ been to Hanoi?", "2. I have ______ been abroad.",
                        "3. Has she ______ tried Korean food?",
                        "4. They have ______ met a foreigner.",
                        "5. Have they ______ written an email in English?"],
                 answers=["1. ever", "2. never", "3. ever", "4. never", "5. ever"],
                 level="E", kind="grammar"),
              EX("U12.3-P3", "Present perfect or past simple?", "Choose the correct form.",
                 items=["1. I (have been / went) to Hue last year.",
                        "2. I (have been / went) to Hue three times.",
                        "3. She (has never eaten / never ate) sushi.",
                        "4. We (have watched / watched) a film yesterday.",
                        "5. (Have you ever met / Did you ever meet) an Australian?"],
                 answers=["1. went", "2. have been", "3. has never eaten", "4. watched",
                          "5. Have you ever met"], level="D", kind="grammar"),
              EX("U12.3-P4", "Write questions", "Write 'Have you ever…?' questions.",
                 items=["1. (be / on a plane) ______", "2. (eat / foreign food) ______",
                        "3. (speak / English to a foreigner) ______",
                        "4. (write / an email in English) ______",
                        "5. (see / the sea) ______"],
                 answers=["1. Have you ever been on a plane?", "2. Have you ever eaten foreign food?",
                          "3. Have you ever spoken English to a foreigner?",
                          "4. Have you ever written an email in English?",
                          "5. Have you ever seen the sea?"], level="M", kind="grammar"),
              EX("U12.3-P5", "Writing", "Write a short paragraph (70–80 words) about your English "
                 "experiences this year.",
                 items=["Use at least three present perfect sentences and one past simple sentence "
                        "with a time word."],
                 answers=["Model: This year I have learned about six hundred new English words and "
                          "I have written twelve compositions. I have never spoken to a native "
                          "speaker, but in March a Korean tourist asked me the way and I answered "
                          "him in English. I have watched more than forty short videos without "
                          "subtitles. I have not become fluent, but I have stopped being afraid, "
                          "and that is the biggest change. (78 words)"],
                 level="D", kind="writing", lines=10)],
    procedure=[ST("Warm-up: Irregular verb race", 5,
                  ["Teams write past forms of ten verbs; then add the third form (past participle)."],
                  "Write past forms.", "Teams", "Slide 2"),
               ST("Presentation: present perfect", 13,
                  ["Draw a life line: BIRTH ——— NOW. Say: 'Somewhere on this line, I have visited "
                   "Hue. When? It doesn't matter. It happened.'",
                   "Build the form: have/has + third form. Show three verbs: be–was–BEEN, "
                   "see–saw–SEEN, eat–ate–EATEN.",
                   "Question with ever, negative with never. Warn: never already means not.",
                   "Then the key contrast: 'I have been to Hue' (no time) vs 'I went to Hue last "
                   "year' (time given → past simple). Put a big TIME? box on the board.",
                   "Vietnamese support: 'đã từng' = present perfect experience."],
                  "Copy the form and the TIME? rule; produce six sentences.", "Whole class",
                  "Slides 3–8"),
               ST("Guided practice", 8, ["U12.3-G1, G2, W1; error clinic U12.3-I1."],
                  "Write participles, questions and answers; correct the errors.", "Pairs",
                  "Student Book p. U12L3"),
               ST("Listening: the class survey", 8,
                  ['Play the recording “The present perfect: ever and never” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; complete the numbers and the details.'],
                  "Listen and complete.", "Individual → pairs", "Slide 9"),
               ST("Speaking: find someone who has…", 9,
                  ["Mingle with six 'Have you ever…?' questions; then three past simple follow-ups "
                   "with one partner."],
                  "Ask, answer, follow up, report.", "Mingle → pairs", "Slides 10–11"),
               ST("Wrap-up and homework", 2, ["Three students report a classmate's experience. "
                                              "Set H1–H4."],
                  "Report; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("The life line",
                     ["(Draw a long line.) This end is the day you were born. This end is today.",
                      "Somewhere on this line — I don't know where and I don't care — you have eaten "
                      "pho. You have seen the sea, or you haven't. You have met a foreigner, "
                      "or you haven't.",
                      "That is the present perfect: something in your life, up to now, "
                      "with no date.",
                      "In Vietnamese we say 'đã từng'. Exactly the same idea. "
                      "Have you ever…? = Bạn đã từng…?"]),
                  TK("The TIME? question",
                     ["Here is the one rule that decides everything. Before you choose the tense, "
                      "ask: does the sentence say WHEN?",
                      "'I have been to Hue.' No date → present perfect. Correct.",
                      "'I have been to Hue last year.' STOP. There is a date. So: 'I WENT to Hue "
                      "last year.' Past simple.",
                      "Write it in your notebook in big letters: TIME WORD → PAST SIMPLE."])],
    support=["Give a list of ten past participles on a desk card.",
             "Provide the six survey questions written out.",
             "Reduce the error clinic to four sentences."],
    challenge=["Add 'How many times…?' and 'for / since' (light contact).",
               "Ask them to explain the TIME? rule to a weaker classmate.",
               "Ask for a paragraph mixing both tenses."],
    assessment=["7 of 8 correct past participles", "Forms 'Have you ever…?' correctly",
                "Chooses the right tense in 4 of 6 items"],
    board_plan=["LEFT: life line BIRTH ——— NOW", "CENTRE: have/has + 3rd form; ever ? / never –",
                "RIGHT: TIME WORD → PAST SIMPLE (big box); Homework H1–H4"],
    materials=["Irregular verb list", 'Recording: The present perfect: ever and never — ELLLO — Sound Grammar (1:23)'],
)

L4 = Lesson(
    code="U12L4", unit=12, number=4, period=89,
    lesson_type="Communication", title="Everyday English: meeting people from other countries",
    objectives=["start and keep a conversation with somebody from another country",
                "ask and answer 'getting to know you' questions",
                "take part in a 10-turn conversation",
                "write a short introduction message about themselves"],
    recycled=["U12L1–L3 country vocabulary and present perfect; Unit 6 question forms; "
              "Unit 1 everyday expressions"],
    vocab=[V("introduce", "v", "/ˌɪntrəˈdjuːs/", "giới thiệu", "Let me introduce myself."),
           V("pen friend", "n", "/ˈpen frend/", "bạn qua thư", "I have a pen friend in Ireland."),
           V("in common", "phr", "/ɪn ˈkɒmən/", "điểm chung", "We have a lot in common."),
           V("keep in touch", "v phr", "/kiːp ɪn tʌtʃ/", "giữ liên lạc", "Let's keep in touch!"),
           V("time zone", "n", "/ˈtaɪm zəʊn/", "múi giờ", "There is a five-hour time zone difference."),
           V("misunderstand", "v", "/ˌmɪsʌndəˈstænd/", "hiểu lầm", "Don't worry if you misunderstand.")],
    phrases=["Let me introduce myself.", "Where are you from?", "How long have you been here?",
             "We have a lot in common.", "Could you say that again, please?",
             "Let's keep in touch!"],
    grammar=G("Conversation skills: opening, developing and closing",
              use=["OPEN: Hello. Let me introduce myself. I'm… / Nice to meet you.",
                   "DEVELOP: ask a question, listen, react, ask a follow-up. "
                   "Never answer with one word.",
                   "REPAIR: Sorry, could you say that again, please? / What does … mean? / "
                   "How do you spell that?",
                   "CLOSE: It was nice talking to you. Let's keep in touch."],
              form=[["Stage", "Language"],
                    ["open", "Hi, I'm Mai. Nice to meet you."],
                    ["ask", "Where are you from? / How long have you been in Viet Nam?"],
                    ["react", "Really? That's interesting!"],
                    ["follow up", "And what do you think of the food?"],
                    ["repair", "Sorry, could you say that again, please?"],
                    ["close", "It was nice talking to you. Let's keep in touch!"]],
              examples=["A: How long have you been in Viet Nam? B: Three weeks. "
                        "A: Really? Where have you been so far?",
                        "Sorry, I didn't catch that. Could you repeat it more slowly, please?"],
              pitfall="One-word answers kill a conversation. Teach the rule: ANSWER + ADD. "
                      "'Yes, I have. I went last summer with my family.'",
              note="'Repair' language is the most useful and the least practised. Drill it hard."),
    pron=P("Friendly intonation and clear repair phrases",
           "Openings rise and sound warm. Repair phrases must be clear and slow — that is the whole "
           "point of them.",
           items=["Nice to meet you. ↘ (warm)", "Where are you from? ↘",
                  "Sorry, could you say that again, please? ↗",
                  "Let's keep in touch! ↗"],
           drill=["Hi, I'm Mai. Nice to meet you.",
                  "Sorry, could you say that again, please?",
                  "It was nice talking to you. Let's keep in touch!"],
           vn_note="Students say repair phrases quickly and quietly because they are embarrassed — "
                   "which makes the problem worse. Practise saying them slowly and confidently."),
    listening=AUDIO['U12L4'],
    reading=T("An email to a new pen friend",
              ["Hi Emma,",
               "My teacher gave me your address — I'm your new pen friend! Let me introduce myself.",
               "My name is Tran Thi Mai and I'm thirteen. I live in Nam Dinh, a small city about "
               "ninety kilometres south of Hanoi. There are four people in my family: my parents, "
               "my little brother and me. My father is a mechanic and my mother works in a school "
               "canteen.",
               "I've been learning English for four years, but I have never spoken to somebody from "
               "another country before you. I'm a bit nervous about my grammar, so please tell me "
               "if I write something strange.",
               "In my free time I play badminton and I make paper flowers. I have never been abroad, "
               "but I've been to Ha Long Bay twice and it is the most beautiful place I have seen.",
               "Now some questions for you. What is your school like? Have you ever tried Vietnamese "
               "food? And what is the weather like in October where you live? Here it is still "
               "twenty-eight degrees!",
               "Write soon.",
               "Mai"],
              tasks=[EX("U12.4-R1", "Read and answer", "Answer the questions.",
                        items=["1. Where does Mai live, and how far is it from Hanoi?",
                               "2. Who is in her family, and what do her parents do?",
                               "3. How long has she been learning English?",
                               "4. What is she nervous about?",
                               "5. Write the three questions she asks."],
                        answers=["1. In Nam Dinh, about ninety kilometres south of Hanoi.",
                                 "2. Her parents, her little brother and her; her father is a "
                                 "mechanic and her mother works in a school canteen.",
                                 "3. Four years.", "4. Her grammar.",
                                 "5. What is your school like? Have you ever tried Vietnamese food? "
                                 "What is the weather like in October where you live?"],
                        level="M", kind="reading")]),
    speaking=[EX("U12.4-S1", "Introduce yourself", "Introduce yourself to three classmates as if "
                 "you had never met. Use the opening and closing phrases.",
                 items=["Hi, I'm… Nice to meet you. Where are you from? … It was nice talking to you."],
                 answers=["The point is fluency in the fixed phrases, not new information."],
                 level="E", kind="speaking"),
              EX("U12.4-S2", "The exchange student role play", "A is a visitor from an "
                 "English-speaking country, B is a Vietnamese student. Ten turns.",
                 items=["Checklist: □ introduction □ 3 questions each □ one follow-up question "
                        "□ one repair phrase □ one 'Have you ever…?' □ a polite ending"],
                 answers=["Assessment: task 3, fluency 2.5, pronunciation 2.5, accuracy 2."],
                 level="D", kind="speaking")],
    writing=[EX("U12.4-W1", "Introduce yourself in writing", "Write an introduction message "
                "(80–100 words) to a new pen friend.",
                items=["Name, age, where you live, family, how long you have learned English, "
                       "free time, one experience with 'I have never / I've been to', "
                       "and two questions."],
                answers=["See the model email."], level="M", kind="writing", lines=12)],
    communication={"function": "Meeting somebody new and keeping the conversation going",
                   "phrases": ["Let me introduce myself.", "Nice to meet you.",
                               "Where are you from?", "How long have you been…?",
                               "Have you ever…?", "Sorry, could you say that again, please?",
                               "It was nice talking to you.", "Let's keep in touch!"],
                   "roleplay": "Speed-meeting: three-minute conversations with three different "
                               "'visitors'.",
                   "real_life": "Meeting a foreign visitor, a tourist or a new online friend."},
    guided=[EX("U12.4-G1", "Answer + add", "Improve these one-word answers.",
               items=["1. 'Have you ever been to Hanoi?' – 'Yes.' → ",
                      "2. 'Do you like English?' – 'Yes.' → ",
                      "3. 'Where are you from?' – 'Nam Dinh.' → ",
                      "4. 'Have you ever tried foreign food?' – 'No.' → "],
               answers=["Model: 1. Yes, I have. I went last summer with my family. "
                        "2. Yes, I do — especially speaking, although I'm slow. "
                        "3. I'm from Nam Dinh, a small city about ninety kilometres south of Hanoi. "
                        "4. No, I haven't, but I'd love to try Korean food."],
               level="M", kind="speaking"),
            EX("U12.4-G2", "Repair phrases", "Match the problem with the phrase.",
               items=["1. You didn't hear.", "2. You don't know a word.",
                      "3. They spoke too fast.", "4. You want the spelling.",
                      "a. Could you speak more slowly, please?", "b. How do you spell that?",
                      "c. Sorry, could you say that again, please?",
                      "d. What does … mean?"],
               answers=["1–c", "2–d", "3–a", "4–b"], level="E", kind="mixed")],
    independent=[EX("U12.4-I1", "Complete the conversation", "Write the missing lines.",
                    items=["A: Hi, I'm Nam. ______ (greeting)",
                           "B: Nice to meet you too. Where ______ ?",
                           "A: I'm from Nam Dinh. How long ______ in Viet Nam?",
                           "B: Three weeks.", "A: ______ ever been to Asia before?",
                           "B: No, never.", "A: Sorry, ______ that again, please?",
                           "B: I said no, never. This is my first time.",
                           "A: I see! Well, it ______ talking to you. Let's ______ ."],
                    answers=["A: Nice to meet you.", "B: are you from", "A: have you been",
                             "A: Have you", "A: could you say", "A: was nice; keep in touch"],
                    level="M", kind="mixed"),
                 EX("U12.4-I2", "Speed-meeting", "Do U12.4-S2 with three different partners.",
                    items=[], answers=["See U12.4-S2."], level="D", kind="speaking")],
    review=["Opening, developing, repairing and closing a conversation",
            "ANSWER + ADD instead of one-word answers", "Repair phrases"],
    homework=[EX("U12.4-H1", "Everyday English", "Write what you say.",
                 items=["1. You meet somebody for the first time. ______",
                        "2. You did not hear what they said. ______",
                        "3. You do not know a word they used. ______",
                        "4. You want to end the conversation politely. ______"],
                 answers=["1. Hi, I'm… Nice to meet you.",
                          "2. Sorry, could you say that again, please?",
                          "3. What does … mean?",
                          "4. It was nice talking to you. Let's keep in touch!"],
                 level="M", kind="mixed"),
              EX("U12.4-H2", "Vocabulary", "Complete with introduce, pen friend, in common, "
                 "keep in touch, time zone, misunderstand.",
                 items=["1. Let me ______ myself.", "2. I have a ______ in Ireland.",
                        "3. We have a lot ______ .", "4. Let's ______ !",
                        "5. There is a six-hour ______ difference.",
                        "6. Don't worry if you ______ something."],
                 answers=["1. introduce", "2. pen friend", "3. in common", "4. keep in touch",
                          "5. time zone", "6. misunderstand"], level="E", kind="vocab"),
              EX("U12.4-H3", "Writing", "Write your introduction message (80–100 words) neatly.",
                 items=["Include one present perfect sentence and two questions."],
                 answers=["See U12.4-W1 / the model email."], level="M", kind="writing", lines=12),
              EX("U12.4-H4", "Speaking", "Practise the four repair phrases five times each, "
                 "SLOWLY and CLEARLY.",
                 items=["Sorry, could you say that again, please? / Could you speak more slowly, "
                        "please? / What does … mean? / How do you spell that?"],
                 answers=["Spot-check in Lesson 5."], level="M", kind="pron")],
    workbook=[EX("U12.4-P1", "Order the conversation", "Number the lines 1–8.",
                 items=["___ Nice to meet you too. Where are you from?",
                        "___ Hi, I'm Mai. Nice to meet you.",
                        "___ Two weeks. I've been to Hanoi and Ninh Binh.",
                        "___ From Adelaide, in the south of Australia.",
                        "___ It was nice talking to you. Let's keep in touch!",
                        "___ How long have you been in Viet Nam?",
                        "___ Have you ever been to Asia before?", "___ No, never."],
                 answers=["2, 1, 5, 3, 8, 4, 6, 7"], level="M", kind="mixed"),
              EX("U12.4-P2", "Answer + add", "Write a better answer for each question.",
                 items=["1. 'Do you like your school?' – 'Yes.' →",
                        "2. 'Have you ever been to Hanoi?' – 'No.' →",
                        "3. 'What's your hobby?' – 'Reading.' →"],
                 answers=["Model: 1. Yes, I do. The teachers are strict but the library is great. "
                          "2. No, I haven't, but my sister has and she says it's very busy. "
                          "3. My hobby is reading — mostly comics, about two a week."],
                 level="M", kind="writing"),
              EX("U12.4-P3", "Repair phrases", "Complete the phrases.",
                 items=["1. Sorry, could you ______ that again, please?",
                        "2. Could you speak more ______ , please?",
                        "3. What ______ 'landmark' mean?",
                        "4. How do you ______ that?"],
                 answers=["1. say", "2. slowly", "3. does", "4. spell"], level="E", kind="mixed"),
              EX("U12.4-P4", "Write a message", "Write an introduction message (90–100 words) to a "
                 "pen friend in an English-speaking country.",
                 items=["Include: who you are, your family, your English, one experience "
                        "(present perfect), and three questions."],
                 answers=["See the model email in the Student Book."], level="D", kind="writing",
                 lines=14)],
    procedure=[ST("Warm-up: Have you ever… chain", 5,
                  ["Each student asks the next one a 'Have you ever…?' question. "
                   "Recycles Lesson 3."],
                  "Ask and answer.", "Rows", "Slide 2"),
               ST("Presentation: conversation stages", 9,
                  ["Four stages on the board: OPEN – DEVELOP – REPAIR – CLOSE, with the phrases.",
                   "Demonstrate a bad conversation (one-word answers) and a good one. "
                   "Elicit the difference: ANSWER + ADD."],
                  "Repeat; copy the four stages.", "Whole class", "Slides 3–5"),
               ST("Listening: meeting Sarah", 10,
                  ['Play the recording “Lesson 16: Where Are You From?” twice (three times if the class asks); students do the listening tasks; students do the listening tasks; read the script in role.'],
                  "Listen, complete, read in role.", "Individual → pairs", "Slide 6"),
               ST("Guided practice", 7, ["U12.4-G1 (answer + add), G2 (repair) and I1."],
                  "Improve answers; match repair phrases; complete the dialogue.", "Pairs",
                  "Student Book p. U12L4"),
               ST("Speed-meeting", 11,
                  ["Two rows facing each other; three minutes per pair, then rotate. Three rounds.",
                   "Each student must use one repair phrase and one 'Have you ever…?' each round."],
                  "Meet three 'visitors'.", "Pairs (rotating)", "Slides 7–9"),
               ST("Wrap-up and homework", 3, ["Ask: 'What did you learn about a classmate?' "
                                              "Set H1–H4."],
                  "Report; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("ANSWER + ADD",
                     ["Here is the single most useful conversation rule in English.",
                      "Somebody asks: 'Do you like football?' If you say 'Yes' and stop, "
                      "the conversation dies. The other person must find a new question. "
                      "That is hard work for them.",
                      "So: ANSWER, then ADD one sentence. 'Yes, I do. I play every Sunday with my "
                      "cousins.'",
                      "Now they have something to ask about. Answer plus add. Every time."]),
                  TK("Repair phrases are strength, not weakness",
                     ["When you don't understand, many students smile and nod. Then they understand "
                      "nothing for ten minutes.",
                      "Saying 'Sorry, could you say that again, please?' is not weak. It is what "
                      "confident speakers do — in every language.",
                      "And say it SLOWLY and CLEARLY. If you mumble it, they will repeat it just as "
                      "fast.",
                      "Everybody, loudly: Sorry, could you say that again, please?"])],
    support=["Give the four-stage phrase card.",
             "Allow weaker students to read the phrases in round one of the speed-meeting.",
             "Provide three ready-made questions."],
    challenge=["Ask them to play the visitor and invent a life abroad.",
               "Ask for three follow-up questions in every conversation.",
               "Ask for a 120-word introduction message."],
    assessment=["Uses ANSWER + ADD in at least three answers",
                "Uses one repair phrase clearly", "Opens and closes the conversation politely"],
    board_plan=["LEFT: OPEN – DEVELOP – REPAIR – CLOSE", "CENTRE: ANSWER + ADD (bad vs good example)",
                "RIGHT: four repair phrases; Homework H1–H4"],
    materials=["Phrase cards", 'Recording: Lesson 16: Where Are You From? — VOA Learning English — Let’s Learn English, Level 1 (3:26)'],
)

L5 = Lesson(
    code="U12L5", unit=12, number=5, period=90,
    lesson_type="Skills 1", title="Reading: English around the world + Speaking: Present a country",
    objectives=["read a 240-word article and answer gist, detail and inference questions",
                "guess new words from context",
                "present a country for 90 seconds using a fact-file plan",
                "answer two questions about their country"],
    recycled=["U12L1–L4: countries, landmarks, superlatives, present perfect; "
              "Unit 9 presenting; Unit 10 opinions"],
    vocab=[V("native speaker", "n", "/ˈneɪtɪv ˈspiːkə/", "người bản ngữ", "Most English speakers are not native speakers."),
           V("accent", "n", "/ˈæksent/", "giọng, khẩu âm", "Everybody has an accent."),
           V("communicate", "v", "/kəˈmjuːnɪkeɪt/", "giao tiếp", "The aim is to communicate, not to be perfect."),
           V("global", "adj", "/ˈɡləʊbl/", "toàn cầu", "English has become a global language."),
           V("useful", "adj", "/ˈjuːsfl/", "hữu ích", "English is useful for many jobs."),
           V("confident", "adj", "/ˈkɒnfɪdənt/", "tự tin", "Be confident, even when you make mistakes.")],
    phrases=["a global language", "a native speaker", "make yourself understood",
             "It doesn't matter if…", "the aim is to…"],
    grammar=G("Presenting a country: fact file language",
              use=["Facts with numbers: The population is about… / It covers … square kilometres.",
                   "Superlatives (Unit 4 and 12L2): It is the … in the world.",
                   "Present perfect for your own experience: I have never been there, but I have "
                   "read that…",
                   "Opinion at the end: What interests me most is… / I would like to visit it "
                   "because…"],
              form=[["Part", "Language", "Example"],
                    ["basic facts", "The capital is… The population is…", "The capital is Ottawa."],
                    ["superlative", "It is the …-est / most … in the world",
                     "It is the second largest country in the world."],
                    ["experience", "I have never been… but I have…",
                     "I have never been there, but I have watched many videos."],
                    ["opinion", "What interests me most is…",
                     "What interests me most is that it has two official languages."]],
              examples=["New Zealand has about five million people — fewer than Hanoi.",
                        "I have never been abroad, but I have read that the south island is the "
                        "most beautiful part."],
              pitfall="A list of facts with no opinion is boring. Every presentation needs one "
                      "sentence beginning 'What interests me most is…'."),
    pron=P("Confident presenting: volume, pace and clusters",
           "Three rules for the end of the year: speak louder than feels natural, slower than feels "
           "natural, and finish every word. Watch the clusters: fir-st, mo-st, la-st, world.",
           items=["first, most, last, world", "'accent (Oo)", "co'mmunicate (oOoo)",
                  "'confident (Ooo)"],
           drill=["The most important thing is to communicate, not to be perfect.",
                  "First, the facts. Second, the reason. Last, my opinion."],
           vn_note="After a year of work, the two habits that matter most are: finish your words, "
                   "and slow down. Both are choices, not abilities."),
    listening=AUDIO['U12L5'],
    reading=T("Whose language is English?",
              ["About one and a half billion people speak English. Only about four hundred million "
               "of them learned it as their first language. In other words, for every native "
               "speaker there are roughly three people who learned English at school — like you.",
               "This changes something important. When a Vietnamese engineer talks to a Japanese "
               "engineer, or a Brazilian doctor talks to a German nurse, they use English — and "
               "there is no native speaker in the room at all. Their English does not have to sound "
               "British or American. It has to WORK.",
               "Researchers who study these conversations have found something surprising: "
               "conversations between two non-native speakers often break down LESS often than "
               "conversations that include a native speaker. Learners speak more slowly, repeat more, "
               "check more and use simpler words. Native speakers use idioms and jokes that nobody "
               "else understands.",
               "None of this means that accuracy does not matter. Grammar and pronunciation help "
               "people understand you, and a clear final consonant can be the difference between "
               "'I can' and 'I can't'.",
               "But it does mean this: your English does not have to be perfect to be useful. "
               "It has to be clear. And the person you will speak it with is probably somebody who, "
               "like you, learned it in a classroom."],
              tasks=[EX("U12.5-R1", "Gist", "Choose the best title.",
                        items=["A. How to speak like a native speaker",
                               "B. English belongs to everybody who uses it",
                               "C. The history of the English language"],
                        answers=["B"], level="E", kind="reading"),
                     EX("U12.5-R2", "Detail", "Answer the questions.",
                        items=["1. How many people speak English, and how many are native speakers?",
                               "2. Give two examples from the text of English being used with no "
                               "native speaker present.",
                               "3. What surprising thing have researchers found?",
                               "4. Why do learner-to-learner conversations work well? (four reasons)",
                               "5. Does the writer say accuracy is unimportant? Explain."],
                        answers=["1. About 1.5 billion; about 400 million native speakers.",
                                 "2. A Vietnamese engineer talking to a Japanese engineer; "
                                 "a Brazilian doctor talking to a German nurse.",
                                 "3. Conversations between two non-native speakers break down less "
                                 "often than ones including a native speaker.",
                                 "4. Learners speak more slowly, repeat more, check more and use "
                                 "simpler words.",
                                 "5. No — grammar and pronunciation help people understand you, and "
                                 "a clear final consonant can change the meaning ('I can' / "
                                 "'I can't')."], level="M", kind="reading"),
                     EX("U12.5-R3", "Vocabulary from context", "Find a word or phrase that means:",
                        items=["1. somebody who learned a language as a baby (paragraph 1)",
                               "2. stops working / fails (paragraph 3)",
                               "3. expressions whose meaning you cannot guess (paragraph 3)",
                               "4. easy to understand (paragraph 5)"],
                        answers=["1. native speaker", "2. break(s) down", "3. idioms", "4. clear"],
                        level="M", kind="reading"),
                     EX("U12.5-R4", "Inference", "Answer with your own ideas.",
                        items=["1. Why does the writer mention 'I can' and 'I can't'?",
                               "2. Does this article make you feel more or less confident? Why?",
                               "3. Do you agree that English 'belongs to everybody who uses it'?"],
                        answers=["1. To show that pronunciation still matters: one missing consonant "
                                 "reverses the meaning.",
                                 "2. Students' own answer with a reason.",
                                 "3. Students' own answer with a reason."], level="D", kind="reading")]),
    speaking=[EX("U12.5-S1", "Prepare your presentation", "Make notes for a 90-second presentation "
                 "of an English-speaking country.",
                 items=["1. Basic facts (capital, population, languages) ______",
                        "2. One famous place with a number ______",
                        "3. One food or custom ______",
                        "4. My own experience (present perfect) ______",
                        "5. What interests me most and why ______"],
                 answers=["Notes only. Part 5 is compulsory."], level="M", kind="speaking"),
              EX("U12.5-S2", "Present your country", "Speak for 90 seconds in a group of four. "
                 "Listeners ask two questions each.",
                 items=["Useful language: 'The capital is…', 'It is the …-est in the world', "
                        "'I have never been there, but I have…', 'What interests me most is…'"],
                 answers=["Assessment: content 3, language 3, delivery 2, answering questions 2."],
                 level="D", kind="speaking")],
    writing=[EX("U12.5-W1", "Notes to sentences", "Turn your five notes into six sentences.",
                items=[], answers=["See the model presentation about Canada in the listening."],
                level="M", kind="writing", lines=8)],
    communication={"function": "Speaking with confidence",
                   "phrases": ["Let me start with…", "The most surprising thing is…",
                               "As I said,…", "To finish,…", "Are there any questions?"],
                   "roleplay": "After each presentation, two listeners ask a question; "
                               "the presenter must answer without notes.",
                   "real_life": "Presenting information clearly and answering questions."},
    guided=[EX("U12.5-G1", "True or false", "Read the text again and write T or F.",
               items=["1. Most English speakers learned it as their first language.",
                      "2. Learner-to-learner conversations break down more often.",
                      "3. Native speakers sometimes use idioms nobody understands.",
                      "4. The writer says grammar does not matter.",
                      "5. A clear final consonant can change the meaning."],
               answers=["1. F – only about a quarter did.", "2. F – LESS often.", "3. T",
                        "4. F – it helps people understand you.", "5. T"],
               level="E", kind="reading"),
            EX("U12.5-G2", "Presentation language", "Complete the sentences.",
               items=["1. The ______ of Canada is Ottawa.",
                      "2. It is the second ______ country in the world.",
                      "3. I have ______ been there, but I have watched a documentary.",
                      "4. What ______ me most is the two languages.",
                      "5. Thank you ______ listening."],
               answers=["1. capital", "2. largest", "3. never", "4. interests", "5. for"],
               level="M", kind="writing")],
    independent=[EX("U12.5-I1", "Retell", "Close the book. Tell your partner the main idea of the "
                    "article in four sentences.", items=[],
                    answers=["Model: About 1.5 billion people speak English, but only 400 million "
                             "learned it as a first language. Most English conversations in the "
                             "world happen between two learners. Researchers found that these "
                             "conversations work well because learners speak slowly and check more. "
                             "So English does not have to be perfect — it has to be clear."],
                    level="M", kind="speaking"),
                 EX("U12.5-I2", "Your presentation", "Do U12.5-S2 in your group.", items=[],
                    answers=["See U12.5-S2."], level="D", kind="speaking")],
    review=["Reading: gist → detail → inference", "Country presentation in five parts",
            "Present perfect for your own experience"],
    homework=[EX("U12.5-H1", "Reading", "Answer in full sentences.",
                 items=["1. For every native speaker, how many learners of English are there?",
                        "2. Why do native speakers sometimes make conversations harder?",
                        "3. What four things do learners do that help communication?",
                        "4. What is the writer's main message?"],
                 answers=["1. About three.",
                          "2. Because they use idioms and jokes that nobody else understands.",
                          "3. They speak more slowly, repeat more, check more and use simpler words.",
                          "4. That your English does not have to be perfect to be useful — "
                          "it has to be clear."], level="M", kind="reading"),
              EX("U12.5-H2", "Vocabulary", "Complete with native speaker, accent, communicate, "
                 "global, confident.",
                 items=["1. English has become a ______ language.",
                        "2. Everybody has an ______ , including native speakers.",
                        "3. The aim is to ______ , not to be perfect.",
                        "4. A ______ learned the language as a baby.",
                        "5. Be ______ , even when you make mistakes."],
                 answers=["1. global", "2. accent", "3. communicate", "4. native speaker",
                          "5. confident"], level="E", kind="vocab"),
              EX("U12.5-H3", "Writing", "Write your country presentation as a paragraph "
                 "(110–120 words).",
                 items=["Five parts; two superlatives; one present perfect sentence."],
                 answers=["See the Canada model."], level="D", kind="writing", lines=16),
              EX("U12.5-H4", "Speaking", "Practise your 90-second presentation three times. "
                 "Louder and slower than feels natural.",
                 items=[], answers=["Presentations in Lesson 6."], level="M", kind="speaking")],
    workbook=[EX("U12.5-P1", "Vocabulary match", "Match the word with the meaning.",
                 items=["1. native speaker", "2. accent", "3. communicate", "4. global",
                        "5. confident",
                        "a. sure of yourself", "b. all over the world",
                        "c. the way somebody's speech sounds", "d. to share information successfully",
                        "e. somebody who learned the language as a baby"],
                 answers=["1–e", "2–c", "3–d", "4–b", "5–a"], level="E", kind="vocab"),
              EX("U12.5-P2", "Reading", "Read and answer.",
                 text=["In Singapore, most students learn English at school from the age of six, "
                       "alongside Mandarin, Malay or Tamil. Many people there speak a local variety "
                       "called Singlish at home and standard English at work. Some officials have "
                       "campaigned against Singlish, saying it makes people harder to understand "
                       "abroad. Others answer that every country has an informal variety, and that "
                       "being able to switch between two kinds of English is a skill, not a problem."],
                 items=["1. From what age do students learn English in Singapore?",
                        "2. What is Singlish?", "3. Why do some officials campaign against it?",
                        "4. What is the counter-argument?"],
                 answers=["1. From the age of six.",
                          "2. A local variety of English spoken at home.",
                          "3. Because they say it makes people harder to understand abroad.",
                          "4. That every country has an informal variety, and switching between two "
                          "kinds of English is a skill, not a problem."], level="M", kind="reading"),
              EX("U12.5-P3", "Presentation sentences", "Write one sentence of each type about a "
                 "country you choose.",
                 items=["1. a fact with a number", "2. a superlative", "3. a present perfect "
                        "experience", "4. an opinion beginning 'What interests me most is…'"],
                 answers=["Model: 1. Australia has about 26 million people. 2. It is the driest "
                          "inhabited continent in the world. 3. I have never been there, but I have "
                          "watched three documentaries about it. 4. What interests me most is that "
                          "80% of its animals live nowhere else."],
                 level="M", kind="writing"),
              EX("U12.5-P4", "Writing", "Write a presentation (110–120 words) about an "
                 "English-speaking country.",
                 items=["Five parts; two superlatives; one present perfect."],
                 answers=["See the Canada model in the listening script."],
                 level="D", kind="writing", lines=16)],
    procedure=[ST("Warm-up: Have you ever… (countries)", 5,
                  ["Students ask each other 'Have you ever…?' questions about foreign things. "
                   "Recycles Lesson 3."],
                  "Ask and answer.", "Rows", "Slide 2"),
               ST("Pre-reading", 6,
                  ["Write two numbers on the board: 1,500,000,000 and 400,000,000. Ask what they "
                   "could be. Predict.",
                   "Pre-teach: native speaker, break down, idiom, clear. Set the gist task."],
                  "Predict; skim for the title.", "Whole class", "Slides 3–4"),
               ST("While-reading", 13,
                  ["R2 detail individually, pair-check; R3 words in context; R4 inference in pairs.",
                   "Take a class vote on question 2 of R4 and hear three reasons."],
                  "Read, answer, discuss.", "Individual → pairs", "Slides 5–7"),
               ST("Post-reading: retell", 4, ["Books closed; the main idea in four sentences."],
                  "Retell.", "Pairs", "Slide 8"),
               ST("Speaking: country presentation", 13,
                  ["Play the Canada model; students find the five parts.",
                   "4 minutes to plan; 90-second presentations in groups of four; two questions each."],
                  "Listen, plan, present, question.", "Individual → groups of 4", "Slides 9–11"),
               ST("Wrap-up and homework", 4, ["Best presentation to the class. Set H1–H4."],
                  "Listen; note homework.", "Whole class", "Slide 12")],
    teacher_talk=[TK("The most important text of the year",
                     ["I have chosen this text for the last unit on purpose.",
                      "For a whole year some of you have been quiet in this room because you were "
                      "afraid of making mistakes in front of a 'perfect' English.",
                      "This text says: that perfect English is not who you will talk to. "
                      "You will talk to another learner — in Bangkok, in Seoul, in an email, at "
                      "university.",
                      "Your job is not to sound British. Your job is to be CLEAR. "
                      "Finish your words, slow down, and say something."]),
                  TK("Presenting with confidence",
                     ["Three rules for your presentation, and none of them is about grammar.",
                      "One: stand up straight and look at three friendly faces.",
                      "Two: speak louder than feels natural. In your head it will sound like "
                      "shouting; in the room it will sound normal.",
                      "Three: slow down. Ninety seconds is longer than you think. "
                      "A slow, clear presentation with five mistakes beats a fast, perfect one that "
                      "nobody hears."])],
    support=["Gloss four words in the margin.", "Give the five-part plan with sentence starters.",
             "Let weaker students present to one partner first."],
    challenge=["Ask for two superlatives and one comparison with Viet Nam.",
               "Ask them to answer three questions without notes.",
               "Ask for a written opinion on the reading (80 words)."],
    assessment=["4 of 5 detail answers", "Presentation covers all five parts",
                "Speaks audibly for about 90 seconds"],
    board_plan=["LEFT: 1.5 billion / 400 million", "CENTRE: presentation plan 1–5",
                "RIGHT: clear, not perfect; Homework H1–H4"],
    materials=["Reading text", "Recording: What is your country's geography like? — ELLLO — One Minute English (1:03)", "Timer"],
)

L6 = Lesson(
    code="U12L6", unit=12, number=6, period=91,
    lesson_type="Skills 2", title="Listening: A student abroad + Writing: An email to a pen friend",
    objectives=["listen to an interview and complete notes",
                "organise an informal email in four paragraphs",
                "write an email of 120–140 words to a pen friend",
                "check a partner's work with a checklist"],
    recycled=["U12L1–L5: countries, present perfect, presenting; Units 2 and 6 email layout"],
    vocab=[V("host family", "n", "/həʊst ˈfæməli/", "gia đình bản xứ đón tiếp", "She stayed with a host family."),
           V("homesick", "adj", "/ˈhəʊmsɪk/", "nhớ nhà", "I was homesick for the first week."),
           V("get used to", "v phr", "/ɡet ˈjuːst tuː/", "quen với", "It took a month to get used to the food."),
           V("similar", "adj", "/ˈsɪmələ/", "giống nhau", "Teenagers are similar everywhere."),
           V("polite", "adj", "/pəˈlaɪt/", "lịch sự", "People are very polite, but quite formal."),
           V("miss", "v", "/mɪs/", "nhớ", "I miss my grandmother's cooking.")],
    phrases=["stay with a host family", "get used to…", "at first… but now…",
             "What I miss most is…", "the biggest difference is…"],
    grammar=G("Informal email: four paragraphs (final writing lesson)",
              use=["1. OPENING: thanks + a question back. Hi…! Thanks for your email. "
                   "How are you?",
                   "2. NEWS: what you have done recently (present perfect + past simple).",
                   "3. THE MAIN TOPIC: answer their question in detail.",
                   "4. CLOSING: two questions + a friendly ending.",
                   "This is the same shape as Unit 2's email of advice and Unit 6's school email — "
                   "you now know it well."],
              form=[["Part", "Language", "Example"],
                    ["opening", "Thanks for your email…", "Hi Emma! Thanks for your last email."],
                    ["news", "present perfect + past simple",
                     "I've finished my exams. We had the English one on Monday."],
                    ["main topic", "detail + examples", "You asked about Tet, so here it is."],
                    ["closing", "two questions + ending", "What about you? Write soon! Mai"]],
              examples=["I've been studying English for four years, and this year I finally spoke "
                        "to a foreigner.",
                        "What I miss most when I stay at my aunt's house is my own bed."],
              pitfall="Students write four paragraphs of facts and forget to ask anything. "
                      "An email without a question is a report."),
    pron=P("End-of-year pronunciation check",
           "Read your email aloud and check the five things we have worked on all year: "
           "final consonants, -s endings, -ed endings, word stress, and sentence stress.",
           items=["final: first, most, island, world", "-s: likes, plays, watches",
                  "-ed: helped, cleaned, visited", "stress: edu'CA-tion, 'COM-for-table",
                  "sentence: I've NEVER been aBROAD."],
           drill=["I've visited three provinces and I've watched hundreds of English videos, "
                  "but I've never been abroad."],
           vn_note="This is the final checklist of the year. Students who can self-check these five "
                   "points can continue improving without a teacher."),
    listening=AUDIO['U12L6'],
    reading=T("Model email",
              ["Hi Emma,",
               "Thanks for your last email — sorry I've been slow. We've just finished our end-of-year "
               "exams and my brain is empty!",
               "Some news first. I've finished Grade 7, and my English mark was the best of the year. "
               "In March our class did a project about English-speaking countries and my group "
               "presented Canada. I've also started a small pen-friend club at school: nine students "
               "have joined so far.",
               "You asked what Tet is like. It's difficult to explain in a short email. "
               "For three days the streets of my city are almost empty, because everybody goes home "
               "to their family. We clean the whole house before, we cook banh chung, and on the "
               "first morning children get lucky money in red envelopes. What I love most is the "
               "silence: for one week Viet Nam is quiet, and it happens only once a year.",
               "Now your turn. What is Christmas like in your family? And have you ever tried "
               "Vietnamese food? If you come here one day, my mother will cook for a week — "
               "I'm warning you now.",
               "Write soon!",
               "Mai (168 words — yours can be shorter!)"],
              tasks=[EX("U12.6-R1", "Analyse the model", "Answer the questions.",
                        items=["1. What is in each of the four paragraphs?",
                               "2. Find two present perfect sentences and one past simple sentence.",
                               "3. Which sentence gives Mai's personal feeling about Tet?",
                               "4. How many questions does she ask at the end?",
                               "5. Why is the last line before 'Write soon' effective?"],
                        answers=["1. Opening/apology; news; the main topic (Tet); questions and "
                                 "closing.",
                                 "2. Present perfect: 'I've finished Grade 7', 'I've also started a "
                                 "small pen-friend club', 'nine students have joined'. "
                                 "Past simple: 'our class did a project… and my group presented "
                                 "Canada'.",
                                 "3. 'What I love most is the silence…'",
                                 "4. Two.",
                                 "5. It is warm and funny, and it invites the friend to visit."],
                        level="M", kind="reading")]),
    speaking=[EX("U12.6-S1", "Say your email", "Tell your partner the four paragraphs of your email "
                 "before you write.",
                 items=["Opening → news → main topic → questions."],
                 answers=["Speaking first improves the writing — for the last time this year!"],
                 level="M", kind="speaking")],
    writing=[EX("U12.6-W1", "Plan your email", "Complete the plan.",
                items=["1. Opening (thanks + how are you): ______",
                       "2. News: two things you have done this year (present perfect) "
                       "+ one detail (past simple): ______",
                       "3. Main topic: a Vietnamese festival, food or custom, with a personal "
                       "feeling: ______",
                       "4. Two questions + closing: ______"],
                answers=["Check every plan before students write."], level="M", kind="writing",
                lines=8),
             EX("U12.6-W2", "Write your email", "Write 120–140 words to a pen friend in an "
                "English-speaking country.",
                items=["Four paragraphs; at least two present perfect sentences; one personal "
                       "feeling; two questions."],
                answers=["See the model email. Marking: content 3, organisation 2, tenses 3, "
                         "vocabulary 1, length 1."],
                level="D", kind="writing", lines=18),
             EX("U12.6-W3", "Peer check", "Swap and tick the checklist.",
                items=["□ greeting and closing", "□ four paragraphs",
                       "□ at least two present perfect sentences",
                       "□ one past simple sentence with a time word",
                       "□ one personal feeling ('What I love most is…')",
                       "□ two questions at the end", "□ 120–140 words"],
                answers=["Write one thing you liked and one to improve. This is the last peer check "
                         "of the year — make it a good one."], level="M", kind="writing")],
    communication={"function": "Explaining your culture warmly",
                   "phrases": ["It's difficult to explain, but…", "What I love most is…",
                               "You'd have to see it.", "If you come here one day,…",
                               "I'm warning you now!"],
                   "roleplay": "Explain one Vietnamese custom to a partner playing a foreign friend, "
                               "in one minute, including one personal feeling.",
                   "real_life": "Writing to a friend abroad and explaining your life."},
    guided=[EX("U12.6-G1", "Which paragraph?", "Write 1, 2, 3 or 4.",
               items=["1. Thanks for your last email. ___", "2. I've finished Grade 7. ___",
                      "3. What I love most is the silence. ___",
                      "4. Have you ever tried Vietnamese food? ___",
                      "5. In March our class did a project. ___"],
               answers=["1. P1", "2. P2", "3. P3", "4. P4", "5. P2"], level="E", kind="writing"),
            EX("U12.6-G2", "Present perfect or past simple?", "Complete the email extract.",
               items=["1. I ______ (finish) Grade 7 last week.",
                      "2. I ______ (never / be) abroad.",
                      "3. In March our class ______ (do) a project about Canada.",
                      "4. Nine students ______ (join) the club so far.",
                      "5. We ______ (have) our English exam on Monday."],
               answers=["1. finished", "2. have never been", "3. did", "4. have joined", "5. had"],
               level="D", kind="grammar")],
    independent=[EX("U12.6-I1", "Write your email", "Do U12.6-W1 and W2.", items=[],
                    answers=["See the model email."], level="D", kind="writing", lines=18),
                 EX("U12.6-I2", "Read it aloud", "Read your email aloud to your partner and check "
                    "the five pronunciation points of the year.",
                    items=["Final consonants · -s · -ed · word stress · sentence stress"],
                    answers=["This is the end-of-year self-check."], level="M", kind="speaking")],
    review=["Interview listening with attitudes", "Four-paragraph informal email",
            "Present perfect for news, past simple for details",
            "The five pronunciation points of the year"],
    homework=[EX("U12.6-H1", "Listening / vocabulary", "Complete from the interview.",
                 items=["1. Trang spent ______ months in ______ .",
                        "2. The first ______ weeks were terrible.",
                        "3. She learned to say: 'Sorry, could you ______ that again more "
                        "______ ?'",
                        "4. She missed food and ______ .",
                        "5. Her advice: learn the ______ before you go."],
                 answers=["1. three; Adelaide", "2. two", "3. say; slowly", "4. noise",
                          "5. repair phrases"], level="E", kind="listening"),
              EX("U12.6-H2", "Vocabulary", "Complete with host family, homesick, get used to, "
                 "similar, polite, miss.",
                 items=["1. She stayed with a ______ .", "2. I was ______ for the first week.",
                        "3. It took a month to ______ the food.",
                        "4. Teenagers are ______ everywhere.",
                        "5. People there are very ______ but quite formal.",
                        "6. I ______ my grandmother's cooking."],
                 answers=["1. host family", "2. homesick", "3. get used to", "4. similar",
                          "5. polite", "6. miss"], level="E", kind="vocab"),
              EX("U12.6-H3", "Writing", "Rewrite your email neatly after correction. This is your "
                 "final piece of writing for the year — make it your best.",
                 items=["Use the 7-point checklist."],
                 answers=["Marking: content 3, organisation 2, tenses 3, vocabulary 1, length 1."],
                 level="D", kind="writing", lines=18),
              EX("U12.6-H4", "Speaking", "Read your email aloud twice and check the five "
                 "pronunciation points.",
                 items=["Final consonants · -s · -ed · word stress · sentence stress"],
                 answers=["Spot-check in Lesson 7."], level="M", kind="pron")],
    workbook=[EX("U12.6-P1", "Email parts", "Write O (opening), N (news), T (topic) or "
                 "C (closing).",
                 items=["1. Thanks for your email. ___", "2. I've finished my exams. ___",
                        "3. You asked about Tet, so here it is. ___",
                        "4. What is Christmas like in your family? ___",
                        "5. Write soon! ___"],
                 answers=["1. O", "2. N", "3. T", "4. C", "5. C"], level="E", kind="writing"),
              EX("U12.6-P2", "Complete the email", "Use the words in the box.",
                 wordbank=["Thanks", "have", "did", "What", "soon"],
                 items=["Hi Sam, (1) ______ for your email. I (2) ______ just finished Grade 7. "
                        "In April our class (3) ______ a project about Australia. "
                        "(4) ______ I love most about our school year was the film club. "
                        "Write (5) ______ ! Nam"],
                 answers=["1. Thanks", "2. have", "3. did", "4. What", "5. soon"],
                 level="E", kind="writing"),
              EX("U12.6-P3", "Correct the email", "Find and correct five mistakes.",
                 text=["Hi Emma. Thanks for you email. I have finished Grade 7 last week. "
                       "I have never been abroad but I have talk to three foreigners. "
                       "What I love most are Tet. Write soon."],
                 items=["Write the five corrections."],
                 answers=["1. 'you email' → 'your email'",
                          "2. 'I have finished Grade 7 last week' → 'I finished Grade 7 last week'",
                          "3. 'I have talk' → 'I have talked'",
                          "4. 'What I love most are Tet' → 'What I love most is Tet'",
                          "5. 'Hi Emma.' → 'Hi Emma,' (comma after the greeting)"],
                 level="D", kind="grammar"),
              EX("U12.6-P4", "Writing", "Write an email (120–140 words) to a pen friend explaining "
                 "one Vietnamese custom.",
                 items=["Four paragraphs; two present perfect sentences; one personal feeling; "
                        "two questions."],
                 answers=["See the model email."], level="D", kind="writing", lines=18)],
    procedure=[ST("Warm-up: Have you ever… (final round)", 5,
                  ["Quick mingle: three 'Have you ever…?' questions about this school year."],
                  "Ask and answer.", "Mingle", "Slide 2"),
               ST("Pre-listening", 5,
                  ["Ask: 'What would be hardest about studying in another country?' Collect ideas.",
                   "Pre-teach: host family, homesick, get used to, direct."],
                  "Predict; copy the notes frame.", "Whole class", "Slides 3–4"),
               ST("Listening", 11,
                  ['Play the recording “Where does your family live?” twice (three times if the class asks); students do the listening tasks; students do the listening tasks.',
                   "Discuss: 'Do you agree with her advice?'"],
                  "Listen and complete the notes.", "Individual → pairs", "Slide 5"),
               ST("Writing: analyse the model email", 8,
                  ["Model email on the slide; colour the four paragraphs; find the tenses and the "
                   "personal feeling. Do U12.6-G1 and G2."],
                  "Identify the parts and the tenses.", "Whole class → pairs", "Slides 6–7"),
               ST("Writing: plan, say, draft", 12,
                  ["Plan (check every plan); say it aloud; write 120–140 words."],
                  "Plan, say, write.", "Individual → pairs → individual", "Slide 8"),
               ST("Peer check and wrap-up", 4, ["Checklist swap; read one good email aloud. "
                                                "Set H1–H4."],
                  "Peer-check.", "Pairs", "Slides 9–10")],
    teacher_talk=[TK("Trang's real lesson",
                     ["Listen to what actually helped Trang. It was not more grammar.",
                      "One: she stopped trying to understand every word. Two: she learned to say "
                      "'Could you say that again more slowly?'",
                      "Both are STRATEGIES, not knowledge. And both are things you can decide to do "
                      "tomorrow.",
                      "That is my last message of this unit: the students who improve most next year "
                      "will not be the ones who know most. They will be the ones who ask."]),
                  TK("Your last email of Grade 7",
                     ["This is the final piece of writing you will do this year, so make it a real "
                      "one.",
                      "Look back at your first email in Unit 2 — the advice email. Compare the two.",
                      "Longer? Better organised? More tenses? More YOU in it?",
                      "That difference is what a year of work looks like. Keep both pieces in your "
                      "folder."])],
    support=["Give the notes frame with four answers filled in.",
             "Provide an email frame with the four paragraph openers.",
             "Allow 90–110 words."],
    challenge=["Ask for 150–160 words with three present perfect sentences.",
               "Ask them to write the pen friend's reply as well.",
               "Ask them to compare this email with their Unit 2 email in three sentences."],
    assessment=["8 of 12 items in the listening notes",
                "Email has four paragraphs and correct tense use",
                "Two questions at the end"],
    board_plan=["LEFT: listening notes frame", "CENTRE: four-paragraph email plan",
                "RIGHT: present perfect (news) | past simple (when); Homework H1–H4"],
    materials=['Recording: Where does your family live? — ELLLO — One Minute English (1:03)', "Model email slide", "Students' Unit 2 emails if kept"],
)

L7 = Lesson(
    code="U12L7", unit=12, number=7, period=92,
    lesson_type="Looking Back & Project", title="Unit 12 review and the Country Corner showcase",
    objectives=["recall the vocabulary of Unit 12",
                "use the present perfect and superlatives accurately",
                "correct the six typical mistakes of the unit",
                "host a country corner and answer visitors' questions"],
    recycled=["ALL of Unit 12 + the whole year"],
    vocab=[V("showcase", "n", "/ˈʃəʊkeɪs/", "buổi trưng bày", "Our end-of-year showcase is on Friday."),
           V("host", "v", "/həʊst/", "làm chủ nhà, tiếp đón", "Each group hosts a corner."),
           V("achievement", "n", "/əˈtʃiːvmənt/", "thành tựu", "Look at what you have achieved this year.")],
    phrases=["Welcome to our corner.", "Have you ever…?", "Would you like to try our quiz?",
             "Thank you for visiting."],
    grammar=G("Unit 12 grammar in one page",
              use=["have/has + past participle for experiences (ever, never, been to)",
                   "With a past time word → past simple",
                   "Superlatives: the -est / the most … IN the world",
                   "one of the most … + plural noun",
                   "the UK / the USA take 'the'; most countries do not"],
              form=[["Structure", "Example", "Common mistake"],
                    ["present perfect", "I have never been abroad.", "*I have never not been."],
                    ["with a time word", "I went to Hue last year.", "*I have been to Hue last year."],
                    ["ever in questions", "Have you ever eaten sushi?", "*Did you ever eaten sushi?"],
                    ["superlative + in", "the largest country in the world",
                     "*the largest of the world"],
                    ["one of the… + plural", "one of the most famous places",
                     "*one of the most famous place"],
                    ["nationality capital", "She is Vietnamese.", "*She is vietnamese."]],
              examples=["I have never been to Australia, but I went to Laos in 2023. "
                        "Ha Long Bay is one of the most beautiful places in the world."],
              pitfall="Add these six to the classroom wall list — the last six of the year."),
    pron=P("End-of-year pronunciation review",
           "The five things we have worked on all year: final consonants, -s endings, -ed endings, "
           "word stress, sentence stress. Check all five in your presentation today.",
           items=["final: first, most, island, world", "-s: likes, plays, watches",
                  "-ed: helped, cleaned, visited", "stress: edu'CA-tion, 'COM-for-table",
                  "sentence: I've NEVER been aBROAD."],
           drill=["I've visited three provinces, watched hundreds of videos and helped two tourists, "
                  "but I've never been abroad."],
           vn_note="Give every student a written copy of the five checks to keep for Grade 8."),
    listening=AUDIO['U12L7'],
    reading=T("What one year of English looks like",
              ["At the start of Grade 7, a teacher in Hai Duong asked her class to write for ten "
               "minutes about their summer. The average length was 41 words, and eleven students "
               "wrote nothing at all.",
               "In May, she gave exactly the same task. The average was 118 words. Nobody wrote "
               "nothing.",
               "She kept both pieces of paper for every student and gave them back on the last day, "
               "stapled together.",
               "'Some of them didn't believe it was their own writing,' she said. 'One boy read his "
               "September paper and laughed. Then he read it again and went quiet.'",
               "The class had not become fluent. Many still made the same mistakes with -ed endings "
               "and articles. But the difference between 41 words and 118 words is not a small "
               "thing: it is the difference between a student who cannot start and a student who can.",
               "'I tell them every year,' the teacher said. 'You will not remember the grammar tests. "
               "You will remember the first time somebody from another country understood you.'"],
              tasks=[EX("U12.7-R1", "Read and answer", "Answer the questions.",
                        items=["1. What was the task, and what was the average in September?",
                               "2. What was the average in May?",
                               "3. What did the teacher do with the two pieces of paper?",
                               "4. Did the class become fluent? What does the writer say instead?",
                               "5. What does the teacher say students will remember?"],
                        answers=["1. To write for ten minutes about their summer; the average was "
                                 "41 words (and eleven wrote nothing).",
                                 "2. 118 words, and nobody wrote nothing.",
                                 "3. She kept both and gave them back stapled together on the last "
                                 "day.",
                                 "4. No — many still made the same mistakes, but the difference is "
                                 "between a student who cannot start and one who can.",
                                 "5. Not the grammar tests, but the first time somebody from another "
                                 "country understood them."], level="M", kind="reading")]),
    speaking=[EX("U12.7-S1", "Host your country corner", "Host your corner for five minutes, "
                 "then visit two others.",
                 items=["Frame: 'Welcome to our corner. This is… The capital is… It is the …-est… "
                        "Have you ever…? Would you like to try our quiz? Thank you for visiting.'"],
                 answers=["Marking: content 3, language 3, poster 2, hosting 2."],
                 level="D", kind="speaking")],
    writing=[EX("U12.7-W1", "Corner text and quiz", "Write your eight fact-file sentences and five "
                "quiz questions with answers.",
                items=["Include two superlatives and one present perfect sentence.",
                       "Quiz questions must have clear, checkable answers."],
                answers=["Model: Canada is the second largest country in the world. Its capital is "
                         "Ottawa, not Toronto. It has two official languages, English and French. "
                         "About forty million people live there — fewer than in Viet Nam. "
                         "Niagara Falls is one of the most visited waterfalls in the world. "
                         "Canada is famous for ice hockey and maple syrup. Nobody in our group has "
                         "ever been to Canada. What interests us most is the two languages.",
                         "Quiz: 1. What is the capital of Canada? (Ottawa) 2. How many official "
                         "languages? (Two)"],
                level="M", kind="writing", lines=14)],
    communication={"function": "Hosting and celebrating",
                   "phrases": ["Welcome to our corner!", "Would you like to try our quiz?",
                               "Well done — four out of five!", "Thank you for visiting.",
                               "Have a great summer!"],
                   "roleplay": "Country Corner showcase: groups host and visit; visitors take the "
                               "quizzes; the class votes for the best corner.",
                   "real_life": "Hosting an event and presenting information to visitors."},
    guided=[EX("U12.7-G1", "Vocabulary race", "Write the word.",
               items=["1. somebody who learned English as a baby: a ______",
                      "2. the number of people in a country: the ______",
                      "3. a famous place people recognise: a ______",
                      "4. the family you stay with abroad: a ______",
                      "5. missing your home: ______", "6. sure of yourself: ______"],
               answers=["1. native speaker", "2. population", "3. landmark", "4. host family",
                        "5. homesick", "6. confident"], level="E", kind="vocab"),
            EX("U12.7-G2", "Error clinic – the six Unit 12 mistakes", "Correct one mistake in each "
               "sentence.",
               items=["1. I have never not been abroad.",
                      "2. I have been to Hanoi last year.",
                      "3. Have you ever went to Hue?",
                      "4. It is the largest country of the world.",
                      "5. It is one of the most famous place in Asia.",
                      "6. She is vietnamese."],
               answers=["1. I have never been abroad.", "2. I went to Hanoi last year.",
                        "3. Have you ever been to Hue?",
                        "4. It is the largest country in the world.",
                        "5. It is one of the most famous places in Asia.",
                        "6. She is Vietnamese."], level="D", kind="grammar")],
    independent=[EX("U12.7-I1", "Mixed review", "Complete the text.",
                    text=["My name is Linh and I (1. be) ______ thirteen. I (2. learn) ______ "
                          "English for four years. I (3. never / be) ______ abroad, but last April I "
                          "(4. meet) ______ two Australian tourists near the lake and I "
                          "(5. speak) ______ English to them for five minutes. Ha Long Bay is one of "
                          "the most beautiful (6. place) ______ in the world, and it is the "
                          "(7. famous) ______ place in my country."],
                    items=["Write the seven answers."],
                    answers=["1. am", "2. have learned/have been learning", "3. have never been",
                             "4. met", "5. spoke", "6. places", "7. most famous"],
                    level="D", kind="grammar"),
                 EX("U12.7-I2", "Project work", "Finish your country corner and prepare to host.",
                    items=[], answers=["Check the superlatives and the present perfect sentence."],
                    level="D", kind="mixed")],
    review=["Country and culture vocabulary (26 items)", "Present perfect with ever/never/been to",
            "Past simple with a time word", "Superlatives and 'one of the most…'",
            "Conversation and email skills"],
    homework=[EX("U12.7-H1", "Vocabulary", "Write 10 words from Unit 12 with Vietnamese meanings.",
                 items=[], answers=["Any 10 of the unit's items."], level="E", kind="vocab"),
              EX("U12.7-H2", "Grammar", "Choose the correct answer.",
                 items=["1. I have (never / never not) been abroad.",
                        "2. I (have been / went) to Hue last year.",
                        "3. (Have you ever been / Did you ever been) to Hanoi?",
                        "4. It is the largest country (in / of) the world.",
                        "5. It is one of the most famous (place / places) in Asia.",
                        "6. She is (vietnamese / Vietnamese)."],
                 answers=["1. never", "2. went", "3. Have you ever been", "4. in", "5. places",
                          "6. Vietnamese"], level="M", kind="grammar"),
              EX("U12.7-H3", "Writing (final task of the year)",
                 "Write a letter (130–150 words) to yourself at the beginning of Grade 8.",
                 items=["Tell yourself: what you have learned this year (present perfect), "
                        "what you found hardest, one thing you are proud of, and two goals for "
                        "next year (will)."],
                 answers=["Model: Dear me in Grade 8, This year you have learned about six hundred "
                          "new words and you have written more than thirty compositions. "
                          "In September you could not write forty words without stopping; in May you "
                          "wrote a hundred and twenty in ten minutes. The hardest thing was speaking. "
                          "For six months you said almost nothing in class, and then in March you "
                          "gave a talk about your hobby and nobody laughed. You are proud of that — "
                          "you should be. Next year you will speak in every lesson, even when you are "
                          "not sure. And you will finish your words: the -s, the -ed and the last "
                          "consonant. Good luck. Don't be quiet. (139 words)"],
                 level="D", kind="writing", lines=20),
              EX("U12.7-H4", "Summer challenge", "Over the summer, do THREE of these five things and "
                 "write one line about each in your notebook.",
                 items=["□ Watch five short videos in English without subtitles.",
                        "□ Write three emails or messages in English.",
                        "□ Learn the words for everything in your kitchen.",
                        "□ Speak English to somebody for five minutes.",
                        "□ Read one short story or article a week."],
                 answers=["Collect the notebooks in the first week of Grade 8 — and read some aloud."],
                 level="M", kind="mixed")],
    workbook=[EX("U12.7-P1", "Crossword clues", "Write the word.",
                 items=["1. The number of people in a country. (10)",
                        "2. A famous place people recognise. (8)",
                        "3. Somebody who learned the language as a baby. (6,7)",
                        "4. Missing your home. (8)", "5. Sure of yourself. (9)"],
                 answers=["1. population", "2. landmark", "3. native speaker", "4. homesick",
                          "5. confident"], level="E", kind="vocab"),
              EX("U12.7-P2", "Mixed grammar", "Put the words in order.",
                 items=["1. never / abroad / I / been / have",
                        "2. ever / you / been / have / to Hue / ?",
                        "3. last / went / I / year / to Hanoi",
                        "4. in / largest / it / the / country / world / the / is",
                        "5. famous / one / places / of / most / the / in Asia / it / is"],
                 answers=["1. I have never been abroad.", "2. Have you ever been to Hue?",
                          "3. I went to Hanoi last year.",
                          "4. It is the largest country in the world.",
                          "5. It is one of the most famous places in Asia."],
                 level="M", kind="grammar"),
              EX("U12.7-P3", "Reading review", "Read and choose.",
                 text=["Research on language learning gives one clear message about teenagers: "
                       "the students who improve fastest are not the ones with the best memory. "
                       "They are the ones who use the language even when they are not ready. "
                       "They write messages with mistakes, they answer questions with half a "
                       "sentence, and they ask people to repeat. Waiting until your English is good "
                       "before you use it is like waiting until you can swim before you get in "
                       "the water."],
                 items=["1. Who improves fastest? A. students with the best memory  "
                        "B. students who use the language early  C. students who study grammar most",
                        "2. What three things do they do? (write your answer)",
                        "3. What does the swimming comparison mean?"],
                 answers=["1. B",
                          "2. They write messages with mistakes, answer with half a sentence, "
                          "and ask people to repeat.",
                          "3. You learn by doing: you cannot become ready without using the "
                          "language."], level="M", kind="reading"),
              EX("U12.7-P4", "Unit 12 test yourself (10 marks)", "Answer about yourself "
                 "(2 marks each).",
                 items=["1. One place you have been to: ______",
                        "2. One thing you have never done: ______",
                        "3. A 'Have you ever…?' question: ______",
                        "4. A superlative sentence about Viet Nam: ______",
                        "5. What you will do to improve your English next year: ______"],
                 answers=["Model: 1. I have been to Ha Long Bay twice. 2. I have never been abroad. "
                          "3. Have you ever spoken English to a foreigner? 4. Ha Long Bay is one of "
                          "the most beautiful places in Viet Nam. 5. I will speak in every lesson, "
                          "even when I am not sure."], level="D", kind="mixed")],
    procedure=[ST("Warm-up: The year in ten words", 6,
                  ["Ask: 'Give me ten English words you did not know in September.' "
                   "Write them on the board and leave them there."],
                  "Recall words learned this year.", "Whole class", "Slide 2"),
               ST("Vocabulary and listening review", 6,
                  ["U12.7-G1 race; then the listening quiz U12.7-L1."],
                  "Write words; complete sentences.", "Pairs", "Slides 3–4"),
               ST("Grammar review + final error clinic", 9,
                  ["Grammar table; U12.7-G2 in pairs with explanations.",
                   "Then look at the whole wall list of the year (72 sentences) and ask: "
                   "'Which of these do you still get wrong?' Each student writes THEIR three."],
                  "Correct, explain, and choose their own three weak points.", "Pairs → individual",
                  "Slides 5–7"),
               ST("Mixed practice", 5, ["U12.7-I1 gap-fill; fast finishers do Workbook P2."],
                  "Complete the text.", "Individual", "Student Book p. U12L7"),
               ST("Project: Country Corner showcase", 15,
                  ["Groups set up their corners with posters and quizzes.",
                   "Half the class hosts for five minutes; then swap; then a third round if there "
                   "is time.",
                   "Visitors take at least two quizzes.",
                   "Vote for the best corner and the best quiz question."],
                  "Host, visit, take quizzes, vote.", "Groups of 4", "Slides 8–10"),
               ST("Wrap-up: the end of the year", 4,
                  ["Give back the students' first piece of writing from Unit 1 next to their last "
                   "one from Unit 12.",
                   "Set the summer challenge (H4) and say goodbye properly."],
                  "Compare their September and May writing.", "Whole class", "Slide 12")],
    teacher_talk=[TK("Show them the distance they have travelled",
                     ["(Hand back the Unit 1 paragraph and the Unit 12 email together.)",
                      "Look at the paper on the left. You wrote that in September. Now look at the "
                      "one on the right.",
                      "Same person. Same brain. Nine months of work.",
                      "You may still make mistakes with -ed and articles. So do I sometimes. "
                      "But look at the length. Look at the ideas. Look at the fact that you STARTED.",
                      "That is what a year looks like. Keep both papers."]),
                  TK("The last thing I want you to remember",
                     ["Of everything in this course, remember two sentences.",
                      "One: 'Sorry, could you say that again, please?' — because that sentence keeps "
                      "every conversation alive.",
                      "Two: your English does not have to be perfect. It has to be CLEAR.",
                      "Finish your words. Slow down. Say something. Have a wonderful summer — "
                      "and I will see you in Grade 8."])],
    support=["Give the error clinic with mistakes underlined.",
             "Provide the eight fact-file sentences as a frame.",
             "Assign the quiz-master role at the corner."],
    challenge=["Ask them to answer visitors' questions without notes.",
               "Ask for three superlatives and two present perfect sentences.",
               "Ask for 160 words in the letter to themselves."],
    assessment=["Unit 12 checklist: 5 of 6 'I can' statements", "Error clinic 5 of 6",
                "Hosts the corner and answers two questions",
                "END-OF-YEAR: compare the Unit 1 and Unit 12 writing for each student"],
    board_plan=["LEFT: ten words we did not know in September",
                "CENTRE: Unit 12 grammar table + the year's wall list",
                "RIGHT: showcase instructions; summer challenge"],
    materials=["Poster paper, quiz cards", "Students' Unit 1 writing (kept since September)",
               'Recording: Looking Back — listen again (replay — see the lesson page)'],
)

UNIT.lessons = [L1, L2, L3, L4, L5, L6, L7]

UNIT.revision = [
    EX("R12-1", "Vocabulary", "Complete with a word from Unit 12.",
       items=["1. The c______ of Australia is Canberra.",
              "2. The p______ of New Zealand is about five million.",
              "3. The Opera House is a famous l______ .",
              "4. A n______ s______ learned English as a baby.",
              "5. She stayed with a h______ family in Adelaide.",
              "6. Be c______ , even when you make mistakes."],
       answers=["1. capital", "2. population", "3. landmark", "4. native speaker", "5. host",
                "6. confident"], level="E", kind="vocab"),
    EX("R12-2", "Grammar: present perfect", "Complete with the present perfect or past simple.",
       items=["1. I ______ (never / be) abroad.", "2. We ______ (go) to Hue last summer.",
              "3. ______ you ever ______ (eat) sushi?",
              "4. She ______ (write) six emails this month.",
              "5. He ______ (see) the sea for the first time in 2022.",
              "6. They ______ (visit) Australia twice."],
       answers=["1. have never been", "2. went", "3. Have … eaten", "4. has written", "5. saw",
                "6. have visited"], level="M", kind="grammar"),
    EX("R12-3", "Grammar: superlatives and articles", "Complete.",
       items=["1. Russia is ______ (large) country ______ the world.",
              "2. It is one of ______ (famous) place______ in Asia.",
              "3. She comes from ______ UK. She is ______ .",
              "4. He comes from ______ Australia. He is ______ .",
              "5. Ha Long Bay is ______ (beautiful) place I have ever seen."],
       answers=["1. the largest … in", "2. the most famous … places", "3. the; British",
                "4. – ; Australian", "5. the most beautiful"], level="M", kind="grammar"),
    EX("R12-4", "Reading", "Read and answer.",
       text=["English is an official language in more than sixty countries, but it is nobody's "
             "'property'. About 1.5 billion people speak it and only about 400 million learned it "
             "as their first language. Most English conversations in the world today happen between "
             "two people who both learned it at school. Research shows that these conversations "
             "often succeed better than conversations with a native speaker, because learners "
             "speak more slowly and check more often."],
       items=["1. In how many countries is English official?",
              "2. How many people speak English, and how many as a first language?",
              "3. Between whom do most English conversations happen today?",
              "4. Why do these conversations often succeed?",
              "5. What does 'it is nobody's property' mean?"],
       answers=["1. More than sixty.", "2. About 1.5 billion; about 400 million as a first language.",
                "3. Between two people who both learned it at school.",
                "4. Because learners speak more slowly and check more often.",
                "5. That English does not belong to one country any more — it belongs to everybody "
                "who uses it."], level="M", kind="reading"),
    EX("R12-5", "Writing", "Write an email (120–140 words) to a pen friend in an English-speaking "
       "country.",
       items=["Four paragraphs: opening – your news (present perfect) – one Vietnamese custom "
              "with a personal feeling – two questions and a closing."],
       answers=["See U12.6-W2 model. Marking: content 3, organisation 2, tenses 3, vocabulary 1, "
                "length 1."], level="D", kind="writing", lines=18),
]
