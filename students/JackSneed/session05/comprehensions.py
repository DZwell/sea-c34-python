def comprehend():
    """Can a replicate a traditional for loop with comprehension?"""
    numbers = range(10)

    hard_copy = []

    for i in numbers:
        hard_copy.append(i)
        print(hard_copy)

    hard_copy2 = [i for i in numbers]
    print(hard_copy2)

comprehend()


def make_a_float():
    """Using comprehension, can I zip a dict of iinteger keys with there float
    value?

    """
    numbers = range(0, 16)
    float_value = dict(zip(numbers, [float(f_number) for f_number in numbers]))
    print float_value

make_a_float()


def math_stuff():
    """Can I get the value of key * 11?"""
    equation = {i: i*2 for i in range(1, 6)}
    print(equation)

math_stuff()
