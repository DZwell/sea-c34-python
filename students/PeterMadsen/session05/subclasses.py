class SpecialList(list):

    def __init__(self):
        list.__init__(self)

    # Question 1
    """can you override default methods to deal with your object"""
    def append(self, value):
        self[0] = value

    # Question 2
    def pop(self, value):
        """Can overload and operator"""
        pass

    # Question 3

    # Question 4

if __name__ == '__main__':
    test_list = SpecialList()
    test_list.extend([1, 2, 3])
    test_list.append(45)
    test_list.pop(1)
    print(test_list)
