
# Import the python modules
import pygame


# Import the base entity
from gui.entities.player import *


# Import the player controller
from core.controllers.playercontroller import *


class PhysicsPlayer(Player):


    def __init__(self, screen, player = 0):

        super(PhysicsPlayer, self).__init__(screen, player)

        self.__controller = PlayerController()


    def update(self):

        
        # Render the player (Leave this on the end)
        self.render()
