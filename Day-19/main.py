from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def forward():
    timmy.forward(10)


def backward():
    timmy.backward(10)


def right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=right, key="a")
screen.onkey(fun=left, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
