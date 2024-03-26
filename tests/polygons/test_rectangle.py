import unittest
from mathematical_function.polygons.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_rectangle(self):
        base = 5
        height = 6
        rectangle = Rectangle(base=base, height=height)
        self.assertEqual(round(float(base * height), 2), rectangle.area())
        self.assertEqual((base + height) * 2, rectangle.perimeter())

    '''
    def test_rectangle_not_valid(self):
        with self.assertRaises(Exception) as context:
            RectangleValidated(base=-3, height=10)
        self.assertTrue("Input should be greater than 0" in str(context.exception))

        with self.assertRaises(Exception) as context:
            RectangleValidated(base=3, height=-10)
        self.assertTrue("Input should be greater than 0" in str(context.exception))
    '''


