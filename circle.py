import arcade
import win
from shot import Shot


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 24
        self.h = 24
        self.color = arcade.color.WHITE
    
    def setup(self):
        pass

    def update(self, delta_time, main):
        self.x = win.CENTER_W + main.view_left
        self.y = win.CENTER_H + main.view_bottom

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
