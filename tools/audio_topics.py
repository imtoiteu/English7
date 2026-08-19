# -*- coding: utf-8 -*-
"""Per-session pedagogical anchors for the real recordings.

gist  = the correct answer to "What is the recording mainly about?"
focus = the target language to blank out in the notice-the-form task
        (matched case-insensitively as whole words against the real transcript)
"""
TOPICS = {
 # ---- Unit 1  Hobbies ----
 "U1L1": ("watching people in a park as a free-time activity", ["like","love","watch","favorite","people"]),
 "U1L2": ("how often people do things in their free time", ["always","usually","often","sometimes","never"]),
 "U1L3": ("what people do every day and at work", ["work","live","study","start","finish"]),
 "U1L4": ("reading the news and always making the same mistake", ["always","never","usually"]),
 "U1L5": ("making plans with a friend for the weekend", ["free","busy","tonight","weekend","plans"]),
 "U1L6": ("what one person does at the weekend", ["weekend","usually","like","spend"]),
 # ---- Unit 2  Healthy Living ----
 "U2L1": ("choosing between healthy food and junk food", ["healthy","should","eat","junk","exercise"]),
 "U2L2": ("how much and how many of things people have", ["much","many","lot","few","little"]),
 "U2L3": ("giving instructions and telling somebody what to do", ["don't","please","put","take","turn"]),
 "U2L4": ("training for a marathon as a fitness goal", ["habit","start","every","should","try"]),
 "U2L5": ("which snacks are healthy and which are not", ["healthy","snack","eat","fruit","sugar"]),
 "U2L6": ("which foods are not healthy", ["healthy","food","eat","sugar","fried"]),
 # ---- Unit 3  Community Service ----
 "U3L1": ("offering help to other people", ["help","can","need","volunteer","carry"]),
 "U3L2": ("what people did yesterday", ["re:\\b\\w+ed\\b"]),
 "U3L3": ("what people did last night and last weekend", ["went","did","had","saw","made","ate","got","took","came","was","were"]),
 "U3L4": ("working together as a team", ["team","together","work","help","idea"]),
 "U3L5": ("visiting a historic house and the person who lived there", ["was","were","played","wanted","lived","had"]),
 "U3L6": ("passing a driving test and renting a car", ["passed","practiced","test","studied","tried"]),
 # ---- Unit 4  Music and Arts ----
 "U4L1": ("a road trip across the United States and a famous song", ["song","sing","land","country","music"]),
 "U4L2": ("the best, the fastest and the most popular things", ["best","fastest","most","biggest","worst"]),
 "U4L3": ("comparing two things", ["better","cheaper","lighter","more","than"]),
 "U4L4": ("inviting friends to a party", ["party","come","can","invite","bring"]),
 "U4L5": ("auditioning for a part in a stage show", ["loudly","quietly","slowly","line","page","say","walk"]),
 "U4L6": ("saying that two things are the same", ["also","too","well","same","both"]),
 # ---- Unit 5  Food and Drink ----
 "U5L1": ("cooking dinner together", ["cook","dinner","make","food","recipe"]),
 "U5L2": ("talking about amounts of things", ["some","any","much","many","lot"]),
 "U5L3": ("asking for and offering things", ["any","some","have","need","want"]),
 "U5L4": ("ordering and choosing food", ["want","like","order","food","try"]),
 "U5L5": ("what one person eats for breakfast", ["breakfast","eat","because","bread","cheese","fruit"]),
 "U5L6": ("which fruits one person likes", ["fruit","like","eat","favorite","sweet"]),
 # ---- Unit 6  A Visit to a School ----
 "U6L1": ("going back to school and studying a subject", ["study","school","class","learn","subject"]),
 "U6L2": ("arrangements people have already made for later", ["going","leaving","meeting","coming","tomorrow"]),
 "U6L3": ("what people are doing right now", ["doing","writing","cooking","going","watching","making"]),
 "U6L4": ("getting to work and asking when things start", ["start","when","time","work","first"]),
 "U6L5": ("one person's schedule for today", ["today","schedule","then","after","class"]),
 "U6L6": ("when one person starts and finishes the day", ["start","finish","day","morning","evening"]),
 # ---- Unit 7  Traffic ----
 "U7L1": ("asking where a place is", ["where","near","next","behind","street","in","on","at","to"]),
 "U7L2": ("saying where places and things are", ["in","on","near","next","between","behind"]),
 "U7L3": ("things people must do and things they do not have to do", ["have","must","don't","need","should"]),
 "U7L4": ("being careful and staying safe", ["careful","watch","stop","safe","look"]),
 "U7L5": ("how one person travels in the city", ["bus","train","use","travel","city","country"]),
 "U7L6": ("living near a train station", ["train","station","near","live","buses","trains"]),
 # ---- Unit 8  Films ----
 "U8L1": ("playing a game to find American symbols at the memorials", ["fun","game","play","win","exciting"]),
 "U8L2": ("describing things with adjectives", ["new","old","difficult","easy","boring","interesting","good","bad","big","small","nice","great"]),
 "U8L3": ("joining ideas with but, so and because", ["but","so","because","however","although"]),
 "U8L4": ("two people who have different opinions", ["think","agree","disagree","opinion","but"]),
 "U8L5": ("a television advertisement for a hair product", ["unbelievable","really","tired","windy","perfect","good"]),
 "U8L6": ("a spy story and a museum about spies", ["spy","secret","museum","find","story"]),
 # ---- Unit 9  Festivals ----
 "U9L1": ("celebrating a famous writer's birthday", ["birthday","celebrate","play","famous","year","the","a","an"]),
 "U9L2": ("months of the year and when things happen", ["January","March","June","July","September","December"]),
 "U9L3": ("asking for everyday objects", ["a","an","the","pen","book"]),
 "U9L4": ("going to a baseball game", ["game","team","play","ball","fans"]),
 "U9L5": ("festivals in different months of the year", ["January","June","October","festival","people"]),
 "U9L6": ("who visits at holiday times", ["visits","holidays","sister","eats","likes","sleeps"]),
 # ---- Unit 10  Energy Sources ----
 "U10L1": ("choosing a Halloween costume for a party", ["will","costume","party","wear","think"]),
 "U10L2": ("plans people have already made", ["going","tonight","tomorrow","plan","weekend"]),
 "U10L3": ("predictions and promises about the future", ["will","won't","think","probably","promise"]),
 "U10L4": ("fixing something that is broken", ["fix","broken","can","need","work"]),
 "U10L5": ("what one person will do in the near future", ["will","won't","going","next","think"]),
 "U10L6": ("what will happen if we do something", ["if","will","won't","rain","then"]),
 # ---- Unit 11  Travelling in the Future ----
 "U11L1": ("plans for a trip next summer", ["summer","go","travel","next","visit"]),
 "U11L2": ("what people can and cannot do", ["can","can't","play","speak","swim"]),
 "U11L3": ("things that are possible but not certain", ["may","might","maybe","sure","probably"]),
 "U11L4": ("changing the plan when something goes wrong", ["plan","change","instead","try","another"]),
 "U11L5": ("who one person will meet later today", ["will","see","tonight","meet","friend"]),
 "U11L6": ("the things people can do at work", ["can","do","work","help","use"]),
 # ---- Unit 12  English-Speaking Countries ----
 "U12L1": ("experiences people have had in their lives", ["ever","never","been","have","before"]),
 "U12L2": ("countries, nationalities and languages", ["English","Spanish","French","country","speak"]),
 "U12L3": ("places people have been to", ["ever","never","been","have","visited"]),
 "U12L4": ("where different people come from", ["from","country","live","born","city"]),
 "U12L5": ("the geography of one person's country", ["some","any","also","coast","south","north"]),
 "U12L6": ("where one person's family lives", ["family","live","country","city","house"]),
 # ---- Review & Test blocks ----
 "REV1L1": ("introducing the people in a family", ["family","mother","father","sister","brother"]),
 "REV1L2": ("what somebody did yesterday", ["was","went","did","had","yesterday"]),
 "REV2L1": ("choosing what to wear for an evening at the theatre", ["like","this","that","buy","how"]),
 "REV2L2": ("what people are doing at the moment", ["doing","working","reading","now","am"]),
 "REV3L1": ("the places in a neighbourhood", ["street","near","house","store","park"]),
 "REV3L2": ("a boat trip on a river", ["river","boat","water","go","ride"]),
 "REV4L1": ("trying something new and taking a chance", ["try","new","chance","will","can"]),
 "REV4L2": ("asking to borrow things", ["may","borrow","can","please","thank"]),
}
