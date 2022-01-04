from until_function import load_image, terminate
from constants import PATH_OF_SETTINGFON, FPS
import pygame as pg
from classes.config import Config
from classes.buttons import Button

pg.init()


class SettingsScreen:

    def __init__(self, size: tuple, screen, clock):
        fon = pg.transform.scale(load_image(PATH_OF_SETTINGFON), size)
        font = pg.font.Font(None, 30)
        string_settings = font.render("Настройки", True, pg.Color('white'))
        intro_rect = string_settings.get_rect()
        intro_rect.left = size[0] / 2 - intro_rect.width / 2

        client = Config()

        clock = clock

        btn_save = Button('green', size[0] // 2 - 50, size[1] - 100, 100, 50, 'Сохранить')

        color_inactive = pg.Color('lightskyblue3')
        color_active = pg.Color('dodgerblue2')

        pg.key.set_repeat(200, 25)

        width = font.render('Длина экрана:', True, color_inactive)
        width_rect = width.get_rect()
        width_rect.right = size[0] / 2 - 102
        width_rect.top = size[1] * 0.328 + 5

        height = font.render('Высота экрана:', True, color_inactive)
        height_rect = height.get_rect()
        height_rect.right = size[0] / 2 - 102
        height_rect.top = size[1] * 0.328 + 55

        width_input = pg.Rect(size[0] / 2 - 100, size[1] * 0.328, 200, 30)
        height_input = pg.Rect(size[0] / 2 - 100, size[1] * 0.328 + 50, 200, 30)

        active_width = False
        active_height = False

        text_width, text_height = map(str, client.get_screen_size())
        running = True
        while running:
            screen.blit(fon, (0, 0))
            screen.blit(string_settings, intro_rect)
            screen.blit(height, height_rect)
            screen.blit(width, width_rect)
            btn_save.draw(screen, 'green')

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
                if event.type == pg.MOUSEBUTTONDOWN:

                    if width_input.collidepoint(event.pos):
                        active_width = not active_width
                    else:
                        active_width = False

                    if height_input.collidepoint(event.pos):
                        active_height = not active_height
                    else:
                        active_height = False

                    if btn_save.is_clicked(event.pos):
                        client.save_screen_size(text_width, text_height)
                        running = False
                        break

                if event.type == pg.KEYDOWN:

                    if active_height:
                        if event.key == pg.K_RETURN:
                            print(text_height)
                            text_height = ''
                        elif event.key == pg.K_BACKSPACE:
                            text_height = text_height[:-1]
                        else:
                            letter: str = event.unicode
                            if letter.isdigit():
                                text_height += letter

                    if active_width:
                        if event.key == pg.K_RETURN:
                            print(text_width)
                            text_width = ''
                        elif event.key == pg.K_BACKSPACE:
                            text_width = text_width[:-1]
                        else:
                            letter: str = event.unicode
                            if letter.isdigit():
                                text_width += letter

            txt_surface_w = font.render(text_width, True, color_active if active_width else color_inactive)
            screen.blit(txt_surface_w, (width_input.x + 5, width_input.y + 5))
            pg.draw.rect(screen, color_active if active_width else color_inactive, width_input, 2)

            txt_surface_h = font.render(text_height, True, color_active if active_height else color_inactive)
            screen.blit(txt_surface_h, (height_input.x + 5, height_input.y + 5))
            pg.draw.rect(screen, color_active if active_height else color_inactive, height_input, 2)

            pg.display.flip()
            clock.tick(FPS)
