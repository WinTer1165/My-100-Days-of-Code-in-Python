from turtle import Turtle, Screen
import random
import turtle

red = Turtle()
red.color("red")
red.shape("turtle")
red.penup()

blue = Turtle()
blue.color("blue")
blue.shape("turtle")
blue.penup()

green = Turtle()
green.color("green")
green.shape("turtle")
green.penup()

purple = Turtle()
purple.color("purple")
purple.shape("turtle")
purple.penup()

black = Turtle()
black.color("black")
black.shape("turtle")
black.penup()

orange = Turtle()
orange.color("orange")
orange.shape("turtle")
orange.penup()

pink = Turtle()
pink.color("pink")
pink.shape("turtle")
pink.penup()

gold = Turtle()
gold.color("gold")
gold.shape("turtle")
gold.penup()

yellow = Turtle()
yellow.color("yellow")
yellow.shape("turtle")
yellow.penup()

screen = Screen()
screen.setup(800, 400)
user_bet = screen.textinput(
    "Make your bet", "Who will win the race? Enter a color: ")

red.goto(-380, 190)
blue.goto(-380, 142.5)
green.goto(-380, 95)
purple.goto(-380, 47.5)
black.goto(-380, 0)
orange.goto(-380, -47.5)
pink.goto(-380, -95)
gold.goto(-380, -142.5)
yellow.goto(-380, -185)


while True:
    red.forward(random.randint(0, 10))
    blue.forward(random.randint(0, 10))
    green.forward(random.randint(0, 10))
    purple.forward(random.randint(0, 10))
    black.forward(random.randint(0, 10))
    orange.forward(random.randint(0, 10))
    pink.forward(random.randint(0, 10))
    gold.forward(random.randint(0, 10))
    yellow.forward(random.randint(0, 10))

    if red.xcor() > 380:
        winning_color = red.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif blue.xcor() > 380:
        winning_color = blue.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif green.xcor() > 380:
        winning_color = green.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif purple.xcor() > 380:
        winning_color = purple.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif black.xcor() > 380:
        winning_color = black.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif orange.xcor() > 380:
        winning_color = orange.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif pink.xcor() > 380:
        winning_color = pink.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif gold.xcor() > 380:
        winning_color = gold.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break
    elif yellow.xcor() > 380:
        winning_color = yellow.pencolor()
        if winning_color == user_bet:
            print(f"You have won! The {winning_color} turtle is the winner.")
        else:
            print(f"You have lost! The {winning_color} turtle is the winner.")
            break


screen.exitonclick()
