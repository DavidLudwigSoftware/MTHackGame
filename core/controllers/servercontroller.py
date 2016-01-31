


class ServerController:


    def __init__(self, player):

        self.__player = player


    def setData(self, data):

        self.__player.setX(data['px'])
        self.__player.setY(data['px'])
        self.__player.setAngle('ngl')
        self.__player.setSprite(data['spr'])
