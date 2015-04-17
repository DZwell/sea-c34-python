'''
This is for Task 18- Exploring Session 7 - Static and Class methods

The question I would like to answer is "Does a subclass inherit
the superclass' static method"?

Kimberlee Nighelli - 7 April 2015
'''


class SquareValues(object):
    ''' A class that squares a value '''
    @staticmethod
    def square(n):
        return n ** 2


class SubSquare(SquareValues):
    ''' A subclass inheriting from SquareValues '''
    pass


def q1():
    '''' Does a subclass inherit the superclass' static method"?'''
    v1 = SquareValues.square(10)
    v2 = SubSquare.square(10)
    print v1, v2

if __name__ == "__main__":
    q1()

    for i in range(10):
        assert SquareValues.square(i) == SubSquare.square(i)

    print "Tests passed- Static methods can be inherited"
