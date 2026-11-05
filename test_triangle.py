import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(3, 4), 6.0)
        self.assertEqual(area(10, 5), 25.0)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0.0)
        self.assertEqual(area(5, 0), 0.0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(10, 10, 10), 30)

    def test_perimeter_with_strings(self):
        with self.assertRaises(TypeError):
            perimeter(3, "4", 5)
        with self.assertRaises(TypeError):
            perimeter("a", "b", "c")

    def test_area_string_by_string(self):
        with self.assertRaises(TypeError):
            area("abc", "def")
        with self.assertRaises(TypeError):
            area("", "")

    def test_area_with_negative_values(self):
        with self.assertRaises(ValueError):
            area(-3, 4)
        with self.assertRaises(ValueError):
            area(-5, -4)

    def test_perimeter_with_negative_values(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(-5, -5, -5)

if __name__ == '__main__':
    unittest.main()
