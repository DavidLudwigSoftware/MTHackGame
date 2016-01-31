from core.application import *
from core.controllers.mousecontroller import *


class Level:


    def __init__(self, app):

        # Store the application instance
        self.__app    = app

        # Store the entities
        self.__entities = {}


    def update(self):

        # Override this method to update the world
        pass


    def app(self):

        # Return the application instance
        return self.__app


    def screen(self):

        # Return the screen
        return self.__app.screen()


    def __del__(self):

        pass
