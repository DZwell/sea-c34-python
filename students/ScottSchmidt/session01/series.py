def fib(fibIndex):
    """ Return the nth number of the Fibonacci sequence.

        Arg:
            fibIndex: Provide Integer value argument for nth index of
            Fibonacci series.

        Return:
            Return single integer value of Fibonacci sequence at index,
            determined by function argument. """
    first, second, count = 0, 1, 1
    while count < fibIndex:
        first, second, count = second, first + second, count+1
    return first


def lucas(lucIndex):
    """ Return the nth number of the Lucas sequence.

        Arg:
            lucIndex: Provide Integer value argument for nth index of Lucas
            series.

        Return:
            Return single integer value of Lucas sequence at index,
            determined by function argument. """
    first, second, count = 2, 1, 1
    while count < lucIndex:
        first, second, count = second, first + second, count + 1
    return first


def sum_series(nth, first=0, second=1):
    """ Return the nth number of the Lucas sequence from user input.

        Arg:
            nth: Provide Integer value argument for nth index of Lucas
            series.

            first: Optional parameter argument, determine the beginning
            integer value of the series.

            second: Optional parameter argument, determine the second
            integer value of the series.


        Return:
            Return single integer value of the sequence at index,
            determined by user input, and use optional argument values
            for first and second index values of series. """
    count = 1
    while count < nth:
        first, second, count = second, first + second, count + 1
    return first


if __name__ == "__main__":
    """Test output values for each given index argument."""
    assert fib(10) == 34
    assert fib(11) == 55
    assert fib(12) == 89

    assert lucas(10) == 76
    assert lucas(11) == 123
    assert lucas(12) == 199

    assert sum_series(10) == 34
    assert sum_series(11, 2, 5) == 343
    assert sum_series(12, 4, 3) == 487
