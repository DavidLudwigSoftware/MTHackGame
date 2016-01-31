
# Import the python modules
import pygame


# Import the widgets
from gui.widgets.widget import *
from gui.widgets.text   import *


class Button(Widget):


    def __init__(self, screen, text, x, y, width, height, textSize = 30):

        # Call the superclass
        super(Button, self).__init__(screen, x, y, width, height)

        # Create the button text
        self.__text = Text(screen, text, (240, 240, 240), x, y, width, height, True, textSize = textSize)

        # Store the mouse state
        self.__mouseDown = False

        # Store callbacks
        self.__clickCallback = None


    def onClick(self, callback):

        self.__clickCallback = callback


    def render(self):

        # Check if the button is hovered
        if self.isInside(pygame.mouse.get_pos()):

            # Set the hover color
            color = (0xbf, 0x36, 0x0c)

            # Check if the mouse is pressed
            if pygame.mouse.get_pressed()[0] and not self.__mouseDown:

                self.__mouseDown = True

                # Check if a callback has been set
                if self.__clickCallback:

                    # Call the callback
                    self.__clickCallback()


        else:

            # Set the default color
            color = (0xff, 0x57, 0x22)

        # Draw the button shape
        pygame.draw.rect(self.screen().surface(), color, self.rect())

        # Render the text
        self.__text.render()
