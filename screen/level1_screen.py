import pygame
import sprite_groups
from generate_level import generate_level, load_level
from classes.camera_new import Camera
from until_function import terminate
from constants import FPS, TILE_SIZE
from screen.game_over_screen import GameOverScreen
from screen.level2_screen import Level2Screen


class Level1Screen:
    def __init__(self, size: tuple, screen, clock):

        self.level_map = load_level('level_2')
        self.player, self.level_x, self.level_y = generate_level(self.level_map)

        self.camera = Camera(self.level_x * TILE_SIZE, self.level_y * TILE_SIZE)

        up = left = right = False

        running = True
        while running:
            screen.fill('white')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if not self.player.is_alive():
                    GameOverScreen(size, screen, clock)
                if pygame.sprite.spritecollideany(self.player, sprite_groups.danger):
                    print('tut')
                    GameOverScreen(size, screen, clock)
                if pygame.sprite.spritecollideany(self.player, sprite_groups.level_end):

                    # sprite_groups.bricks = pygame.sprite.Group()
                    # sprite_groups.all_sprites = pygame.sprite.Group()
                    # sprite_groups.tiles = pygame.sprite.Group()
                    # sprite_groups.player.remove(self.player)
                    # # sprite_groups.enemies = pygame.sprite.Group()
                    # sprite_groups.danger = pygame.sprite.Group()
                    # sprite_groups.teleporter = pygame.sprite.Group()
                    # sprite_groups.level_end = pygame.sprite.Group()
                    # sprite_groups.collision = pygame.sprite.Group()
                    # sprite_groups.not_collision = pygame.sprite.Group()
                    # sprite_groups.moving_platform = pygame.sprite.Group()

                    Level2Screen(size, screen, clock)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        up = True
                    if event.key == pygame.K_LEFT:
                        left = True
                    if event.key == pygame.K_RIGHT:
                        right = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        up = False
                    if event.key == pygame.K_RIGHT:
                        right = False
                    if event.key == pygame.K_LEFT:
                        left = False
            self.player.update(left, right, up)
            self.camera.update(self.player)
            sprite_groups.danger.update()
            sprite_groups.moving_platform.update()
            for e in sprite_groups.all_sprites:
                screen.blit(e.image, self.camera.apply(e))
            pygame.display.update()
            clock.tick(FPS)
