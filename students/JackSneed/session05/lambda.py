def function_builder(n):
    """
    Write a function that returns a list of n functions, such that each one,
    when called, will return the input value, incremented by an increasing
    number.

    """
    return [lambda a, b=c: a + b for c in range(n)]

if __name__ == "__main__":
    the_list = function_builder(4)
    for f in the_list:
        print(f(5), f(9))
    assert(the_list[0](2) == 2)
    assert(the_list[1](2) == 3)
