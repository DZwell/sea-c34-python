import unittest
from series import sum_series


class MySeriesTest(unittest.TestCase):
    def test_my_series(self):
        test_vals = (3, 2, 1)
        expected = 4
        actual = sum_series(*test_vals)
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
