from turtle import Turtle, Screen, colormode
import random

colormode(255)

tim = Turtle()
tim.shape("turtle")

my_screen = Screen()



def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def movel_left():
    tim.left(15)

def move_right():
    tim.right(15)

def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=movel_left)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="c", fun=clean)
my_screen.exitonclick()