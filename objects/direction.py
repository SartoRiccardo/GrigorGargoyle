"""
An object dedicated to reporting where an Entity is going.
"""


class Direction:

    IS_GOING_UP, IS_GOING_RIGHT = 1, 1
    IS_GOING_DOWN, IS_GOING_LEFT = -1, -1
    IS_STILL = 0

    STILL = 1
    UP = 2
    DOWN = 3
    LEFT = 5
    RIGHT = 7
    UP_LEFT = UP * LEFT
    UP_RIGHT = UP * RIGHT
    DOWN_LEFT = DOWN * LEFT
    DOWN_RIGHT = DOWN * RIGHT

    __DIRECTIONS = [STILL, UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]
    __AXIS = [UP, DOWN, LEFT, RIGHT]

    __DIRECTIONS_TO_STRING = {
        STILL: "still",
        UP: "up",
        DOWN: "down",
        LEFT: "left",
        RIGHT: "right",
        UP_LEFT: "up-left",
        UP_RIGHT: "up-right",
        DOWN_LEFT: "down-left",
        DOWN_RIGHT: "down-right"
    }

    def __init__(self):
        self.__instance = self.STILL

    def changeDirection(self, new_direction):
        """
        Override the current direction.
        :param new_direction: The new direction
        """
        if new_direction not in self.__DIRECTIONS:
            self.__instance = self.STILL
        else:
            self.__instance = new_direction

    def turn(self, direction):
        """
        Turn to the given direction. Only UP, DOWN, LEFT and RIGHT are value parameters.
        :param direction: The new direction
        """
        if direction not in self.__AXIS or \
                direction == self.STILL or \
                self.isGoing(direction):
            return

        if direction == Direction.UP and self.isGoing(Direction.DOWN):
            self.__instance /= Direction.DOWN
        elif direction == Direction.DOWN and self.isGoing(Direction.UP):
            self.__instance /= Direction.UP
        elif direction == Direction.LEFT and self.isGoing(Direction.RIGHT):
            self.__instance /= Direction.RIGHT
        elif direction == Direction.RIGHT and self.isGoing(Direction.LEFT):
            self.__instance /= Direction.LEFT
        else:
            self.__instance *= direction

        if self.__instance not in self.__DIRECTIONS:
            self.__instance = Direction.STILL

    def goBack(self, direction):
        """
        Stop going towards the given direction. Only UP, DOWN, LEFT and RIGHT are value parameters.
        :param direction: The old direction
        """
        if direction not in self.__AXIS or direction == self.STILL:
            return

        if self.isGoing(direction):
            self.__instance /= direction

        if self.__instance not in self.__DIRECTIONS:
            self.__instance = Direction.STILL

    # Getters

    def __str__(self):
        return "<objects.direction.Direction object value={} ({})>".format(self.__DIRECTIONS_TO_STRING[self.__instance],
                                                                           self.__instance)

    def verticalDirection(self):
        """
        Returns whether the direction is pointing upwards, downwards or none
        :return: the vertical direction
        """
        if self.isGoing(Direction.UP):
            return self.IS_GOING_UP
        elif self.isGoing(Direction.DOWN):
            return self.IS_GOING_DOWN
        else:
            return self.IS_STILL

    def horizontalDirection(self):
        """
        Returns whether the direction is pointing right, left or none
        :return: the horizontal direction
        """
        if self.isGoing(Direction.RIGHT):
            return self.IS_GOING_RIGHT
        elif self.isGoing(Direction.LEFT):
            return self.IS_GOING_LEFT
        else:
            return self.IS_STILL

    def value(self):
        return self.__instance

    def isGoing(self, direction):
        return self.__instance % direction == 0


if __name__ == '__main__':
    d = Direction()

    d.turn(Direction.DOWN)
    d.turn(Direction.RIGHT)
    print(d)
    d.turn(Direction.LEFT)
    print(d)
    d.turn(Direction.LEFT)
    print(d)
    d.turn(Direction.UP)
    print(d)
