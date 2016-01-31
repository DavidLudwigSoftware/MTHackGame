# Import python modules
import pygame
import random

from gui.display import *

# Import the core modules
from core.server import *
from core.client import *

# Import the levels
from gui.levels.connectingmenu import *
from gui.levels.mainmenu       import *
from gui.levels.joinmenu       import *
from gui.levels.arena1         import *


class Application:

    # Store the current application instance
    __instance = None


    # Store the battle arenas
    Arenas = (
        Arena1,
    )


    @staticmethod
    def instance():

        # Return the application instance
        return Application.__instance


    def __init__(self, argv):

        global app

        # Store the current application instance
        Application.__instance = self

        # Initialize the server variable
        self.__server = None

        # Initialize pygame
        pygame.init()

        # Load music
        pygame.mixer.init()
        pygame.mixer.music.load('res/sounds/music/superspacefreak.wav')
        pygame.mixer.music.play(-1)

        # Create the display
        self.__screen = Display(800, 600)

        # Set running to true
        self.__running = True

        # Initialize the level variable
        self.__level = None

        # Set the level to the main menu
        self.setLevel(MainMenu)


    def exec_(self):

        # Create the clock
        clock = pygame.time.Clock()

        # Loop while the app is runnnig
        while self.__running:

            # Loop through the pygame events
            for event in pygame.event.get():

                # Check if the game should quit
                if event.type == pygame.QUIT:

                    # Close the application and return the exit code
                    return self.close()

            # Update the frame
            self.update()

            # Wait until next frame is ready
            clock.tick(60)


    def update(self):

        # Update the level
        self.__level.update()

        # Render the screen
        self.__screen.render()

        if self.__server:

            self.__server.update()


    def screen(self):

        # Return the screen
        return self.__screen


    def level(self):

        # Return the current level
        return self.__level


    def setLevel(self, level, player = None):

        # Check if a level is currently active
        if self.__level:

            # Delete the current level
            del self.__level

        if player:

            self.__level = level(self, player)

        else:

            # Create the new level
            self.__level = level(self)


    def setArena(self, level, player):

        self.setLevel(Application.Arenas[level], player)


    def mainMenu(self):

        self.setLevel(MainMenu)


    def joinMenu(self):

        self.setLevel(JoinMenu)


    def host(self):

        arena = random.randrange(0, len(Application.Arenas))

        # Set the level to a random arena
        self.setLevel(
            Application.Arenas[
                arena
            ]
        )

        if self.__server:

            del self.__server

        self.__server = Server(self.level())


    def join(self, serverIp):

        self.setLevel(ConnectingMenu)

        self.__server = Client(self, serverIp)


    def close(self, exitCode = 0):

        # Set running to false
        self.__running = False

        # Quit pygame
        pygame.quit()

        # Return the exit code
        return exitCode
