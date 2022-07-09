from turtle import Turtle, Screen, colormode
import random

a = Turtle()

a.speed(0)
a.pensize(15)
a.hideturtle()
colormode(255)


def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a.pencolor(r, g, b)


def random_left_right():
    x = random.randint(0, 1)
    if x == 0:
        a.left(random.choice([0, 90, 180, 270]))
    elif x == 1:
        a.right(random.choice([0, 90, 180, 270]))


def move():
    a.forward(30)


while True:
    random_color()
    random_left_right()
    move()

# ! ALTERNATE SOLUTION :

# directions = [0, 90, 180, 270]
# a.pensize(15)
# a.speed("fastest")

# for _ in range(200):
#     a.color(random.choice(colours))
#     a.forward(30)
#     a.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
