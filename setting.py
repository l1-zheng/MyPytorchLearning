class Settings():
    """存储所有设置的类"""

    def __init__(self):
        """初始胡游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (250, 230, 230)
        self.ship_speed_factor = 1.5
        # 子弹设置,速度低于飞船
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 100, 100, 100
        self.bullet_allowed = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1



