import pygame
# sprite类是一个简单的精灵类，可以将游戏中相关的元素编组，进而同时操作编组中的所有元素
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, al_settings, screen, ship):
        """在飞船所处位置创建一个子弹对象"""

        # 类继承
        super(Bullet, self).__init__()
        self.screen = screen
        # 在(0,0)处创建子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, al_settings.bullet_width, al_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = al_settings.bullet_color
        self.speed_factor = al_settings.bullet_speed_factor

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

