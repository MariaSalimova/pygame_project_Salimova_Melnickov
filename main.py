import pygame
from classes import config
from screen.main_screen import MainScreen


def main():
    pygame.init()
    pygame.key.set_repeat(25)
    client_config = config.Config()
    clock = pygame.time.Clock()
    size = width, height = client_config.get_screen_size()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Cat Rescue')
    pygame.key.set_repeat(200, 25)
    MainScreen(size, screen, clock)
    print(size)


if __name__ == '__main__':
    main()
