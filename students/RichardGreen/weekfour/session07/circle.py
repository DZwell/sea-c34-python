#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @diameter.setter
    def diameter(self, diameter):
        self._radius = diameter / 2

    def __add__(self, c):
        return Circle(self.radius + c.radius)

    def __repr__(self):
        return 'Circle(%g)' % self._radius

    def __cmp__(self, c):
        return cmp(self.radius, c.radius)

    def __str__(self):
        return 'Circle with radius: %.6f' % self.radius

    def __mul__(self, num):
        return Circle(num * self.radius)
