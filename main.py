from fastapi import FastAPI
from dice import Dice, RollHistory, DiceRoller
from collections import deque

app = FastAPI()

dice_list = deque([], maxlen=5)
roll_history = RollHistory()
dice_roller = DiceRoller(dice_list, roll_history)


@app.post("/add-dice")
async def add_dice(sides: int):
    dice = Dice(sides)
    dice_list.append(dice)
    return {
        "message": f"{dice} has been added to the dice list. Current list: {list(dice_list)}"
    }


@app.post("/clear-dice")
async def clear_dice():
    dice_list.clear()
    return {
        "message": f"Dice list has been cleared. Please add new dices using '/add-dice' endpoint."
    }


@app.post("/roll-dice/{number_of_rolls}")
async def roll_dice(number_of_rolls: int):
    dice_roller.roll_multiple_times(number_of_rolls)
    return {"message": f"Rolled dice {number_of_rolls} times."}


@app.get("/last-rolls/{n}")
async def get_last_rolls(n: int):
    rolls = dice_roller.roll_history.get_last_rolls(n)
    return {"last_rolls": rolls}


@app.post("/save-rolls")
async def save_rolls(file_name: str = "rolls"):
    dice_roller.save_rolls_to_file(file_name)
    return {"message": f"Rolls saved to {file_name}.bin"}


@app.post("/load-rolls")
async def load_rolls(file_name: str = "rolls"):
    dice_roller.load_rolls_from_file(file_name)
    return {"message": f"Rolls loaded from {file_name}.bin"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)


# TODO:
# Support from 1 to 5 dice. ✅
# 1 to 100 sides ✅
# Rolling the dice one or more times ✅
# Returning the values of the dice. ✅
# Store the information about the last 100 rolls ✅
# Documentation ✅
# Unit Tests ✅
# Web API (USE FASTAPI) ✅
# Support for weighted Dice


# IMPROVEMENTS:
# - Storing last 100 rolls with more info about what kind of dice, etc.. Maybe as key value pairs
# - CLI for using the dice roller
# - Using a more user friendly format for saving files (just wanted to test arrays for this, thus .bin)
# - Making the code more modular using ABC, Design Paterns...
# - Change the return value of roll_multiple_times method to better suit the web API and directly return the results.
# - Add requirements.txt
