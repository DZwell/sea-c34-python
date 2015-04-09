#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius
        self._diameter = radius * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        self._diameter = value
