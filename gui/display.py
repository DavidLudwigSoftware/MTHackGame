import pygame


class Display:

    def __init__(self, width, height):

        # The width and height of the window
        self.__width  = width
        self.__height = height

        # Create the pygame window
        self.__screen = pygame.display.set_mode((width, height))


    def width(self):

        return self.__width


    def height(self):

        return self.__height


    def render(self):

        # Render the screen
        pygame.display.flip()


    def surface(self):

        # Return the raw pygame screen
        return self.__screen
