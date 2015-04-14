my_word = "Hello"


def map_string(word):
    """
    Can I map a string together with another string?

    Arg:
        word(str)
    Return: Mapped strings.
    """
    return "%s howdy" % (word)

print(map(map_string, my_word))


def float_filter():
    """
    Can I print only floats using filter?
    """
    my_list = [12, 44.5, 15, 88.72]

    print(filter(lambda x: x % 1, my_list))

float_filter()


def string_reduce():
    """
    Can I reduce list of letters into a string?
    """
    letter_list = ["H", "E", "L", "L", "O"]

    print(reduce(lambda x, y: x + y, letter_list))

string_reduce()
