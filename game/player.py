import pygame
from constants import *
from robot import Robot

WIDTH, HEIGHT = 750, 750

class Player(Robot):
    """ The player character.
        Attributes:
            robot_img (image): The cowboy image.
            ball_img (image): The ball image.
            mask: pygame element.
            max_health (int): The player's health.
    """
    def __init__(self, x, y, health=100):
        """ Contructs the player cowboy.
            Paramaters:
                x (int): The x coordinate.
                y (int): The y coordinate.
                health (int): The health of the player. 
        """
        super().__init__(x, y, health)
        self.robot_img = COWBOY
        self.ball_img = BLACK_BALL
        self.mask = pygame.mask.from_surface(self.robot_img)
        self.max_health = health

    def move_balls(self, vel, objs):
        """ Move the balls according to their velocity. Calls the collision(obj) function.
            Paramaters:
                vel (int): How fast the ball is moving.
                objs (balls, robots, or cowboys): An array of objects.
        """
        self.cooldown()
        for ball in self.balls:
            ball.move(vel)
            if ball.off_screen(HEIGHT):
                self.balls.remove(ball)
            else:
                for obj in objs:
                    if ball.collision(obj):
                        objs.remove(obj)
                        if ball in self.balls:
                            self.balls.remove(ball)

    def draw(self, window):
        """ Places the player in the game.
            Paramaters:
                window: pygame element.
        """
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        """ Updates the player's health bar.
            Paramaters:
                window: pygame element.
        """
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.robot_img.get_height() + 10, self.robot_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.robot_img.get_height() + 10, self.robot_img.get_width() * (self.health/self.max_health), 10))
