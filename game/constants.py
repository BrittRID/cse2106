import pygame
import os

WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Shooter")

# Backgrounds
bg_level_1 = "bg_grass.png"
bg_level_2 = "bg_road.png"
bg_level_3 = "bg_city.png"
bg_level_4 = "bg_rocket.png"
bg_level_5 = "bg_clouds.png"
bg_level_6 = "bg_hall.png"

# Robots
robot_red = "robot_red.png"
robot_green = "robot_green.png"
robot_blue = "robot_blue.png"
robot_yellow = "robot_yellow.png"

# Cowboy
# cowboy_img = "cowboy.png"

# Balls
ball_red = "ball_red.png"
ball_green = "ball_green.png"
ball_blue = "ball_blue.png"
ball_yellow = "ball_yellow.png"
# ball_black = "ball_black.png"

# This could be turned into a function to make the image loading look more clean

# Backgrounds
BG_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", bg_level_1)), (WIDTH, HEIGHT))
BG_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", bg_level_2)), (WIDTH, HEIGHT))
BG_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", bg_level_3)), (WIDTH, HEIGHT))
BG_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", bg_level_4)), (WIDTH, HEIGHT))
BG_5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", bg_level_5)), (WIDTH, HEIGHT))
BG_6 = pygame.transform.scale(pygame.image.load(os.path.join("assets", bg_level_6)), (WIDTH, HEIGHT))


# Enemy Robots
RED_ROBOT = pygame.image.load(os.path.join("assets", robot_red))
GREEN_ROBOT = pygame.image.load(os.path.join("assets", robot_green))
BLUE_ROBOT = pygame.image.load(os.path.join("assets", robot_blue))
YELLOW_ROBOT = pygame.image.load(os.path.join("assets", robot_yellow))


# Player Cowboy
# COWBOY = pygame.image.load(os.path.join("assets", cowboy_img))


# Balls
RED_BALL = pygame.image.load(os.path.join("assets", ball_red))
GREEN_BALL = pygame.image.load(os.path.join("assets", ball_green))
BLUE_BALL = pygame.image.load(os.path.join("assets", ball_blue))
YELLOW_BALL = pygame.image.load(os.path.join("assets", ball_yellow))
# BLACK_BALL = pygame.image.load(os.path.join("assets", ball_black))
