# Question One and Test
def mulltiply_functions(object1, object2):
    """
    Can you write a function that multiples different functions?
    Without knowing in advance what the return values of the functions
    are? Function will raise an error if you cannot multiply the types.

    """
    try:
        one = object1
        two = object2
        return one * two
    except TypeError as e:
        print(e)


def test_function_1(value):
    return value


def test_function_2(value):
    return value

print(mulltiply_functions(test_function_1(4), test_function_2(5)))
print(mulltiply_functions(test_function_1(4), test_function_2("hi ")))
print(mulltiply_functions(test_function_1(4), test_function_2(lambda x: x)))


# Question two
def question_two():
    pass
