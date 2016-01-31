
# Import the python modules
import pygame


# Import the base widget
from gui.widgets.widget import *

# Import the text widget
from gui.widgets.text import *


class IpInput(Widget):

    FocusColor   = (0x42, 0x42, 0x42)
    DefaultColor = (0x42, 0x42, 0x42)

    def __init__(self, screen, x, y, width, height):

        super(IpInput, self).__init__(screen, x, y, width, height)

        self.__text = Text(screen, 'IP Address', (240, 240, 240), x, y, width, height, True)

        self.__isFocused = False


    def render(self):

        if self.isInside(pygame.mouse.get_pos()):

            color = IpInput.FocusColor

            if pygame.mouse.get_pressed()[0]:

                self.__isFocused = True


        elif self.__isFocused:

            color = IpInput.FocusColor


        elif pygame.mouse.get_pressed()[0]:

            color = IpInput.DefaultColor
            self.__isFocused = False

        else:

            color = IpInput.DefaultColor


        pygame.draw.rect(self.screen().surface(), color, self.rect(), 2)
