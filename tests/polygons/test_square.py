import unittest
from mathematical_function.polygons.square import Square


class SquareTest(unittest.TestCase):

    def test_square(self): 
        base = 5
        rectangle = Square(side=base)
        self.assertEqual(round(float(base * base), 2), rectangle.area())
        self.assertEqual(base * 4, rectangle.perimeter())
