import random

def logo():
    return r"""
  ____    _     _____                        _                  
 |  _ \  (_)   |  __ \                      | |                 
 | |_) |  _    | |  | |   __ _   _ __     __| |   ___    _ __  
 |  _ <  | |   | |  | |  / _` | | '_ \   / _` |  / _ \  | '_ \ 
 | |_) | | |   | |__| | | (_| | | | | | | (_| | | (_) | | | | |
 |____/  |_|   |_____/   \__,_| |_| |_|  \__,_|  \___/  |_| |_|
"""

def welcome():
    print("Welcome to the game!")
    print("*" * 10)

def finish(computer_number, count):
    print("*" * 10)
    print(f"Computer number: {computer_number}\nFound it in {count} tries!")
    print()
    answer = input("Would you like to play again? (y/n): ")
    if answer.lower() == "y":
        return True
    else:
        return False

def win(computer_number, guess):
    return computer_number == guess

def answer(computer_number, guess):
    if computer_number > guess:
        return 'My number is larger'
    elif computer_number < guess:
        return 'My number is smaller'
    return 'Correct!'

def get_a_guess():
    while True:
        try:
            guess = int(input('What is your guess? '))
            if 1 <= guess <= 20:
                return guess
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print(logo())
welcome()
continue_playing = True

while continue_playing:
    computer_number = random.randint(1, 20)
    guess = 0
    count = 0

    while not win(computer_number, guess):
        guess = get_a_guess()
        count += 1
        print(answer(computer_number, guess))

    continue_playing = finish(computer_number, count)