import unittest
from mathematical_function.polygons.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_rectangle(self):
        base = 5
        height = 6
        rectangle = Rectangle(base=base, height=height)
        self.assertEqual(round(float(base * height), 2), rectangle.area())
        self.assertEqual((base + height) * 2, rectangle.perimeter())
