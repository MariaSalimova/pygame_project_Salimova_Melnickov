from until_function import load_image
import pygame

pygame.init()
# Значения
FPS = 60
GRAVITY = 1
TILE_SIZE = 100
MOVE_SPEED = 5
JUMP_POWER = 25

# Пути
PATH_OF_TEXTURE = 'data/texture'
PATH_OF_MUSIC = 'data/sound/music'
PATH_OF_MAINFON = 'data/texture/fons/background.png'
PATH_OF_SETTINGFON = 'data/texture/fons/background.png'

# Игрок
PATH_OF_MC_IDLE_LEFT = 'data/texture/entities/main_character/main_character_idle/mc_idle_left.png'
PATH_OF_MC_IDLE_RIGHT = 'data/texture/entities/main_character/main_character_idle/mc_idle_right.png'
PATH_OF_MC_JUMP_LEFT = 'data/texture/entities/main_character/main_character_jump/mc_jump_left.png'
PATH_OF_MC_JUMP_RIGHT = 'data/texture/entities/main_character/main_character_jump/mc_jump_right.png'
PATH_OF_MC_RUN_LEFT1 = 'data/texture/entities/main_character/main_character_run/mc_run_left1.png'
PATH_OF_MC_RUN_LEFT2 = 'data/texture/entities/main_character/main_character_run/mc_run_left2.png'
PATH_OF_MC_RUN_RIGHT1 = 'data/texture/entities/main_character/main_character_run/mc_run_right1.png'
PATH_OF_MC_RUN_RIGHT2 = 'data/texture/entities/main_character/main_character_run/mc_run_right2.png'

# Враг
PATH_OF_ENEMY_RUN_LEFT1 = 'data/texture/entities/enemy/enemy_run/enemy_run1l.png'
PATH_OF_ENEMY_RUN_RIGHT1 = 'data/texture/entities/enemy/enemy_run/enemy_run1r.png'
PATH_OF_ENEMY_RUN_LEFT2 = 'data/texture/entities/enemy/enemy_run/enemy_run2l.png'
PATH_OF_ENEMY_RUN_RIGHT2 = 'data/texture/entities/enemy/enemy_run/enemy_run2r.png'
PATH_OF_ENEMY_IDLE_LEFT = 'data/texture/entities/enemy/enemy_idle/enemy_idle_l.png'
PATH_OF_ENEMY_IDLE_RIGHT = 'data/texture/entities/enemy/enemy_idle/enemy_idle_r.png'

# Текстуры
PATH_OF_BRICK = 'data/texture/tiles/brick_tile.png'
PATH_OF_MOVING_PLATFORM = 'data/texture/tiles/moving_platform.png'
PATH_OF_BOX_CAT = 'data/texture/tiles/box_cat.png'
PATH_OF_AIR = 'data/texture/tiles/air.png'

STORY_BEGINNING = [load_image('data/texture/controls.png', colorkey=None),
                   load_image('data/texture/story1.png', colorkey=None),
                   load_image('data/texture/story2.png', colorkey=None),
                   load_image('data/texture/story3.png', colorkey=None),
                   ]
STORY_ENDING1 = [load_image('data/texture/ending1_1.png', colorkey=None),
                 load_image('data/texture/ending1_2.png', colorkey=None)]
STORY_ENDING2 = [load_image('data/texture/ending2_1.png', colorkey=None),
                 load_image('data/texture/ending2_2.png', colorkey=None)]
FOUND_A_CAT = 'data/texture/found_a_cat.png'
CATS_FOUND0 = 'data/texture/cats_found0.png'
CATS_FOUND1 = 'data/texture/cats_found1.png'
CATS_FOUND2 = 'data/texture/cats_found2.png'
CATS_FOUND3 = 'data/texture/cats_found3.png'
CATS_FOUND4 = 'data/texture/cats_found4.png'
