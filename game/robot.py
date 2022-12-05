from ball import Ball
from constants import *


class Robot:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.robot_img = None
        self.ball_img = None
        self.balls = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.robot_img, (self.x, self.y))
        for ball in self.balls:
            ball.draw(window)

    def move_balls(self, vel, obj):
        self.cooldown()
        for ball in self.balls:
            ball.move(vel)
            if ball.off_screen(HEIGHT):
                self.balls.remove(ball)
            elif ball.collision(obj):
                obj.health -= 10
                self.balls.remove(ball)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            ball = Ball(self.x, self.y, self.ball_img)
            self.balls.append(ball)
            self.cool_down_counter = 1

    def get_width(self):
        return self.robot_img.get_width()

    def get_height(self):
        return self.robot_img.get_height()
