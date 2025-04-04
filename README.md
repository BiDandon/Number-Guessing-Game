
# Number Guessing Game


A simple yet entertaining number guessing game written in Python where the player tries to guess a randomly generated number between 1 and 20.

## Features

- Clean console interface with ASCII art
- Input validation to prevent errors
- Hint system ("higher/lower") to guide the player
- Attempt counter to track performance
- Play-again functionality

## How to Play

1. The computer generates a random number between 1 and 20
2. You guess what the number is
3. The computer tells you if your guess is higher or lower than the secret number
4. Keep guessing until you find the correct number
5. The game shows how many attempts you took
6. Choose to play again or quit

## Requirements

- Python 3.x

## Installation

No installation required! Just run the script directly:

```bash
python number_guesser.py
```

## Code Structure

- `logo()` - Displays the game's ASCII art logo
- `welcome()` - Shows welcome message
- `get_a_guess()` - Handles player input with validation
- `answer()` - Provides higher/lower feedback
- `win()` - Checks for correct guess
- `finish()` - Handles end-game flow and replay option

## Example Gameplay

```
  ____    _     _____                        _                  
 |  _ \  (_)   |  __ \                      | |                 
 | |_) |  _    | |  | |   __ _   _ __     __| |   ___    _ __  
 |  _ <  | |   | |  | |  / _` | | '_ \   / _` |  / _ \  | '_ \ 
 | |_) | | |   | |__| | | (_| | | | | | | (_| | | (_) | | | | |
 |____/  |_|   |_____/   \__,_| |_| |_|  \__,_|  \___/  |_| |_|

Welcome to the game!
**********
What is your guess? 10
My number is larger
What is your guess? 15
My number is smaller
What is your guess? 13
Correct!
**********
Computer number: 13
Found it in 3 tries!

Would you like to play again? (y/n): n
```

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your improvements.
