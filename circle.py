import arcade
from helper import *


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 24
        self.h = 24
        self.color = arcade.color.WHITE
        self.shape = arcade.create_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
        self.element = newShapeElement(self.shape)

    
    def setup(self):
        return self.element

    def update(self, delta_time, left, bottom):
        self.x = CENTER_W + left
        self.y = CENTER_H + bottom

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
        pass

    