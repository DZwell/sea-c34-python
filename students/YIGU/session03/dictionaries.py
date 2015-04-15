# Dictionaries and Sets questions


def q1():
    """What happen when I have the same keys in a dict?"""
    q1 = {1: 1, 2: 2, 1: 3}

    print q1[1]
    print q1
    # Anwser: the key get overwrite
    # 3
    # {1: 3, 2: 2}
q1()


def q2():
    """Can I have dict inside of dict?"""
    q2 = {1: {'key1': 'a', 'key2': 'b'}, 2: {'key1': 'c', 'key2': 'd'}}

    print q2
    # Anwser: Yes
    # {1: {'key1': 'a', 'key2': 'b'}, 2: {'key1': 'c', 'key2': 'd'}}

q2()


def q3():
    """What happen when I sort by keys or values?"""
    q3t = {1: ('c', 'd'), 3: ('a', 'b'), 2: ('j', 'k')}
    q3l = {1: ['c', 'd'], 3: ['a', 'b'], 2: ['j', 'k']}
    q3d = {1: {'k1': 'k', 'k2': 'z'}, 2: {'k1': 'c', 'k2': 'd'}, 3: {'k1': 'a', 'k2' : 'b'}}
    q3mix = {1: ('c', 'd'), 3: ['a', 'b'], 2: {'k1': 'c', 'k2': 'd'}}

    print sorted(q3t.keys())
    # a:[1, 2, 3]
    print sorted(q3t.values())
    # a:[('a', 'b'), ('c', 'd'), ('j', 'k')]
    print sorted(q3l.values())
    # a:[['a', 'b'], ['c', 'd'], ['j', 'k']]
    print sorted(q3d.values())
    # a:[{'k2': 'b', 'k1': 'a'}, {'k2': 'd', 'k1': 'c'}, {'k2': 'z', 'k1': 'k'}]
    print sorted(q3mix.values())
    # a:[{'k2': 'd', 'k1': 'c'}, ['a', 'b'], ('c', 'd')]

q3()


def q4():
    """I don't understand pop out an arbitrary key, value pair example."""
    q1 = {1: 1, 2: 2, 1: 3}

    q4_1 = q1.popitem()

    print q4_1
    q1 = {1: 1, 2: 2, 1: 3}
    q4_2 = q1.popitem()

    print q4_2
    q1 = {1: 1, 2: 2, 1: 3}
    q4_3 = q1.popitem()

    print q4_3

# pop out an arbitrary key = pop out an random key then turn them into tuple
# I don't know when will I use it.
# (2,2)
# (1,1)
# (1,1)

q4()
