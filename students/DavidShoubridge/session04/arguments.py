my_list = list(range(0, 11))


def default_var_list(y, x=my_list):
    """
    Can a default variable be set to a list?

    Args:
        y(int): Placeholder.
        x=my_list(lst): Default arg set to list of numbers 0-11.
    """
    print(y)
    print(x)

default_var_list(25)


def can_iterate_over_default_arg(y, x=my_list):
    """
    Can a default variable, as a list, be iterated over?

    Args:
        y(int): Placeholder.
        x=my_list(lst): Default arg to be iterated over.
    """
    for number in x:
        if number <= 3:
            print("I'm not dead yet!")
        elif number <= 6:
            print("You will be!")
        else:
            print("'Tis only a flesh wound!")

can_iterate_over_default_arg(25)


def print_me(*args):
    """
    Can I print an indefinite amount of arguments?

    Args:
        *args
    Return:
        Print all arguments given.
    """
    print(args)

print_me("Hey", "howdy", "hey", 5, 3, 2, 1)