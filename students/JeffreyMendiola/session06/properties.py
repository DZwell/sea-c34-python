"""
===============================================================================
file: properties.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/08/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #18 Investigate Session 7
===============================================================================
"""


class Foo(object):
    """
    Can you increment the setter property using a loop?
    Output:
        12
        22
    Answer: Yes
    """
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

sample = Foo(12)
print sample.x

for i in range(10):
    sample.x += 1

print sample.x
