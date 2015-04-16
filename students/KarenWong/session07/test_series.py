import unittest
from series import fibonacci


class SeriestestingCase(unittest.TestCase):
    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(10) == 55

if __name__ == '__main__':
    unittest.main()
