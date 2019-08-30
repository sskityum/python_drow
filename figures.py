import turtle

class Figure:
    pen = turtle.Pen()
    
    def __init__(self, color='black', width=1, angle=60, size=100):
        self.pen.color(color)
        self.pen.width(width)
        self.angle = angle
        self.size = size

    def render(self, itters, is_right=True):
        itters = range(itters)

        turn = self.pen.right if is_right else self.pen.left

        for i in itters:
            self.pen.forward(self.size)
            turn(self.angle)

        turtle.done()


class DynamicFigure(Figure):
    def __init__(self, color='black', width=1, angle=60, size=100, diff=5):
        super().__init__(color='black', width=1, angle=60, size=100)
        self.diff = diff

    def render(self, itters, is_right=True):
        itters = range(itters)

        turn = self.pen.right if is_right else self.pen.left

        for i in itters:
            self.size -= self.diff

            self.pen.forward(self.size)
            turn(self.angle)

        turtle.done()

    
class ColorfulFigure(Figure):
    def __init__(self, color='black', width=1, angle=60, size=100, colors=None):
        super().__init__(color='black', width=10, angle=60, size=100)
        self.colors = colors if colors else [] 

    def render(self, itters, is_right=True):
        itters = range(itters)
        colors_count = len(self.colors)

        turn = self.pen.right if is_right else self.pen.left

        for i in itters:
            cur_color = self.colors[i % colors_count]

            self.pen.color(cur_color)
            self.pen.forward(self.size)
            turn(self.angle)

        turtle.done()

        
