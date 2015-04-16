import unittest
from break_me import name_error_function


class BreakMeTestingCase(unittest.TestCase):
    def test_break_me_function(self):
        self.assertRaises(NameError, name_error_function)

if __name__ == '__main__':
    unittest.main()
