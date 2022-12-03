import turtle as t
# from game.actor import Actor

class Paddle():
    """"""

    def __init__(self):
        """"""
        # super().__init__()
        self._paddle = t.Turtle()
        self._paddle.speed(0)
        self._paddle.shape("square")
        self._paddle.color("blue")
        self._paddle.shapesize(stretch_wid=5, stretch_len=1)
        self._paddle.penup()
        self._paddle.goto(-350, 0)

    def move_up(self):
        y = self._paddle.ycor()
        y = y + 15
        self._paddle.sety(y)

    def move_down(self):
        y = self._paddle.ycor()
        y = y - 15
        self._paddle.sety(y)

