def arg_comprehension(*args):
    """
        Can *args be used in list comprehension?

        Args:
            *args
        Return:
            Appendning *args to list
    """

    my_list = [args for argument in args]
    print(my_list)

arg_comprehension("Heeeey", "brother")


def stop():
    """
        Used to answer below question. Needed a way to stop the loop from \
        iterating.
    """
    raise StopIteration


def print_the_first(*args):
    """
        Can only the first argument be printed, using comprehension?

        Args:
            *args
        Return:
            Print the first argument given.
        Result: Had to use 2 functions to make it work, and it's kind of a \
        cheat, but it works.
    """

    my_list = list(args[0] if argument == 1 else stop() for argument in args)
    print(my_list)

print_the_first(1, 2, 3, 4)

text = "Hello, how are you?"


def print_third_character(text):
    """ Can I print only the 3rd character of any given arguments using \
    comprehension?

        Args:
            text(str): String to be iterated over.
        Return:
            Only the third character of each word given.
    """
    third_character = [word[2] for word in text.split()]
    print(third_character)

print_third_character(text)
