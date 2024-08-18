import unittest
from unittest.mock import patch
import io
import sys
import project

class TestPersonalityQuiz(unittest.TestCase):

    def setUp(self):
        project.s = 0
        project.c = 0
        project.m = 0
        project.p = 0

    def test_question_one(self):
        with patch('builtins.input', return_value='1'):
            project.question_one()
            self.assertEqual(project.s, 1)
            self.assertEqual(project.c, 0)
            self.assertEqual(project.m, 0)
            self.assertEqual(project.p, 0)

    def test_question_two(self):
        with patch('builtins.input', return_value='4'):
            project.question_two()
            self.assertEqual(project.s, 0)
            self.assertEqual(project.c, 1)
            self.assertEqual(project.m, 0)
            self.assertEqual(project.p, 0)

    def test_question_one_invalid_input(self):
        with patch('builtins.input', side_effect=['5', '1']):
            project.question_one()
            self.assertEqual(project.s, 1)

    def test_result(self):
        project.s = 1
        project.c = 0
        project.m = 0
        project.p = 0
        with patch('builtins.input', return_value='n'):
            captured_output = io.StringIO()
            sys.stdout = captured_output
            project.result()
            sys.stdout = sys.__stdout__
            self.assertIn("SANGUINE", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
