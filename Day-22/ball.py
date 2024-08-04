from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1.5, 1.5)
        self.goto(0, 0)

    def move_ball(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x, y)
