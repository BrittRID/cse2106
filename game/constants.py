import pygame
import os

WIDTH, HEIGHT = 1000, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Shooter")


# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))



# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "spaceship.png")) #insert new image file here
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "spaceship.png")) #insert new image file here
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "spaceship.png")) #insert new image file here

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png")) #insert new image file here
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png")) #insert new image file here
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png")) #insert new image file here
YELLOW_LASER = pygame.image.load(os.path.join("assets", "soccer_ball.png")) #insert new image file here