# from cast import Cast
import turtle as t
from game.window import Window
from game.ball import Ball
from game.border import Border

class Director():
    """"""
    def __init__(self):
        self.player_a_score = 0
        self.player_b_score = 0
        self._playing = True
    
    def start_game(self):
        """"""

        while self._playing == True:
            window = Window()
            window._window.update()
            ball = Ball()
            border = Border()

            ball.move()

            # player_a_score = self.player_a_score
            # player_b_score = self.player_b_score

            # print(border.check_border())
            border.check_border(self.player_a_score, self.player_b_score)
            # border.check_border()
            # border.check_border(0, 0)

        