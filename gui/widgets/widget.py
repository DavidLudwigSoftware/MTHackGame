


class Widget:


    def __init__(self, x, y, width, height):

        # Save the rectangle of the widget
        self.__rect = x, y, width, height


    def isInside(self, x, y):

        # Check if the point is within the x axis of the widget
        if x >= self.__rect[0] and x <= self.__rect[0] + self.__rect[2]:

            # Check if the point is within the y axis of the widget
            if y >= self.__rect[1] and y <= self.__rect[1] + self.__rect[3]:

                # The point is inside of the widget
                return True

        # The point is not inside of the widget
        return False


    def x(self):

        # Return the x coordinate
        return self.__rect[0]


    def y(self):

        # Return the y coordinate
        return self.__rect[1]


    def width(self):

        # Return the width
        return self.__rect[2]


    def height(self):

        # Return the height
        return self.__rect[3]


    def render(self):

        pass
