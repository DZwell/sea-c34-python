def change_copy():
    """
    Can you change the content of a copy without touching the original file?
    """
    list1 = [[1, 2, 3], [4, 5, 6]]
    list2 = list1[:]
    print list1[0] is list2[0]
    list2[0] = ['a', 'b', 'c']
    print (list1)
    print (list2)
    print list1[0] is list2[0]  # Yes, you can


def empty_argument(*args, **kwargs):
    """
    What happen when you pass in empty args and kwargs for a function?
    """
    print (args)
    print (kwargs)  # prints out an empty tuble and empty dictionary


def string_format():
    """
    Can you pass a tuble to the string.format method?
    """
    t = ("Karen", "Wong")
    print "this is %s %s" % t   # yes you can


change_copy()
empty_argument()
string_format()
