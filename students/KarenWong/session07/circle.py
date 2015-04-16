#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = math.pi * (self.radius ** 2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = math.pi * radius ** 2

    @ property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        self._diameter = value
        self._area = math.pi * (value / 2) ** 2

    @property
    def area(self):
        return self._area

    def __str__(self):
        return 'Circle with radius: %.6f' % self.radius

    def __repr__(self):
        return("Circle({r})".format(r=str(self.radius)))

    def __add__(self, new):
        return Circle(self.radius + new.radius)

    def __mul__(self, new):
        return Circle(self.radius * new)

    def __cmp__(self, other):
        return self.radius - other.radius

    def __ne__(self, other):
        return self.radius != other.radius
