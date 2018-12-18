from objects.entity import Entity
from objects.projectile import Projectile
import time


class Enemy(Entity):
    def __init__(self, canvas, sprite, x, y, projectile_cooldown=1.5):
        super().__init__(canvas, sprite, x, y, can_exit_frame=True, can_hurt_player=True,
                         intercepts_projectiles=True, is_killable=True)

        self.__speed = 1

        self.__bullets = []

        self.__projectile_cooldown = projectile_cooldown
        self.__shoot_time = time.time()

    def update(self):
        if len(self.__bullets) < 1 and \
                time.time() - self.__shoot_time > self.__projectile_cooldown:
            self.__shoot_time = time.time()
            self.__bullets.append(Projectile(self, self._canvas, "img/projectile.png", self._x, self._y))

        for b in self.__bullets:
            if b.isOffScreen() or b.wasIntercepted() or not b.isAlive():
                self.__bullets.remove(b)
                b.die()

        self.move(self.__speed)

        if not self.isOffScreen() and not self._has_entered_frame:
            self._has_entered_frame = True

        if self.isOffScreen() and self._has_entered_frame:
            self.die()
