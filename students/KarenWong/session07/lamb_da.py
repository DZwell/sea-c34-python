import unittest


def function_builder(n):
    l = []
    for i in range(n + 1):
        l.append(lambda x, y=i: x + y)
    return l

the_list = function_builder(5)


if __name__ == '__main__':
    unittest.main()
