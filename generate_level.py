from classes import tile, enemy
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
                tile.Air(x, y)
                new_player = MainCharacter(x, y)
            elif level[y][x] == '!':
                enemy.Enemy(x, y)
            elif level[y][x] == '%':
                tile.BoxCat(x, y)
            elif level[y][x] == '$':
                tile.MovingPlatform(x, y)

    return new_player, x, y


def load_level(filename):
    filename = "data/maps of levels/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
