


class Entity:

    def __init__(self, screen, rect):

        self.__screen = screen

        self.__rect = rect


    def update(self):

        pass


    def render(self):

        pass


    def screen(self):

        return self.__screen


    def x(self):

        return self.__rect[0]


    def y(self):

        return self.__rect[1]


    def setX(self, x):

        self.__rect[0] = x


    def setY(self, y):

        self.__rect[1] = y


    def width(self):

        return self.__rect[2]


    def height(self):

        return self.__rect[3]


    def rect(self):

        return self.__rect
