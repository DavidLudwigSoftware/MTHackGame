import pygame
from gui.display import *

# Import the levels
from gui.levels.mainmenu import *


class Application:

    # Store the current application instance
    __instance = None

    # Store the current controller
    __controller = None


    @staticmethod
    def instance():

        # Return the application instance
        return Application.__instance


    def __init__(self, argv):

        global app

        # Store the current application instance
        Application.__instance = self

        # Initialize pygame
        pygame.init()

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


    def screen(self):

        # Return the screen
        return self.__screen


    def level(self):

        # Return the current level
        return self.__level


    def setLevel(self, level):

        # Check if a level is currently active
        if self.__level:

            # Delete the current level
            del self.__level

        # Create the new level
        self.__level = level(self)


    def close(self, exitCode = 0):

        # Set running to false
        self.__running = False

        # Quit pygame
        pygame.quit()

        # Return the exit code
        return exitCode
