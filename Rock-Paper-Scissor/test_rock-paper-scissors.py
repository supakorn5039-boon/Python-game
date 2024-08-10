import unittest
from rock_paper_scissors import get_computer_choice, determine_winner


class TestRockPaperScissors(unittest.TestCase):
    def test_get_computer_choice(self):
        # Run the test multiple times to account for randomness
        for _ in range(100):
            choice = get_computer_choice()
            self.assertIn(choice, ['rock', 'paper', 'scissors'])

    def test_determine_winner(self):
        # Test scenarios where the user wins
        self.assertEqual(determine_winner('rock', 'scissors'), 'user')
        self.assertEqual(determine_winner('paper', 'rock'), 'user')
        self.assertEqual(determine_winner('scissors', 'paper'), 'user')

        # Test scenarios where the computer wins
        self.assertEqual(determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(determine_winner('rock', 'paper'), 'computer')
        self.assertEqual(determine_winner('paper', 'scissors'), 'computer')

        # Test scenarios where it's a draw
        self.assertEqual(determine_winner('rock', 'rock'), 'draw')
        self.assertEqual(determine_winner('paper', 'paper'), 'draw')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'draw')


if __name__ == "__main__":
    unittest.main()
