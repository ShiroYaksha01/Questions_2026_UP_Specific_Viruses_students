#!/usr/bin/env python3
"""Read Clinical Biology MCQs using the PDF's explicit Correct answer lines."""

from bisect import bisect_right
from pathlib import Path
import re

import pymupdf

ROOT = Path(__file__).resolve().parent
SOURCE = "MCQ kru Mona.pdf"


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def read_mona_questions(start_id=211):
    with pymupdf.open(ROOT / SOURCE) as pdf:
        pages = [page.get_text() for page in pdf]
    # Preserve offsets so questions spanning pages retain their starting page.
    page_starts, offset = [], 0
    for page in pages:
        page_starts.append(offset)
        offset += len(page) + 1
    text = "\n".join(pages)
    headings = list(re.finditer(r"(?m)^Lesson (\d+): (.+?)\s*\(Questions \d+[–-]\d+\)\s*$", text))
    if len(headings) != 2:
        raise ValueError("Expected two lesson headings")
    # Blank headings while retaining positions for page and lesson attribution.
    for heading in reversed(headings):
        text = text[:heading.start()] + " " * (heading.end() - heading.start()) + text[heading.end():]
    starts = list(re.finditer(r"(?m)^\s*(\d+)\.\s+", text))
    if [int(match[1]) for match in starts] != list(range(1, 41)):
        raise ValueError("Expected exactly questions 1 through 40")
    questions = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[match.end():end].strip()
        if block.count("Correct answer:") != 1:
            raise ValueError(f"Expected one explicit answer for Q{index + 1}")
        choices, answer = block.split("Correct answer:")
        answer_match = re.fullmatch(r"\s*([A-D])\.\s+(.+?)\s*", answer, re.S)
        options = list(re.finditer(r"(?<!\S)([A-D])\.\s+", choices))
        if answer_match is None or [option[1] for option in options] != list("ABCD"):
            raise ValueError(f"Invalid answer or choices for Q{index + 1}")
        values = {
            option[1]: normalize(choices[option.end():options[n + 1].start()
                                        if n + 1 < len(options) else len(choices)])
            for n, option in enumerate(options)
        }
        correct_letter, correct_text = answer_match[1], normalize(answer_match[2])
        if values[correct_letter] != correct_text:
            raise ValueError(f"Answer letter and answer text disagree for Q{index + 1}")
        question = normalize(choices[:options[0].start()])
        if not question or not all(values.values()):
            raise ValueError(f"Empty question or choice for Q{index + 1}")
        lesson = next(heading for heading in reversed(headings) if heading.start() < match.end())
        questions.append({
            "global_id": start_id + index, "lecture_id": 3,
            "lecture_name": "Clinical Biology", "question_id": index + 1,
            "question": question, "options": values,
            "page": bisect_right(page_starts, match.end()), "source": SOURCE,
            "lesson": lesson[2].strip(),
            "correct_answer": correct_letter, "correct_text": correct_text,
        })
    return questions
