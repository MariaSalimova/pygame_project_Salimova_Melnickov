from until_function import load_image
from constants import PATH_OF_MC_JUMP_LEFT, PATH_OF_MC_RUN_LEFT1, PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_JUMP_RIGHT, \
    PATH_OF_MC_IDLE_RIGHT, PATH_OF_MC_RUN_RIGHT1, PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_IDLE_LEFT, GRAVITY
import pygame
from sprite_groups import player, danger

# TODO: доделать главног персонажа
class MainCharacter(pygame.sprite.Sprite):
    # на карте обозначено @
    def __init__(self, ps_x, pos_y):
        super().__init__()
        self.add(player)
        self.pos = ps_x, pos_y
        self.model = load_image(PATH_OF_MC_IDLE_RIGHT, colorkey=None)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.model)
        self.run_frames_right = [PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_RUN_RIGHT1]
        self.run_frames_left = [PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_RUN_LEFT1]
        self.alive = True


    def set_current_level(self, map):
        self.cur_level = map
    def is_alive(self):
        return self.alive

    def attack(self, enemy):
        # TODO я не совсем понимаю как реализовать возможнось атаки
        pass

    def update(self, key):
        if pygame.sprite.spritecollideany(self, danger):
            self.alive = False
