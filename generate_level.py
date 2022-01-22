from classes import tile, enemy
from classes.main_caharacter_new import MainCharacter
from typing import Union
from lists import collisiond
import sprite_groups


def generate_level(level: Union[list, tuple]) -> (MainCharacter, int, int):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                continue
                # tile.Air(x, y)
            elif level[y][x] == '+':
                b = tile.BrickTile(x, y)
                collisiond.append(b)
            elif level[y][x] == '@':
                tile.Air(x, y)
                new_player = MainCharacter(x, y)
            elif level[y][x] == '!':
                # tile.Air(x, y)
                enemy.Enemy(x, y)
            elif level[y][x] == '%':
                # tile.Air(x, y)
                box_cat1 = tile.BoxCat(x, y)
                sprite_groups.box_cat1.add(box_cat1)
            elif level[y][x] == '$':
                box_cat2 = tile.BoxCat(x, y)
                sprite_groups.box_cat2.add(box_cat2)
            elif level[y][x] == '#':
                box_cat3 = tile.BoxCat(x, y)
                sprite_groups.box_cat3.add(box_cat3)
            elif level[y][x] == '*':
                box_cat4 = tile.BoxCat(x, y)
                sprite_groups.box_cat4.add(box_cat4)
    return new_player, x, y


def load_level(filename: str) -> list:
    """Загрузка карты из файла"""
    filename = "data/maps of levels/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
