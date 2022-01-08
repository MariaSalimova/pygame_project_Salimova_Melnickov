from until_function import load_image
from constants import PATH_OF_MC_JUMP_LEFT, PATH_OF_MC_RUN_LEFT1, PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_JUMP_RIGHT, \
    PATH_OF_MC_IDLE_RIGHT, PATH_OF_MC_RUN_RIGHT1, PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_IDLE_LEFT, GRAVITY, TILE_SIZE
import pygame
from sprite_groups import player, danger, tiles, collision, all_sprites


# TODO: доделать главног персонажа
class MainCharacter(pygame.sprite.Sprite):
    # на карте обозначено @
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, player)
        self.pos = pos_x, pos_y
        self.image = pygame.transform.scale(load_image(PATH_OF_MC_IDLE_RIGHT, colorkey=None), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.run_frames_right = [PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_RUN_RIGHT1]
        self.run_frames_left = [PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_RUN_LEFT1]
        self.alive = True

    def set_current_level(self, map):
        self.cur_level = map

    def is_alive(self):
        return self.alive

    def kill(self):
        self.alive = False

    def attack(self, enemy):
        # TODO я не совсем понимаю как реализовать возможнось атаки
        pass

    def update(self, camera, key=None):
        if not pygame.sprite.spritecollideany(self, collision):
            self.change_model(PATH_OF_MC_JUMP_RIGHT)
            self.rect = self.rect.move(0, GRAVITY)
            camera.dy -= GRAVITY
            for sprite in tiles:
                camera.apply(sprite)

        if pygame.sprite.spritecollideany(self, collision):
            self.change_model(PATH_OF_MC_IDLE_RIGHT)

        if pygame.sprite.spritecollideany(self, danger):
            self.alive = False

    def move(self, x, y, movement, camera):
        camera.dx -= 100 * (x - self.pos[0])
        camera.dy -= 100 * -1 if movement == 'up' else 0
        self.pos = (x, y)
        for sprite in tiles:
            camera.apply(sprite)

    def change_model(self, model):
        self.image = pygame.transform.scale(load_image(model, colorkey=None), (TILE_SIZE, TILE_SIZE))

