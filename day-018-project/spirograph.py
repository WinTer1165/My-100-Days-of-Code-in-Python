import random
from turtle import Turtle, Screen, colormode

a = Turtle()

# a.hideturtle()
a.speed(0)
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        a.color(random_color())
        a.circle(100)
        a.setheading(a.heading() + size_of_gap)


draw_spirograph(50)

screen = Screen()
screen.exitonclick()
