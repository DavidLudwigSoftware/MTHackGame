
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

        name = "res/sprites/players/p" + str(player + 1) + "_"

        self.__sprites = [
            pygame.image.load(name + "lwalk1.png"),
            pygame.image.load(name + "lwalk2.png"),
            pygame.image.load(name + "lwalk3.png"),
            pygame.image.load(name + "lwalk4.png"),
            pygame.image.load(name + "rwalk1.png"),
            pygame.image.load(name + "rwalk2.png"),
            pygame.image.load(name + "rwalk3.png"),
            pygame.image.load(name + "rwalk4.png"),
        ]

        super(Player, self).__init__(screen, world, self.__rect)

        self.__MHP = 100
        self.__HP = self.__MHP

        self.setSprite(4)


    def update(self):

        self.render()

    def hp(self):

        return self.__HP

    def takedamage(self, damage):

        self.__HP = self.__HP - damage


    def sprite(self):

        return self.__sprite


    def setSprite(self, sprite):

        return self.__sprite = sprite[sprite]


    def render(self):

        self.screen().surface().blit(self.__sprite, (self.x(), self.y()))

    def facing(self):
        return self.__facing
