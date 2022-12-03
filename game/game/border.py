import turtle as t
from game.ball import Ball
from game.pen import Pen
# from game.director import Director

class Border():
    """"""

    # def __init__(self):
    #     """"""

    def check_border(player_a_score, player_b_score):
    # def check_border():
        """"""
        if Ball.ball.ycor() > 290:
            Ball.ball.sety(290)
            Ball.ball_y_direction = Ball.ball_y_direction * -1

        if Ball.ball.ycor() < -290:
            Ball.ball.sety(-290)
            Ball.ball_y_direction = Ball.ball_y_direction * -1

        if Ball.ball.xcor() > 390:
            Ball.ball.goto(0, 0)
            Ball.ball_x_direction = Ball.ball_x_direction * -1
            player_a_score = player_a_score + 1
            Pen.pen.clear()
            Pen.pen.write("Player A: {}      Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24,"normal"))

        if Ball.ball.xcor() < -390:
            Ball.ball.goto(0, 0)
            Ball.ball_x_direction = Ball.ball_x_direction * -1
            player_b_score = player_b_score + 1
            Pen.pen.clear()
            Pen.pen.write("Player A: {}      Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24,"normal"))
