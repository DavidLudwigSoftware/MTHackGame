
import pygame


from gui.entities.entity import *


class Gun(Entity):

    FireRate = 0.2
    GunPower = 20

    def __init__(self, screen, world, style = Invisible, x = 0, y = 0, width = 0, height = 0):

        super(Gun, self).__init__(screen, world, (x, y, width, height))

        self.__style = style

        self.__canshoot = 1.0

    def canshoot(self):
        return self.__canshoot

    def shoot(self):
        self.__canshoot = 0.0


    def update(self):

        self.__canshoot = self.canshoot + Gun.FireRate

        if self.__canshoot > 1.0:
            self.__canshoot = 1.0
