from random import random
from typing import List
from collections import deque


class Dice:
    def __init__(self, sides: int) -> None:
        if sides in range(1, 100):
            self.sides = sides
        else:
            raise ValueError("Number of sides should be between 1 and 100")

    def roll(self):
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        return f"Dice({self.sides})"

    def __str__(self) -> str:
        return f"A {self.sides}-sided dice."


class DiceRoller:
    def __init__(self, dice_list: List[Dice]) -> None:
        self.dice_list = dice_list
        self.last_100_rolls = deque([],100)

    def roll(self):
        for dice in self.dice_list:
            roll = random.randint(1, dice.sides)
            if len(self.last_100_rolls) == 100:
                self.last_100_rolls.popleft()
            self.last_100_rolls.append(roll)


            


if __name__ == "__main__":
    dice = Dice(6)
    print(dice)



# TODO: 
# Save and read last_100_rolls from a file
# Add support for 1 to 100 dice
# Multiple dice throws support
# Documentation
# Unit Tests
# Web API
# Support for weighted Dice