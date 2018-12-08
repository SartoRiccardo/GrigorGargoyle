from objects.entity import Entity
from objects.entity import Direction
import tkinter as tk


class Player(Entity):

    __keys = {
        "\uf700": Direction.UP,
        "\uf701": Direction.DOWN,
        "\uf702": Direction.LEFT,
        "\uf703": Direction.RIGHT
    }

    def __init__(self, canvas: tk.Canvas):
        super().__init__(canvas, "img/grigor.png", 250, 250, can_exit_frame=False)
        self.__speed = 2

    def startMoving(self, event):
        if event.char in self.__keys:
            self._direction.turn(self.__keys[event.char])
            while self._direction.value() != Direction.STILL:
                self.move(self.__speed)

    def stop(self, event):
        if event.char in self.__keys:
            self._direction.goBack(self.__keys[event.char])

    def shoot(self):
        pass
