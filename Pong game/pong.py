from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

b = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(b.move_speed)
    screen.update()
    b.move()
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()

    if b.xcor() > 320 and b.distance(r_paddle) < 50 or b.xcor() < -320 and b.distance(l_paddle) < 50:
        b.bounce_x()

    if b.xcor() > 380:
        b.missed()
        score.l_point()

    if b.xcor() < -380:
        b.missed()
        score.r_point()










screen.exitonclick()
