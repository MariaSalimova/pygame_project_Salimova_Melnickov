import pygame.display

from until_function import load_image, terminate
from constants import PATH_OF_SETTINGFON, FPS
import pygame as pg
from classes.config import Config
from classes.buttons import Button

pg.init()


class SettingsScreen:

    def __init__(self, size: tuple[int, int], screen, clock):

        self.size = size
        self.client = Config()
        pg.key.set_repeat(200, 25)

        active_width = False
        active_height = False

        clock = clock

        self.generate()

        running = True
        while running:
            screen.blit(self.fon, (0, 0))
            screen.blit(self.string_settings, self.intro_rect)
            screen.blit(self.height, self.height_rect)
            screen.blit(self.width, self.width_rect)
            self.btn_save.draw(screen, 'green')
            self.btn_exit.draw(screen, 'red')

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
                if event.type == pg.MOUSEBUTTONDOWN:

                    if self.width_input.collidepoint(event.pos):
                        active_width = not active_width
                    else:
                        active_width = False

                    if self.height_input.collidepoint(event.pos):
                        active_height = not active_height
                    else:
                        active_height = False

                    if self.btn_save.is_clicked(event.pos):
                        self.size = tuple(map(int, (self.text_width, self.text_height)))
                        self.client.save_screen_size(self.size[0], self.size[1])

                        resized_screen = pygame.transform.scale(self.get_screen()[0], (size[0], size[1]))
                        screen.blit(resized_screen, (0, 0))
                        self.generate()

                    elif self.btn_exit.is_clicked(event.pos):
                        running = False
                        break

                if event.type == pg.KEYDOWN:

                    if active_height:
                        if event.key == pg.K_RETURN:
                            self.text_height = ''
                        elif event.key == pg.K_BACKSPACE:
                            self.text_height = self.text_height[:-1]
                        else:
                            letter: str = event.unicode
                            if letter.isdigit():
                                self.text_height += letter

                    if active_width:
                        if event.key == pg.K_RETURN:
                            self.text_width = ''
                        elif event.key == pg.K_BACKSPACE:
                            self.text_width = self.text_width[:-1]
                        else:
                            letter: str = event.unicode
                            if letter.isdigit():
                                self.text_width += letter

            txt_surface_w = self.font.render(self.text_width, True, self.color_active if active_width else self.color_inactive)
            screen.blit(txt_surface_w, (self.width_input.x + 5, self.width_input.y + 5))
            pg.draw.rect(screen, self.color_active if active_width else self.color_inactive, self.width_input, 2)

            txt_surface_h = self.font.render(self.text_height, True, self.color_active if active_height else self.color_inactive)
            screen.blit(txt_surface_h, (self.height_input.x + 5, self.height_input.y + 5))
            pg.draw.rect(screen, self.color_active if active_height else self.color_inactive, self.height_input, 2)

            pg.display.flip()
            clock.tick(FPS)

    def get_screen(self):
        return pygame.display.set_mode(self.size), self.size

    def generate(self):

        self.fon = pg.transform.scale(load_image(PATH_OF_SETTINGFON), self.size)
        self.font = pg.font.Font(None, 30)
        self.string_settings = self.font.render("Настройки", True, pg.Color('black'))
        self.intro_rect = self.string_settings.get_rect()
        self.intro_rect.left = self.size[0] / 2 - self.intro_rect.width / 2

        self.btn_save = Button('green', self.size[0] // 2 - 50, self.size[1] - 100, 100, 50, 'Сохранить')
        self.btn_exit = Button('red', 0, self.size[1] - 50, 50, 50, 'E')

        self.color_inactive = pg.Color('black')
        self.color_active = pg.Color('dodgerblue2')

        self.width = self.font.render('Длина экрана:', True, self.color_inactive)
        self.width_rect = self.width.get_rect()
        self.width_rect.right = self.size[0] / 2 - 102
        self.width_rect.top = self.size[1] * 0.328 + 5

        self.height = self.font.render('Высота экрана:', True, self.color_inactive)
        self.height_rect = self.height.get_rect()
        self.height_rect.right = self.size[0] / 2 - 102
        self.height_rect.top = self.size[1] * 0.328 + 55

        self.width_input = pg.Rect(self.size[0] / 2 - 100, self.size[1] * 0.328, 200, 30)
        self.height_input = pg.Rect(self.size[0] / 2 - 100, self.size[1] * 0.328 + 50, 200, 30)

        self.text_width, self.text_height = map(str, self.client.get_screen_size())
