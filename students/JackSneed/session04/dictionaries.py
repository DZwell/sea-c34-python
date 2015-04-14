def getting_sneaky():
    """Can I sneak a list key into a dictionary via tuple?"""

    d = {}
    d[([1, 2, 3])] = u"hope this works!"

# getting_sneaky()
# NO! After testing, returns "TypeError: unhashable type: 'list'


def find_key():
    """What happens when I look for a key that isn't there?"""

    d = {u'here': 1, u'i': 2, u'am': 3}
    print(2 in d)


find_key()


def update_dict():
    """Can I update a dictionary?"""

    d = {u'here': 1, u'i': 2, u'am': 3}
    d.update(oh=1, boy=2)
    print(d)


update_dict()


def set_trippin():
    """Can I create a new set from two existing sets?"""

    s1 = set([1, 2, 3])
    s2 = set([4, 5, 6])
    s3 = s1.union(s2)
    print(s3)

set_trippin()
