import unittest
from mathematical_function.main import main
from unittest.mock import patch


class MainTest(unittest.TestCase):

    def test_main(self):
        with patch('builtins.input', side_effect=['1', '4', '5']):
            area, perimeter = main()
            expected_area, expected_perimeter = 20, 18
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)

        with patch('builtins.input', side_effect=['2', '3']):
            area, perimeter = main()
            expected_area, expected_perimeter = 9, 12
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)

        with patch('builtins.input', side_effect=['5']):
            self.assertEqual(-1, main())

        with patch('builtins.input', side_effect=['2', '-3', '4']):
            area, perimeter = main()
            expected_area, expected_perimeter = 16, 16
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)

        with patch('builtins.input', side_effect=['1', '4', '-5', '3', '2']):
            area, perimeter = main()
            expected_area, expected_perimeter = 6, 10
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)

        with patch('builtins.input', side_effect=['square', '-3', '4']):
            area, perimeter = main()
            expected_area, expected_perimeter = 16, 16
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)


        with patch('builtins.input', side_effect=['square', 'xxxx', '4']):
            area, perimeter = main()
            expected_area, expected_perimeter = 16, 16
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)

        with patch('builtins.input', side_effect=['rectangle', '4', '-5', '3', '2']):
            area, perimeter = main()
            expected_area, expected_perimeter = 6, 10
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)

        with patch('builtins.input', side_effect=['rectangle', '-4', '5', '3', '2']):
            area, perimeter = main()
            expected_area, expected_perimeter = 6, 10
            self.assertEqual(expected_area, area)
            self.assertEqual(expected_perimeter, perimeter)
