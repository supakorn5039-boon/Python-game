import unittest
from unittest.mock import patch
from io import StringIO
from quiz_game import play_quiz


class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.questions = {
            "What does CPU stand for? ": "central processing unit",
            "What does GPU stand for? ": "graphics processing unit",
            "What does RAM stand for? ": "random access memory",
            "What does PSU stand for? ": "power supply"
        }

    @patch('builtins.input', side_effect=[
        "yes", "central processing unit", "graphics processing unit",
        "random access memory", "power supply"
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_quiz_correct(self, mock_stdout, mock_input):
        play_quiz()
        output = mock_stdout.getvalue().strip().split('\n')

        self.assertIn("You got 4 questions correct!", output)
        self.assertIn("Your score is 100.0%", output)

    @patch('builtins.input', side_effect=[
        "yes", "wrong answer", "another wrong answer",
        "yet another wrong answer", "last wrong answer"
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_quiz_incorrect(self, mock_stdout, mock_input):
        play_quiz()
        output = mock_stdout.getvalue().strip().split('\n')

        self.assertIn("You got 0 questions correct!", output)
        self.assertIn("Your score is 0.0%", output)


if __name__ == '__main__':
    unittest.main()
