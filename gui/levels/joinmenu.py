
# Import python modules
import pygame


# Import the base level
from gui.levels.level import *


# Import the widgets
from gui.widgets.button  import *
from gui.widgets.ipinput import *


class JoinMenu(Level):


    def __init__(self, app):

        super(JoinMenu, self).__init__(app)

        self.__controller = MouseController()

        self.__controller.onClick(self.click)

        self.__ipInput    = IpInput(self.screen(), 250, 250, 300, 50)
        self.__joinButton = Button(self.screen(), "Join", 250, 320, 300, 50)


    def click(self, point):

        if self.__joinButton.isInside(point[0], point[1]):

            self.app().join(self.__ipInput.text())


    def update(self):

        super(JoinMenu, self).update()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:

            return self.app().mainMenu()

        self.__controller.update()

        self.screen().surface().fill((0x21, 0x21, 0x21))

        self.__ipInput.render()
        self.__joinButton.render()
