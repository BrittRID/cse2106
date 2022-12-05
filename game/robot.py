from ball import Ball
from constants import *


class Robot:
    """ The base character for the robots and cowboy.
        Attributes:
            x (int): The x coordinate.
            y (int): The y coordinate.
            health (int): The health of the character.
            robot_img (image): The image of the character.
            ball_img (image): The image of the balls.
            balls (array): The balls that belong to the character.
            cool_down_counter (int): The countdown until the character shoots again.
    """
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        """ Constructs a new character base.
            Paramaters:
                x (int): The x coordinate.
                y (int): The y coordinate.
                health (int): The health of the robot.
        """
        self.x = x
        self.y = y
        self.health = health
        self.robot_img = None
        self.ball_img = None
        self.balls = []
        self.cool_down_counter = 0

    def draw(self, window):
        """ Places the character in the game.
            Paramaters:
                window: pygame element.
        """
        window.blit(self.robot_img, (self.x, self.y))
        for ball in self.balls:
            ball.draw(window)

    def move_balls(self, vel, obj):
        """ Move the balls according to their velocity.
            Paramaters:
                vel (int): How fast the ball is moving.
                obj (ball, robot, or cowboy): An object.
        """
        self.cooldown()
        for ball in self.balls:
            ball.move(vel)
            if ball.off_screen(HEIGHT):
                self.balls.remove(ball)
            elif ball.collision(obj):
                obj.health -= 10
                self.balls.remove(ball)

    def cooldown(self):
        """ Resets the cooldown or adds time.
        """
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        """ Shoots a ball.
        """
        if self.cool_down_counter == 0:
            ball = Ball(self.x, self.y, self.ball_img)
            self.balls.append(ball)
            self.cool_down_counter = 1

    def get_width(self):
        """ Gets the width of the character.
            Returns:
                The width of the robot. (int)
        """
        return self.robot_img.get_width()

    def get_height(self):
        """ Gets the height of the character.
            Returns:
                The height of the robot. (int)
        """
        return self.robot_img.get_height()
