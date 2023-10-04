import random
from array import array
from collections import deque


class Dice:
    """
    A class representing a dice with a specific number of sides.

    Args:
        sides (int): The number of sides on the dice.

    Raises:
        ValueError: If the number of sides is not between 1 and 100 (inclusive).

    Attributes:
        sides (int): The number of sides on the dice.
    """

    def __init__(self, sides: int) -> None:
        if sides in range(1, 101):
            self.sides = sides
        else:
            raise ValueError("Number of sides should be between 1 and 100")

    def __repr__(self) -> str:
        return f"Dice({self.sides})"

    def __str__(self) -> str:
        return f"{self.sides}-sided dice"


class DiceRoller:
    """
    A class for rolling multiple dice and managing the results.

    Args:
        dice_list (deque[Dice]): A deque containing Dice objects.

    Attributes:
        dice_list (deque[Dice]): A deque containing Dice objects.
        last_100_rolls (array): An array to store the results of the last 100 rolls.
    """
        
    def __init__(self, dice_list: deque[Dice]) -> None:
        self.dice_list = dice_list
        self.last_100_rolls = array("i", [])

    def throw(self):
        """
        Simulates throwing the dice in the dice_list and prints the results.
        If the number of stored rolls exceeds 100, the oldest roll is removed.
        """
        for dice in self.dice_list:
            roll = random.randint(1, dice.sides)
            print(f"Result of a {dice} roll is {roll}.")

            if len(self.last_100_rolls) == 100:
                self.last_100_rolls.pop(0)

            self.last_100_rolls.append(roll)

    def multiple_throws(self, number_of_throws: int):
        """
        Throws the dice multiple times and prints the results.

        Args:
            number_of_throws (int): The number of times to throw the dice.
        """
        print(f"Throwing dice {number_of_throws} times")
        for i in range(1, number_of_throws + 1):
            print(f"Throw {i}:")
            self.throw()

    def save_rolls_to_file(self, file_name: str) -> None:
        """
        Saves the last 100 rolls to a binary file.

        Args:
            file_name (str): The name of the file to save the rolls to.
        """
        with open(f"{file_name}.bin", "wb") as f:
            self.last_100_rolls.tofile(f)

    def load_rolls_from_file(self, file_name: str) -> None:
        """
        Loads the last 100 rolls from a binary file, if available.

        Args:
            file_name (str): The name of the file to load the rolls from.
        """
        try:
            with open(f"{file_name}.bin", "rb") as f:
                self.last_100_rolls.fromfile(f, 100)
            print("Loaded data for last 100 rolls.")
        except EOFError:
            print("Loaded all available data from the file.")
        except FileNotFoundError:
            print("Data for rolls does not exist.")
            pass

    def show_last_n_rolls(self, n: int):
        print(f"Last {n} rolls:")
        rolls = list(self.last_100_rolls[-n:])
        rolls_str = ', '.join(map(str, rolls))
        print(rolls_str)


def main():
    dice_list = deque([Dice(6), Dice(20), Dice(100), Dice(13)], maxlen=5)

    dice_roller = DiceRoller(dice_list)

    dice_roller.load_rolls_from_file("rolls")

    dice_roller.multiple_throws(10)

    dice_roller.save_rolls_to_file("rolls")

    dice_roller.show_last_n_rolls(20)


if __name__ == "__main__":
    main()
    


# TODO:
# Support from 1 to 5 dice. ✅
# 1 to 100 sides ✅
# Throwing the dice one or more times ✅
# Returning the values of the dice. ✅
# Store the information about the last 100 throws ✅ Maybe store as k(dice sides):v pairs, 
# Documentation
# Unit Tests
# Web API
# Support for weighted Dice
# Improvement suggestions