from turtle import Turtle, Screen


a = Turtle()
a.shape("turtle")
screen = Screen()


def f():
    a.fd(10)


def b():
    a.back(10)


def a_a():
    a.left(10)


def a_d():
    a.right(10)


def clear():
    a.clear()
    a.home()
    a.clear()


screen.onkey(f, "w")
screen.onkey(b, "s")
screen.onkey(a_a, "a")
screen.onkey(a_d, "d")
screen.onkey(clear, "c")

screen.listen()

screen.exitonclick()
