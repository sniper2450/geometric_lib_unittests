import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(0.0), 0.0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(0.0), 0.0)

    def test_area_with_string(self):
        with self.assertRaises(TypeError):
            area("abc")
        with self.assertRaises(TypeError):
            area("")

    def test_perimeter_with_string_behavior(self):
        with self.assertRaises(TypeError):
            perimeter("A")
        with self.assertRaises(TypeError):
            perimeter("xyz")

    def test_area_with_negative_values(self):
        with self.assertRaises(ValueError):
            area(-4)
        with self.assertRaises(ValueError):
            area(-10)

    def test_perimeter_with_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-4)
        with self.assertRaises(ValueError):
            perimeter(-10)

if __name__ == '__main__':
    unittest.main()
