"""
If you operate on a class method when several
 instances of the object are in play does it affect all of them?
"""


class TestClass(object):
    """docstring for TestClass"""
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg)

    @classmethod
    def test_class_method(cls, bar):
        return cls("Fails?")


if __name__ == '__main__':
    test_object1 = TestClass(1)
    test_object2 = test_object1.test_class_method(3)

    print(test_object1)
    print(test_object2)
