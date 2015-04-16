import unittest


def fibonacci(n):
    """return the value in the fibonacci series.

    Args:
        n:the fibonacci index to get the value.

    Returns:
        the fiboncci value of index n.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def lucas(n):
    """return the value of the lucas numbers.

    Args:
        n: the lucas numbers index to get the value.

    Returns:
        the lucas number value of index n.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (lucas(n - 1) + lucas(n - 2))


def sum_series(n, first_value=0, second_value=1):
    """ return the value from the fibonacci series or the lucas numbers or other
        series depending on the parameters.

    Args:
        n : the index of the series, first_value: the first value for the
        series to be produced, second_value: the second value for the series to
        be produced.

    Returns:
        the value of index n from the series to be produced.
    """
    if n == 0:
        return first_value
    elif n == 1:
        return second_value
    else:
        return (sum_series(n - 1, first_value, second_value) +
                sum_series(n - 2, first_value, second_value))

if __name__ == '__main__':
    unittest.main()
