def nested_list_comp():
    """Can I use a list comprehension within another?"""
    outer = [x * y for x in range(1, 10) for y in [i ** 2 for i in range(10)]]
    print outer


nested_list_comp()
# result: Yes I can.


def flip_dict():
    """Can I use a dict comprehension to flip dict keys and values?"""
    d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    e = {value: key for key, value in d.items()}
    print(d)
    print(e)


flip_dict()
# result: Absolutely!


def many_ifs():
    """Can I use multiple if conditions in a comprehension?"""
    s = {x for x in range(11) if not x % 2 if x % 5}
    print(s)


many_ifs()
# result: Yes I can.

