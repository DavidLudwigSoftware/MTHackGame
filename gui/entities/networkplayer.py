
import pygame

from core.controllers.servercontroller import *

from gui.entities.player import *

class NetworkPlayer(Player):


    def __init__(self, screen, world, player = 1):

        self.__controller = ServerController(self)

        self.__angle = 0


    def angle(self):

        return self.__angle


    def setAngle(self, angle):

        self.__angle = angle
