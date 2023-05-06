from turtle import Turtle, Screen, colormode
import random
colormode(255)

toto = Turtle()
toto.shape("turtle")

# for i in range(4):
#     toto.forward(100)
#     toto.right(90)

# for i in range(15):
#     toto.forward(10)
#     toto.penup()
#     toto.forward(10)
#     toto.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    col = (r,g,b)
    return col

color = ['red','blue','green']
dir = [0,90,180,270]
# sides = [3,4,5,6,7,8,9,10]
# for side in sides:
#     toto.color(random.choice(color))
#     for i in range(side):
#         angle = 360/side
#         toto.forward(100)
#         toto.right(angle)
toto.pensize(10)
for i in range(200):
    toto.color(random_color())
    toto.speed(50)
    toto.forward(30)
    toto.setheading(random.choice(dir))


my_screen = Screen()
my_screen.exitonclick()
