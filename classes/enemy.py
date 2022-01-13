from until_function import load_image
import pygame
from constants import PATH_OF_ENEMY_IDLE_LEFT, PATH_OF_ENEMY_IDLE_RIGHT, PATH_OF_ENEMY_RUN_LEFT1, \
    PATH_OF_ENEMY_RUN_LEFT2, PATH_OF_ENEMY_RUN_RIGHT1, PATH_OF_ENEMY_RUN_RIGHT2, TILE_SIZE
from sprite_groups import danger, all_sprites


class Enemy(pygame.sprite.Sprite):
    """На карте обозначено !на карте обозначено '!'"""
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, danger)
        self.image = pygame.transform.scale(load_image(PATH_OF_ENEMY_IDLE_LEFT, colorkey=None), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.run_frames_right = [PATH_OF_ENEMY_RUN_RIGHT2, PATH_OF_ENEMY_RUN_RIGHT1]
        self.run_frames_left = [PATH_OF_ENEMY_RUN_LEFT2, PATH_OF_ENEMY_RUN_LEFT1]

