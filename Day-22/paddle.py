from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        new_dir = self.ycor() + 20
        self.goto(self.xcor(), new_dir)

    def down(self):
        new_dir = self.ycor() - 20
        self.goto(self.xcor(), new_dir)
