import unittest
from testing import my_func
'''Question : I have defined a function that will generate the sum and
multiply it by 17. How can properly unitest by algorithm?'''


class MyFuncTestCase(unittest.TestCase):
    def test_my_func(self):
        test_vals = (2, 3)
        expected = reduce(lambda x, y: 17 * (x + y), test_vals)
        actual = my_func(*test_vals)
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
