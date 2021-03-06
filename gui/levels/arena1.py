
# Import python modules
import pygame


# Import the base level
from gui.levels.level import *


# Import the entities
from gui.entities.physicsplayer import *
from gui.entities.platform      import *


class Arena1(Level):

    Id = 0

    def __init__(self, app, playerId = 0):

        super(Arena1, self).__init__(app)

        self.__gravity = 0.5

        self.__friction = 0.2

        self.__floor = 65

        self.__platforms = [
            Platform(self.screen(), self, Platform.Invisible, -1-8, 0, 1, self.screen().height()),
            Platform(self.screen(), self, Platform.Invisible, self.screen().width()+1+8, 0, 1, self.screen().height()),
            Platform(self.screen(), self, Platform.Invisible, 0, -1, self.screen().width(), 1)
        ]

        self.__background = pygame.image.load('res/textures/spacebkg.png')

        self.__players = [
            PhysicsPlayer(app.screen(), self, playerId),
        ]


    def addPlayer(self, player):

        self.__players.append(player)


    def gravity(self):

        return self.__gravity


    def friction(self):

        return self.__friction


    def floor(self):

        return self.__floor


    def platforms(self):

        return self.__platforms


    def player(self, player = 0):

        return self.__players[player]


    def update(self):

        super(Arena1, self).update()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:

            return self.app().mainMenu()

        self.screen().surface().blit(self.__background, (0, 0))

        for platform in self.__platforms:

            platform.render()


        for player in self.__players:

            player.update()
