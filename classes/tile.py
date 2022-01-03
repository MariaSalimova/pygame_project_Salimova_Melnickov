import pygame
from sprite_groups import tiles, all_sprites
from constants import TILE_SIZE
from until_function import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, tile_image_path):
        super().__init__(tiles, all_sprites)
        self.image = load_image(tile_image_path, colorkey=None)
        self.rect = self.image.get_rect().move(
            TILE_SIZE * pos_x, TILE_SIZE * pos_y)
        self.type = tile_type