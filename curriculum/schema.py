"""Data schema for the Grade 7 English course.

One lesson object feeds ALL six deliverables (teacher book, student book,
workbook, homework book, answer key, slides).  Anything a teacher sees is
derived from here, so the materials cannot drift out of sync.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any


# --------------------------------------------------------------------------
# Small building blocks
# --------------------------------------------------------------------------

@dataclass
class Word:
    """A vocabulary item."""
    word: str
    pos: str            # n, v, adj, adv, phr
    ipa: str
    vn: str             # Vietnamese gloss
    example: str

    def as_row(self):
        return [self.word, self.pos, self.ipa, self.vn, self.example]


def V(word, pos, ipa, vn, example):
    return Word(word, pos, ipa, vn, example)


@dataclass
class Grammar:
    point: str                       # e.g. "The present simple"
    use: List[str] = field(default_factory=list)      # when we use it
    form: List[List[str]] = field(default_factory=list)  # table rows (first row = header)
    examples: List[str] = field(default_factory=list)
    pitfall: str = ""                # typical Vietnamese-learner error
    note: str = ""                   # extra teacher note / contrast


def G(point, use=None, form=None, examples=None, pitfall="", note=""):
    return Grammar(point, use or [], form or [], examples or [], pitfall, note)


@dataclass
class Pron:
    focus: str                       # e.g. "Sounds /ə/ and /ɜː/"
    tip: str                         # how to make the sound (learner-friendly)
    items: List[str] = field(default_factory=list)    # words / minimal pairs
    drill: List[str] = field(default_factory=list)    # sentences to drill
    vn_note: str = ""                # why this is hard for Vietnamese learners


def P(focus, tip, items=None, drill=None, vn_note=""):
    return Pron(focus, tip, items or [], drill or [], vn_note)


@dataclass
class Audio:
    """A listening text.

    Since the real-audio rebuild every listening item is an EXTERNAL, REAL
    HUMAN RECORDING.  `script` holds the published transcript.  The `source_*`
    fields carry everything a teacher needs to find, play and credit it.
    """
    title: str
    context: str
    script: List[str]
    tasks: List["Ex"] = field(default_factory=list)
    source: str = ""
    source_page: str = ""
    audio_urls: List[str] = field(default_factory=list)
    licence: str = ""
    attribution: str = ""
    speakers: str = ""
    duration: str = ""
    speech_rate: str = ""
    level: str = ""
    script_is_excerpt: bool = False
    recycled_from: List[str] = field(default_factory=list)
    teacher_note: str = ""


def A(title, context, script, tasks=None, source="", source_page="", audio_urls=None,
      licence="", attribution="", speakers="", duration="", speech_rate="", level="",
      script_is_excerpt=False, recycled_from=None, teacher_note=""):
    return Audio(title, context, script, tasks or [], source, source_page,
                 audio_urls or [], licence, attribution, speakers, duration,
                 speech_rate, level, script_is_excerpt, recycled_from or [], teacher_note)


@dataclass
class Text:
    """A reading text + tasks."""
    title: str
    body: List[str]                  # paragraphs
    tasks: List["Ex"] = field(default_factory=list)
    glossary: List[Word] = field(default_factory=list)


def T(title, body, tasks=None, glossary=None):
    return Text(title, body, tasks or [], glossary or [])


@dataclass
class Ex:
    """One exercise. Used in the student book, workbook, homework book.

    level: 'E' easy / 'M' medium / 'D' difficult
    kind:  vocab | grammar | pron | reading | listening | speaking | writing | mixed
    """
    ref: str                          # unique reference, e.g. "U1.3-B"
    title: str
    instruction: str
    items: List[str] = field(default_factory=list)
    answers: List[str] = field(default_factory=list)
    level: str = "E"
    kind: str = "mixed"
    wordbank: List[str] = field(default_factory=list)
    text: List[str] = field(default_factory=list)   # optional stimulus text
    note: str = ""                    # answer-key explanation
    lines: int = 0                    # blank writing lines to print


def EX(ref, title, instruction, items=None, answers=None, level="E", kind="mixed",
       wordbank=None, text=None, note="", lines=0):
    return Ex(ref, title, instruction, items or [], answers or [], level, kind,
              wordbank or [], text or [], note, lines)


@dataclass
class Stage:
    """One stage of the teaching procedure."""
    name: str
    minutes: int
    teacher: List[str]               # what the teacher does / says
    students: str                    # what students do
    mode: str = "Whole class"        # interaction pattern
    material: str = ""               # slide / page reference


def ST(name, minutes, teacher, students, mode="Whole class", material=""):
    return Stage(name, minutes, teacher if isinstance(teacher, list) else [teacher],
                 students, mode, material)


@dataclass
class Talk:
    """A suggested teacher explanation (scripted language for the teacher)."""
    cue: str                          # when to say it
    say: List[str]                    # the words


def TK(cue, say):
    return Talk(cue, say if isinstance(say, list) else [say])


# --------------------------------------------------------------------------
# The lesson
# --------------------------------------------------------------------------

@dataclass
class Lesson:
    code: str                         # "U1L3"
    unit: int
    number: int                       # lesson number inside the unit
    period: int                       # running period number in the year
    lesson_type: str                  # Getting Started / A Closer Look 1 ...
    title: str
    objectives: List[str] = field(default_factory=list)
    recycled: List[str] = field(default_factory=list)   # language brought back
    vocab: List[Word] = field(default_factory=list)
    phrases: List[str] = field(default_factory=list)    # collocations / chunks
    grammar: Optional[Grammar] = None
    pron: Optional[Pron] = None
    listening: Optional[Audio] = None
    reading: Optional[Text] = None
    speaking: List[Ex] = field(default_factory=list)
    writing: List[Ex] = field(default_factory=list)
    communication: Dict[str, Any] = field(default_factory=dict)  # function/phrases/roleplay
    guided: List[Ex] = field(default_factory=list)
    independent: List[Ex] = field(default_factory=list)
    review: List[str] = field(default_factory=list)     # consolidation points
    homework: List[Ex] = field(default_factory=list)
    workbook: List[Ex] = field(default_factory=list)    # extra practice, E->M->D
    procedure: List[Stage] = field(default_factory=list)
    teacher_talk: List[Talk] = field(default_factory=list)
    support: List[str] = field(default_factory=list)    # weaker students
    challenge: List[str] = field(default_factory=list)  # stronger students
    assessment: List[str] = field(default_factory=list)
    board_plan: List[str] = field(default_factory=list)
    materials: List[str] = field(default_factory=list)
    slides: List[Dict[str, Any]] = field(default_factory=list)  # optional overrides

    # -- convenience ------------------------------------------------------
    @property
    def full_title(self):
        return f"Unit {self.unit} – Lesson {self.number}: {self.lesson_type} – {self.title}"

    @property
    def short_title(self):
        return f"U{self.unit}L{self.number} {self.lesson_type}"

    def all_exercises(self):
        """Every exercise that has an answer, in book order."""
        out = []
        for group in (self.guided, self.independent, self.speaking, self.writing):
            out.extend(group)
        if self.reading:
            out.extend(self.reading.tasks)
        if self.listening:
            out.extend(self.listening.tasks)
        out.extend(self.workbook)
        out.extend(self.homework)
        # de-duplicate by ref, keep order
        seen, uniq = set(), []
        for e in out:
            if e.ref not in seen:
                seen.add(e.ref)
                uniq.append(e)
        return uniq


@dataclass
class Unit:
    number: int
    title: str
    theme: str
    can_do: List[str] = field(default_factory=list)     # unit outcomes
    grammar_focus: List[str] = field(default_factory=list)
    pron_focus: str = ""
    vocab_focus: str = ""
    project: Dict[str, Any] = field(default_factory=dict)
    lessons: List[Lesson] = field(default_factory=list)
    revision: List["Ex"] = field(default_factory=list)   # end-of-unit revision set (Homework Book)


# ==========================================================================
# DIAGNOSTIC & ADAPTIVE SYSTEM
#
# Added by the diagnostic rebuild.  These types are ADDITIVE: nothing above
# this line changed, so every existing unit file keeps working unaltered.
#
#   Item     one markable question
#   Task     a group of items sharing one stimulus (a recording, a text…)
#   Section  one strand of a paper (Listening, Reading, Grammar…)
#   Paper    a whole diagnostic (initial / mid-year / final)
#   Criterion / Rubric   how productive work is marked
#   Band     an ability level the results sort students into
#   Trigger  a class-level result that CHANGES the teaching programme
#   Bridge   a prerequisite lesson for students below the expected level
#   Extension an activity for students above it
# ==========================================================================

BANDS_OF_DIFFICULTY = ("pre-A1", "A1", "A1+", "A2")


@dataclass
class Item:
    """One markable test item.

    `band` is the difficulty the item is calibrated at, `tests` names the
    construct it probes.  Both are what make a diagnostic profile possible:
    without them a wrong answer is just a lost mark, with them it is evidence.
    """
    n: str                            # "1", "2" …
    prompt: str
    answer: str
    marks: float = 1.0
    band: str = "A1"                  # pre-A1 | A1 | A1+ | A2
    tests: str = ""                   # "past simple, regular -ed"
    options: List[str] = field(default_factory=list)   # for multiple choice
    note: str = ""                    # marking note / why learners fail it


def IT(n, prompt, answer, marks=1.0, band="A1", tests="", options=None, note=""):
    return Item(str(n), prompt, answer, marks, band, tests, options or [], note)


@dataclass
class Task:
    """A group of items that share one stimulus."""
    code: str                         # "A-L1"
    title: str
    instruction: str
    items: List[Item] = field(default_factory=list)
    audio_key: str = ""               # key into curriculum.audio_diagnostic.DIAG_AUDIO
    audio_part: int = 1
    excerpt: str = ""                 # "play 0:00–1:20, stop after: …"
    plays: int = 2
    text_title: str = ""
    text: List[str] = field(default_factory=list)      # reading stimulus
    wordbank: List[str] = field(default_factory=list)
    lines: int = 0                    # blank writing lines to print
    rubric: str = ""                  # name of the Rubric that marks it
    band: str = ""                    # overall calibration of the task
    note: str = ""

    @property
    def marks(self):
        return sum(i.marks for i in self.items)


def TA(code, title, instruction, items=None, audio_key="", audio_part=1, excerpt="",
       plays=2, text_title="", text=None, wordbank=None, lines=0, rubric="", band="", note=""):
    return Task(code, title, instruction, items or [], audio_key, audio_part, excerpt,
                plays, text_title, text or [], wordbank or [], lines, rubric, band, note)


@dataclass
class Section:
    """One strand of a paper."""
    code: str                         # "A-S1"
    name: str                         # "Listening"
    strand: str                       # listening|reading|vocab|grammar|writing|speaking|pron
    marks: float
    minutes: int
    period: int                       # which 45' period it is sat in
    instruction: str
    tasks: List[Task] = field(default_factory=list)
    admin: List[str] = field(default_factory=list)     # how to administer it
    reads: str = ""                   # what the section actually measures

    @property
    def counted(self):
        return sum(t.marks for t in self.tasks)


def SEC(code, name, strand, marks, minutes, period, instruction, tasks=None,
        admin=None, reads=""):
    return Section(code, name, strand, marks, minutes, period, instruction,
                   tasks or [], admin or [], reads)


@dataclass
class Paper:
    code: str                         # "A"
    name: str
    when: str                         # "Periods 1–2, first week of the year"
    total: float
    sections: List[Section] = field(default_factory=list)
    purpose: List[str] = field(default_factory=list)
    admin: List[str] = field(default_factory=list)
    parallel_to: str = ""             # code of the paper it is a parallel form of

    @property
    def counted(self):
        return sum(s.counted for s in self.sections)

    def strand(self, name):
        return [s for s in self.sections if s.strand == name]

    def all_items(self):
        return [i for s in self.sections for t in s.tasks for i in t.items]


@dataclass
class Criterion:
    name: str
    max: float
    descriptors: List[List[str]] = field(default_factory=list)   # [marks, descriptor]
    vn_note: str = ""                 # the L1 interference to expect


def CR(name, mx, descriptors=None, vn_note=""):
    return Criterion(name, mx, descriptors or [], vn_note)


@dataclass
class Rubric:
    name: str
    total: float
    criteria: List[Criterion] = field(default_factory=list)
    how_to_use: List[str] = field(default_factory=list)
    diagnostic_use: List[str] = field(default_factory=list)   # what each criterion tells you

    @property
    def counted(self):
        return sum(c.max for c in self.criteria)


def RB(name, total, criteria=None, how_to_use=None, diagnostic_use=None):
    return Rubric(name, total, criteria or [], how_to_use or [], diagnostic_use or [])


@dataclass
class Band:
    key: str                          # foundation | core | extension
    name: str
    lo: float                         # inclusive, marks out of 80
    hi: float                         # inclusive
    meaning: str
    looks_like: List[str] = field(default_factory=list)
    programme: List[str] = field(default_factory=list)
    never: List[str] = field(default_factory=list)   # what NOT to do with this group


@dataclass
class Trigger:
    """A class-level diagnostic result that changes the teaching programme.

    Two kinds of change, and keeping them apart is what makes the adapted
    Teacher's Coursebook readable:

    `insert_at`  explicit lesson codes that get a full ADAPTIVE INSERT box
                 printed under the procedure.  Use this for a change that
                 happens in a particular lesson, at a particular moment.
    `standing`   one line describing a change that runs across the year — a
                 daily drill, a pairing rule, a marking rule.  Printed ONCE in
                 the front matter.  Stamping "open every lesson with a
                 retrieval quiz" onto all ninety-four lesson plans does not
                 make a teacher more likely to do it; it makes them stop
                 reading the boxes.

    `affects` stays prose, for the trigger's own page in Book 6.
    """
    code: str                         # "T1"
    name: str
    fires_when: str
    evidence: str                     # which items / rubric criteria to total
    interpretation: str
    changes: List[str] = field(default_factory=list)
    resources: List[str] = field(default_factory=list)   # B1…B6 / E1…E6 / audio keys
    affects: List[str] = field(default_factory=list)     # prose scope, for Book 6
    retire_when: str = ""             # when to stop doing it
    insert_at: List[str] = field(default_factory=list)   # lesson codes to stamp
    standing: str = ""                # always-on change, printed once


@dataclass
class Bridge:
    """A prerequisite lesson for students below the expected level."""
    code: str                         # "B1"
    title: str
    prerequisite_for: str
    why: str                          # the Grade 7 content that silently assumes it
    objectives: List[str] = field(default_factory=list)
    content: List[str] = field(default_factory=list)
    procedure: List[Stage] = field(default_factory=list)
    exercises: List[Ex] = field(default_factory=list)
    success: str = ""                 # the exit check
    minutes: int = 45


@dataclass
class Extension:
    """An activity for students above the expected level.

    The design rule is DIFFERENT COGNITIVE DEMAND, never more of the same
    exercises.  `demand` says what the activity adds that the core lesson
    cannot.
    """
    code: str                         # "E1"
    title: str
    units: str                        # "1–2"
    demand: str
    steps: List[str] = field(default_factory=list)
    output: str = ""
    assess: str = ""
    resources: List[str] = field(default_factory=list)
    minutes: str = ""
