"""
===============================================================================
file: special.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/08/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #18 Investigate Session 7
===============================================================================
"""


class Square(object):
    """How do you use special methods"""
    def __init__(self, side):
        self.side = side

    def __per__(self):
        return self.side * 4

    def __area__(self):
        return self.side ** 2


def test_special(x):
    square1 = Square(x)
    print "perimeter:", square1.__per__()

    print "area:", square1.__area__()

input_val = int(raw_input("Enter the length of a side of a square: "))
test_special(input_val)
