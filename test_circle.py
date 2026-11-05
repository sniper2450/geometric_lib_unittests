import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertAlmostEqual(area(3), math.pi * 9)
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(0.0), 0.0)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)
        self.assertAlmostEqual(perimeter(1.5), 2 * math.pi * 1.5)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(0.0), 0.0)

    def test_with_strings(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            perimeter("abc")
        with self.assertRaises(TypeError):
            area("")

    def test_area_with_negative_values(self):
        with self.assertRaises(ValueError):
            area(-3)
        with self.assertRaises(ValueError):
            area(-10)

    def test_perimeter_with_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-3)
        with self.assertRaises(ValueError):
            perimeter(-5)

if __name__ == '__main__':
    unittest.main()
