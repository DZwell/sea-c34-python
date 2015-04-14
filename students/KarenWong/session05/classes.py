def same_attribute():
    """
    If two instances of the class have the same attributes are
    they the same instance?
    """
    class Point(object):
        x = 1
        y = 2
    p = Point()
    g = Point()
    print p is g
    print p.x is g.x   # Just to confirm they have the same attributes
    print p.y is p.y


same_attribute()
