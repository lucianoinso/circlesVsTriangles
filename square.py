import arcade
import win


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.a = 0
        self.color = arcade.color.RED

        w_half = self.w/2
        h_half = self.h/2
        self.p1 = (self.x - w_half, self.y - h_half)
        self.p2 = (self.x, self.y + h_half)
        self.p3 = (self.x + w_half, self.y - h_half)
            
    def setup(self):
        pass

    def update(self, delta_time, angle, left, bottom):
        self.a += 3
        self.x, self.y = arcade.rotate_point(self.x, self.y, win.CENTER_W + left, win.CENTER_H + bottom, angle)

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.color, self.a)
        pass