import socket


class Server:

    def __init__(self, arena):

        self.__arena   = arena
        self.__players = {}

        self.__socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket.bind(('', 42069))


    def onConnected(self, addr, data):

        if len(self.__players) > 1:

            self.__players[addr] = NetworkPlayer()


    def onDisconnected(self, addr):

        pass


    def spawn(self, player, delay):

        pass


    def kill(self, player):

        pass


    def shoot(self, player, position, angle):

        pass


    def parseData(self, data):

        pass


    def update(self):

        while not self.__done:

            try:

                data, addr = socket.recvfrom(1024)

                data = eval(parseData(data))

                if addr not in self.__players:

                    self.onConnected(addr, data)

                else:

                    parseData(data)

            except socket.error:

                break
