"""
What would a simple test class look like for unit testing for the Circle.py?
"""

import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius
        self.diameter = 3 * radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return math.pi * self.diameter


# Test Class
import unittest


class CircleClassTest(unittest.TestCase):
    assert_radius = 2
    test_object = Circle(assert_radius)

    def test_calculate_area(self):
        expected = math.pi * (self.assert_radius ** 2)
        actual = self.test_object.calculate_area()
        self.assertEquals(expected, actual)

    def test_calculate_perimeter(self):
        expected = math.pi * self.assert_radius * 2
        actual = self.test_object.calculate_perimeter()
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
