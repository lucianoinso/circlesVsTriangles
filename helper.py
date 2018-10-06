import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

CENTER_W = SCREEN_WIDTH/2
CENTER_H = SCREEN_HEIGHT/2

def newShapeElement(shape):
    element = arcade.ShapeElementList()
    element.center_x = CENTER_W
    element.center_y = CENTER_H
    element.append(shape)
    return element