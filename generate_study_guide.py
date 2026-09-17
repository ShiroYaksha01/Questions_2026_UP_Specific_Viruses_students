#!/usr/bin/env python3
"""
generate_study_guide.py
Generates the comprehensive Markdown study guide VIROLOGY_EXAM_REVIEW_STUDY_GUIDE.md.
"""

import json

def main():
    with open("questions_db.json", encoding="utf-8") as f:
        db = json.load(f)

    # Group by lecture
    lectures = {}
    for item in db:
        lec_name = item["lecture_name"]
        if lec_name not in lectures:
            lectures[lec_name] = []
        lectures[lec_name].append(item)

    lines = []
    lines.append("# Comprehensive Virology QCM Exam Review & Study Guide")
    lines.append("## University of Puthisastra (UP) — Specific Viruses 2026 Examination Review")
    lines.append("")
    lines.append("> **Document Overview:** Complete verified answer key, rationale, and high-yield notes for all **241 multiple-choice questions** across 11 medical virology lectures.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("1. [Quick-Reference Answer Key (All 241 Questions)](#quick-reference-answer-key)")
    for idx, lec_name in enumerate(lectures.keys(), 1):
        slug = lec_name.lower().replace(" ", "-").replace("–", "-").replace("(", "").replace(")", "").replace("/", "")
        lines.append(f"{idx + 1}. [Lecture {idx}: {lec_name} ({len(lectures[lec_name])} Questions)](#lecture-{idx}-{slug})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Quick Reference Answer Key Table
    lines.append("## Quick-Reference Answer Key")
    lines.append("")
    lines.append("| Lecture | Questions | Answer Sequence |")
    lines.append("| :--- | :---: | :--- |")
    for idx, (lec_name, q_list) in enumerate(lectures.items(), 1):
        seq = " ".join([f"**Q{q['question_id']}:** {q['correct_answer']}" for q in q_list])
        lines.append(f"| **L{idx}: {lec_name}** | {len(q_list)} | {seq} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Lecture details
    for idx, (lec_name, q_list) in enumerate(lectures.items(), 1):
        slug = lec_name.lower().replace(" ", "-").replace("–", "-").replace("(", "").replace(")", "").replace("/", "")
        lines.append(f"## Lecture {idx}: {lec_name}")
        lines.append(f"**Total Questions:** {len(q_list)} | **Focus Area:** High-Yield Medical & Clinical Virology")
        lines.append("")

        for q in q_list:
            qid = q["question_id"]
            correct = q["correct_answer"]
            correct_txt = q["correct_text"]
            lines.append(f"### Q{qid}. {q['question']}")
            lines.append("")
            for opt_key, opt_val in q["options"].items():
                if opt_key == correct:
                    lines.append(f"- [x] **{opt_key}) {opt_val}** *(Correct Answer)*")
                else:
                    lines.append(f"- [ ] {opt_key}) {opt_val}")
            lines.append("")
            lines.append(f"> **Correct Answer:** **{correct}) {correct_txt}**")
            lines.append(">")
            lines.append(f"> **Explanation & Rationale:** {q['explanation']}")
            lines.append(">")
            lines.append(f"> **High-Yield Takeaway:** `{q['takeaway']}`")
            lines.append("")

        lines.append("---")
        lines.append("")

    content = "\n".join(lines)
    with open("VIROLOGY_EXAM_REVIEW_STUDY_GUIDE.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("Generated VIROLOGY_EXAM_REVIEW_STUDY_GUIDE.md successfully!")

if __name__ == "__main__":
    main()
