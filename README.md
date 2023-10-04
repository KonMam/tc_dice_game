# Dice Roller

This Python script allows you to simulate rolling dice with various numbers of sides and manage a history of your rolls. 

## Features

- Simulate rolling dice with different numbers of sides.
- Keep track of your roll history.
- Load and save roll history to a binary file.
- Display the last N rolls from your history.

## Usage

TBD

## Classes and Functions

### `Dice` Class

- Represents a dice with a specific number of sides.
- Takes the number of sides as an argument during initialization.
- Ensures that the number of sides is between 1 and 100 (inclusive).

### `RollHistory` Class

- Manages the history of dice rolls.
- Stores the last rolls in an array.
- Provides methods to add rolls, retrieve the last N rolls, load roll history from a file, and save roll history to a file.

### `DiceRoller` Class

- Simulates rolling dice using a list of `Dice` objects.
- Manages roll history using a `RollHistory` object.
- Provides methods to throw dice, perform multiple throws, save roll history to a file, load roll history from a file, and display the last N rolls.

## Example Usage

```python
# Create a list of dice with different numbers of sides
dice_list = deque([Dice(6), Dice(20), Dice(100), Dice(13)], maxlen=5)

# Initialize a roll history
roll_history = RollHistory()

# Create a DiceRoller object
dice_roller = DiceRoller(dice_list, roll_history)

# Load roll history from a file (if available)
dice_roller.load_rolls_from_file("rolls")

# Simulate multiple throws of dice
dice_roller.multiple_throws(25)

# Save roll history to a file
dice_roller.save_rolls_to_file("rolls")

# Display the last 100 rolls
dice_roller.show_last_n_rolls(100)
```
