from pyglet.window import Window
from pyglet.app import run as run_app
from pyglet.graphics import Batch
from pyglet.clock import schedule
from src import *
from random import randint
from time import time

window = Window(1000, 1000)
click_count = 0
BATCH = Batch()

i, j = 0, 0
I, J = 0, 0
w, h, = 100, 100

color = GRAYS[list(GRAYS.keys())[int(i ** j + 1) % len(GRAYS.keys())]]


@window.event
def on_draw():
    if not color:
        pass
    Rect(i, j, w, h, color=color, draw=True, batch=BATCH, id_=None)
    BATCH.draw()


def on_call(delta):
    global i, j, I, J, w, h, color
    if i < window.width - I:
        i += w
    else:
        if j < window.height:
            j += h
        else:
            I += w
            J += h
            i = 0
            j = J

    color = GRAYS[list(GRAYS.keys())[int(i ** j + 1) % len(GRAYS.keys())]]


# @window.event
# def on_mouse_press(x, y, button, mod):
#     W, H = randint(0, window.width // 8), randint(0, window.height // 8)
#     W, H = 10, 10
#     start = time()
#     print("Started;")
#     for i in range(0, window.width + W, (W // 2) + 1):
#         print(f"Outer increment {i - 1} -> {i};")
#         per_start = time()
#         for j in range(0, window.height + H, (H // 2) + 1):
#             # print(i, j)
#             color = GRAYS[list(GRAYS.keys())[int(i ** j + 1) % len(GRAYS.keys())]]
#             Rect(i, j, W, H, color=color, radians=False, draw=True, batch=BATCH)
#         per_stop = time()
#         print(f"Inner time taken: {per_stop - per_start};")

#     stop = time()
#     print("Done")
#     print(f"Time taken: {stop - start};")

schedule(on_call)
if __name__ == "__main__":
    run_app()
