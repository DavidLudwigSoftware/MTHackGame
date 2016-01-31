for platform in self.world().platforms():


    # Check if over or below a platform
    if self.right() > platform.x() and self.x() < platform.right():

        if self.bottom() <= platform.y() and newy > platform.y():

            newy = platform.y() - self.height()
            self.__dy = 0.0

        elif self.top() >= platform.bottom() and newy < platform.bottom():

            newy = platform.bottom()
            self.__dy = 0.0
