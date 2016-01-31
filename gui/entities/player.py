
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
        self.__rect = [0, 0, 70, 70]

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


    def update(self):

        self.render()


    def render(self):

        self.screen().surface().blit(self.__sprites[4], (self.x(), self.y()))

    def facing(self):
        return self.__facing
