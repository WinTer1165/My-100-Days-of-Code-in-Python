from turtle import Turtle, Screen, colormode
import random
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145,
                                                                                                                                                                                                                                               178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

colormode(255)
a = Turtle()
a.speed("fastest")
a.penup()
a.hideturtle()
a.setheading(225)
a.forward(300)
a.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    a.dot(20, random.choice(color_list))
    a.forward(50)

    if dot_count % 10 == 0:
        a.setheading(90)
        a.forward(50)
        a.setheading(180)
        a.forward(500)
        a.setheading(0)
screen = Screen()
screen.exitonclick()
