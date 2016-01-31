
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

        self.__speed = 1

        self.__controller = PlayerController()
        self.__controller.onKeyPress(self.keypress)
        self.__controller.onKeyRelease(self.keyrelease)


    def calcposition(self):

        #creates tempx, temph, tempw and tempy vars for checking collision and calculating things
        tempx = self.x() - self.__dx
        tempy = self.y() - self.__dy
        tempw = self.right() - self.__dx
        temph = self.bottom() - self.__dy

        #gets keyboard input

        if self.__controller.key(pygame.K_LEFT):
            if self.__dx <= 5:
                self.__dx = self.__dx + self.__speed
        elif self.__controller.key(pygame.K_RIGHT):
            if self.__dx >= -5:
                self.__dx = self.__dx - self.__speed
        else:
            if self.__dx > 0.0:
                self.__dx = self.__dx - self.world().friction()
                if self.__dx < 0.0:
                    self.__dx = 0.0
            elif self.__dx < 0.0:
                self.__dx = self.__dx + self.world().friction()
                if self.__dx > 0.0:
                    self.__dx = 0.0


        #calculate gravity
        if self.__dy <= 10:
            self.__dy = self.__dy - self.world().gravity()

        #sets the delta y properly
        if (self.screen().height() - self.world().floor()/2) <= self.bottom():
            self.__dy = self.__dy + (self.bottom() - (self.screen().height() - self.world().floor()/2)) - self.height()
            if self.__dy < 0.0:
                self.__dy = 0.0

        newx = self.x() - self.__dx
        newy = self.y() - self.__dy


        #saftey for if the object goes past floor
        if (self.screen().height() - self.world().floor()/2) < self.bottom():
            newy = (self.screen().height() - self.world().floor()/2) - self.height()


        #anti jitter
        if ((self.screen().height() - self.world().floor()/2) <= temph) and (self.__dy < 0.0):
            newy = (self.screen().height() - self.world().floor()/2) - self.height()

        #set the new x and y variable
        self.setX(newx)
        self.setY(newy)

    def keypress(self, key):
        if key == pygame.K_z:
            self.__dy = 10

    def keyrelease(self, key):
        if key == pygame.K_x:
            pass

    def update(self):

        self.__controller.update()

        self.calcposition()

        # Render the player (Leave this on the end)
        self.render()
