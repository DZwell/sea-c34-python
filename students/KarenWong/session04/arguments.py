def empty(*args, **kwargs):
    """ what happens when you have empty args or kwargs in a function? Does it
    raise an error?"""
    print args
    print kwargs
# it prints out an empty tuble and empty dictionary


def stringformat():
    """What happens when you put the {} inside another curly brace while passing
    a dict to the string.format()method? Does it raise an error"""
    d = {"last": "wong", "first": "Karen"}
    print "My name is {first{last}}".format(**d)
# it raises the key EnvironmentError


def shallowcopy():
    """can you use a shallow copy to change an object without
    touching the original?"""
    list1 = [[2, 3, 4], ["k", "a"]]
    list2 = list1[:]
    print list1[0] is list2[0]
    list2[0] = [5, 6, 7]
    print list1[0] is list2[0]
# yes
