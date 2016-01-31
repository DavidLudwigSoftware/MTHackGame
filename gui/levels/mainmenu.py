
# Import python modules
import pygame


# Import the base level
from gui.levels.level import *


# Import the widgets
from gui.widgets.button  import *


class MainMenu(Level):


    def __init__(self, app):

        super(MainMenu, self).__init__(app)

        self.__controller = MouseController()

        self.__hostButton = Button(self.screen(), "Host", 250, 200, 300, 50)
        self.__joinButton = Button(self.screen(), "Join", 250, 270, 300, 50)

        self.__hostButton.onClick(self.app().host)
        self.__joinButton.onClick(self.app().joinMenu)


    def update(self):

        super(MainMenu, self).update()

        self.__controller.update()

        self.screen().surface().fill((0x21, 0x21, 0x21))

        self.__hostButton.render()
        self.__joinButton.render()
