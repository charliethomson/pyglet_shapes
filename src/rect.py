from pyglet.gl import GL_QUADS
from pyglet.graphics import draw as gl_draw, Batch

from typing import Tuple

# COLOR CONSTANTS

RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PINK = (255, 0, 200)
GREEN = (0, 255, 0)
BROWN = (80, 50, 0)
ORANGE = (255, 90, 0)
PURPLE = (140, 0, 255)
YELLOW = (255, 255, 0)
SEA_GREEN = (0, 255, 192)

BLACK = (0, 0, 0)
DARK_GRAY = (64, 64, 64)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
WHITE = (255, 255, 255)

COLORS = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "CYAN": (0, 255, 255),
    "PINK": (255, 0, 200),
    "GRAY": (128, 128, 128),
    "BLACK": (0, 0, 0),
    "GREEN": (0, 255, 0),
    "BROWN": (80, 50, 0),
    "WHITE": (255, 255, 255),
    "ORANGE": (255, 90, 0),
    "PURPLE": (140, 0, 255),
    "YELLOW": (255, 255, 0),
    "DARK_GRAY": (64, 64, 64),
    "SEA_GREEN": (0, 255, 192),
    "LIGHT_GRAY": (192, 192, 192),
}
# end

# MODE CONSTANTS

CENTER = "center"
CORNER = "corner"
CORNERS = "corners"

# end

# TYPES

Color = Tuple[int, int, int]

# end


class Rect:
    """
    user/pyglet interface class for drawing a rectangle
    """

    def __init__(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        id_: str,
        mode: str = "center",
        color: Color = DARK_GRAY,
        draw: bool = True,
        batch: Batch = None,
    ):
        """
        args:
            x: int; the x anchor position of the rectangle-
            y: int; the y anchor position of the rectangle
            w: int; the width of the rectangle
            h: int; the height of the rectangle
            id_: str; the logical id for the rectangle (ex. `background`)
        kwargs:
            mode: str; default "center"; the draw mode of the rectangle, "center", "corner", "corners"
            color: Color - 3 int Tuple; default DARK_GRAY - (64, 64, 64)
            draw: bool; default True; tells the rectangle to draw or not
        """

        self.x, self.y = x, y
        self.w, self.h = w, h
        self.color = color

        self.id_ = id_

        mode = mode.lower()

        if mode == CENTER:
            self.coords = [
                self.x - self.w // 2,
                self.y + self.h // 2,
                self.x + self.w // 2,
                self.y + self.h // 2,
                self.x + self.w // 2,
                self.y - self.h // 2,
                self.x - self.w // 2,
                self.y - self.h // 2,
            ]
        elif mode == CORNER:
            self.coords = [
                self.x,
                self.y,
                self.x,
                self.y + self.h,
                self.x + self.w,
                self.y + self.h,
                self.x + self.w,
                self.y,
            ]
        elif mode == CORNERS:
            self.coords = [
                self.x,
                self.y,  # x1, y1
                self.x,
                self.h,  # x1, y2,
                self.w,
                self.h,  # x2, y2,
                self.w,
                self.y,  # x2, y1
            ]

        if draw:
            self.draw()
        if batch:
            batch.add(4, GL_QUADS, None, ("v2i", self.coords), ("c3B", self.color * 4))

    def update_pos(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        gl_draw(4, GL_QUADS, ("v2i", self.coords), ("c3B", self.color * 4))
