import turtle as t
# from game.actor import Actor

class Pen():
    """"""

    def __init__(self):
        """"""
        self._pen = t.Turtle()
        self._pen.speed(0)
        self._pen.color("blue")
        self._pen.penup()
        self._pen.hideturtle()
        self._pen.goto(0, 260)
        self._pen.write("Player A: 0      Player B: 0", align="center", font=("Arial", 24, "normal"))
