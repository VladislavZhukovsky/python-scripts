import math
from collections import namedtuple

Coordinates = namedtuple('Coordinates', 'x y')

class Line():
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        return math.sqrt((c1.y - c2.y) ** 2 + (c1.x - c2.x) ** 2)

    def slope(self):
        x1,y1 = c1.x, c1.y
        x2,y2 = c2.x, c2.y
        return (y2 - y1) / (x2 - x1)

c1 = Coordinates(3,2)
c2 = Coordinates(8,10)
line = Line(c1,c2)
print(line.distance())
print(line.slope())