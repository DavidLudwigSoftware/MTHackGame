


class Entity:

    def __init__(self, screen, world, rect):

        self.__screen = screen
        self.__world = world

        self.__rect = rect


    def update(self):

        pass


    def render(self):

        pass


    def screen(self):

        return self.__screen


    def world(self):

        return self.__world


    def x(self):

        return self.__rect[0]


    def y(self):

        return self.__rect[1]


    def centerX(self):

        return self.__rect[0] + self.__rect[2] / 2


    def centerY(self):

        return self.__rect[1] + self.__rect[3] / 2


    def setX(self, x):

        self.__rect[0] = int(x)


    def setY(self, y):

        self.__rect[1] = int(y)


    def width(self):

        return self.__rect[2]


    def height(self):

        return self.__rect[3]


    def bottom(self):

        return self.height() + self.y()


    def right(self):

        return self.width() + self.x()


    def rect(self):

        return self.__rect
