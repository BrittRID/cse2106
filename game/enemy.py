import pygame
from robot import Robot
from ball import Ball
from constants import *


class Enemy(Robot):
    """ An enemy robot.
        Attributes:
            x (int): The x coordinate.
            y (int): The y coordinate.
            color: Determines the image used.
    """

    COLOR_MAP = {
        "red": (RED_ROBOT, RED_BALL),
        "green": (GREEN_ROBOT, GREEN_BALL),
        "blue": (BLUE_ROBOT, BLUE_BALL),
        "yellow": (YELLOW_ROBOT, YELLOW_BALL)
    }

    def __init__(self, x, y, color, health=100):
        """ Constructs a new enemy robot.
            Paramaters:
                x (int): The x coordinate.
                y (int): The y coordinate.
                color: Determines the image used.
                health (int): The health of the robot.
        """
        super().__init__(x, y, health)
        self.robot_img, self.ball_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.robot_img)

    def move(self, vel):
        """ Moves the enemy according to it's velocity.
            Paramaters:
                vel (int): How fast the robot is moving.
        """
        self.y += vel

    def shoot(self):
        """ Shoots a ball.
        """
        if self.cool_down_counter == 0:
            ball = Ball(self.x-20, self.y, self.ball_img)
            self.balls.append(ball)
            self.cool_down_counter = 1
