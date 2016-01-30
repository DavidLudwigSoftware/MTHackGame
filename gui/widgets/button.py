from gui.widgets.widget import *
import pygame


class Button(Widget):


    def __init__(self, screen, text, x, y, width, height):
        super(Button, self).__init__(x, y, width, height)

        self.__screen = screen
        self.__text = text

        self.__rect = (x, y, width, height)

        font = pygame.font.SysFont("monospace", 30)

        self.__label = font.render(text, 1, (240, 240, 240))


    def render(self):

        pygame.draw.rect(self.__screen.surface(), (0xff, 0x57, 0x22), self.__rect)

        self.__screen.surface().blit(self.__label, (self.__rect[0] + 120, self.__rect[1] + 9))
