import unittest

from build_mona_data import read_mona_questions


class MonaDataTests(unittest.TestCase):
    def test_complete_answer_key(self):
        questions = read_mona_questions()
        self.assertEqual(len(questions), 40)
        self.assertEqual([q['question_id'] for q in questions], list(range(1, 41)))
        for q in questions:
            self.assertEqual(q['lecture_id'], 3)
            self.assertEqual(set(q['options']), set('ABCD'))
            self.assertEqual(q['correct_text'], q['options'][q['correct_answer']])
            self.assertNotIn('Correct answer:', q['question'])
            self.assertTrue(all('Correct answer:' not in value for value in q['options'].values()))
        self.assertEqual(questions[0]['correct_answer'], 'B')
        self.assertEqual(questions[0]['correct_text'], 'Stop blood loss after blood vessel injury')
        self.assertEqual(questions[3]['options']['D'], 'Prevent all coagulation')
        self.assertEqual(questions[4]['options']['D'], 'Hemoglobin')
        self.assertEqual(questions[34]['correct_text'], 'Easy bruising and nosebleeds')
        self.assertEqual(questions[37]['correct_text'],
                         'It consumes platelets and clotting factors while causing widespread clot formation')
        self.assertEqual(questions[-1]['correct_text'], 'Treat the underlying cause')


if __name__ == '__main__':
    unittest.main()
