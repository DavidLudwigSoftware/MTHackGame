
# Import the python modules
import pygame

# Import the base entity
from gui.entities.entity import *


class Player(Entity):


    def __init__(self, screen, player = 0):

        self.__player = player
        self.__rect = [0, 0, 50, 50]

        super(Player, self).__init__(screen, self.__rect)


    def update(self):

        self.render()


    def render(self):

        pygame.draw.rect(self.screen().surface(), (0xff, 0x00, 0x00), self.rect())
