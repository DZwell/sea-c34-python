"""
===============================================================================
file: testing.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/08/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #18 Investigate Session 7
===============================================================================
"""
import unittest


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def loop_count(a):
    total = 0
    while 0 < a:
        total += 1
        a -= 1
    return total


class TestFunctions(unittest.TestCase):
    def test_add(self):
        add_result = addition(5, 7)
        self.assertEquals(12, add_result)

    def test_sub(self):
        sub_result = subtraction(22, 10)
        self.assertEquals(12, sub_result)

    def test_loop(self):
        loop_result = loop_count(12)
        self.assertEquals(12, loop_result)

if __name__ == '__main__':
    unittest.main()
