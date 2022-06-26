import random
from high_low_art import logo
import os


def clear():
    return os.system('cls')


print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

computer_think = random.randint(1, 101)
print(f"I am thinking {computer_think}")

user = input("Choose a difficulty. Type 'easy' or 'hard': ")
if user == "easy":
    print("You have 10 attempts remaining to guess the number.")
    guesses = 10

    while True:

        user_num = int(input("Guess: "))
        if user_num > computer_think:
            print("Too High")
        elif user_num < computer_think:
            print("Too Low")
        else:
            print("Correct")
            break

        guesses -= 1
        print(f"You have {guesses} attempts remaining to guess the number.")
        if guesses == 0:
            print("You Lose!")
            break
else:
    print("You have 5 attempts remaining to guess the number.")
    guesses = 5

    while True:

        user_num = int(input("Guess: "))
        if user_num > computer_think:
            print("Too High")
        elif user_num < computer_think:
            print("Too Low")
        else:
            print("Correct")
            break

        guesses -= 1
        print(f"You have {guesses} attempts remaining to guess the number.")
        if guesses == 0:
            print("You Lose!")

            break
