#!/usr/bin/env python3
"""Build the whole course: 5 DOCX books + one PPTX deck per session."""
import os, sys, time
from generators import teacher_book, student_book, workbook, homework, answer_key, slides
from curriculum import all_lessons, load_units

OUT = "output"
BOOKS = [
    (teacher_book, "01_Teachers_Coursebook.docx"),
    (student_book, "02_Student_Coursebook.docx"),
    (workbook,     "03_Exercise_and_Practice_Book.docx"),
    (homework,     "04_Homework_Book.docx"),
    (answer_key,   "05_Teachers_Answer_Key.docx"),
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
    ex = sum(len(l.all_exercises()) for l in ls)
    vocab = sum(len(l.vocab) for l in ls)
    print(f"\n  {len(load_units())} units · {len(ls)} sessions · {ex} exercises · {vocab} vocabulary items")
    print(f"  built in {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
