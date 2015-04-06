class SpecialList(list):

    def __init__(self):
        list.__init__(self)

    # Question 1
    """can you override Python default methods to deal with your object"""
    def append(self, value):
        self[0] = value

    # Question 2
    def pop(self):
        """Can overload an operator with a different default value"""
        self[-1]

    # Question 3
    def spam(self):
        """
        How would you have a method to overwrite all entries in a
        SpecialList with 'spam'

        """
        for index in range(len(self)):
            self[index] = 'spam'

    # Question 4

if __name__ == '__main__':
    test_list = SpecialList()
    test_list.extend([1, 2, 3])
    test_list.append(45)
    print(test_list)
    test_list.pop()
    print(test_list)
    test_list.spam()
    print(test_list)
