class GameStarts:

    def __init__(self, al_settings):
        self.al_settings = al_settings
        self.ships_left = 0
        self.rect_starts()
        self.game_active = False

    def rect_starts(self):
        self.ships_left = self.al_settings.ship_limit

