# This is the module to test testing.py
import unittest
from testing import my_division_function

test_data = [5, 0]


def test_my_division_function_that_has_error(self):
    test_fn = lambda x, y: x / y
    self.assertRaises(ZeroDivisionError, test_fn, 5, 0)


@unittest.skipIf(0 in test_data,
                 "Cannot divide by zero.")
def test_skip_if(self):
    [1 / x for x in test_data]

if __name__ == '__main__':
    unittest.main()
# yes, you can skip a zeroDivisionError
