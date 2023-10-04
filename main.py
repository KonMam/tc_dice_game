import random
from array import array
from collections import deque
from typing import List


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
        if 1 <= sides <= 100:
            self.sides = sides
        else:
            raise ValueError("Number of sides should be between 1 and 100")

    def __repr__(self) -> str:
        return f"Dice({self.sides})"

    def __str__(self) -> str:
        return f"{self.sides}-sided dice"


class RollHistory:
    """
    Initialize a RollHistory object.

    Args:
        max_history_size (int): The maximum number of rolls to store in the history.

    Attributes:
        max_history_size (int): The maximum number of rolls to store.
        last_rolls (array): An array to store the roll history.
    """

    def __init__(self, max_history_size: int = 100) -> None:
        self.max_history_size = max_history_size
        self.last_rolls = array("i", [])

    def add_roll(self, roll: int) -> None:
        """
        Add a roll to the history.

        Args:
            roll (int): The value of the roll to be added.
        """
        if len(self.last_rolls) == self.max_history_size:
            self.last_rolls.pop(0)
        self.last_rolls.append(roll)

    def get_last_rolls(self, n: int) -> List[int]:
        """
        Get the last n rolls from the history.

        Args:
            n (int): The number of last rolls to retrieve.

        Returns:
            List[int]: A list of the last n rolls.
        """
        return list(self.last_rolls[-n:])

    def load_from_file(self, file_name: str) -> None:
        """
        Load roll history from a binary file.

        Args:
            file_name (str): The name of the file to load data from.
        """
        try:
            with open(f"{file_name}.bin", "rb") as f:
                self.last_rolls.fromfile(f, self.max_history_size)
            print("Loaded data for the last rolls.")
        except EOFError:
            print("Loaded all available data from the file.")
        except FileNotFoundError:
            print("Data for rolls does not exist.")
            pass

    def save_to_file(self, file_name: str):
        """
        Save roll history to a binary file.

        Args:
            file_name (str): The name of the file to save data to.
        """
        with open(f"{file_name}.bin", "wb") as f:
            self.last_rolls.tofile(f)


class DiceRoller:
    """
    Initialize a DiceRoller object.

    Args:
        dice_list (deque[Dice]): A deque containing Dice objects.
        roll_history (RollHistory): A RollHistory object to manage roll history.
    """

    def __init__(self, dice_list: deque[Dice], roll_history: RollHistory) -> None:
        self.dice_list = dice_list
        self.roll_history = roll_history

    def throw(self) -> "DiceRoller":
        """
        Simulate throwing the dice and store the result in roll history.

        Returns:
            DiceRoller: The DiceRoller object for method chaining.
        """
        for dice in self.dice_list:
            roll = random.randint(1, dice.sides)
            print(f"Result of a {dice} roll is {roll}.")
            self.roll_history.add_roll(roll)
        return self

    def roll_multiple_times(self, number_of_throws: int) -> "DiceRoller":
        """
        Simulate rolling the dice multiple times and print the results.

        Args:
            number_of_throws (int): The number of times to throw the dice.

        Returns:
            DiceRoller: The DiceRoller object for method chaining.
        """
        print(f"Throwing dice {number_of_throws} times")
        for i in range(1, number_of_throws + 1):
            print(f"Throw {i}:")
            self.throw()
        return self

    def save_rolls_to_file(self, file_name: str = "rolls") -> "DiceRoller":
        """
        Save the roll history to a binary file.

        Args:
            file_name (str): The name of the file to save roll history to. Defaults to 'rolls'.

        Returns:
            DiceRoller: The DiceRoller object for method chaining.
        """
        self.roll_history.save_to_file(file_name)
        return self

    def load_rolls_from_file(self, file_name: str = "rolls") -> "DiceRoller":
        """
        Load roll history from a binary file.

        Args:
            file_name (str): The name of the file to load data from.

        Returns:
            DiceRoller: The DiceRoller object for method chaining.
        """
        self.roll_history.load_from_file(file_name)
        return self

    def display_last_rolls(self, n: int) -> "DiceRoller":
        """
        Display the last n rolls from the roll history.

        Args:
            n (int): The number of last rolls to display.

        Returns:
            DiceRoller: The DiceRoller object for method chaining.
        """
        print(f"Last {n} rolls:")
        rolls = self.roll_history.get_last_rolls(n)
        rolls_str = ", ".join(map(str, rolls))
        print(rolls_str)
        return self


def main():
    dice_list = deque([Dice(6), Dice(20), Dice(100), Dice(13), Dice(99)], maxlen=5)
    roll_history = RollHistory()

    dice_roller = DiceRoller(dice_list, roll_history)

    dice_roller = DiceRoller(dice_list, roll_history)

    dice_roller.load_rolls_from_file().roll_multiple_times(
        3
    ).save_rolls_to_file().display_last_rolls(10)


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
