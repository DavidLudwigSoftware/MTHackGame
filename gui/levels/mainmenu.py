from gui.levels.level import *
from gui.widgets.button import *
from gui.widgets.player import *
import pygame

class MainMenu(Level):


    def __init__(self, app):

        super(MainMenu, self).__init__(app)

        self.__controller = MouseController()

        self.__controller.onClick(self.click)

        self.__hostButton = Button(self.screen(), "Host", 250, 200, 300, 50)
        self.__joinButton = Button(self.screen(), "Join", 250, 270, 300, 50)

        self.__player = Player()


    def click(self, point):

        if self.__hostButton.isInside(point[0], point[1]):

            print("You click the host button")

        elif self.__joinButton.isInside(point[0], point[1]):

            print("You click the join button")


    def update(self):

        super(MainMenu, self).update()

        self.__controller.update()

        self.screen().surface().fill((0x21, 0x21, 0x21))

        self.__hostButton.render()
        self.__joinButton.render()

        self.__player.render(self.screen().surface())
