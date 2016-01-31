
# Import the python modules
import pygame


# Import the base entity
from gui.entities.player import *


# Import the player controller
from core.controllers.playercontroller import *


class PhysicsPlayer(Player):


    def __init__(self, screen, world, player = 0):

        super(PhysicsPlayer, self).__init__(screen, world, player)

        self.__dx = 0.0
        self.__dy = 0.0

        self.__controller = PlayerController()


    def calcposition(self):

        #creates tempx, temph, tempw and tempy vars for checking collision and calculating things
        tempx = self.x() - self.__dx
        tempy = self.y() - self.__dy
        tempw = self.right() - self.__dx
        temph = self.bottom() - self.__dy

        #calculate gravity
        if self.__dy <= 10:
            self.__dy = self.__dy - self.world().gravity()

        if (self.screen().height() - self.world().floor()/2) <= temph:
            self.__dy = self.__dy + (temph - (self.screen().height() - self.world().floor()/2))
            if self.__dy < 0.0:
                print("This happened", temph, self.screen().height() - self.world().floor()/2)
                self.__dy = 0.0

        print(self.__dy)

        newx = self.x() - self.__dx
        newy = self.y() - self.__dy

        if (self.screen().height() - self.world().floor()/2) < self.bottom():
            newy = (self.screen().height() - self.world().floor()/2) - self.height()

        #set the new x and y variable
        self.setX(newx)
        self.setY(newy)

        return newx, newy


    def update(self):

        tx, ty = self.calcposition()

        # Render the player (Leave this on the end)
        try:
            self.render()
        except:
            pass
