import unittest

from circle import Circle
from main import parse_numbers
from rectangle import Rectangle


class GeometryCalculatorTests(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(Circle(3).area(), 28.274333882308138)

    def test_rectangle_area(self):
        self.assertEqual(Rectangle(4, 5).area(), 20)

    def test_parse_numbers_accepts_space_separated_values(self):
        self.assertEqual(parse_numbers("4 5"), [4.0, 5.0])

    def test_parse_numbers_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            parse_numbers("abc")


if __name__ == "__main__":
    unittest.main()
