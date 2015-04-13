t = (lambda x, y: x + y,)
"""
Can you put lambda in a tuple?
"""
print t[0](3, 4)  # Yes


reduce(lambda x, y: x + y, t)
"""
Can you use "reduce" on tuples?
"""
t = (2, 4, 6, 8, 10)  # Yes


l = [1, 2, 3, 4, 5]


def tuple_map(x):
    """
    Can you use "map" on tuples?
    """
    return x * 2

map(tuple_map, l)  # Yes
