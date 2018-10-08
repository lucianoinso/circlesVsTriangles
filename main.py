import arcade
import random
import os

from circle import Circle, Shot
from square import Square
import win

class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        # Donde deberian estar los sprites y audios
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

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
        self.shot_list = arcade.SpriteList()
        self.square_list = arcade.SpriteList()
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
        self.square_list.draw()
        self.shot_list.draw()

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
        # Probabilidad 1 en algo
        if random.randrange(10) == 0 and len(self.square_list) < 5:
            rx = random.randrange(self.view_left, self.view_left+win.WIDTH)
            ry = random.randrange(self.view_bottom, self.view_bottom+win.HEIGHT)
            square = Square(rx, ry)
            self.square_list.append(square)
        
        # Morir
        squares = arcade.geometry.check_for_collision_with_list(self.circle, self.square_list)
        if len(squares) > 0:
            arcade.pause(2)
            arcade.close_window()

        for s in self.shot_list:
            squares = arcade.geometry.check_for_collision_with_list(s, self.square_list)
            # Solo el primero
            if len(squares) > 0:
                squares[0].kill()
                s.kill()

        # Quitar balas que estan fuera de la pantalla
        for s in self.shot_list:
            if s.is_out():
                s.kill()

        # Actualizar shapes
        self.circle.update(delta_time, self)
        for s in self.square_list:
            s.update(delta_time, self)
        for s in self.shot_list:
            s.update(delta_time, self)

        arcade.set_viewport(self.view_left,
                            self.view_left + win.WIDTH,
                            self.view_bottom,
                            self.view_bottom + win.HEIGHT)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_left = -8
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_left = 8
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_bottom = 8
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_bottom = -8
        elif key == arcade.key.SPACE:
            shot = Shot(self.circle.center_x, self.circle.center_y)
            self.shot_list.append(shot)
        elif key == arcade.key.Q or key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_left = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_left = 0
        elif key == arcade.key.UP or key == arcade.key.W:
            self.change_bottom = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.change_bottom = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.change_angle = delta_x

    def on_mouse_press(self, x, y, button, key_modifiers):
        if button == 1:
            shot = Shot(self.circle.center_x, self.circle.center_y)
            self.shot_list.append(shot)

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    """ Main method """
    game = MyGame(win.WIDTH, win.HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
