class Circle:
    def __init__(self, x, y, radius, resolution=20, draw=True):
        self.x, self.y = x, y
        self.radius = radius
        self.resolution = resolution
        self.coords = self._get_coords()

        if draw:
            self.draw()

    def __repr__(self):
        return f"Circle:\
             \n\tpos: ({self.x}, {self.y});\
             \n\tradius: {self.radius};\
             \n\tresolution: {self.resolution};"

    def _get_coords(self):
        pass

    def draw(self):
        return
