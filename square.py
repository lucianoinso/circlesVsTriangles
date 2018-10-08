import arcade
import win
import math


class Square(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("sprites/square_001.png")
        self.center_x = x
        self.center_y = y
        self.a = 0 # Angulo
        self.t = 0 # Tiempo
        self.d = 0 # Direccion

    def setup(self):
        pass

    def update(self, delta_time, main):
        # Movimiento en mi mismo
        self.angle += 10 * math.sin(main.frame_count/4)
        # # Movimiento para mantenerlo donde corresponde
        self.center_x, self.center_y = arcade.rotate_point(self.center_x, self.center_y, 
                                             win.CENTER_W + main.view_left, 
                                             win.CENTER_H + main.view_bottom,
                                             main.change_angle)
        # Movimiento para alcanzar al circulo
        self.t += delta_time        
        if (self.t > 1): # seg
            self.t = 0
            # Position the start at the enemy's current location
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for the bullet
            dest_x = main.circle.center_x
            dest_y = main.circle.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            self.d = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(self.d) * 3
        self.change_y = math.sin(self.d) * 3

        super().update()