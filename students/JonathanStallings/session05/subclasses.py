from __future__ import print_function
import sys
import traceback

# 4 Questions


def class_chaos():
    """What happens if I try something silly, like cyclical inheritance?"""
    class Foo(Bar):
        """Set up class Foo"""
        color = "red"

        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Bar(Foo):
        """Set up class Bar"""
        color = "green"

        def __init__(self, x, y):
            self.x = x
            self.y = y

    b = Bar(10, 5)
    print(b.color)


def import_list_methods():
    """Can I use subclassing to import built-in list methods?"""
    class my_list(list):
        """Set up my list class."""
        pass

    a = my_list()
    print(
        u"my_list methods include: {methods}"
        .format(methods=dir(a))
    )


def update_superclass_attributes():
    """Will a changed superclass attribute update in instance?"""
    class Foo(object):
        """Set up class Foo."""
        color = "red"

    class Bar(Foo):
        """Set up class Bar"""
        def __init__(self, x, y):
            self.x = x
            self.y = y

    thing = Bar(10, 20)
    assert(thing.color == "red")
    print(thing.color)

    Foo.color = "green"
    assert(thing.color == "green")
    print(thing.color)


def update_superclass_methods():
    """Will a changed superclass method update in instance?"""
    class Foo(object):
        """Set up class Foo."""
        def __init__(self, x, y):
            """Set up class Foo."""
            self.x = x
            self.y = y

        def move(self):
            """Move to a forward along x axis."""
            print(u"Moving!")
            self.x += 10

        def report(self):
            """Print out current position."""
            print(
                u"I am at position {x}, {y}."
                .format(x=self.x, y=self.y)
            )

    class Bar(Foo):
        """Set up class Bar."""
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def move_faster(self):
        """Updated move method."""
        print(u"Moving faster!")
        self.x += 20

    thing = Bar(10, 20)
    thing.report()
    thing.move()
    thing.report()
    Foo.move = move_faster
    thing.move()
    thing.report()


if __name__ == '__main__':
    print(u"\nQuestion 1:\n")
    try:
        class_chaos()
    except UnboundLocalError:
        traceback.print_exc(file=sys.stdout)

    # result: This silly setup doesn't even get off the ground due to an
    # UnboundLocalError since Bar is reference on line 10 before assignment.

    print(u"\nQuestion 2:\n")
    import_list_methods()
    # result: Yes, I can.

    print(u"\nQuestion 3:\n")
    update_superclass_attributes()
    # result: Yes, the changes are updated in derived instances.

    print(u"\nQuestion 4:\n")
    update_superclass_methods()
    # result: Yes, the changes are updated in derived instances.

