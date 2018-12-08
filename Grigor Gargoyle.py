import tkinter as tk
from objects.player import Player

if __name__ == '__main__':
    root = tk.Tk()
    root.configure(background="black")
    root.title("Grigor Gargoyle")

    canvas = tk.Canvas(root, width=500, height=500, bg="#EFEFEF")
    canvas.configure(borderwidth=0, highlightthickness=0)
    canvas.focus_set()
    canvas.pack()

    player = Player(canvas)
    canvas.bind("<KeyPress>", player.startMoving)
    canvas.bind("<KeyRelease>", player.stop)

    root.mainloop()
