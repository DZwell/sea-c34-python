'''This function performs a fibonacci series based off of a single user
defined value.The function should returns  ``nth`` value in the fibonacci
series
'''


def fibonacci(n=5):
    '''
    Numeric arguments:
    n an integer
    Returns: an integer
    '''
# Returns the fibonacci series based off a user defined number
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    '''
    This function performs a lucas number series using an integer
    defined value. This function is similar to a fibonacci but instead of
    starting with integers 0 and 1 its starts with 2 and 1. The function
    should return  the nth value in the lucas number series.
    Numeric arguments: n an integer
    Returns: an integer
    '''
# Returns the lucas numbers based off a user defined number
    if n < 0:
        return None
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n0=0, n1=1):
    '''
    This function performs a sum series based off the previous functions
    outlined above: the fibonacci and lucas numbers are based off a single
    user defined value and 2 optional user defined values. This function has
    default values of 0 and 1 to determine the first two values in the series
    to be produced. With no optional paramters the function produces numbers
    from the fibonacci series function. With optional arguments 2 and 1  the
    function produces the lucas numbers series. When other values for the
    optional parameters are entered the function will produce a different nth'
    value in its series. Numeric arguments: n an integer, n0 an integer,
    n1: an integer
    Returns: an integer
    '''
    if n < 0:
        return None
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)

# if __name__ == "__main__":
#     # lets test the fibnonacci module on an increasing set of integers
#     assert(fibonacci(1) == 1)
#     assert(fibonacci(5) == 5)
#     assert(fibonacci(7) == 13)
#     assert(fibonacci(15) == 610)
#     # now lets test the lucas numbers function on a set of integers
#     assert(lucas(7) == 29)
#     assert(lucas(10) == 123)
#     assert(lucas(15) == 1364)
#     # And lastly we test our sum series function
#     # # on an increasing set of integers
#     assert(sum_series(5, n0=1, n1=5) == 28)
#     assert(sum_series(2) == 1)
#     assert(sum_series(3, n0=2, n1=1) == 4)
