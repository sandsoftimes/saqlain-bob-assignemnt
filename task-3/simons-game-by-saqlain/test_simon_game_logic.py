import unittest
from simon_game import SimonGameLogic

class TestSimonGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = SimonGameLogic()

    def test_start_game(self):
        sequence = self.game.start_game()
        self.assertIsInstance(sequence, list)
        self.assertEqual(len(sequence), 1)

    def test_check_sequence_correct(self):
        self.game.start_game()
        color = self.game.sequence[0]
        score = self.game.check_sequence(color)
        self.assertEqual(score, 1)

    def test_check_sequence_wrong(self):
        self.game.start_game()
        correct_color = self.game.sequence[0]
        wrong_color = "black"  # Assuming "black" is not in the sequence
        result = self.game.check_sequence(wrong_color)
        self.assertEqual(result, -1)

    def test_sequence_length_increase(self):
        self.game.start_game()
        initial_sequence_length = len(self.game.sequence)
        self.game.add_to_sequence()
        self.assertEqual(len(self.game.sequence), initial_sequence_length + 1)

    def test_get_colors(self):
        colors = self.game.get_colors()
        self.assertIsInstance(colors, list)
        self.assertEqual(len(colors), 4)

if __name__ == '__main__':
    unittest.main()

