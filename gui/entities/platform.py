
import pygame


from gui.entities.entity import *


class Platform(Entity):

    Invisible = 0

    def __init__(self, screen, world, style = Invisible, x = 0, y = 0, width = 0, height = 0):

        super(Platform, self).__init__(screen, world, (x, y, width, height))

        self.__style = style


    def render(self):

        pass

        #if self.__style == Platform.Invisible:

            #pygame.draw.rect(self.screen().surface(), (0x00, 0xff, 0x00), self.rect())
