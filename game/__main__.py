import pygame
import random
from enemy import Enemy
from player import Player
from constants import *
from sound_service import sound_service

pygame.font.init()


def collide(obj1, obj2):
    """ Handles the collisions of two objects
        Pramaters:
            obj1 (ball, robot, or cowboy): Object 1.
            obj2 (ball, robot, or cowboy): Object 2.
        Returns:
            The overlaping pygame object mask.
    """
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main():
    """ The 'director' of the game. 
        Handles updates and keeps the game running.
    """
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("lucidaconsole", 50)
    lost_font = pygame.font.SysFont("lucidaconsole", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    ball_vel = 5

    player = Player(300, 630)

    sound = sound_service()
    sound.background_sound()

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        if level == 0:
            WIN.blit(BG_0, (0, 0))
        elif level == 1:
            WIN.blit(BG_1, (0, 0))
        elif level == 2:
            WIN.blit(BG_2, (0, 0))
        elif level == 3:
            WIN.blit(BG_3, (0, 0))
        elif level == 4:
            WIN.blit(BG_4, (0, 0))
        elif level > 4:
            WIN.blit(BG_5, (0, 0))

        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (0, 255, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 0, 0))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 0, 0))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -
                              100), random.choice(["red", "blue", "green", "yellow"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_balls(ball_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
                # Do explosion sound
                sound.explosion_sound()
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
                sound.explosion_sound()


        player.move_balls(-ball_vel, enemies)


def main_menu():
    """ Initiates the game. Calls the main() function.
    """
    title_font = pygame.font.SysFont("lucidaconsole", 40)
    run = True
    while run:
        WIN.blit(BG_1, (0, 0))
        title_label = title_font.render(
            "Left click to begin...", 1, (255, 0, 0))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


if __name__ == "__main__":
    main_menu()
