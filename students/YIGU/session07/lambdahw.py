# This function returns a list of n functions, such that each one, when\
# called, will return the input value, incremented by an increasing number.


def var_factory(n):
    return lambda x: x+n


def list_functions(n):
    functions = []
    for i in range(n):
        functions.append(var_factory(i))
    return functions
