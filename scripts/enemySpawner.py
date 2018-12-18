import json
import time
from random import randint
from objects.enemy import Enemy
from scripts.globalVariables import updates


class EnemySpawner:

    __ENEMIES = "data/enemies.json"

    def __init__(self, canvas, cooldown, range, enable=True, starting_time=5):
        with open(self.__ENEMIES) as fin:
            self.__enemy_types = json.load(fin)

        self.__canvas = canvas

        self.__starting_time = starting_time
        self.__started = False

        self.__last_enemy = time.time()
        self.__ideal_cooldown = cooldown
        self.__range = range
        self.__real_cooldown = randint(self.__ideal_cooldown - self.__range,
                                       self.__ideal_cooldown + self.__range)

        if enable:
            updates.append(self.update)

    def update(self):
        if not self.__started and \
                time.time() - self.__last_enemy > self.__starting_time:
            self.__last_enemy = time.time()
            self.__started = True
        elif not self.__started:
            return

        if time.time() - self.__last_enemy > self.__real_cooldown:
            enemy_type = self.__enemy_types[randint(0, len(self.__enemy_types)-1)]

            x = randint(enemy_type["x_min"], enemy_type["x_max"])
            y = randint(enemy_type["y_min"], enemy_type["y_max"])
            new_enemy = Enemy(self.__canvas, enemy_type["sprite"], x, y,
                              projectile_cooldown=enemy_type["projectile_cooldown"])
            new_enemy.getDirection().changeDirection(
                            getattr(new_enemy.getDirection(), enemy_type["direction"])
            )

            self.__real_cooldown = randint(self.__ideal_cooldown - self.__range,
                                           self.__ideal_cooldown + self.__range)
            self.__last_enemy = time.time()

    def stop(self):
        updates.remove(self.update)
