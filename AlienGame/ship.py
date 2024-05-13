import pygame


class Ship:

    def __init__(self, screen, al_settings):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.al_settings = al_settings
        # 加载飞船图像
        self.image = pygame.image.load('images/ship_2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 调整飞船位置，底部中央
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置,飞船不会飞出屏幕"""
        if self.moving_right & (self.rect.right < self.screen_rect.right):
            self.center += self.al_settings.ship_speed_factor
        if self.moving_left & (self.rect.left > 0):
            self.center -= self.al_settings.ship_speed_factor
        # 更新rect
        self.rect.centerx = self.center

    def blit_me(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


