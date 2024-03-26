import unittest
from mathematical_function.polygons.square import Square


class SquareTest(unittest.TestCase):

    def test_square(self): ###NB deve iniziare con test_
        base = 5
        rectangle = Square(side=base)
        self.assertEqual(round(float(base * base), 2), rectangle.area())
        self.assertEqual(base * 4, rectangle.perimeter())

    '''
    def test_square_not_valid(self):
        with self.assertRaises(Exception) as context:
            SquareValidated(side=-3)
        self.assertTrue("Input should be greater than 0" in str(context.exception))
    '''

