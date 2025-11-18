import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

users_guess_count = 0

while True:
    choice = input("Which math operation would you like to use? (+, -, *, /)")
    if choice not in ['+', '-', '*', '/']:
        print("Invalid operation! Please choose from +, -, *, /.")
        continue
    elif choice == '+':
        math_operator = "+"
    elif choice == '-':
        math_operator = "-"
    elif choice == '*':
        math_operator = "*"
    elif choice == '/':
        math_operator = "/"

    choice = input("Do you Want to play in Easy, Medium or Hard mode? (E/M/H): ").strip().upper()
    if choice == "E":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    elif choice == "M":
        a = random.randint(11, 100)
        b = random.randint(11, 100)
    elif choice == "H":
        a = random.randint(101, 1000)
        b = random.randint(101, 1000)

    if math_operator == "+":
        correct_answer = a + b
    elif math_operator == "-":
        correct_answer = a - b
    elif math_operator == "*":
        correct_answer = a * b
    elif math_operator == "/":
        correct_answer = a / b

    while True:
    
        try:
            users_answer = int(input(f"What is {a} {math_operator} {b}? "))
        except ValueError:
            print("Please enter ONLY a number.")
            continue

        users_guess_count += 1

        if users_answer == (f"{correct_answer}"):
            print(f"Correct! It takes you {users_guess_count} attempts.")
            break
        else:
            print("Incorrect! Try again.")
    
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice == "no":
        print("Thanks for playing!")
        break 
    else:
        clear_console()                    
