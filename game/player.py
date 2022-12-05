import pygame
import os
from robot import Robot

WIDTH, HEIGHT = 750, 750

COWBOY = pygame.image.load(os.path.join("assets", "cowboy.png"))
BLACK_BALL = pygame.image.load(os.path.join("assets", "ball_black.png"))


class Player(Robot):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.robot_img = COWBOY
        self.ball_img = BLACK_BALL
        self.mask = pygame.mask.from_surface(self.robot_img)
        self.max_health = health

    def move_balls(self, vel, objs):
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
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.robot_img.get_height() + 10, self.robot_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.robot_img.get_height() + 10, self.robot_img.get_width() * (self.health/self.max_health), 10))
