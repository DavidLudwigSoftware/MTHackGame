
# Import the python modules
import pygame

# Import the base entity
from gui.entities.entity import *


class Player(Entity):

    FacingLeft    = 0
    FacingRight   = 1
    FacingUp      = 0
    FacingDown    = 10
    FacingNeutral = 20


    def __init__(self, screen, world, player = 0, facing = FacingLeft+FacingNeutral):

        self.__player = player
        self.__rect = [0, 0, 50, 50]

        self.__facing = facing

        super(Player, self).__init__(screen, world, self.__rect)

        self.__MHP = 100
        self.__HP = self.__MHP

        


    def update(self):

        self.render()

    def hp(self):

        return self.__HP

    def takedamage(self, damage):

        self.__HP = self.__HP - damage


    def render(self):

        pygame.draw.rect(self.screen().surface(), (0xff, 0x00, 0x00), self.rect())

    def facing(self):
        return self.__facing
