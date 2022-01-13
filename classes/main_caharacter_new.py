from classes import pyganim
from until_function import get_icon_dir
from constants import PATH_OF_MC_JUMP_LEFT, PATH_OF_MC_RUN_LEFT1, PATH_OF_MC_RUN_LEFT2, PATH_OF_MC_JUMP_RIGHT, \
    PATH_OF_MC_IDLE_RIGHT, PATH_OF_MC_RUN_RIGHT1, PATH_OF_MC_RUN_RIGHT2, PATH_OF_MC_IDLE_LEFT, GRAVITY, TILE_SIZE, \
    MOVE_SPEED, JUMP_POWER
import pygame
from sprite_groups import player, danger, all_sprites
import lists


class MainCharacter(pygame.sprite.Sprite):
    """На карте обозначено '@'"""

    ANIMATION_DELAY = 0.1
    # os.chdir("..")
    ICON_DIR = get_icon_dir()

    ANIMATION_RIGHT = [(f'{ICON_DIR}/%s' % PATH_OF_MC_IDLE_RIGHT),
                       (f'{ICON_DIR}/%s' % PATH_OF_MC_RUN_RIGHT1),
                       (f'{ICON_DIR}/%s' % PATH_OF_MC_RUN_RIGHT2)]

    ANIMATION_LEFT = [(f'{ICON_DIR}/%s' % PATH_OF_MC_IDLE_LEFT),
                      (f'{ICON_DIR}/%s' % PATH_OF_MC_RUN_LEFT1),
                      (f'{ICON_DIR}/%s' % PATH_OF_MC_RUN_LEFT2)]
    ANIMATION_JUMP_LEFT = [(f'{ICON_DIR}/%s' % PATH_OF_MC_JUMP_LEFT,
                            0.1)]
    ANIMATION_JUMP_RIGHT = [(f'{ICON_DIR}/%s' % PATH_OF_MC_JUMP_RIGHT,
                             0.1)]
    ANIMATION_STAY = [(f'{ICON_DIR}/%s' % PATH_OF_MC_IDLE_RIGHT, 0.1)]
    COLOR = "#888888"

    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, player)

        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = pos_x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = pos_y
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(pygame.Color(self.COLOR))
        self.rect = self.image.get_rect().move(TILE_SIZE * pos_x, TILE_SIZE * pos_y)
        # self.image.set_colorkey(pygame.Color(self.COLOR))
        self.alive = True

        boltAnim = []
        for anim in self.ANIMATION_RIGHT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in self.ANIMATION_LEFT:
            boltAnim.append((anim, self.ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)

        self.boltAnimStay = pyganim.PygAnimation(self.ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(self.ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(self.ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(self.ANIMATION_JUMP_LEFT)
        self.boltAnimJump.play()

    def set_current_level(self, map):
        # TODO зачем это?
        self.cur_level = map

    def is_alive(self):
        """Возвращает живой ли игрок"""
        return self.alive

    def kill(self):
        """Устанавливает мёртое состояние персонажа"""
        self.alive = False

    def update(self, left, right, up) -> None:
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
            self.image.fill(pygame.Color(self.COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(pygame.Color(self.COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(pygame.Color(self.COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
            if not up:
                self.image.fill(pygame.Color(self.COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, lists.collisiond)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, lists.collisiond)

        if pygame.sprite.spritecollideany(self, danger):
            self.alive = False

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
