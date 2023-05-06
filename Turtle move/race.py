from turtle import Turtle, Screen, colormode
import random
colormode(255)

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Bet", prompt="Which color do you think will win? ")
colors = ['violet','indigo','blue','green','yellow','orange','red']
pos = [-75, -50, -25, 0, 25, 50, 75]
all_turtles = []

for turtle_index in range(7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=pos[turtle_index])
    tim.color(colors[turtle_index])
    all_turtles.append(tim)

if bet:
    race_on = True

while race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            race_on = False
            win_color = i.pencolor()
            if win_color == bet:
                print(f"You have won !!{win_color} turtle is winner.")
            else:
                print(f"You lost !!{win_color} turtle is winner.")
        i.forward(random.randint(1,10))










screen.exitonclick()