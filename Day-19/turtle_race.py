from turtle import Turtle, Screen
import random

timmy_red = Turtle()
timmy_orange = Turtle()
timmy_yellow = Turtle()
timmy_green = Turtle()
timmy_blue = Turtle()
timmy_purple = Turtle()

screen = Screen()

screen.setup(width=500, height=400)
user_choice = screen.textinput("title", "Who will win the race? Enter a color: ")

timmy_red.color("red")
timmy_orange.color("orange")
timmy_yellow.color("yellow")
timmy_green.color("green")
timmy_blue.color("blue")
timmy_purple.color("purple")

timmy_red.shape("turtle")
timmy_orange.shape("turtle")
timmy_yellow.shape("turtle")
timmy_green.shape("turtle")
timmy_blue.shape("turtle")
timmy_purple.shape("turtle")


def move_to_start(timmy, x, y):
    timmy.penup()
    timmy.goto(x, y)


move_to_start(timmy_purple, -230, -100)
move_to_start(timmy_blue, -230, -60)
move_to_start(timmy_orange, -230, -20)
move_to_start(timmy_red, -230, 20)
move_to_start(timmy_yellow, -230, 60)
move_to_start(timmy_green, -230, 100)


turtle_list = ["green", "yellow", "red", "orange", "blue", "purple"]

random_list = [5, 10, 15, 20, 25]
move = [0, 0, 0, 0, 0, 0]
game = True


while game:
    def move_one_step(turtle, index):
        random_step = random.choice(random_list)
        turtle.forward(random_step)
        move[index] += random_step
        screen.delay(10)

    for i in range(len(move)):
        if move[i] >= 450:
            winner = i
            game = False

    move_one_step(timmy_green, 0)
    move_one_step(timmy_yellow, 1)
    move_one_step(timmy_red, 2)
    move_one_step(timmy_orange, 3)
    move_one_step(timmy_blue, 4)
    move_one_step(timmy_purple, 5)


if user_choice == turtle_list[winner]:
    print("U Win!!")
else:
    print(f"U lose, the winner is {turtle_list[winner]}")
screen.exitonclick()
