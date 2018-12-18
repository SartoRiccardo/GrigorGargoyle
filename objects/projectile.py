from objects.entity import Entity
import scripts.globalVariables as gVar


class Projectile(Entity):
    def __init__(self, master, canvas, sprite, x, y):
        Entity.__init__(self, canvas, sprite, x, y, can_exit_frame=True, intercepts_projectiles=True)
        self._direction.turn(self._direction.RIGHT)
        self.__master = master

        self.__intercepted = False

    def wasIntercepted(self):
        return self.__intercepted

    def getMaster(self):
        return self.__master

    def update(self):
        self.move(10)

        if self.isOffScreen():
            self.die()

        for e in gVar.entities:
            if e != self.__master and e != self and self.collidesWith(e):
                if e.interceptsProjectiles():
                    self.__intercepted = True
                if e.isKillable():
                    e.die()
