"""
A generic entity. Superclass of Obstacle, Player, Projectile and Enemy.
"""
import tkinter as tk
from objects.hitbox import Hitbox
from objects.direction import Direction


class Entity:

    def __init__(self, canvas: tk.Canvas, sprite: str, x=0, y=0):
        self._canvas = canvas

        self._sprite = tk.PhotoImage(file=sprite)
        self._id = canvas.create_image(x, y, image=self._sprite, anchor=tk.NW)

        self._hitbox = Hitbox(x, y, self._sprite.width(), self._sprite.height())

        self._direction = Direction()

        self._x = x
        self._y = y

    def move(self, amount):
        """
        Moves the entity
        :param amount: the amount of pixels you want to move the entity
        :param direction: the direction to move the entity towards
        """
        if amount < 0:
            return

        amount_x, amount_y = 0, 0

        if self._direction.isGoing(Direction.RIGHT):
            amount_x += amount
        elif self._direction.isGoing(Direction.LEFT):
            amount_x -= amount

        if self._direction.isGoing(Direction.UP):
            amount_y -= amount
        elif self._direction.isGoing(Direction.DOWN):
            amount_y += amount

        self._x += amount_x
        self._y += amount_y
        self._canvas.move(self._id, amount_x, amount_y)
        self._canvas.update()
