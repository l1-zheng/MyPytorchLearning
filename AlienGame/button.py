import pygame.font


class Button():

    def __init__(self, al_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

