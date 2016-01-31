
# Import the python modules
import pygame


class PlayerController:


    def __init__(self):

        self.__keyPressCallback   = None
        self.__keyReleaseCallback = None

        self.__keyMap = {
            pygame.K_z     : False,
            pygame.K_x     : False,
            pygame.K_c     : False,
            pygame.K_UP    : False,
            pygame.K_DOWN  : False,
            pygame.K_LEFT  : False,
            pygame.K_RIGHT : False,
        }

        self.__enabled = True


    def onKeyPress(self, callback):

        self.__keyPressCallback = callback


    def onKeyRelease(self, callback):

        self.__keyReleaseCallback = callback


    def key(self, key):

        if self.__enabled:

            return self.__keyMap[key]

        return 0


    def update(self):

        if not self.__enabled:
            return

        keys = pygame.key.get_pressed()

        for key in self.__keyMap.keys():

            if keys[key] != self.__keyMap[key]:

                if keys[key]:

                    self.__keyPressCallback(key)

                else:

                    self.__keyReleaseCallback(key)

                self.__keyMap[key] = keys[key]
