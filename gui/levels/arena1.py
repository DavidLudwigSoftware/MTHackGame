
# Import python modules
import pygame


# Import the base level
from gui.levels.level import *


# Import the entities
from gui.entities.physicsplayer import *


class Arena1(Level):


    def __init__(self, app):

        super(Arena1, self).__init__(app)

        self.__player = PhysicsPlayer(app.screen())


    def update(self):

        super(Arena1, self).update()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:

            return self.app().mainMenu()

        self.screen().surface().fill((0, 0, 0))

        self.__player.update()
