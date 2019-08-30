import turtle

class Figure:
    pen = turtle.Pen()

    def __init__(self, color, width, angle, size, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pen.color(color)
        self.pen.width(width)
        self.size = size
        self.angle = angle

    def render(self, num_rep):
        iter = range(num_rep)

        for i in iter:
            self.pen.forward(self.size)
            self.pen.left(self.angle)

        turtle.done()

class DynFig(Figure):

    def __init__(self, color, width, angle, size, diff):
        super().__init__(color, width, angle, size)
        self.diff = diff

    def render(self, num_rep):
        iter = range(num_rep)

        for i in iter:
            self.size -= self.diff
            self.pen.forward(self.size)
            self.pen.right(self.angle)

        turtle.done()

class ColorFig(Figure):

    def __init__(self, color, width, angle, size, colors):
        super().__init__(color, width, angle, size)
        self.colors = colors

    def render(self, num_rep):
        iters = range(num_rep)
        n = 0
        for i in iters:
            if i % len(self.colors):
                self.pen.color(self.colors[n])
                self.pen.forward(self.size)
                self.pen.right(self.angle)
                n += 1
            else:
                n = 0

        turtle.done()

class ColDifFig(Figure):

    def __init__(self, color, width, angle, size, colors, diff, speed):
        super().__init__(color, width, angle, size)
        self.pen.speed(speed)
        self.colors = colors
        self.diff = diff

    def render(self, num_rep):
        iters = range(num_rep)
        n = 0
        for i in iters:
            if i % len(self.colors):
                self.size -= self.diff
                self.pen.color(self.colors[n+1])
                self.pen.forward(self.size)
                self.pen.right(self.angle)
                n += 1
            else:
                n = 0

        turtle.done()

