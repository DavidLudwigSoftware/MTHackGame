
# Import python modules
import pygame

# Import the base widget
from gui.widgets.widget import *


class Text(Widget):


    def __init__(self, screen, text = "", color = (255, 255, 255), x = 0, y = 0, width = 0, height = 0, center = False, font = "monospace", textSize = 30):

        # Call the superclass
        super(Text, self).__init__(screen, x, y, width, height)

        # Save the parameters
        self.__color  = color
        self.__center = center

        # Create the font
        self.__font   = pygame.font.SysFont(font, textSize)

        # Initialize the bitmap and save rectangle
        self.__blit = None
        self.__rect = x, y, width, height

        # Set the text
        self.setText(text)


    def setText(self, text):

        # Update the text
        self.__text = text

        # Delete the old text bitmap
        del self.__blit

        # Create the new text bitmap
        self.__blit = self.__font.render(text, 1, self.__color)

        # Resize the rectangle
        self.resize(self.__blit.get_rect())


    def setColor(self, color):

        # Set the text color
        self.__color = color

        # Reset the text
        self.setText(self.__text)


    def render(self):

        
        if self.__center:

            # Create the coordinate point
            point = (
                self.__rect[0] + (self.__rect[2] / 2) - (self.__blit.get_width()  / 2),
                self.__rect[1] + (self.__rect[3] / 2) - (self.__blit.get_height() / 2)
            )

        else:

            # Create the coordinate point
            point = (
                self.__rect[0],
                self.__rect[1] + (self.__rect[3] / 2) - (self.__blit.get_height() / 2)
            )

        # Draw the text on the screen
        self.screen().surface().blit(self.__blit, point)
