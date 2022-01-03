import pygame
from classes import config, tile, main_character, camera
from screen.main_screen import MainScreen


def main():
    pygame.init()
    client_config = config.Config()
    clock = pygame.time.Clock()
    size = width, height = client_config.get_screen_size()
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Кошки!)')

    MainScreen(size, screen, clock)
    print(size)


if __name__ == '__main__':
    main()
