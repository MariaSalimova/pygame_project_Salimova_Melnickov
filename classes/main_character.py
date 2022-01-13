from until_function import load_image
from constants import PATH_OF_MC_JUMP_LEFT, PATH_OF_MC_RUN_LEFT1, PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_JUMP_RIGHT, \
    PATH_OF_MC_IDLE_RIGHT, PATH_OF_MC_RUN_RIGHT1, PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_IDLE_LEFT, GRAVITY, TILE_SIZE
import pygame
from sprite_groups import player, danger, tiles, collision, all_sprites
from math import ceil


class MainCharacter(pygame.sprite.Sprite):
    """На карте обозначено '@'"""
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, player)
        self.pos = pos_x, pos_y
        self.a_pos = pos_x * TILE_SIZE, pos_y * TILE_SIZE  # Абсолютные координаты
        self.image = pygame.transform.scale(load_image(PATH_OF_MC_IDLE_RIGHT, colorkey=None), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y)
        # self.mask = pygame.mask.from_surface(self.image)
        self.run_frames_right = [PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_RUN_RIGHT1]
        self.run_frames_left = [PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_RUN_LEFT1]
        self.alive = True

    def set_current_level(self, map):
        # TODO зачем это?
        self.cur_level = map

    def is_alive(self):
        """Возвращает живой ли игрок"""
        return self.alive

    def kill(self):
        """Устанавливает мёртое состояние персонажа"""
        self.alive = False

    def update(self, camera, key=None) -> None:
        if not pygame.sprite.spritecollideany(self, collision):
            if not pygame.sprite.spritecollideany(self, collision):
                self.change_model(PATH_OF_MC_JUMP_RIGHT)
                self.rect = self.rect.move(0, GRAVITY)
                camera.dy -= GRAVITY
                self.a_pos = (self.a_pos[0], self.a_pos[1] - GRAVITY)
                for sprite in tiles:
                    camera.apply(sprite)
                self.pos = self.pos[0], ceil(self.a_pos[1] / TILE_SIZE)

        if pygame.sprite.spritecollideany(self, collision):
            self.change_model(PATH_OF_MC_IDLE_RIGHT)

        if pygame.sprite.spritecollideany(self, danger):
            self.alive = False

    def move(self, x: int, y: int, movement: str, camera) -> None:
        dx = 100 * (x - self.pos[0])
        dy = 100 * -1 if movement == 'up' else 0
        camera.dx -= dx
        camera.dy -= dy
        self.a_pos = self.a_pos[0] - dx, self.a_pos[1] - dy
        self.pos = (x, y)
        self.a_pos = x * TILE_SIZE, y * TILE_SIZE
        for sprite in tiles:
            camera.apply(sprite)

    def change_model(self, model) -> None:
        self.image = pygame.transform.scale(load_image(model, colorkey=None), (TILE_SIZE, TILE_SIZE))

