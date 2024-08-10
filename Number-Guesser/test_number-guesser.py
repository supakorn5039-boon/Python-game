import unittest
from unittest.mock import patch

from number_guesser import get_user_input, is_positive_integer, get_valid_number


class TestGuessingGame(unittest.TestCase):

    def test_is_positive_integer(self):
        self.assertTrue(is_positive_integer("10"))  # Valid positive integer
        self.assertFalse(is_positive_integer("0"))  # Zero is not positive
        self.assertFalse(is_positive_integer("-10"))  # Negative number
        self.assertFalse(is_positive_integer("abc"))  # Non-numeric string
        self.assertFalse(is_positive_integer(""))  # Empty string

    @patch('builtins.input', side_effect=['10'])
    def test_get_user_input_valid(self, mock_input):
        # Testing get_user_input with valid input
        result = get_user_input("Enter a number: ", is_positive_integer)
        self.assertEqual(result, '10')

    @patch('builtins.input', side_effect=['abc', '10'])
    def test_get_user_input_invalid_then_valid(self, mock_input):
        # Testing get_user_input with invalid followed by valid input
        result = get_user_input("Enter a number: ", is_positive_integer)
        self.assertEqual(result, '10')

    @patch('builtins.input', side_effect=['10'])
    def test_get_valid_number(self, mock_input):
        # Testing get_valid_number with valid input
        result = get_valid_number("Enter a number: ")
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
