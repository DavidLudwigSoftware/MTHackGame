import pygame


class MouseController:


    def __init__(self):

        self.__mouseDown = False
        self.__clickCallback = None


    def onClick(self, callback):

        self.__clickCallback = callback


    def update(self):

        if pygame.mouse.get_pressed()[0] and not self.__mouseDown:

            self.__mouseDown = True

            if self.__clickCallback:

                self.__clickCallback(pygame.mouse.get_pos())

                print(pygame.key.get_pressed())


        elif not pygame.mouse.get_pressed()[0]:

            self.__mouseDown = False
