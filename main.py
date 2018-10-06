import arcade
from circle import Circle, Shot
from triangles import Triangle
import win

class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, fullscreen=True)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(False)
        self.set_exclusive_mouse(True)
        
        win.WIDTH, win.HEIGHT = self.get_size()
        win.CENTER_W = win.WIDTH/2
        win.CENTER_H = win.HEIGHT/2
        arcade.set_viewport(0, win.WIDTH, 0, win.HEIGHT)

        self.change_angle = 0
        self.change_bottom = 0
        self.change_left = 0
        self.view_bottom = 0
        self.view_left = 0
        
        self.circle = Circle(win.CENTER_W, win.CENTER_H)
        self.triangles_list = []
        for i in range(0,3):
            triangle = Triangle(i*300+150, i*300+150)
            self.triangles_list.append(triangle)

    def setup(self):
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.circle.draw()
        for shape in self.triangles_list:
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
        if self.change_angle != 0:
            self.change_angle = self.change_angle/2

        self.circle.update(delta_time, self.view_left, self.view_bottom)
        for t in self.triangles_list:
            t.update(delta_time, self.change_angle, self.view_left, self.view_bottom)
        
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
