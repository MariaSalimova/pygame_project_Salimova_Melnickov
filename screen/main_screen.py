import pygame
from classes import config
from until_function import load_image, terminate
from constants import FPS, PATH_OF_MAINFON
from classes.buttons import Button
from screen.settings_screen import SettingsScreen
from screen.the_game_itself import TheGameItself
pygame.init()


class MainScreen:
    client_config = config.Config()

    def __init__(self, size: tuple, screen, clock):

        self.size = size
        self.generate()

        while True:
            screen.blit(self.fon, (0, 0))
            self.btn_exit.draw(screen, 1)
            self.btn_start.draw(screen, 1)
            self.btn_settings.draw(screen, 1)
            screen.blit(self.string_rendered, self.intro_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                    if self.btn_exit.is_clicked(pos):
                        terminate()

                    elif self.btn_start.is_clicked(pos):
                        TheGameItself(size, screen, clock)

                    elif self.btn_settings.is_clicked(pos):
                        s = SettingsScreen(self.size, screen, clock)
                        screen2, self.size = s.get_screen()
                        resized_screen = pygame.transform.scale(screen2, (size[0], size[1]))
                        screen.blit(resized_screen, (0, 0))
                        self.generate()

            pygame.display.flip()
            clock.tick(FPS)

    def generate(self):
        self.fon = pygame.transform.scale(load_image(PATH_OF_MAINFON), self.size)

        font = pygame.font.Font(None, 100)
        self.string_rendered = font.render("Cat Rescue", True, pygame.Color('black'))
        self.intro_rect = self.string_rendered.get_rect()
        self.intro_rect.left = self.size[0] / 2 - self.intro_rect.width / 2
        self.intro_rect.top = self.intro_rect.height

        h = round(self.size[1] * 0.1)
        w = round(self.size[0] * 0.8)
        pos_x = round(self.size[0] * 0.1)

        self.btn_start = Button('white', pos_x, round(self.size[1] * 0.3), w, h, 'Играть')

        self.btn_settings = Button('white', pos_x, round(self.size[1] * 0.5), w, h, 'Настройки')

        self.btn_exit = Button('white', pos_x, round(self.size[1] * 0.7), w, h, 'Выход')
