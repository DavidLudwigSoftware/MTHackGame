
# Import python modules
import pygame


# Import the base level
from gui.levels.level import *


# Import the entities
from gui.entities.physicsplayer import *


class Arena1(Level):


    def __init__(self, app):

        super(Arena1, self).__init__(app)

        self.__gravity = 0.5

        self.__friction = 0.2

        self.__floor = 65

        self.__player = PhysicsPlayer(app.screen(), self)


    def gravity(self):

        return self.__gravity


    def friction(self):

        return self.__friction


    def floor(self):

        return self.__floor


    def update(self):

        super(Arena1, self).update()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:

            return self.app().mainMenu()

        self.screen().surface().fill((0, 0, 0))

        self.__player.update()
