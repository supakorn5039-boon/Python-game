import unittest
from unittest.mock import patch
import random


# Function to simulate rolling the dice
def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


class TestDiceGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', 'y', 'y', 'n', 'y', 'n', 'n'])
    @patch('random.randint', side_effect=[5, 1, 6, 4, 2, 1, 1, 5])
    def test_gameplay(self, mock_randint, mock_input):
        # Test the main game logic
        player_scores = [0, 0, 0]
        expected_scores = [5, 6, 2]  # Based on the mocked rolls and input

        # Simulating a single round of play
        for player_idx in range(3):
            current_score = 0
            while True:
                should_roll = input("Would you like to roll (y/n): ")
                if should_roll.lower() != 'y':
                    break
                value = roll()
                if value == 1:
                    current_score = 0
                    break
                current_score += value

            player_scores[player_idx] += current_score

        print(f"Player scores: {player_scores}")  # Debugging output
        self.assertEqual(player_scores, expected_scores)

    @patch('builtins.input', side_effect=['1', '0', '5', '2'])
    def test_invalid_player_input(self, mock_input):
        # Test handling of invalid player input
        player = 0
        while True:
            player = input("Enter the number of players (2 - 4): ")
            if player.isdigit():
                player = int(player)
                if 2 <= player <= 4:
                    break
                else:
                    print("Must be between 2 - 4 players")
            else:
                print("Invalid, try again.")

        self.assertEqual(player, 2)

    @patch('builtins.input', side_effect=['4'])
    def test_valid_player_input(self, mock_input):
        # Test handling of valid player input
        player = input("Enter the number of players (2 - 4): ")
        self.assertEqual(int(player), 4)


if __name__ == '__main__':
    unittest.main()
