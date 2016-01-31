import socket

from gui.levels.arena1 import *

from gui.entities.networkplayer import *

class Client:


    def __init__(self, app, ip):

        self.__app = app
        self.__addr = (ip, 42069)

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.setblocking(False)

        self.__players = {}

        self.__connected = False

        self.__id = -1

        self.__socket.sendto(bytes("{'c':1}".encode()), self.__addr)


    def sendUpdates(self):

        player = self.__app.level().player()

        data = {
            'spr' : player.sprite(),
            'x'   : player.x(),
            'y'   : player.y(),
            'ngl' : 0
        }

        self.send(data)


    def send(self, data):

        self.__socket.sendto(bytes(str(data).encode()), self.__addr)


    def parseData(self, data):

        for player in data:

            if player['p'] != self.__id:

                if player['p'] not in self.__players:

                    self.__players[player['p']] = NetworkPlayer(self.__app.screen(), self.__app.level(), player['p'])
                    self.__app.level().addPlayer(self.__players[player['p']])

                playerObject = self.__players[player['p']]

                playerObject.setSprite(player['spr'])
                playerObject.setX(player['x'])
                playerObject.setY(player['y'])


    def update(self):

        while True:

            if self.__connected:

                self.sendUpdates()

            try:

                data, addr = self.__socket.recvfrom(1024)

                data = eval(data.decode())

                if not self.__connected:

                    self.__id = data['p']
                    self.__app.setArena(data['lvl'], self.__id)

                    self.__connected = True

                else:

                    self.parseData(data)

            except socket.error:

                break
