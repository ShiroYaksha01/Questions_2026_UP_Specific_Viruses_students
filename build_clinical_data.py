#!/usr/bin/env python3
"""Rebuild both clinical subjects from highlighted and explicitly keyed PDFs."""

from collections import Counter
import json
from pathlib import Path
import re

import pymupdf
from build_mona_data import SOURCE as MONA_SOURCE, read_mona_questions

ROOT = Path(__file__).resolve().parent
SOURCE = "Clinical Bio+chem final.pdf"
SUBJECTS = {"Clinical Biochemistry": (2, 40), "Clinical Biology": (3, 10)}
QUESTION = re.compile(r"^(\d+)\.\s+(.+)$")
OPTION = re.compile(r"^([a-d])\.\s+(.+)$")


def clean(text):
    # Restore chemical notation split across PDF lines and superscript spans.
    text = text.translate(str.maketrans("𝑃𝐶𝑂𝐻", "PCOH"))
    text = re.sub(r"HCO3\s*−\s*", "HCO₃⁻ ", text)
    text = re.sub(r"PCO2\s*", "PCO₂ ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"([₂⁻])\s+([?.),;:])", r"\1\2", text)


def read_clinical_questions(start_id=161):
    questions = []
    subject = current = letter = None
    answer_letters = set()
    matched_fills = set()
    fill_count = 0

    def finish():
        if current is None:
            return
        if set(current["options"]) != set("ABCD") or len(answer_letters) != 1:
            raise ValueError(f"Incomplete choices or ambiguous highlight: {current}")
        current["question"] = clean(current["question"])
        current["options"] = {key: clean(value) for key, value in current["options"].items()}
        current["correct_answer"] = next(iter(answer_letters))
        current["correct_text"] = current["options"][current["correct_answer"]]
        if not current["question"] or not all(current["options"].values()):
            raise ValueError("Empty question or option")

    with pymupdf.open(ROOT / SOURCE) as pdf:
        for page_number, page in enumerate(pdf, 1):
            fills = [drawing["rect"] for drawing in page.get_drawings()
                     if drawing.get("fill") == (1.0, 1.0, 0.0)]
            fill_count += len(fills)
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    text = "".join(span["text"] for span in line["spans"]).strip()
                    if not text:
                        continue
                    bounds = pymupdf.Rect(line["bbox"])
                    hits = {index for index, fill in enumerate(fills)
                            if (bounds & fill).get_area() >= fill.get_area() * 0.5}
                    matched_fills.update((page_number, index) for index in hits)
                    heading = text.rstrip(":").strip()
                    if heading in SUBJECTS:
                        finish()
                        subject, current, letter = heading, None, None
                        continue
                    question_match, option_match = QUESTION.match(text), OPTION.match(text)
                    if question_match:
                        finish()
                        if subject is None:
                            raise ValueError("Question before subject heading")
                        number = int(question_match[1])
                        expected = sum(q["lecture_name"] == subject for q in questions) + 1
                        if number != expected:
                            raise ValueError(f"Unexpected number {number} in {subject}")
                        current = {
                            "global_id": start_id + len(questions),
                            "lecture_id": SUBJECTS[subject][0], "lecture_name": subject,
                            "question_id": number, "question": question_match[2],
                            "options": {}, "page": page_number, "source": SOURCE,
                        }
                        questions.append(current)
                        letter, answer_letters = None, set()
                    elif option_match:
                        if current is None:
                            raise ValueError("Option before question")
                        letter = option_match[1].upper()
                        if letter != "ABCD"[len(current["options"])]:
                            raise ValueError("Unexpected option order")
                        current["options"][letter] = option_match[2]
                        if hits:
                            answer_letters.add(letter)
                    elif current is not None:
                        if letter:
                            current["options"][letter] += " " + text
                            if hits:
                                answer_letters.add(letter)
                        else:
                            current["question"] += " " + text
        finish()
    counts = Counter(q["lecture_name"] for q in questions)
    if counts != Counter({name: spec[1] for name, spec in SUBJECTS.items()}):
        raise ValueError(f"Unexpected subject counts: {counts}")
    if len(matched_fills) != fill_count:
        raise ValueError(f"Only {len(matched_fills)} of {fill_count} yellow fills matched text")
    return questions


def main():
    output = ROOT / "questions_db.json"
    existing = json.loads(output.read_text(encoding="utf-8"))
    existing = [q for q in existing if q.get("source") not in (SOURCE, MONA_SOURCE)]
    added = read_clinical_questions(max(q["global_id"] for q in existing) + 1)
    added.extend(read_mona_questions(added[-1]["global_id"] + 1))
    combined = existing + added
    if len({q["global_id"] for q in combined}) != len(combined):
        raise ValueError("Duplicate question IDs")
    output.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Verified and added {len(added)} clinical MCQs; {len(combined)} total")
    for subject in SUBJECTS:
        print(subject, dict(Counter(q["correct_answer"] for q in added if q["lecture_name"] == subject)))


if __name__ == "__main__":
    main()
