from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

paddle = Turtle()
paddle.goto(350,0)
paddle.color("white")
paddle.shape("square")
paddle.penup()
paddle.shapesize(5, 1)


def up():
    new_up = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_up)

def down():
    new_up = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_up)


screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()