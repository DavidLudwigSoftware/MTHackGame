import socket


class Server:

    # Constants
    Host   = 0
    Client = 1

    def __init__(self, mode):

        # Create the list of clients
        self.__clients = []
