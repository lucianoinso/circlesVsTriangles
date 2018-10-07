import arcade
import random
from circle import Circle, Shot
from square import Square
import win

class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(False)
        self.set_exclusive_mouse(True)

        self.change_angle = 0
        self.change_bottom = 0
        self.change_left = 0
        self.view_bottom = 0
        self.view_left = 0
        self.frame_count = 0
        
        self.circle = Circle(win.CENTER_W, win.CENTER_H)
        self.square_list = []
        for i in range(0,3):
            square = Square(i*300+150, i*300+150)
            self.square_list.append(square)

    def setup(self):
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.circle.draw()
        for shape in self.square_list:
            shape.draw()

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.view_bottom += self.change_bottom
        self.view_left += self.change_left
        self.frame_count += 1

        # Disminuir el giro de la camara exponencialmente
        if self.change_angle != 0:
            self.change_angle = self.change_angle/2

        # Crear nuevos shapes
        # Probabilidad 1 en 100
        if random.randrange(100) == 0:
            rx = random.randrange(self.view_left, self.view_left+win.WIDTH)
            ry = random.randrange(self.view_bottom, self.view_bottom+win.HEIGHT)
            square = Square(rx, ry)
            self.square_list.append(square)

        # Actualizar shapes
        for s in self.square_list + [self.circle]:
            s.update(delta_time, self)
        
        arcade.set_viewport(self.view_left,
                            self.view_left + win.WIDTH,
                            self.view_bottom,
                            self.view_bottom + win.HEIGHT)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.change_left = -8
        elif key == arcade.key.RIGHT:
            self.change_left = 8
        elif key == arcade.key.UP:
            self.change_bottom = 8
        elif key == arcade.key.DOWN:
            self.change_bottom = -8
        elif key == arcade.key.SPACE:
            self.circle.shoot()

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.change_left = 0
        elif key == arcade.key.RIGHT:
            self.change_left = 0
        elif key == arcade.key.UP:
            self.change_bottom = 0
        elif key == arcade.key.DOWN:
            self.change_bottom = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.change_angle = delta_x

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    """ Main method """
    game = MyGame(win.WIDTH, win.HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
