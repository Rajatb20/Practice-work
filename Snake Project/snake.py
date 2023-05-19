POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.new_snakes = []
        self.create_snake()
        self.head = self.new_snakes[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        toto = Turtle("square")
        toto.color('white')
        toto.penup()
        toto.goto(position)
        self.new_snakes.append(toto)

    def extend(self):
        self.add_segment(self.new_snakes[-1].position())

    def move(self):
        for seg in range(len(self.new_snakes) - 1, 0, -1):
            new_x = self.new_snakes[seg - 1].xcor()
            new_y = self.new_snakes[seg - 1].ycor()
            self.new_snakes[seg].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
