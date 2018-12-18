"""
A generic entity. Superclass of Obstacle, Player, Projectile and Enemy.
"""
import tkinter as tk
from objects.hitbox import Hitbox
from objects.direction import Direction
import scripts.globalVariables as gVars


class Entity:

    def __init__(self, canvas: tk.Canvas, sprite: str, x=0, y=0, can_exit_frame=True,
                 can_hurt_player=False, is_killable=True, intercepts_projectiles=False):
        self._canvas = canvas

        self._sprite = tk.PhotoImage(file=sprite)
        self._hitbox = Hitbox(x, y, self._sprite.width(), self._sprite.height())
#        self._hitbox.display(self._canvas)

        self._ID = canvas.create_image(x, y, image=self._sprite, anchor=tk.NW)

        self._direction = Direction()

        self._x = x
        self._y = y

        self._alive = True

        self._can_exit_frame = can_exit_frame

        gVars.entities.append(self)
        gVars.updates.append(self.update)
        if can_hurt_player:
            gVars.enemies.append(self)
        self._is_killable = is_killable
        self._intercepts_projectiles = intercepts_projectiles

        self._has_entered_frame = not self.isOffScreen()

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
        if self.update in gVars.updates:
            gVars.updates.remove(self.update)

    def isOffScreen(self):
        return self._x + self._sprite.width() <= 0 or \
                self._x > int(self._canvas["width"]) or \
                self._y > int(self._canvas["height"]) or \
                self._y + self._sprite.height() <= 0

    def collidesWith(self, entity):
        return self._hitbox.collidesWith(entity.getHitbox())

    def __str__(self):
        return f"<{type(self)} object x={self._x} y={self._y}>"

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

    def getDirection(self):
        return self._direction

    def interceptsProjectiles(self):
        return self._intercepts_projectiles

    def isKillable(self):
        return self._is_killable

    def isAlive(self):
        return self._alive

    # Overrideable procedures

    def update(self):
        pass

    def die(self):
        self.stopUpdating()
        self._canvas.delete(self._ID)
        self._alive = False

        if self in gVars.enemies:
            gVars.enemies.remove(self)
        if self in gVars.entities:
            gVars.entities.remove(self)

        self._hitbox.hide()
