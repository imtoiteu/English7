#!/usr/bin/env python3
"""Build the whole course: 7 DOCX books + one PPTX deck per teaching session."""
import os, sys, time
from generators import (teacher_book, student_book, workbook, homework, answer_key,
                        diagnostic_book, test_papers, slides)
from curriculum import all_lessons, teaching_lessons, load_units, load_papers, load_profile

OUT = "output"
BOOKS = [
    (teacher_book,    "01_Teachers_Coursebook.docx"),
    (student_book,    "02_Student_Coursebook.docx"),
    (workbook,        "03_Exercise_and_Practice_Book.docx"),
    (homework,        "04_Homework_Book.docx"),
    (answer_key,      "05_Teachers_Answer_Key.docx"),
    (diagnostic_book, "06_Diagnostic_and_Adaptive_System.docx"),
    (test_papers,     "07_Diagnostic_Test_Papers.docx"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    for mod, name in BOOKS:
        p = mod.build(os.path.join(OUT, name))
        print(f"  ✓ {name:42s} {os.path.getsize(p)/1024:8.0f} KB")
    decks = slides.build(os.path.join(OUT, "slides"))
    print(f"  ✓ {len(decks)} PPTX decks in {OUT}/slides/")

    ls = all_lessons()
    teach = teaching_lessons()
    ex = sum(len(l.all_exercises()) for l in teach)
    vocab = sum(len(l.vocab) for l in teach)
    papers = load_papers()
    items = sum(len(p.all_items()) for p in papers)
    marks = sum(p.total for p in papers)

    print(f"\n  {len(load_units())} units · {len(ls)} sessions "
          f"({len(teach)} taught + {len(ls) - len(teach)} diagnostic) · "
          f"{ex} exercises · {vocab} vocabulary items")
    print(f"  {len(papers)} diagnostic papers · {items} test items · {marks:g} marks")
    print(f"  {len(decks)} slide decks — the diagnostic sessions are paper-based and have none")

    CP = load_profile()
    if CP is not None:
        if CP.DIAGNOSED:
            print(f"\n  ADAPTED: {CP.summary()}")
        else:
            print("\n  Class not diagnosed yet — books built as designed. "
                  "Fill in curriculum/class_profile.py and rebuild to adapt.")
    print(f"  built in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
