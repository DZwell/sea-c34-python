'''
This is for Task 18 - Exploring Session 7 - Properties

The function below holds a question I had while reviewing
the session 7 notes.

Kimberlee Nighelli - 8 April 2015
'''


class K(object):
    ''' A class the gets and sets some values '''

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value % 2 == 1:
            self._x = (value * 2)
        else:
            self._x = (value * 3)


def q1():
    ''' Can I set rules on a setter function? '''

    a = K(45)
    b = K(20)
    c = K(19)

    print "The original value: ", a.x
    a.x = 23
    print "The new value from the setter: ", a.x

    print "The original value: ", b.x
    b.x = 12
    print "The new value from the setter: ", b.x

    print "Only if you redefine (variable).x do we "\
          "enter the setter function. But yes, we can set rules! "

if __name__ == "__main__":
    q1()

'''
Output:
    The original value:  45
    The new value from the setter:  46
    The original value:  20
    The new value from the setter:  36
    Only if you redefine (variable).x do we enter the setter function.
    But yes, we can set rules!
'''
