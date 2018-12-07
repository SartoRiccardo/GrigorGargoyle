"""
A square hitbox for entities to detect collisions.
"""
import tkinter as tk
from random import randint


class Hitbox:

    X_AXIS = 0
    Y_AXIS = 1

    def __init__(self, x, y, width, height):
        self.__width = abs(width)
        self.__height = abs(height)
        self.__x = x
        self.__y = y

        self.__canvas = None
        self.__visual = None

    def collidesWith(self, hitbox):
        """
        Checks if this instance of a hitbox collides with the one given as a parameter
        Instead of checking whether they collide, the function checks if they DON'T collide and
        returns a negated boolean instead. It's easier this way.
        :param hitbox: Hitbox object
        :return: True if it collides with the given hitbox
        """
        x_doesnt_collide = self.__x + self.__width < hitbox.getX() if self.__x < hitbox.getX() \
                      else hitbox.getX() + hitbox.getWidth() < self.__x
        y_doesnt_collide = self.__y + self.__height < hitbox.getY() if self.__y < hitbox.getY() \
                      else hitbox.getY() + hitbox.getHeight() < self.__y

        return not x_doesnt_collide and not y_doesnt_collide

    def move(self, amount: int, direction=X_AXIS):
        """
        Moves the hitbox
        :param amount: the amount of pixels you want to move the hitbox
        :param direction: the direction you want to move the hitbox
        """
        if direction == self.X_AXIS:
            self.__x += amount
        elif direction == self.Y_AXIS:
            self.__y -= amount

    # Setters

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setWidth(self, width):
        self.__width = width

    def setHeight(self, height):
        self.__height = height

    # Getters

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    # Debug

    def display(self, canvas: tk.Canvas):
        """
        Displays the hitbox as a black square in the given canvas
        :param canvas: A Tkinter Canvas object
        """
        colors = ("black", "white", "red", "purple", "blue", "green", "yellow", "magenta")
        if not self.__canvas:
            self.__canvas = canvas
            self.__visual = canvas.create_polygon(self.__x, self.__y,
                                                  self.__x + self.__width, self.__y,
                                                  self.__x + self.__width, self.__y + self.__height,
                                                  self.__x, self.__y + self.__height,
                                                  fill=colors[randint(0, len(colors)-1)])

    def hide(self):
        """
        Hides the hitbox if display has been called before
        """
        if self.__visual:
            self.__canvas.delete(self.__visual)
            self.__canvas = None
            self.__visual = None


if __name__ == '__main__':
    """Collision test"""
    root = tk.Tk()

    do_they_collide = tk.Label(root)
    do_they_collide.pack()

    canvas = tk.Canvas(root, width=500, height=500, bg="gray")
    canvas.pack()

    X1, X2 = 150, 250
    Y1, Y2 = 150, 50
    WIDTH1, WIDTH2 = 200, 200
    HEIGHT1, HEIGHT2 = 100, 300

    hb1 = Hitbox(X1, Y1, WIDTH1, HEIGHT1)
    hb1.display(canvas)

    hb2 = Hitbox(X2, Y2, WIDTH2, HEIGHT2)
    hb2.display(canvas)

    do_they_collide["text"] = str(hb1.collidesWith(hb2))
    
    root.mainloop()
