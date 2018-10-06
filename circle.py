import arcade
from helper import *

class Shot:
    def __init__(self, x, y):
        self.origX = x
        self.origY = y
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.color = arcade.color.BABY_BLUE
        self.shape = arcade.create_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
        self.element = newShapeElement(self.shape)
        self.alive = True

    def update(self, delta_time):
        if((self.y > self.origY + CENTER_H) or (self.y < self.origY - CENTER_H) or
           (self.x > self.origX + CENTER_W) or (self.x < self.origX - CENTER_W )):
            self.alive = False
            print("dead")

        else:
            print("still going")
            self.y += 5


    def draw(self):
        if self.alive == True:
            arcade.draw_ellipse_filled(self.x, self.y, self.w, self.h, self.color)


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 24
        self.h = 24
        self.color = arcade.color.WHITE
        self.shape = arcade.create_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
        self.element = newShapeElement(self.shape)
        self.shoots = []

    def shoot(self):
        shot = Shot(self.x, self.y + self.h + 4)
        self.shoots.append(shot)
    
    def setup(self):
        return self.element

    def update(self, delta_time, left, bottom):
        self.x = CENTER_W + left
        self.y = CENTER_H + bottom

        for i in self.shoots:
            if(i.alive):
                i.update(delta_time)

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.w, self.h, self.color)
        for i in self.shoots:
            i.draw()

    