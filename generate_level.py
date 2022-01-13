from classes import tile, enemy
from classes.main_caharacter_new import MainCharacter
from typing import Union
from lists import collisiond


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
            elif level[y][x] == '/':
                tile.DeathTile(x, y)
            elif level[y][x] == '@':
                tile.Air(x, y)
                new_player = MainCharacter(x, y)
            elif level[y][x] == '!':
                # tile.Air(x, y)
                enemy.Enemy(x, y)
            elif level[y][x] == '%':
                # tile.Air(x, y)
                tile.BoxCat(x, y)
            elif level[y][x] == '$':
                m = tile.MovingPlatform(x, y)
                collisiond.append(m)

    return new_player, x, y


def load_level(filename: str) -> list:
    """Загрузка карты из файла"""
    filename = "data/maps of levels/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
