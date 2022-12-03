import turtle as t
from game.ball import Ball
from game.paddle import Paddle
from game.paddle_b import PaddleB

class Border():
    """"""

    def __init__(self):
        """"""

    def check_collisions(self):
        """"""
        if Ball.ball.xcor() > 340 and Ball.ball.xcor() < 350 and Ball.ball.ycor() < PaddleB.paddle.ycor() + 40 and Ball.ball.ycor() > PaddleB.paddle.ycor() - 40:
            Ball.ball.setx(340)
            ball_x_direction = ball_x_direction * -1

        if Ball.ball.xcor() < -340 and Ball.ball.xcor() < -350 and Ball.ball.ycor() < Paddle.paddle.ycor() + 40 and Ball.ball.ycor() > Paddle.paddle.ycor() - 40:
            Ball.ball.setx(-340)
            ball_x_direction = ball_x_direction * -1