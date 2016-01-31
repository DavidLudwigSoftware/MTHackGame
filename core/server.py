import socket


class Server:

    MaxPlayers

    def __init__(self, arena):

        self.__arena   = arena
        self.__players = {}

        self.__socket = socket(AF_INET, SOCK_DGRAM)
        self.__socket.bind(('', 42069))


    def onConnected(self, addr, data):

        player = NetworkPlayer(
            self.__arena,
            self.__arena.world(),
            len(self.__players[])
        )

        player.setController(ServerController())

        self.__players[addr] = player

        self.send(addr, {"c":1,"lvl":0,"p":len(self.__players)}


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


    def sendUpdates(self):

        data = {}

        for key in self.__players:

            controller = self.__players[key]
            score =

        for addr in self.__players:

            self.send(addr, )


    def update(self):

        while not self.__done:

            try:

                data, addr = socket.recvfrom(1024)

                data = eval(parseData(data))

                if addr not in self.__players and len(self.__players) < Server.MaxPlayers:

                    self.onConnected(addr, data)

                else:

                    parseData(data)

            except socket.error:

                break

            self.sendUpdates()
