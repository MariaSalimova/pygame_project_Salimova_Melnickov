import pygame
import sprite_groups
from generate_level import generate_level, load_level
from classes.camera import Camera
from until_function import terminate
from constants import FPS
from screen.game_over_screen import GameOverScreen


class Level1Screen:
    def __init__(self, size: tuple, screen, clock):

        pygame.key.set_repeat(200, 25)

        self.level_map = load_level('level_2')
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.move("up")
                    elif event.key == pygame.K_s:
                        self.move("down")
                    elif event.key == pygame.K_a:
                        self.move("left")
                    elif event.key == pygame.K_d:
                        self.move("right")

            self.camera.update(self.player)
            self.player.update(self.camera)
            sprite_groups.tiles.draw(screen)
            sprite_groups.player.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)

    def move(self, movement):
        x, y = self.player.pos
        if movement == "up":
            if y > 0 and self.level_map[y - 1][x] == '.':
                self.player.move(x, y - 1, self.camera)
        elif movement == "down":
            if y < self.level_y - 1 and self.level_map[y + 1][x] == '.':
                self.player.move(x, y + 1, self.camera)
        elif movement == "left":
            if x > 0 and self.level_map[y][x - 1] == '.':
                self.player.move(x - 1, y, self.camera)
        elif movement == "right":
            if x < self.level_x and self.level_map[y][x + 1] == '.':
                self.player.move(x + 1, y, self.camera)
