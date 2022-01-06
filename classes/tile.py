import pygame
from sprite_groups import tiles, all_sprites
from constants import TILE_SIZE, PATH_OF_BOX_CAT, PATH_OF_BRICK, PATH_OF_MOVING_PLATFORM, PATH_OF_AIR
from until_function import load_image

# TODO: доделать тайлы
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, tile_image_path, collision=False):
        super().__init__(tiles, all_sprites)
        self.image = load_image(tile_image_path, colorkey=None)
        self.rect = self.image.get_rect().move(
            TILE_SIZE * pos_x, TILE_SIZE * pos_y)
        self.collision = collision

    def can_go_trough(self):
        return self.collision


class BrickTile(Tile):
    # на карте обозначено +
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_BRICK, collision=True)


class BoxCat(Tile):
    # на карте обозначено %
    # переносит на следующую карту
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_BOX_CAT, collision=True)


class Air(Tile):
    # на карте обозначено .
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_AIR, collision=False)


class DeathTile(Tile):
    # на карте обозначено /
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_AIR, collision=True)


class MovingPlatform(Tile):
    # на карте обозначено $
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PATH_OF_MOVING_PLATFORM, collision=True)