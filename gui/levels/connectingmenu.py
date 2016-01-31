
# Import python modules
import pygame


# Import the base level
from gui.levels.level import *


# Import the widgets
from gui.widgets.text import *


class ConnectingMenu(Level):


    def __init__(self, app):

        super(ConnectingMenu, self).__init__(app)

        self.__text = Text(self.screen(), "Joining...", (255, 255, 255),
            0, 0, self.screen().width(), self.screen().height(), True
        )


    def update(self):

        super(ConnectingMenu, self).update()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:

            return self.app().mainMenu()

        self.screen().surface().fill((0x21, 0x21, 0x21))

        self.__text.render()
