'''
This is for Task 13- List Comprehensions

The first part of this assignment was to take an online quiz in Canvas,
which I have already completed. Please see the quiz "Comprehension
Comprehension"

The task had the following instruction: Return the number of even ints in
the given array. Note: the % "mod" operator computes the remainder,
e.g. 5 % 2 is 1.

Below is the function doing that.

Kimberlee Nighelli - 31 March 2015
'''


def count_evens(nums):
    ''' Given an array, returns the count of even numbers in it '''
    return len([x for x in nums if x % 2 == 0])

'''
Testing
'''

if __name__ == "__main__":
    assert count_evens([2, 4, 5, 7]) == 2
    assert count_evens([-3, -2, -1, 0, 1, 2, 3, 4]) == 4
    assert count_evens([3, 5, 9, 273]) == 0
    assert count_evens([8, 2, 7, 1, 0, 2, 2, 0, 5, 9, 3, 22, 104]) == 8

    print "All tests passed"
