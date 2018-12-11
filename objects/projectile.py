from objects.entity import Entity


class Projectile(Entity):
    def __init__(self, canvas, sprite, x, y, is_player_bullet=False):
        Entity.__init__(self, canvas, sprite, x, y, can_exit_frame=True)
        self._direction.turn(self._direction.RIGHT)
        self.__player = is_player_bullet

    def update(self):
        self.move(10)
        if self.isOffScreen():
            self.stopUpdating()
