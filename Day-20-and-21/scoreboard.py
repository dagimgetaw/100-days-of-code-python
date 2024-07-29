from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 260)

    def increase(self, score):
        self.color("white")
        self.ht()
        self.write(f"Score = {score}", False, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=("Arial", 16, "normal"))


