from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 5


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            first_snake = Turtle()
            first_snake.color("white")
            first_snake.shape("square")
            first_snake.penup()
            first_snake.goto(position)
            self.segments.append(first_snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
        # self.segments[0].left(90)c

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)

