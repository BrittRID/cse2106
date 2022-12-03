import turtle as t
from game.paddle import Paddle
from game.paddle_b import PaddleB

class Window():
    """"""

    def __init__(self):
        """"""
        self._window = t.Screen()
        self._window.listen()
        self._window.onkeypress(Paddle.move_up, "w")
        self._window.onkeypress(Paddle.move_up, "s")
        self._window.onkeypress(PaddleB.move_up, "i")
        self._window.onkeypress(PaddleB.move_up, "k")
