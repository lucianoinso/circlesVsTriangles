"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from circle import Circle
from triangles import Triangle
from helper import *



class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        self.word_angle = 0
        self.word_view = (-1, 1, -1, 1)

        self.circle = Circle(CENTER_W, CENTER_H)
        self.triangles_list = []
        for i in range(0,3):
            triangle = Triangle(i*300+150, i*300+150)
            self.triangles_list.append(triangle)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here

        # shape = self.circle.setup()
        # self.shape_list.append(shape)

        # for t in self.triangles_list:
        #     shape = t.setup()
        #     self.shape_list.append(shape)
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
        self.circle.update(delta_time)
        for t in self.triangles_list:
            t.update(delta_time, self.word_angle)

        

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.word_angle -= 3
        elif key == arcade.key.RIGHT:
            self.word_angle += 3
        elif key == arcade.key.UP:
            pass
        elif key == arcade.key.DOWN:
            pass
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT:
            self.word_angle = 0
        elif key == arcade.key.RIGHT:
            self.word_angle = 0
        elif key == arcade.key.UP:
            self.word_view[0]
            pass
        elif key == arcade.key.DOWN:
            pass
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
