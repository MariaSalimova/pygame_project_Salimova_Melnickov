import pygame
import sprite_groups
from generate_level import generate_level, load_level
from classes.camera import Camera
from until_function import terminate
from constants import FPS
import constants
from screen.game_over_screen import GameOverScreen
from screen.end_of_story_screen import EndOfStoryScreen


class Level3Screen:
    def __init__(self, size: tuple, screen, clock):

        # pygame.key.set_repeat(200, 25)

        self.level_map = load_level('level_3')
        self.player, self.level_x, self.level_y = generate_level(self.level_map)

        self.camera = Camera()

        running = True
        while running:
            screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if not self.player.is_alive():
                    GameOverScreen(size, screen, clock)
                if pygame.sprite.spritecollideany(self.player, sprite_groups.danger):
                    GameOverScreen(size, screen, clock)
                if pygame.sprite.spritecollideany(self.player, sprite_groups.level_end):
                    EndOfStoryScreen(size, screen, clock)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.move("up")

                    elif event.key == pygame.K_a:
                        self.move("left")
                    elif event.key == pygame.K_d:
                        self.move("right")

                    # if event.key in [pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT]:
                    #     if event.key == pygame.K_UP:
                    #         self.camera.dy -= 100
                    #     elif event.key == pygame.K_DOWN:
                    #         self.camera.dy += 100
                    #     elif event.key == pygame.K_LEFT:
                    #         self.camera.dx -= 100
                    #     elif event.key == pygame.K_RIGHT:
                    #         self.camera.dx += 100
                    #     for sprite in sprite_groups.all_sprites:
                    #         self.camera.apply(sprite)
            self.player.update(self.camera)
            self.camera.update(self.player)
            sprite_groups.danger.update()
            sprite_groups.moving_platform.update()
            sprite_groups.moving_platform.draw()
            sprite_groups.danger.draw()
            sprite_groups.tiles.draw(screen)
            sprite_groups.player.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)

    def move(self, movement):
        x, y = self.player.pos
        print(x, y, movement)
        if movement == "up":
            if self.level_map[y - 1][x] in ['.', '@', '%'] and pygame.sprite.spritecollideany(self.player, sprite_groups.collision):
                self.player.change_model(constants.PATH_OF_MC_JUMP_RIGHT)
                self.player.move(x, y, movement, self.camera)
        elif movement == "left":
            if x > 0 and self.level_map[y][x - 1] in ['.', '@', '%']:
                self.player.change_model(constants.PATH_OF_MC_RUN_LEFT2)
                self.player.move(x - 1, y, movement, self.camera)
                self.player.change_model(constants.PATH_OF_MC_IDLE_LEFT)
        elif movement == "right":
            if x < self.level_x and self.level_map[y][x + 1] in ['.', '@', '%']:
                self.player.change_model(constants.PATH_OF_MC_RUN_RIGHT2)
                self.player.move(x + 1, y, movement, self.camera)
                self.player.change_model(constants.PATH_OF_MC_IDLE_RIGHT)
