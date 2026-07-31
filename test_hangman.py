import unittest
from unittest.mock import patch
import io
import sys
import hangman

class TestHangman(unittest.TestCase):
    def test_display_word(self):
        self.assertEqual(hangman.display_word("apple", set()), "_ _ _ _ _")
        self.assertEqual(hangman.display_word("apple", {"a", "p"}), "A P P _ _")
        self.assertEqual(hangman.display_word("apple", {"a", "p", "l", "e"}), "A P P L E")
        self.assertEqual(hangman.display_word("pizza", {"p", "i", "z", "a"}), "P I Z Z A")

    @patch('random.choice', return_value='apple')
    @patch('builtins.input', side_effect=['a', 'p', 'l', 'e'])
    def test_win_game(self, mock_input, mock_choice):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            hangman.play_hangman()
        finally:
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        self.assertIn("Word: _ _ _ _ _", output)
        self.assertIn("Word: A P P L E", output)
        self.assertIn("Congratulations!", output)
        self.assertIn("You Won!", output)
        self.assertIn("The Word is APPLE", output)

    @patch('random.choice', return_value='pizza')
    @patch('builtins.input', side_effect=['1', 'x', 'x', 'p', 'i', 'z', 'a'])
    def test_duplicate_and_invalid_inputs(self, mock_input, mock_choice):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            hangman.play_hangman()
        finally:
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        self.assertIn("Invalid input! Please enter a single alphabetic letter.", output)
        self.assertIn("You already guessed that letter.", output)

    @patch('random.choice', return_value='apple')
    @patch('builtins.input', side_effect=['q', 'w', 'r', 't', 'y', 'u'])
    def test_lose_game(self, mock_input, mock_choice):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            hangman.play_hangman()
        finally:
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        self.assertIn("Game Over", output)
        self.assertIn("Attempts Left: 0", output)
        self.assertIn("The correct word was APPLE", output)

if __name__ == '__main__':
    unittest.main()
