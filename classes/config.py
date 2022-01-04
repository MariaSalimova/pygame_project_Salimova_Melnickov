import configparser
import pygame


class Config:

    def __init__(self, config_title='main.ini'):
        self.config_title = config_title
        self.client = configparser.ConfigParser()
        self.read_config()

    def save_config(self) -> None:
        """Запись файла конфига"""
        with open(self.config_title, 'w') as config_file:
            self.client.write(config_file)

    def read_config(self) -> None:
        """Считывание файла конфига"""
        self.client.read(self.config_title)

    def save_screen_size(self, width, height):
        screen = {'width': int(width),
                  'height': int(height)}
        self.client['screen'] = screen
        self.save_config()

    def get_screen_size(self):
        size = tuple(self.client['screen'].values())
        info_object = pygame.display.Info()
        if all(size):
            return tuple(map(int, size))
        size = info_object.current_w, info_object.current_h
        self.client['screen'] = {'width': size[0], 'height': size[1]}
        self.save_config()
        return size
