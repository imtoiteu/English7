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
