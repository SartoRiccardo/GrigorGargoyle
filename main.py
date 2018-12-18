import tkinter as tk
from objects.player import Player
from objects.enemy import Enemy
from scripts.enemySpawner import EnemySpawner
import scripts.globalVariables as gVars


def mainloop():
    #print(gVars.entities)
    for u in gVars.updates:
        u()
    canvas.update()


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(background="black")
    root.title("Grigor Gargoyle")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=1000, height=750, bg="#EFEFEF", borderwidth=0, highlightthickness=0)
    canvas.focus_set()
    canvas.pack()

    player = Player(canvas)
    canvas.bind("<KeyPress>", player.action)
    canvas.bind("<KeyRelease>", player.stop)

#    enemy = Enemy(canvas, "img/enemy.png", 300, 300)

    enemy_spawner = EnemySpawner(canvas, 2, 1)

    try:
        while True:
            mainloop()
    except tk.TclError as e:  # Closing the window
        enemy_spawner.stop()
