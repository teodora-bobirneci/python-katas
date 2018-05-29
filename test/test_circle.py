import unittest

from math import pi
from katas.circle import area


class CircleTests(unittest.TestCase):

    def test_area_positive_scenarios(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), pi)
        self.assertAlmostEqual(area(3),  pi * 3 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, area, -2)

    def test_types(self):
        self.assertRaises(TypeError, area, 3 + 5j)
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, "some string")
