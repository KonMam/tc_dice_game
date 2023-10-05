# Dice Roller Project

This is a Python project that simulates rolling dice with different numbers of sides and manages a history of rolls. 

## Project Structure

The project consists of three main classes: `Dice`, `RollHistory`, and `DiceRoller`. Here's an overview of each class and its purpose:

### Dice Class

The `Dice` class represents a single dice with a specific number of sides. You can create a `Dice` object with the desired number of sides, and it will ensure that the number of sides is between 1 and 100.

Example Usage:
```python
# Create a 6-sided dice
dice = Dice(6)
```

### WeightedDice Class

The `WeightedDice` class represents a single dice with a specific number of sides that might be weighted. You can create a `WeightedDice` object with the desired number of sides, and it will ensure that the number of sides is between 1 and 100 and that weights add up to a 100.

Example Usage:
```python
# Create a 6-sided dice
dice = WeightedDice(6, [0.1, 0.8, 0.1, 0, 0, 0])
```

### RollHistory Class

The `RollHistory` class is responsible for managing the history of dice rolls. It can store a specified number of rolls and provides methods for adding rolls, retrieving the last rolls, and saving/loading the roll history to/from a binary file.

Example Usage:
```python
# Create a RollHistory object with a maximum history size of 100
roll_history = RollHistory(100)

# Add a roll to the history
roll_history.add_roll(5)

# Retrieve the last 10 rolls
last_rolls = roll_history.get_last_rolls(10)
```

### DiceRoller Class

The `DiceRoller` class is the core of the project. It allows you to simulate rolling multiple dice, save and load roll history, and display the last rolls. You can create a `DiceRoller` object by providing a list of `Dice` objects and a `RollHistory` object.

Example Usage:
```python
# Create a list of Dice objects and a RollHistory object
dice_list = deque([Dice(6), Dice(20), Dice(100)])
roll_history = RollHistory()

# Create a DiceRoller object
dice_roller = DiceRoller(dice_list, roll_history)

# Simulate rolling the dice
dice_roller.roll_multiple_times(3)

# Save the roll history to a file
dice_roller.save_rolls_to_file()

# Load the roll history from a file
dice_roller.load_rolls_from_file()

# Display the last 10 rolls
dice_roller.display_last_rolls(10)
```

### FastAPI Integration
The project includes a FastAPI app that exposes endpoints for interacting with the dice rolling functionality through HTTP requests. Below are the endpoints you can use:

POST /add-dice: Adds a new dice to the list of dice with a specified number of sides.

POST /clear-dice: Clears the list of dices.

POST /roll-dice/{number_of_rolls}: Simulates rolling the dice a specified number of times.

GET /last-rolls/{n}: Retrieves the last n rolls from the roll history.

POST /save-rolls: Saves the roll history to a binary file.

POST /load-rolls: Loads roll history from a binary file.

## Getting Started

To use this project, follow these steps:

1. Import the necessary classes: `Dice`, `RollHistory`, and `DiceRoller`.
2. Create `Dice` objects with the desired number of sides and add them to a list.
3. Create a `RollHistory` object with the desired maximum history size.
4. Create a `DiceRoller` object by providing the list of `Dice` objects and the `RollHistory` object.
5. Use the `DiceRoller` methods to simulate dice rolls, manage history, and display results.

## File Management

The project allows you to save and load roll history to/from a binary file. By default, the file name is "rolls.bin," but you can specify a different name if needed.

To save roll history to a file:
```python
dice_roller.save_rolls_to_file()
```

To load roll history from a file:
```python
dice_roller.load_rolls_from_file()
```

## Example Usage

A complete example of using the project is provided in the `main()` function at the end of the code. It creates a `DiceRoller` object, simulates rolling dice, saves and loads roll history, and displays the last rolls.
