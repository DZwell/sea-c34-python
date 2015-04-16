import unittest
from special import AddSpecialMethod


class SpecialtestingCase(unittest.TestCase):
    def test_special(self):
        assert AddSpecialMethod(10) + AddSpecialMethod(5) == 15

if __name__ == '__main__':
    unittest.main()
