Number Guessing Game 🎲
This Python program is an interactive Number Guessing Game, where players try to guess a randomly generated number between 1 and 20. The game provides feedback after each guess, indicating whether the target number is larger or smaller, and allows players to play multiple rounds.

Features 📋
- Logo Display: A custom ASCII logo is shown at the start of the program for a creative touch.
- Interactive Gameplay: Players receive real-time feedback on their guesses.
- Input Validation: Ensures players provide valid guesses within the range (1–20).
- Play Again Option: After completing a game, players can choose to play another round.
- Error Handling: Catches invalid inputs (e.g., non-numeric values) and prompts the user to try again.


How It Works 🚀
Step-by-step:
- The program starts by displaying a welcome message and a logo.
- The computer generates a random number between 1 and 20.
- The player guesses numbers, and the program provides feedback:- "My number is larger" if the guess is too low.
- "My number is smaller" if the guess is too high.
- "Correct!" when the guess matches the computer's number.

- Once the number is guessed, the program:- Shows the computer's number and the number of attempts.
- Offers the player the option to play another round.



Installation 📦
Requirements:
- Python 3.x

Instructions:
- Clone the repository:git clone https://github.com/yourusername/number-guessing-game.git

- Navigate to the project directory:cd number-guessing-game

- Run the Python script:python game.py



Code Explanation 🛠
Functions:
- logo(): Displays the game's ASCII logo.
- welcome(): Prints a welcome message and decorative lines.
- finish(computer_number, count): Displays the result of the game and checks if the player wants to replay.
- win(computer_number, guess): Determines if the player has guessed the correct number.
- answer(computer_number, guess): Provides feedback based on the player's guess.
- get_a_guess(): Validates the player's input and ensures it falls within the range.

Main Gameplay Loop:
- The game continues in the while continue_playing loop until the player chooses to quit.
- The guessing logic is implemented in the inner while not win(computer_number, guess) loop.


Example Output 📄
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
What is your guess? 12
Correct!
**********
Computer number: 12
Found it in 3 tries!

Would you like to play again? (y/n): n



Contributing 🤝
Contributions are welcome! If you'd like to add new features, optimize the code, or fix issues:
- Fork the repository.
- Create a new branch:git checkout -b feature-name

- Commit and push your changes.
- Create a pull request.
