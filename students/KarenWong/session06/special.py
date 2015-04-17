def add():
    """
    How to make a class behave like a number by using the __add__ special
    method?
    """
    class AddSpecialMethod(object):

        def __init__(self, x):
            self.x = x

        def __add__(self, other):
            return self.x + other.x

    a = AddSpecialMethod(10)
    b = AddSpecialMethod(5)
    print a + b

if __name__ == '__main__':
    add()
