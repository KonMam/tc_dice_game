import unittest
from unittest.mock import patch
from io import StringIO
from main import Dice, DiceRoller

class TestDice(unittest.TestCase):
    def test_valid_sides(self):
        dice = Dice(6)
        self.assertEqual(dice.sides, 6)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            Dice(0)

    def test_repr(self):
        dice = Dice(20)
        self.assertEqual(repr(dice), "Dice(20)")

    def test_str(self):
        dice = Dice(10)
        self.assertEqual(str(dice), "A 10-sided dice.")

class TestDiceRoller(unittest.TestCase):
    def setUp(self):
        self.dice_list = [Dice(6), Dice(10)]
        self.roller = DiceRoller(self.dice_list)

    @patch('sys.stdout', new_callable=StringIO)
    def test_throw(self, mock_stdout):
        self.roller.throw()
        output = mock_stdout.getvalue().strip()
        self.assertTrue(all(int(roll) in range(1, 7) or int(roll) in range(1, 11) for roll in output.split()))

    def test_multiple_throws(self):
        self.roller.multiple_throws(5)
        self.assertEqual(len(self.roller.last_100_rolls), 10)

    def test_save_and_load_rolls(self):
        file_name = "test_rolls"
        self.roller.multiple_throws(100)
        self.roller.save_rolls_to_file(file_name)
        self.roller.load_rolls_from_file(file_name)
        self.assertEqual(len(self.roller.last_100_rolls), 200)

if __name__ == "__main__":
    unittest.main()