from unicodedata import name
from high_low_data import data
from high_low_art import logo, vs
import random
import os


def clear():
    return os.system('cls')


def random_a():
    choice_a = random.choice(data)
    name_a = choice_a['name']
    description_a = choice_a['description']
    country_a = choice_a['country']
    print(f"Compare A: {name_a}, {description_a}, {country_a}")
    global follower_a
    follower_a = choice_a['follower_count']
    print(follower_a)


def random_b():
    choice_b = random.choice(data)
    name_b = choice_b['name']
    description_b = choice_b['description']
    country_b = choice_b['country']
    print(f"Compare B: {name_b}, {description_b}, {country_b}")
    global follower_b
    follower_b = choice_b['follower_count']
    print(follower_b)


score = 0
while True:
    clear()
    print(logo)
    print(f"You're right! Current score:  {score}")
    random_a()
    print(vs)
    random_b()

    user_input = (input("Who has more followers? Type 'A' or 'B':  ")).upper()
    if user_input == "A" and follower_a > follower_b:
        score += 1
        print(f"You're right! Current score:  {score}")
    elif user_input == "B" and follower_b > follower_a:
        score += 1
        print(f"You're right! Current score:  {score}")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score:  {score}")
        break
