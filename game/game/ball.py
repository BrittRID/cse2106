import turtle as t
# from game.actor import Actor

class Ball():
    """"""

    def __init__(self):
        """"""
        self._ball = t.Turtle()
        self._ball.speed(0)
        self._ball.shape("circle")
        self._ball.color("red")
        self._ball.penup()
        self._ball.goto(5, 5)
        self._ball_x_direction = 1.8
        self._ball_y_direction = 1.8

    def move(self):
        self._ball.setx(self._ball.xcor() + self._ball_x_direction)
        self._ball.sety(self._ball.ycor() + self._ball_y_direction)