


class Widget:


    def __init__(self, screen, x, y, width, height):

        # Save the screen
        self.__screen = screen

        # Save the rectangle of the widget
        self.__mRect = x, y, width, height


    def isInside(self, x, y = None):

        if y is None:

            # Extract the x and y from the x variable (x is a list in this case)
            x, y = x

        # Check if the point is within the x axis of the widget
        if x >= self.__mRect[0] and x <= self.__mRect[0] + self.__mRect[2]:

            # Check if the point is within the y axis of the widget
            if y >= self.__mRect[1] and y <= self.__mRect[1] + self.__mRect[3]:

                # The point is inside of the widget
                return True

        # The point is not inside of the widget
        return False


    def screen(self):

        # Return the screen
        return self.__screen


    def x(self):

        # Return the x coordinate
        return self.__mRect[0]


    def y(self):

        # Return the y coordinate
        return self.__mRect[1]


    def width(self):

        # Return the width
        return self.__mRect[2]


    def height(self):

        # Return the height
        return self.__mRect[3]


    def rect(self):

        # Return the rectangle
        return self.__mRect


    def resize(self, rect):

        # Resize the rectangle
        self.__mRect = rect


    def render(self):

        pass
