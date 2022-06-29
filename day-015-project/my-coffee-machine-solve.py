import os


def clear():
    return os.system('cls')


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee_machine():

    print("Please insert coins.")
    global total

    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    if total >= 1.5 and user_coffee == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        total -= 1.5
        print(f"Here is {round(total, 2)} in change.")
        total = 0
        print("Here is your espresso ☕. Enjoy!")

    elif total >= 2.5 and user_coffee == "latte":
        total -= 2.5
        print(f"Here is {round(total, 2)} in change.")
        total = 0
        print("Here is your Latte ☕. Enjoy!")
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]

    elif total >= 3.0 and user_coffee == "cappuccino":
        total -= 3.0
        print(f"Here is {round(total, 2)} in change.")
        total = 0
        print("Here is your Cappuccino ☕. Enjoy!")
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

    else:
        print("Sorry that's not enough money. Money refunded.")


def check_ingredients():

    if user_coffee == "espresso" and resources["water"] < 50:
        print("Sorry there is not enough water.")
    elif user_coffee == "latte" and resources["water"] < 200:
        print("Sorry there is not enough water.")
    elif user_coffee == "cappuccino" and resources["water"] < 250:
        print("Sorry there is not enough water.")
    elif user_coffee == "latte" and resources["milk"] < 150:
        print("Sorry there is not enough milk.")
    elif user_coffee == "cappuccino" and resources["milk"] < 100:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < 18:
        print("Sorry there is not enough coffee.")
    else:
        print("Please type the correct command.")


is_on = True

while is_on:

    user_coffee = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if user_coffee == "off":
        clear()
        #! can also write like this --> is_on = False
        print("The Coffee Machine is shutting down... ")
        break

    elif user_coffee == "report":
        print(
            f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")

    elif user_coffee == "espresso" and resources["water"] > MENU["espresso"]["ingredients"]["water"] and resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
        coffee_machine()
        continue

    elif user_coffee == "latte" and resources["water"] > MENU["latte"]["ingredients"]["water"] and resources["coffee"] > MENU["latte"]["ingredients"]["coffee"] and resources["milk"] > MENU["latte"]["ingredients"]["milk"]:
        coffee_machine()
        continue

    elif user_coffee == "cappuccino" and resources["water"] > MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] > MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] > MENU["cappuccino"]["ingredients"]["milk"]:
        coffee_machine()
        continue

    else:
        check_ingredients()
