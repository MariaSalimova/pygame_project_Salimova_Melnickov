import pygame
from classes import tile
from classes.main_character import MainCharacter

# TODO: доделать generate_level
def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                tile.Air(x, y)
            elif level[y][x] == '+':
                tile.BrickTile(x, y)
            elif level[y][x] == '/':
                tile.DeathTile(x, y)
            elif level[y][x] == '@':
                MainCharacter(x, y)

            pass
    return new_player, x, y