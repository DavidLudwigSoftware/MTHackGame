import socket

from gui.entities.networkplayer import *
from core.controllers.servercontroller import *

class Server:

    MaxPlayers = 4

    def __init__(self, arena):

        self.__arena   = arena
        self.__players = {'127.0.0.1': arena.player()}

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(('', 42069))
        self.__socket.setblocking(False)

        self.__done = False


    def onConnected(self, addr, data):

        player = NetworkPlayer(
            self.__arena.screen(),
            self.__arena,
            len(self.__players)
        )

        self.__arena.addPlayer(player)

        player.setController(ServerController(player))

        self.__players[addr] = player

        self.send(addr, {"c":1,"lvl":self.__arena.Id,"p":len(self.__players) - 1})


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

        for player in self.__players.values():

            data[player] = {
                'p'   : player.id(),
                'spr' : player.sprite(),
                'x'   : player.x(),
                'y'   : player.y(),
                'ngl' : 0,
            }

        for addr in self.__players:

            self.send(addr, data)


    def send(self, addr, data):

        pass


    def update(self):

        while not self.__done:

            try:

                data, addr = self.__socket.recvfrom(1024)

                data = eval(data.decode())

                if addr not in self.__players and len(self.__players) < Server.MaxPlayers:

                    self.onConnected(addr, data)

                else:

                    self.parseData(data)

            except socket.error:

                break

            self.sendUpdates()


    def __del__(self):

        self.__socket.close()
