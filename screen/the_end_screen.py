import pygame
from constants import PATH_OF_MAINFON
from until_function import terminate, load_image
pygame.init()


class TheEndScreen:
    def __init__(self, size: tuple, screen, clock):
        bg = pygame.transform.scale(pygame.transform.scale(load_image(PATH_OF_MAINFON), size), size)
        text = ['Esc - выйти из игры',
                'КОНЕЦ'
                ]
        screen.blit(bg, (0, 0))
        font = pygame.font.Font(None, 100)
        text_coord = size[1] // 2
        self.running = True
        for line in text:
            string_rendered = font.render(line, True, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()

            pygame.display.flip()
            clock.tick(30)
