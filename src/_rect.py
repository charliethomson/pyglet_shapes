from pyglet.graphics import Batch, draw as gl_draw
from pyglet.gl import GL_QUADS
from math import radians as radian, atan, degrees, sin, cos

from pprint import pprint

from src import *


class Rect:
    "Interface class for pyglet Rectangles"

    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        rotation: float = 0.0,
        radians: bool = False,
        color: tuple = GRAY,
        batch: Batch = None,
        draw: bool = True,
    ):
        """
Initialise the Rect class
args:
    x: int; The center x position
    y: int; The center y position
    w: int; The rectangle's width
    h: int; The rectangle's height
kwargs:
    angle:    float;                 0.0;   the angle of the rectangle around it's center in degrees
    radians:  bool;                  False; set true if 
    color:    tuple / int;           GRAY;  if tuple: 
                                                len 3:
                                                    RGB color for the whole rectangle
                                                len 12: 
                                                    RGB colors for each corner (TL, TR, BR, BL)
                                                if int: 
                                                the grayscale value for the whole rectangle 
    batch:    pyglet.graphics.Batch; None;  The batch to add the rectangle to
    draw:     bool;                  True;  whether or not to draw the rectange on initialisation
        """

        self.x, self.y = x, y
        self.w, self.h = w, h
        self.angle = rotation
        self.radians = radians
        self.color = self._get_color(color)
        self.coords = self.get_coords()
        self.batch = batch

        if draw:
            self.draw()

    def __repr__(self):
        return f"Rect:\
            \n\tpos: ({self.x}, {self.y});\
            \n\tw, h: {self.w}, {self.h};\
            \n\tangle: {self.angle};\
            \n\tradians: {self.radians};\
            \n\tcolor:\
            \n\t\n\t{self.color};\
            \n\tcoords:\
            \n\t\n\t{self.coords};"

    def _get_color(self, color):
        "format the color of the rectangle"
        # raise an error if the color is not a tuple
        assert isinstance(color, (tuple, int)), "rect color must be type tuple or int"

        # For the rectangle, we need 12 values, i.e. a tuple len 12
        # (3 RGB values per corner, 4 corners, 12 values)
        if len(color) == 1:
            return (color,) * 12
        if len(color) == 3:
            return color * 4
        if len(color) == 12:
            return color

        raise ValueError("Data for color incorrect length")

    def get_coords(self):
        "get the coordinates of the rectangle's vertices"
        if not self.radians:
            self.angle = radian(self.angle)

        diag = ((self.w ** 2) + (self.h ** 2)) ** 0.5

        x_diff1 = (diag / 2) * sin(self.angle + radian(45))
        y_diff1 = (diag / 2) * cos(self.angle + radian(45))

        # x_diff2 =
        # y_diff2 =

        return [
            # top left
            self.x - x_diff1,
            self.y + y_diff1,
            # top right
            self.x + x_diff1,
            self.y + y_diff1,
            # bottom right
            self.x + x_diff1,
            self.y - y_diff1,
            # bottom left
            self.x - x_diff1,
            self.y - y_diff1,
        ]

    def draw(self):
        "draw the rectangle"

        for coord in self.coords:
            if isinstance(coord, int):
                coord = float(coord)
            elif not isinstance(coord, float):
                raise TypeError(f"coordinate '{coord}' type incorrect ({type(coord)})")

        # if there's no batch, draw the shape, if there is a batch, add the shape to the batch
        if not self.batch:
            gl_draw(4, GL_QUADS, ("v2f", self.coords), ("c3B", self.color))
            # pprint(rectargs)
        else:
            self.batch.add(4, GL_QUADS, None, ("v2f", self.coords), ("c3B", self.color))

