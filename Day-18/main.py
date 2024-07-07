import random
from turtle import Turtle, Screen

color_list = ["aquamarine", "brown", "coral", "DarkSeaGreen", "black", "LightBlue", "red", "blue", "green", "yellow"]
angle_list = [0, 90, 180, 270]

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
screen.delay(2)

timmy.width(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r, g, b)

    return rgb


def move(step):
    for i in range(step):
        timmy.color(random_color())
        timmy.forward(20)
        timmy.setheading(random.choice(angle_list))
        timmy.forward(20)


move(40)

screen.exitonclick()
