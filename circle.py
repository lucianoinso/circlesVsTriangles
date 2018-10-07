import arcade
import win
import os
from shot import Shot


class Circle(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("sprites/circle_001.png")
        self.center_x = x
        self.center_y = y

    def update(self, delta_time, main):
        self.center_x = win.CENTER_W + main.view_left
        self.center_y = win.CENTER_H + main.view_bottom
