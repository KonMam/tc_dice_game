import random
from typing import List
from array import array


class Dice:
    def __init__(self, sides: int) -> None:
        if sides in range(1, 101):
            self.sides = sides
        else:
            raise ValueError("Number of sides should be between 1 and 100")

    def __repr__(self) -> str:
        return f"Dice({self.sides})"

    def __str__(self) -> str:
        return f"A {self.sides}-sided dice."


class DiceRoller:
    def __init__(self, dice_list: List[Dice]) -> None:
        self.dice_list = dice_list
        self.last_100_rolls = array("i", [])

    def throw(self):
        for dice in self.dice_list:
            roll = random.randint(1, dice.sides)

            if len(self.last_100_rolls) == 100:
                self.last_100_rolls.pop(0)

            self.last_100_rolls.append(roll)

    def multiple_throws(self, number_of_throws: int):
        for i in range(number_of_throws):
            self.throw()

    def save_rolls_to_file(self, file_name: str) -> None:
        with open(f"{file_name}.bin", "wb") as f:
            self.last_100_rolls.tofile(f)

    def load_rolls_from_file(self, file_name: str) -> None:
        try:
            with open(f"{file_name}.bin", "rb") as f:
                self.last_100_rolls.fromfile(f, 100)
            print("Loaded data for last 100 rolls.")
        except EOFError:
            print("Loaded all available data from the file.")


if __name__ == "__main__":
    dice_list = [Dice(6), Dice(20), Dice(100)]
    # Create a DiceRoller instance
    dice_roller = DiceRoller(dice_list)

    dice_roller.load_rolls_from_file("rolls")

    dice_roller.multiple_throws(100)

    dice_roller.save_rolls_to_file("rolls")

    # Display the last 100 rolls
    print("Last 100 Rolls:")
    for roll in dice_roller.last_100_rolls:
        print(roll)


# TODO:
# Save and read last_100_rolls from a file ✅
# Add support for 1 to 100 dice
# Multiple dice throws support
# Documentation
# Unit Tests
# Web API
# Support for weighted Dice
