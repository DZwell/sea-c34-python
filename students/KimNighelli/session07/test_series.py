import unittest
from series import fibonacci, lucas


class MyTests(unittest.TestCase):
    ''' A class to run unittests on series.py '''

    def test_fib(self):
        ''' Test the outputs of the fibonnaci function '''
        assert fibonacci(-1) is None
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

    def test_lucas(self):
        ''' Test the outputs of the lucas function '''
        assert lucas(-14) is None
        assert lucas(0) == 2
        assert lucas(1) == 1
        assert lucas(6) == 18

if __name__ == "__main__":
    unittest.main()
