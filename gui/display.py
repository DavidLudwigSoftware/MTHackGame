import pygame


class Display:

    def __init__(self, width, height):

        self.__width  = width
        self.__height = height

        self.__screen = pygame.display.set_mode((width, height))


    def update(self):

        pygame.display.flip()
