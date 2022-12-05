import pygame
import os

WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Invasion")

# Backgrounds
BG_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_road.png")), (WIDTH, HEIGHT))
BG_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_city.png")), (WIDTH, HEIGHT))
BG_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_rocket.png")), (WIDTH, HEIGHT))
BG_4 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_clouds.png")), (WIDTH, HEIGHT))
BG_5 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_hall.png")), (WIDTH, HEIGHT))

# Enemy Robots
RED_ROBOT = pygame.image.load(os.path.join("assets", "robot_red.png"))
GREEN_ROBOT = pygame.image.load(os.path.join("assets", "robot_green.png"))
BLUE_ROBOT = pygame.image.load(os.path.join("assets", "robot_blue.png"))
YELLOW_ROBOT = pygame.image.load(os.path.join("assets", "robot_yellow.png"))

# Balls
RED_BALL = pygame.image.load(os.path.join("assets", "ball_red.png"))
GREEN_BALL = pygame.image.load(os.path.join("assets", "ball_green.png"))
BLUE_BALL = pygame.image.load(os.path.join("assets", "ball_blue.png"))
YELLOW_BALL = pygame.image.load(os.path.join("assets", "ball_yellow.png"))

# Player Cowboy
COWBOY = pygame.image.load(os.path.join("assets", "cowboy.png"))
BLACK_BALL = pygame.image.load(os.path.join("assets", "ball_black.png"))
