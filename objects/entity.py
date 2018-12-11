"""
A generic entity. Superclass of Obstacle, Player, Projectile and Enemy.
"""
import tkinter as tk
from objects.hitbox import Hitbox
from objects.direction import Direction
from objects.queue import updates


class Entity:

    def __init__(self, canvas: tk.Canvas, sprite: str, x=0, y=0, can_exit_frame=True):
        self._canvas = canvas

        self._sprite = tk.PhotoImage(file=sprite)
        self._hitbox = Hitbox(x, y, self._sprite.width(), self._sprite.height())

#        self._hitbox.display(self._canvas)
        self._ID = canvas.create_image(x, y, image=self._sprite, anchor=tk.NW)

        self._direction = Direction()

        self._x = x
        self._y = y

        self._can_exit_frame = can_exit_frame

        updates.add(self.update)

    def move(self, amount):
        """
        Moves the entity
        :param amount: the amount of pixels you want to move the entity
        :param direction: the direction to move the entity towards
        """
        if amount < 0 or self._direction.isStill():
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
        if (0 > self._x or self._x + self._sprite.width() > int(self._canvas["width"])) and \
                not self._can_exit_frame:
            self._x -= amount_x
            amount_x = 0
        self._y += amount_y
        if (0 > self._y or self._y + self._sprite.height() > int(self._canvas["height"])) and \
                not self._can_exit_frame:
            self._y -= amount_y
            amount_y = 0

        self._canvas.move(self._ID, amount_x, amount_y)
        self._hitbox.move(amount_x, amount_y)

    def stopUpdating(self):
        if self.update in updates.getQueue():
            updates.remove(self.update)

    def isOffScreen(self):
        return self._x + self._sprite.width() <= 0 or \
                self._x > int(self._canvas["width"]) or \
                self._y > int(self._canvas["height"]) or \
                self._y + self._sprite.height() <= 0

    # Getters

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getSprite(self):
        return self._sprite

    def getHitbox(self):
        return self._hitbox

    def getID(self):
        return self._ID

    # Overrideable procedures

    def update(self):
        pass
