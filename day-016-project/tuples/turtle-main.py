import turtle
from turtle import Screen, Turtle

# ? turtle docs - https://docs.python.org/3/library/turtle.html
# ? turtle colors - https://cs111.wellesley.edu/reference/colors
#! I accidentally deleted my tuple experimental files :( and I couldn't retrieve it :( #Then, I started experimenting with different tuple code from internet.

my_screen = Screen()
ts = turtle.getscreen()

a = Turtle()

ts.bgcolor("black")
a.color("yellow")
a.width(12)
for i in range(5):
    a.forward(150)
    a.right(144)
my_screen.resetscreen()

c = a.clone()
my_screen.title("rainbow spiral")
c.speed(15)
ts.bgcolor("black")
r, g, b = 255, 0, 0

for i in range(255*2):
    ts.colormode(255)
    if i < 255//3:
        g += 3
    elif i < 255*2//3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255*4//3:
        g -= 3
    elif i < 255*5//3:
        r += 3
    else:
        b -= 3
    c.fd(50+i)
    c.rt(91)
    c.pencolor(r, g, b)


my_screen.exitonclick()
