from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

color_list = ["aquamarine", "beige", "brown", "coral", "DarkSeaGreen", "ivory", "LightBlue"]


def draw_shap(s):
    timmy.pencolor(random.choice(color_list))
    angle = round(360 / s, 0)
    for i in range(s):
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 11):
    draw_shap(i)

screen = Screen()
screen.exitonclick()