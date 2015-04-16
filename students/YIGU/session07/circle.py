
# !/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)
        self._diameter = radius * 2
        self._area = radius**2 * math.pi

    @property
    def diameter(self):
        return self._diameter
    @property
    def area(self):
        return self._area

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        self._diameter = value

    def __str__(self):
        return 'Circle with radius: %.6f' % float(self.radius)

    def __repr__(self):
        return 'Circle(%.0f)' % self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius*other)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius
