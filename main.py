import tkinter as tk
from objects.player import Player
from objects.queue import updates

FPS = 30


def mainloop():
    for u in updates.getQueue():
        u()
    canvas.update()


if __name__ == '__main__':
    root = tk.Tk()
    root.configure(background="black")
    root.title("Grigor Gargoyle")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=500, height=500, bg="#EFEFEF", borderwidth=0, highlightthickness=0)
    canvas.focus_set()
    canvas.pack()

    player = Player(canvas)
    canvas.bind("<KeyPress>", player.action)
    canvas.bind("<KeyRelease>", player.stop)

    try:
        while True:
            mainloop()
    except tk.TclError as e:  # Closing the window
        pass
