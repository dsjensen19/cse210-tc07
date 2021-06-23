from game.point import Point
from actor import Actor
from constants import LIBRARY
import constants
from random import randint
from math import(
    sin,
    cos,
    degrees,
)
class Word(Actor):
    def __init__(self):
        super().__init__()
        self.text = LIBRARY[randint(0,len(LIBRARY))]
        x = randint(0,constants.MAX_X)
        y = randint(0,constants.MAX_Y)
        self.set_position(Point(x,y))

        angle = randint(0,359)
        dx = cos(angle)
        dy = sin(angle)
        self.set_velocity(Point(dx,dy))