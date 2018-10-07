import arcade
import math
import win

class Shot(arcade.Sprite):
    def __init__(self, x, y):
        self.origX = x
        self.origY = y
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.alive = True
        self.d = math.radians(90) # Direccion
        self.color = arcade.color.BABY_BLUE

    def is_alive(self):
        return self.alive or not((self.y > self.origY + win.CENTER_H) or
                                (self.y < self.origY - win.CENTER_H) or
                                (self.x > self.origX + win.CENTER_W) or
                                (self.x < self.origX - win.CENTER_W))

    def update(self, delta_time, main):
        # Actualizar la direccion
        self.d += math.radians(main.change_angle)

        # Movimiento para mantenerse en el lugar
        self.x, self.y = arcade.rotate_point(self.x, self.y,
                                                win.CENTER_W + main.view_left,
                                                win.CENTER_H + main.view_bottom,
                                                main.change_angle)
        # Avanzar en linea recta
        self.x += math.cos(self.d) * 5
        self.y += math.sin(self.d) * 5

        """ Special shot
                    if angle != 0:
                        self.angle += angle

                    self.x, self.y = arcade.rotate_point(self.x, self.y, CENTER_W + left, CENTER_H + bottom, self.angle)
                    self.y += 5
        """

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
