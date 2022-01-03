import pygame
from classes import config
from until_function import load_image, terminate
from constants import FPS, PATH_OF_MAINFON
from classes.buttons import Button


pygame.init()


class MainScreen:

    client_config = config.Config()

    def __init__(self, size: tuple, screen, clock):

        fon = pygame.transform.scale(load_image(PATH_OF_MAINFON), size)
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        string_rendered = font.render("Главное меню", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.left = size[0] / 2 - intro_rect.width / 2
        screen.blit(string_rendered, intro_rect)
        h = round(size[1] * 0.1)
        w = round(size[0] * 0.8)
        pos_x = round(size[0] * 0.1)
        start = Button('white', pos_x, round(size[1] * 0.3), w, h, 'Играть')
        start.draw(screen)

        settings = Button('white', pos_x, round(size[1] * 0.5), w, h, 'Настройки')
        settings.draw(screen)

        test = Button('white', pos_x, round(size[1] * 0.7), w, h, 'Выход')
        test.draw(screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            clock.tick(FPS)
