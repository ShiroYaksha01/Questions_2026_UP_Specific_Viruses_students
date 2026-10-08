#!/usr/bin/env python3
"""Build the standalone site's question database from the marked MCQ PDF."""

from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
PDF = ROOT / "MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf"
OUTPUT = ROOT / "questions_db.json"
QUESTION_RE = re.compile(r"^\s*(\d{1,3})\.\s+(.+)$")
OPTION_RE = re.compile(r"^\s*([A-D])\.\s+(.+)$")
EXPECTED_ANSWERS = Counter({"A": 125, "B": 33, "C": 2})


def poppler(*args):
    """Run a Poppler utility and return its UTF-8 output."""
    try:
        result = subprocess.run(args, check=True, capture_output=True)
    except FileNotFoundError as exc:
        raise RuntimeError(f"Missing Poppler utility: {args[0]}") from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(exc.stderr.decode("utf-8", errors="replace")) from exc
    return result.stdout.decode("utf-8")


def read_questions():
    text = poppler("pdftotext", "-f", "1", "-l", "18", "-layout", str(PDF), "-")
    pages = text.split("\f")[:18]
    if len(pages) != 18:
        raise ValueError(f"Expected 18 PDF text pages, found {len(pages)}")

    questions = []
    current = None
    current_option = None
    ended_at_case = False

    for page_number, page_text in enumerate(pages, start=1):
        for raw_line in page_text.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith("Case 1:"):
                ended_at_case = True
                break

            question_match = QUESTION_RE.match(line)
            option_match = OPTION_RE.match(line)
            if question_match:
                number = int(question_match.group(1))
                if number != len(questions) + 1:
                    raise ValueError(f"Unexpected question number {number} on page {page_number}")
                current = {
                    "global_id": number,
                    "lecture_id": 1,
                    "lecture_name": "Metabolic Biochemistry",
                    "question_id": number,
                    "question": question_match.group(2),
                    "options": {},
                    "page": page_number,
                }
                questions.append(current)
                current_option = None
            elif option_match:
                if current is None:
                    raise ValueError(f"Option before question on page {page_number}: {line}")
                letter = option_match.group(1)
                expected = "ABCD"[len(current["options"])] if len(current["options"]) < 4 else None
                if letter != expected:
                    raise ValueError(f"Unexpected option {letter} for Q{current['question_id']}")
                current["options"][letter] = option_match.group(2)
                current_option = letter
            elif current is not None:
                if current_option is None:
                    current["question"] += " " + line
                else:
                    current["options"][current_option] += " " + line
        if ended_at_case:
            break

    if not ended_at_case:
        raise ValueError("Case 1 boundary was not found on page 18")
    if len(questions) != 160:
        raise ValueError(f"Expected 160 MCQs, found {len(questions)}")
    for question in questions:
        if not question["question"].strip() or set(question["options"]) != set("ABCD"):
            raise ValueError(f"Incomplete question or choices for Q{question['question_id']}")
        if any(not value.strip() for value in question["options"].values()):
            raise ValueError(f"Blank choice for Q{question['question_id']}")
        if re.search(r"Case\s+\d+:|Matching:|Exercise\s+\d+:", question["question"]):
            raise ValueError(f"Non-MCQ content in Q{question['question_id']}")
    return questions


def positioned_options(page_number):
    xml = poppler("pdftotext", "-f", str(page_number), "-l", str(page_number),
                  "-bbox-layout", str(PDF), "-")
    root = ET.fromstring(xml)
    options = []
    for element in root.iter():
        if not element.tag.endswith("line"):
            continue
        text = " ".join((word.text or "") for word in element if word.tag.endswith("word"))
        match = OPTION_RE.match(text)
        if match:
            options.append((float(element.attrib["yMin"]),
                            float(element.attrib["yMax"]), match.group(1)))
    return options


def add_highlighted_answers(questions):
    reader = PdfReader(PDF)
    if len(reader.pages) < 18:
        raise ValueError("The source PDF has fewer than 18 pages")

    all_options = []
    highlighted_options = set()
    option_highlights = 0
    text_highlights = 0

    for page_number in range(1, 19):
        page = reader.pages[page_number - 1]
        options = positioned_options(page_number)
        all_options.extend((page_number, *option) for option in options)
        page_height = float(page.mediabox.top)

        for annotation_ref in page.get("/Annots", []):
            annotation = annotation_ref.get_object()
            if str(annotation.get("/Subtype")) != "/Highlight":
                continue
            x0, y0, _, y1 = map(float, annotation["/Rect"])
            if x0 >= 75:
                text_highlights += 1
                continue
            option_highlights += 1
            center_y = page_height - (y0 + y1) / 2
            matches = [index for index, (top, bottom, _) in enumerate(options)
                       if top - 5 <= center_y <= bottom + 5]
            if len(matches) != 1:
                raise ValueError(f"Could not uniquely match highlight on page {page_number} at y={center_y:.1f}")
            key = (page_number, matches[0])
            if key in highlighted_options:
                raise ValueError(f"Two highlights map to one choice on page {page_number}")
            highlighted_options.add(key)

    if (len(all_options), option_highlights, text_highlights) != (640, 160, 5):
        raise ValueError("Expected 640 choices, 160 answer highlights and 5 text highlights; "
                         f"found {len(all_options)}, {option_highlights} and {text_highlights}")

    source_options = [(question["question_id"], letter)
                      for question in questions for letter in "ABCD"]
    answers = {}
    page_option_index = Counter()
    for global_index, (page_number, _, _, positioned_letter) in enumerate(all_options):
        question_id, source_letter = source_options[global_index]
        if positioned_letter != source_letter:
            raise ValueError(f"Positioned choice order differs at Q{question_id} {source_letter}")
        local_index = page_option_index[page_number]
        page_option_index[page_number] += 1
        if (page_number, local_index) in highlighted_options:
            if question_id in answers:
                raise ValueError(f"Two answers for Q{question_id}")
            answers[question_id] = source_letter

    if len(answers) != 160 or Counter(answers.values()) != EXPECTED_ANSWERS:
        raise ValueError(f"Incomplete or unexpected answer key: {Counter(answers.values())}")
    for question in questions:
        answer = answers[question["question_id"]]
        question["correct_answer"] = answer
        question["correct_text"] = question["options"][answer]


def main():
    questions = read_questions()
    add_highlighted_answers(questions)
    OUTPUT.write_text(json.dumps(questions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(questions)} verified MCQs to {OUTPUT.name}")


if __name__ == "__main__":
    main()
