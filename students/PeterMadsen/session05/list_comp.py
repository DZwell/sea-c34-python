def count_evens(nums):
    """ This function returns the number of evens in a given list"""
    return len([i for i in nums if i % 2 == 0])

# TEST CODE
# Tests are verbatum to the requirements posted.
# All should evaluate to True
if __name__ == '__main__':
    print(count_evens([2, 1, 2, 3, 4]) == 3)
    print(count_evens([2, 2, 0]) == 3)
    print(count_evens([1, 3, 5]) == 0)
