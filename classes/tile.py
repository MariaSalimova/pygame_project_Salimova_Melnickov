import pygame

import sprite_groups
from sprite_groups import tiles, all_sprites, collision
from constants import TILE_SIZE, PATH_OF_BOX_CAT, PATH_OF_BRICK, PATH_OF_MOVING_PLATFORM, PATH_OF_AIR
from until_function import load_image


class Tile(pygame.sprite.Sprite):
    """Основной класс объекта в игре"""
    def __init__(self, pos_x: int, pos_y: int, tile_image_path: str) -> None:
        super().__init__(tiles, all_sprites)
        self.image = pygame.transform.scale(load_image(tile_image_path, colorkey=None), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect().move(
            TILE_SIZE * pos_x, TILE_SIZE * pos_y)


class BrickTile(Tile):
    """На карте обозначено '+'"""
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_BRICK)
        self.add(collision)
        self.add(sprite_groups.bricks)


class BoxCat(Tile):
    """На карте обозначено '%'
    Переносит на следующую карту"""
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_BOX_CAT)
        self.add(sprite_groups.level_end)


class Air(Tile):
    """На карте обозначено '.'"""
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_AIR)


class DeathTile(Tile):
    """На карте обозначено '/'"""
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_AIR)
        self.add(sprite_groups.danger)


class MovingPlatform(Tile):
    """На карте обозначено '$'"""
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_MOVING_PLATFORM)
        self.add(collision)
        self.add(sprite_groups.moving_platform)
        self.v = 1
        self.x = pos_x

    def update(self):
        """Движение платформы """
        if pygame.sprite.spritecollideany(self, sprite_groups.bricks):
            self.v = -self.v
        self.x += self.v
