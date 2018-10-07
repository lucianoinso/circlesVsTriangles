import arcade
import math
import win

class Shot(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("sprites/shot_001.png")
        self.center_x = x
        self.center_y = y
        self.orig_x = x
        self.orig_y = y
        self.d = math.radians(90) # Direccion

    def is_out(self):
        return ((self.center_y > self.orig_y + win.CENTER_H) or
                (self.center_y < self.orig_y - win.CENTER_H) or
                (self.center_x > self.orig_x + win.CENTER_W) or
                (self.center_x < self.orig_x - win.CENTER_W))

    def update(self, delta_time, main):
        # Actualizar la direccion
        self.d += math.radians(main.change_angle)

        # Movimiento para mantenerse en el lugar
        self.center_x, self.center_y = arcade.rotate_point(self.center_x, self.center_y,
                                                            win.CENTER_W + main.view_left,
                                                            win.CENTER_H + main.view_bottom,
                                                            main.change_angle)
        # Avanzar en linea recta
        self.change_x = math.cos(self.d) * 10
        self.change_y = math.sin(self.d) * 10

        super().update()

        """ Special shot
                    if angle != 0:
                        self.angle += angle

                    self.x, self.y = arcade.rotate_point(self.x, self.y, CENTER_W + left, CENTER_H + bottom, self.angle)
                    self.y += 5
        """

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
