"""
===============================================================================
file: static.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/08/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #18 Investigate Session 7
===============================================================================
"""


class StaticFunction(object):
    @staticmethod
    def add(a, b):
        return a + b


class Sub(StaticFunction):
    print "This is the sub function."


def test_function():
    """
    Do sub-classes inherit static methods?
    Output:
        This is the sub function
        2
    Answer: Yes
    """
    print(Sub.add(1, 1))

test_function()
