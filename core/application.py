import pygame
from gui.display import *


class Application:


    def __init__(self, argv):

        pygame.init()

        self.__display = Display(800, 600)

        self.__running = True


    def exec_(self):

        clock = pygame.time.Clock()

        while self.__running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    return self.close()

            self.__display.update()

            clock.tick(60)


    def close(self):

        return 0
