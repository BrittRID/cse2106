import pygame
import os
# Add 

class sound_service:

    def __init__(self):
        pygame.mixer.init()
        self._folder = 'assets/sounds'
        self._explosion_sound = pygame.mixer.Sound(os.path.join(self._folder, 'explosion.ogg'))
        pygame.mixer.music.load(os.path.join(self._folder, 'background.ogg'))

    def explosion_sound(self):
        self._play_sound('explosion')

    def background_sound(self):
        self._play_sound('background')

    def _play_sound(self, name):
        if name == 'explosion':
            pygame.mixer.Sound.play(self._explosion_sound)

        if name == 'background':
            pygame.mixer.music.play(-1)

