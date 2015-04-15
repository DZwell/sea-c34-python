from __future__ import print_function

# 2 Questions (Side note: This section is two bare for questions that
# don't fit better in classes.py or subclasses.py)


def instance_type():
    """What is the type of an intance?"""
    class Foo(object):
        """Set up class Foo."""
        def __init__(self, message):
            self.message = message

    bar = Foo("Hello world")
    print(type(bar))


def instance_type_on_import():
    """What is the type of an instance on import?"""
    class Foo(object):
        """Set up class Foo."""
        def __init__(self, message):
            self.message = message

    print(u"\nQuestion 2:\n")
    bar = Foo("Hello world")
    print(type(bar))


if __name__ == '__main__':
    print(u"\nQuestion 1:\n")
    instance_type()
    # result: The type is "class '__main__.Foo'".

    # Question 2 must be run by importing and running function directly.
    # Method for my test was: "from oop import instance_type_on_import".

    # result: The type is "class 'oop.Foo'". So, Foo is put in the oop
    # namespace rather than the __main__ namespace this way.

