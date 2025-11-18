import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

random_number = random.randint(1, 10)
user_guess_count = 0

while True:
    user_guess = int(input("Guess a number between 1 and 10: "))
    user_guess_count += 1
    clear_console()

    if user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number and user_guess <= 10:
        print("Too high! Try again.")
    elif user_guess > 10:
        print("Your guess is out of bounds! Please guess a number between 1 and 10.")
    else: 
        print(f"Congratulations! You've guessed the number {random_number} in {user_guess_count} attempts.")
        break