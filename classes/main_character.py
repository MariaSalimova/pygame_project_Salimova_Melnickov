from until_function import load_image
from constants import PATH_OF_MC_JUMP_LEFT, PATH_OF_MC_RUN_LEFT1, PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_JUMP_RIGHT, \
    PATH_OF_MC_IDLE_RIGHT, PATH_OF_MC_RUN_RIGHT1, PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_IDLE_LEFT, GRAVITY
import pygame


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, ps_x, pos_y):
        super().__init__()
        self.pos = ps_x, pos_y
        self.model = load_image(PATH_OF_MC_IDLE_RIGHT, colorkey=None)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.model)
        self.run_frames_right = [PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_RUN_RIGHT1]
        self.run_frames_left = [PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_RUN_LEFT1]

    def attack(self, enemy):
        """я не совсем понимаю как реализовать возможнось атаки"""
        pass

    def update(self, key):
        pass
