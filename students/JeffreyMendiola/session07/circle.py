#!/usr/bin/env python
"""
===============================================================================
file: circle.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/01/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #19 Testing, Testing, 1 2 3
Description:
    Create a circle class that passes all the tests.
===============================================================================
"""

import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius
        self._diameter = radius * 2
        self._area = math.pi * (radius ** 2)

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
        self._diameter = value

    @property
    def area(self):
        return self._area

    def __str__(self):
        return("Circle with radius: %.6f" % self.radius)

    def __repr__(self):
        return("Circle(%i)" % self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __cmp__(self, other):
        if self._area > other._area:
            return 1
        elif self._area < other._area:
            return -1
        else:
            return 0
