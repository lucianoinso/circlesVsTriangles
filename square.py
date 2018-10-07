import arcade
import win
import math


class Square(arcade.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 50 # Ancho
        self.h = 50 # Alto
        self.a = 0 # Angulo
        self.t = 0 # Tiempo
        self.d = 0 # Direccion
        self.color = arcade.color.RED

        w_half = self.w/2
        h_half = self.h/2
        self.p1 = (self.x - w_half, self.y - h_half)
        self.p2 = (self.x, self.y + h_half)
        self.p3 = (self.x + w_half, self.y - h_half)
            
    def setup(self):
        pass

    def update(self, delta_time, main):
        # Movimiento en mi mismo
        self.a += 10 * math.sin(main.frame_count/4)
        # Movimiento para mantenerlo donde corresponde
        self.x, self.y = arcade.rotate_point(self.x, self.y, 
                                             win.CENTER_W + main.view_left, 
                                             win.CENTER_H + main.view_bottom,
                                             main.change_angle)
        # Movimiento para alcanzar al circulo
        self.t += delta_time
        if (self.t > 0): # seg
            self.t = 0
            # Position the start at the enemy's current location
            start_x = self.x
            start_y = self.y

            # Get the destination location for the bullet
            dest_x = main.circle.x
            dest_y = main.circle.y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            self.d = math.atan2(y_diff, x_diff)

        self.x += math.cos(self.d) * 3
        self.y += math.sin(self.d) * 3

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.color, self.a)
        pass