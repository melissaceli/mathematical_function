from mathematical_function.polygons.polygon import Polygon


class Rectangle(Polygon):

    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return round(float(self.base * self.height), 2)

    def perimeter(self):
        return (self.base + self.height) * 2

