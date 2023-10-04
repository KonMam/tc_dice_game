import unittest
import os
from collections import deque
from main import Dice, RollHistory, DiceRoller


class TestDice(unittest.TestCase):
    def test_dice_creation_valid(self):
        # Test creating a dice with valid sides
        dice = Dice(6)
        self.assertEqual(dice.sides, 6)

    def test_dice_creation_invalid(self):
        # Test creating a dice with invalid sides (should raise ValueError)
        with self.assertRaises(ValueError):
            Dice(0)


class TestRollHistory(unittest.TestCase):
    def setUp(self):
        self.roll_history = RollHistory()

    def test_add_roll(self):
        # Test adding a roll to the history
        self.roll_history.add_roll(4)
        self.assertEqual(list(self.roll_history.last_rolls), [4])

    def test_get_last_rolls(self):
        # Test getting the last n rolls from the history
        for i in range(1, 11):
            self.roll_history.add_roll(i)
        last_rolls = self.roll_history.get_last_rolls(5)
        self.assertEqual(last_rolls, [6, 7, 8, 9, 10])

    def test_save_and_load_from_file(self):
        # Test saving and loading roll history from a file
        self.roll_history.add_roll(4)
        self.roll_history.save_to_file("test_rolls")
        loaded_history = RollHistory()
        loaded_history.load_from_file("test_rolls")
        self.assertEqual(list(loaded_history.last_rolls), [4])

    def tearDown(self):
        # Clean up test files
        if os.path.exists("test_rolls.bin"):
            os.remove("test_rolls.bin")


class TestDiceRoller(unittest.TestCase):
    def setUp(self):
        dice_list = deque([Dice(6), Dice(5)], maxlen=5)
        roll_history = RollHistory()
        self.dice_roller = DiceRoller(dice_list, roll_history)

    def test_roll(self):
        # Test throwing the dice
        self.dice_roller.roll()
        last_rolls = list(self.dice_roller.roll_history.last_rolls)
        self.assertTrue(all(1 <= roll <= 6 for roll in last_rolls))

    def test_roll_multiple_times(self):
        # Test rolling the dice multiple times
        self.dice_roller.roll_multiple_times(3)
        last_rolls = list(self.dice_roller.roll_history.last_rolls)
        self.assertEqual(len(last_rolls), 6)  # 3 rolls for each of 2 dice

    def tearDown(self):
        # Clean up test files
        if os.path.exists("test_rolls.bin"):
            os.remove("test_rolls.bin")


if __name__ == "__main__":
    unittest.main()
