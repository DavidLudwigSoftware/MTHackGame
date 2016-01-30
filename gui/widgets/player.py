from gui.widgets.widget import *
import pygame


class Player(Widget):

    def __init__(self):

        self.bitmap = pygame.image.load("res/sprites/players/player_1.png")
        self.rect = self.bitmap.get_rect()


    def render(self, screen):

        screen.blit(self.bitmap, self.rect)
