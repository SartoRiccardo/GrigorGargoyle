from objects.entity import Entity
from objects.entity import Direction
from objects.projectile import Projectile
import tkinter as tk
import time


class Player(Entity):

    __keys = {
        "\uf700": Direction.UP,
        "\uf701": Direction.DOWN,
        "\uf702": Direction.LEFT,
        "\uf703": Direction.RIGHT
    }

    PLAYER_SPRITE = "img/grigor.png"
    BULLET_SPRITE = "img/projectile.png"

    STARTING_X = 250
    STARTING_Y = 250

    SHOOT_COOLDOWN = 0.15

    def __init__(self, canvas: tk.Canvas):
        super().__init__(canvas, self.PLAYER_SPRITE, self.STARTING_X, self.STARTING_Y, can_exit_frame=False)
        self.__speed = 2

        self.__last_bullet = time.time()
        self.__bullets = []

    def action(self, event):
        if event.char in self.__keys:
            self._direction.turn(self.__keys[event.char])
        elif event.char == "z":
            self.shoot()

    def update(self):
        self.move(self.__speed)
        for b in self.__bullets:
            if b.isOffScreen() or b.wasIntercepted() or not b.isAlive():
                self.__bullets.remove(b)
                b.die()

    def stop(self, event):
        if event.char in self.__keys:
            self._direction.goBack(self.__keys[event.char])

    def shoot(self):
        if len(self.__bullets) < 3 and \
                time.time() - self.__last_bullet > self.SHOOT_COOLDOWN:
            self.__last_bullet = time.time()
            self.__bullets.append(Projectile(self, self._canvas, self.BULLET_SPRITE,
                                             self._x, self._y))
