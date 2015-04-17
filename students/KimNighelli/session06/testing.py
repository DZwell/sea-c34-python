'''
This is for Task 18- Exploring Session 7 - Testing

I wanted to know what to do if the code I'm testing could
potentially throw an error and how to test with that in mind.
Please see the file example.py to see the function I'm testing.

Kimberlee Nighelli - 8 April 2015
'''

import unittest
from example import float_division


class MyFuncTestCase(unittest.TestCase):
    ''' A testing class '''
    def test_example(self):
        ''' Tests the example.py file '''

        test_values = [(0, 0), (1, 0)]
        for value in test_values:
            with self.assertRaises(AssertionError):
                with self.assertRaises(ZeroDivisionError):
                    expected = "You cannot divide by 0"
            actual = float_division(*value)
            print expected, actual
            self.assertEquals(expected, actual)

        test_values_2 = [(2, 4), (6, 3), (10000, 1000)]
        for value in test_values_2:
            actual = float_division(*value)
            expected = reduce(lambda x, y: float(x)/float(y), value)
            print expected, actual
            self.assertEquals(expected, actual)


def q1():
    '''
    How can I handle errors, like the Zero Division Error,
    while testing?
    '''
    if __name__ == "__main__":
        unittest.main()

if __name__ == "__main__":
    q1()
