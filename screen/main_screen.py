import pygame
from classes import config
from until_function import load_image, terminate
from constants import FPS, PATH_OF_MAINFON
from classes.buttons import Button
from screen.settings_screen import SettingsScreen

pygame.init()


class MainScreen:
    client_config = config.Config()

    def __init__(self, size: tuple, screen, clock):

        fon = pygame.transform.scale(load_image(PATH_OF_MAINFON), size)

        font = pygame.font.Font(None, 30)
        string_rendered = font.render("Главное меню", True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.left = size[0] / 2 - intro_rect.width / 2

        h = round(size[1] * 0.1)
        w = round(size[0] * 0.8)
        pos_x = round(size[0] * 0.1)
        btn_start = Button('white', pos_x, round(size[1] * 0.3), w, h, 'Играть')

        btn_settings = Button('white', pos_x, round(size[1] * 0.5), w, h, 'Настройки')

        btn_exit = Button('white', pos_x, round(size[1] * 0.7), w, h, 'Выход')

        while True:
            screen.blit(fon, (0, 0))
            btn_exit.draw(screen, 1)
            btn_start.draw(screen, 1)
            btn_settings.draw(screen, 1)
            screen.blit(string_rendered, intro_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if btn_exit.is_clicked(pos):
                        terminate()
                    elif btn_start.is_clicked(pos):
                        # TODO Вызов окна игры
                        pass
                    elif btn_settings.is_clicked(pos):
                        SettingsScreen(size, screen, clock)

            pygame.display.flip()
            clock.tick(FPS)
