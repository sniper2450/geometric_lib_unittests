import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(3, 5), 15)
        self.assertEqual(area(10, 2), 20)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 5), 16)
        self.assertEqual(perimeter(10, 2), 24)

    def test_perimeter_with_strings(self):
        with self.assertRaises(TypeError):
            perimeter(10, "5")
        with self.assertRaises(TypeError):
            perimeter("abc", "def")

    def test_area_string_and_string(self):
        with self.assertRaises(TypeError):
            area("abc", "def")
        with self.assertRaises(TypeError):
            area("", "")

    def test_area_string_and_int(self):
        with self.assertRaises(TypeError):
            area("A", 3)
        with self.assertRaises(TypeError):
            area("xyz", 2)

    def test_area_with_negative_values(self):
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_perimeter_with_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(-10, -5)

if __name__ == '__main__':
    unittest.main()
