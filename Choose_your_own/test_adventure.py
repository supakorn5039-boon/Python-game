import unittest
from unittest.mock import patch
from Choose_your_own_adventure import adventure_game


class TestAdventureGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['John', 'left', 'walk'])
    @patch('builtins.print')
    def test_left_walk(self, mock_print, mock_input):
        adventure_game()
        expected_output = [
            'Welcome John to this adventure!',
            'You walked for many miles, ran out of water and you lost the game!!',
            'Thank you for trying, John!'
        ]
        actual_output = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['Alice', 'right', 'back'])
    @patch('builtins.print')
    def test_right_back(self, mock_print, mock_input):
        adventure_game()
        expected_output = [
            'Welcome Alice to this adventure!',
            'You go back and lose!!',
            'Thank you for trying, Alice!'
        ]
        actual_output = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=['Bob', 'left', 'swim'])
    @patch('builtins.print')
    def test_left_swim(self, mock_print, mock_input):
        adventure_game()
        expected_output = [
            'Welcome Bob to this adventure!',
            'You swim across and were eaten by an alligator.',
            'Thank you for trying, Bob!'
        ]
        actual_output = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
