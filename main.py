import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from blocks import Blocks
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to Breakout!")
screen.tracer(0)
screen.setup(width=600, height=800)

paddle = Paddle((0, -350))
ball = Ball()
blocks = Blocks()
scoreboard = Scoreboard()

screen.getcanvas().bind('<Motion>', paddle.position)  # MOUSE MOVEMENTS

game_is_on = True
while game_is_on:
    time.sleep(0.0001)
    screen.update()
    ball.move()
    scoreboard.score()

    if ball.xcor() >= 280 or ball.xcor() <= -280:  # Hit side wall
        ball.side_wall_bounce()

    if ball.ycor() >= 200:  # Hit ceiling
        ball.top_wall_bounce()

    if abs(paddle.xcor() - ball.xcor()) <= 50 and ball.ycor() <= -330:  # Hit paddle
        ball.paddle_bounce(paddle.xcor() - ball.xcor())

    for block in blocks.blocks:  # Hit block
        if abs(block.xcor() - ball.xcor()) <= 35.75 and abs(block.ycor() - ball.ycor()) <= 30:  # Add 10 for ball radius
            if abs(ball.xcor() - block.xcor()) >= 25.75 and abs(ball.ycor() - block.ycor()) < 20:  # Catch ball moving
                ball.side_wall_bounce()
                block.reset()
                scoreboard.new_score()
            if abs(ball.xcor() - block.xcor()) < 25.75 and abs(ball.ycor() - block.ycor()) >= 20:
                ball.top_wall_bounce()
                block.reset()
                scoreboard.new_score()

    if ball.ycor() < -350:  # Reset ball if falls below paddle
        time.sleep(1)
        ball.reset_position()
        scoreboard.reset()

screen.exitonclick()
