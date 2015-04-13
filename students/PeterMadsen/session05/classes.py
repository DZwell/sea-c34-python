class TestClass(object):
    """
    Can you overwrite the constructor function with one that
    contains default values (as shown below the answer is NO)
    The way you do it was a little confusing to me, and I hope
    to spend more time on it soon.

    """
    def __init__(self, x=1, y=2):
        self.x = x
        self.y = y

    def multiply_values(self):
        return self.x * self.y

# Test Code
if __name__ == '__main__':
    FirstObj = TestClass()
    print(FirstObj.multiply_values())
    SecondObj = TestClass(x=4, y=4)
    print(FirstObj.multiply_values())
