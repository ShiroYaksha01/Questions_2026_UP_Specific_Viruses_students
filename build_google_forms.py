#!/usr/bin/env python3
"""Generate a self-contained Apps Script with all current website MCQs."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    questions = json.loads((ROOT / 'questions_db.json').read_text(encoding='utf-8'))
    subjects = {}
    ids = set()
    for question in questions:
        if question['global_id'] in ids:
            raise ValueError('Duplicate question ID')
        ids.add(question['global_id'])
        if (not question['question'] or set(question['options']) != set('ABCD') or
                not all(question['options'].values()) or
                question['correct_text'] != question['options'][question['correct_answer']]):
            raise ValueError(f"Invalid question {question['global_id']}")
        subject = subjects.setdefault(question['lecture_id'], {
            'id': str(question['lecture_id']), 'name': question['lecture_name'], 'questions': []
        })
        if subject['name'] != question['lecture_name']:
            raise ValueError('Inconsistent subject name')
        subject['questions'].append({
            key: question[key] for key in
            ('question', 'question_id', 'options', 'correct_answer', 'correct_text')
        } | {
            'source': question.get('source', 'MCQ-Final assessment-Metabolic biochem Year 2-Alone.pdf'),
            'lesson': question.get('lesson', ''),
        })
    data = json.dumps(list(subjects.values()), ensure_ascii=False, indent=2)
    digest = hashlib.sha256(data.encode('utf-8')).hexdigest()
    template = (ROOT / 'google_forms_template.js').read_text(encoding='utf-8')
    script = template.replace('__MCQ_SUBJECTS__', data).replace('__MCQ_EXPORT_HASH__', digest)
    output = ROOT / 'google_forms_mcq.gs'
    output.write_text(script, encoding='utf-8')
    print(f'Generated {output.name}: {len(questions)} questions in {len(subjects)} separate quizzes')


if __name__ == '__main__':
    main()
