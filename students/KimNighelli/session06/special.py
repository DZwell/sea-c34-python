'''
This is for Task 18- Explore Session 7- Special Methods.

In this program, I will explore the special methods __len__,
and __reversed__ to run some tests and manipulations
on some values.

Kimberlee Nighelli- 7 April 2015
'''


class Values(object):
    ''' A class holding some tests about values '''
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __reversed__(self):
        return reversed(self.values)


def q1():
    ''' Can use __len__ and __reversed__ to manipulate a list? '''
    values = Values([1, 2, 3, 5, 6, 7, 8, 2, 4])
    print "__len__ method:"
    print values.__len__()
    print "Iterating through values from the __reversed__ method: "
    for value in values.__reversed__():
        print value

if __name__ == "__main__":
    q1()

'''
Output

__len__ method:
    9
Iterating through values from the __reversed__ method:
    4
    2
    8
    7
    6
    5
    3
    2
    1
'''
