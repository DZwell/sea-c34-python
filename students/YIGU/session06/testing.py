# Testing: can I use unit test in the same file as my code?

# in my_mod.py


def q():
        def my_func(val1, val2):
            return val1 * val2

        # in test_my_mod.py
        import unittest

        class MyFuncTestCase(unittest.TestCase):
            def test_my_func(self):
                test_vals = (2, 3)
                expected = reduce(lambda x, y: x * y, test_vals)
                # expected = reduce(lambda x, y: x + y, test_vals)
                print expected
                actual = my_func(*test_vals)
                print actual
                self.assertEquals(expected, actual)

        if __name__ == '__main__':
            unittest.main()

q()
# Answer: Yes
