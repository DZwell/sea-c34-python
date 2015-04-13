class SpecialList(list):

    def __init__(self):
        list.__init__(self)

    # Question 1
    """can you override Python default methods to deal with your object"""
    def append(self, value):
        self[0] = value

    # Question 2
    def replace(self, index, value):
        """
        How would you write a method that would allow you to replace
        a value in a list with a different value but would return the original
        value?

        """
        try:
            temp = self[index]
            self[index] = value
            return temp
        except IndexError as e:
            print(e)

    # Question 3
    def spam(self):
        """
        How would you have a method to overwrite all entries in a
        SpecialList with 'spam'

        """
        for index in range(len(self)):
            self[index] = 'spam'

    # Question 4
    def switch(self, a, b):
        """
        How would you write a method that extends the functionality of
        lists so that you can switch the value of the list at 'a' with the
        value of the list at 'b'?

        """
        try:
            self[a], self[b] = self[b], self[a]
        except IndexError as e:
            print("That index is out of bounds", e)

# Test Code -----
if __name__ == '__main__':
    test_list = SpecialList()
    test_list.extend([1, 2, 3, 4, 5])
    test_list.append(45)
    print(test_list)
    test_list.switch(0, 2)
    print(test_list)
    test_list.spam()
    print(test_list)
    test_var = test_list.replace(4, 12312)
    print(test_list)
    print(test_var)
