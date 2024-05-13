import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
# Group用于存储和管理游戏中的所有精灵（Sprite）对象。提供了一种方便的方式来更新和绘制所有的精灵
from pygame.sprite import Group
from alien import Alien
from game_starts import GameStarts


def run_game():
    # 初始化游戏，并创建一个屏幕对象
    pygame.init()
    pygame.mixer.init(frequency=15500, size=-16, channels=4)
    # 战歌响起~~
    pygame.mixer.music.load('musics/BGM.flac')
    pygame.mixer.music.play(-1)
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width, al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    # starts = GameStarts(al_settings)
    # 创建飞船
    ship = Ship(screen, al_settings)
    # 创建存储子弹的组
    bullets = Group()
    # 创建存放外星人的组
    aliens = Group()
    # 创建外星人群
    # alien = Alien(al_settings, screen)
    gf.create_fleet(al_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(al_settings, screen, ship,  bullets)
        ship.update()
        gf.update_bullets(bullets, aliens, al_settings, screen, ship)
        gf.update_aliens(al_settings, aliens, ship)
        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(al_settings, screen, ship, bullets, aliens)


run_game()




