import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, al_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.al_settings = al_settings
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # 外星人初始位置都在屏幕左上角
        self.rect.x = 0 # self.rect.width
        self.rect.y = 0 # self.rect.height
        # 存储外星人的位置
        self.x = float(self.rect.x)

    def blit_me(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向左、右移动外星人"""
        self.x += self.al_settings.alien_speed_factor * self.al_settings.fleet_direction
        self.rect.x = self.x

    def check_edge(self):
        """如果外星人位于屏幕边缘，返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def check_bottom(self):
        """如果外星人位于屏幕底部，返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom - self.rect.height:
            # 游戏结束，输了~~
            pygame.mixer.music.load('musics/end.mp3')
            pygame.mixer.music.play(-1)
            return True



