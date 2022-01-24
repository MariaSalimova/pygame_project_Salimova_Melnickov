import pygame
import sprite_groups
from generate_level import generate_level, load_level
from classes.camera_new import Camera
from until_function import terminate, load_image
from constants import FPS, TILE_SIZE
import constants
from screen.game_over_screen import GameOverScreen
from screen.the_end_screen import TheEndScreen


class TheGameItself:
    def __init__(self, size: tuple, screen, clock):

        self.level_map = load_level('map')
        self.player, self.level_x, self.level_y = generate_level(self.level_map)

        self.camera = Camera(self.level_x * TILE_SIZE, self.level_y * TILE_SIZE)

        up = left = right = False
        cats_found = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            # цикл с историей
            running1 = True
            frame = 0
            while running1:

                screen.fill('white')

                screen.blit(pygame.transform.scale(constants.STORY_BEGINNING[frame], size), (0, 0))
                for event1 in pygame.event.get():
                    if event1.type == pygame.QUIT:
                        terminate()
                    elif event1.type == pygame.KEYUP:
                        if event1.key == pygame.K_ESCAPE:
                            running = False
                        if event1.key == pygame.K_n:
                            frame += 1
                            if frame == 4:
                                running1 = False
                pygame.display.update()
                clock.tick(FPS)
            # цикл с геймплеем
            running2 = True
            while running2:
                screen.fill('white')
                for event2 in pygame.event.get():
                    if event2.type == pygame.QUIT:
                        terminate()
                    if not self.player.is_alive():
                        GameOverScreen(size, screen, clock)
                    if pygame.sprite.spritecollideany(self.player, sprite_groups.danger):
                        print('tut')
                        GameOverScreen(size, screen, clock)
                    if pygame.sprite.spritecollideany(self.player, sprite_groups.box_cat1):
                        cats_found += 1
                        sprite_groups.all_sprites.remove(sprite_groups.box_cat1)
                        running3 = True
                        while running3:
                            screen.fill('white')
                            screen.blit(pygame.transform.scale(load_image(constants.FOUND_A_CAT, colorkey=None),
                                                               size), (0, 0))
                            for event3 in pygame.event.get():
                                if event3.type == pygame.QUIT:
                                    terminate()
                                elif event3.type == pygame.KEYUP:
                                    if event3.key == pygame.K_n:
                                        running3 = False
                            pygame.display.update()
                            clock.tick(FPS)
                    if pygame.sprite.spritecollideany(self.player, sprite_groups.box_cat2):
                        cats_found += 1
                        sprite_groups.all_sprites.remove(sprite_groups.box_cat2)
                        running4 = True
                        while running4:
                            screen.fill('white')
                            screen.blit(pygame.transform.scale(load_image(constants.FOUND_A_CAT, colorkey=None),
                                                               size), (0, 0))
                            for event4 in pygame.event.get():
                                if event4.type == pygame.QUIT:
                                    terminate()
                                elif event4.type == pygame.KEYUP:
                                    if event4.key == pygame.K_n:
                                        running4 = False
                            pygame.display.update()
                            clock.tick(FPS)
                    if pygame.sprite.spritecollideany(self.player, sprite_groups.box_cat3):
                        cats_found += 1
                        sprite_groups.all_sprites.remove(sprite_groups.box_cat3)
                        running5 = True
                        while running5:
                            screen.fill('white')
                            screen.blit(pygame.transform.scale(load_image(constants.FOUND_A_CAT, colorkey=None),
                                                               size), (0, 0))
                            for event5 in pygame.event.get():
                                if event5.type == pygame.QUIT:
                                    terminate()
                                elif event5.type == pygame.KEYUP:
                                    if event5.key == pygame.K_n:
                                        running5 = False
                            pygame.display.update()
                            clock.tick(FPS)
                    if pygame.sprite.spritecollideany(self.player, sprite_groups.box_cat4):
                        frame1 = 0
                        sprite_groups.all_sprites.remove(sprite_groups.box_cat4)
                        if cats_found == 0:
                            screens = constants.STORY_ENDING1
                        else:
                            screens = constants.STORY_ENDING2
                        running6 = True
                        while running6:
                            screen.fill('white')
                            screen.blit(pygame.transform.scale(screens[frame1], size), (0, 0))
                            for event6 in pygame.event.get():
                                if event6.type == pygame.QUIT:
                                    terminate()
                                elif event6.type == pygame.KEYUP:
                                    if event6.key == pygame.K_ESCAPE:
                                        running = False
                                    if event6.key == pygame.K_n:
                                        frame1 += 1
                                        if frame1 == 2:
                                            TheEndScreen(size, screen, clock)
                            pygame.display.update()
                            clock.tick(FPS)

                    if event2.type == pygame.KEYDOWN:
                        if event2.key == pygame.K_UP:
                            up = True
                        if event2.key == pygame.K_LEFT:
                            left = True
                        if event2.key == pygame.K_RIGHT:
                            right = True

                    if event2.type == pygame.KEYUP:
                        if event2.key == pygame.K_ESCAPE:
                            running = False
                        if event2.key == pygame.K_UP:
                            up = False
                        if event2.key == pygame.K_RIGHT:
                            right = False
                        if event2.key == pygame.K_LEFT:
                            left = False
                self.player.update(left, right, up)
                self.camera.update(self.player)
                sprite_groups.danger.update()
                for e in sprite_groups.all_sprites:
                    screen.blit(e.image, self.camera.apply(e))
                if cats_found == 0:
                    screen.blit(pygame.transform.scale(load_image(constants.CATS_FOUND0, colorkey=None), size), (0, 0))
                if cats_found == 1:
                    screen.blit(pygame.transform.scale(load_image(constants.CATS_FOUND1, colorkey=None), size), (0, 0))
                if cats_found == 2:
                    screen.blit(pygame.transform.scale(load_image(constants.CATS_FOUND2, colorkey=None), size), (0, 0))
                if cats_found == 3:
                    screen.blit(pygame.transform.scale(load_image(constants.CATS_FOUND3, colorkey=None), size), (0, 0))
                if cats_found == 4:
                    screen.blit(pygame.transform.scale(load_image(constants.CATS_FOUND4, colorkey=None), size), (0, 0))
                pygame.display.update()
                clock.tick(FPS)
            pygame.display.update()
            clock.tick(FPS)
