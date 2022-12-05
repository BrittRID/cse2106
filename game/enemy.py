import pygame
# import os
from robot import Robot
from ball import Ball
from constants import *


class Enemy(Robot):
    COLOR_MAP = {
        "red": (RED_ROBOT, RED_BALL),
        "green": (GREEN_ROBOT, GREEN_BALL),
        "blue": (BLUE_ROBOT, BLUE_BALL),
        "yellow": (YELLOW_ROBOT, YELLOW_BALL)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.robot_img, self.ball_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.robot_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            ball = Ball(self.x-20, self.y, self.ball_img)
            self.balls.append(ball)
            self.cool_down_counter = 1
