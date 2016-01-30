from core.application import *
from core.controllers.mousecontroller import *


class Level:


    def __init__(self, app):

        self.__app    = app
        self.__screen = self.__app.screen()


    def update(self):

        pass


    def screen(self):

        return self.__screen


    def __del__(self):

        pass
