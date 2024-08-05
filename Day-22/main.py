from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

ball = Ball()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    ball.move_ball()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.miss()

    if ball.xcor() > 380:
        ball.miss()

screen.exitonclick()
