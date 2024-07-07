import random
from turtle import Turtle, Screen

color_list = ["aquamarine", "brown", "coral", "DarkSeaGreen", "black", "LightBlue", "red", "blue", "green", "yellow"]

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")


def circle(step):
    for i in range(step):
        timmy.color(random.choice(color_list))
        timmy.circle(100)
        timmy.left(5)


circle(72)


screen.exitonclick()
