from turtle import Turtle, Screen, colormode
import random

colormode(255)

tim = Turtle()
tim.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col = (r, g, b)
    return col


tim.speed(100)


def spirograph(gap):
    for i in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + gap)


spirograph(5)

my_screen = Screen()
my_screen.exitonclick()
