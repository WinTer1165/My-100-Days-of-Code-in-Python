from turtle import Turtle, Screen

a = Turtle()
a.shape("turtle")
a.color("orange red", "green yellow")
a.speed(3)

a.pencolor("violet")
for _ in range(3):
    a.forward(100)
    a.right(120)

a.pencolor("cornflowerblue")
for _ in range(4):
    a.forward(100)
    a.right(90)

a.pencolor("cyan")
for _ in range(5):
    a.forward(100)
    a.right(72)

a.pencolor("darkorange")
for _ in range(6):
    a.forward(100)
    a.right(60)

a.pencolor("hotpink")
for _ in range(7):
    a.forward(100)
    a.right(51.43)

a.pencolor("firebrick")
for _ in range(8):
    a.forward(100)
    a.right(45)

a.pencolor("gold")
for _ in range(9):
    a.forward(100)
    a.right(40)

a.pencolor("LightSlateGray")
for _ in range(10):
    a.forward(100)
    a.right(36)

screen = Screen()
screen.exitonclick()

# ! ALTERNATE SOLUTION :
# import random
# import turtle as t
# tim = t.Turtle()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)
