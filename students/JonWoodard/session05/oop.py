"""
This file will contain two questions about object oriented progamming.
"""


class Animal(object):
    """A new class called 'Animal'."""

    def __init__(self, name, sound):
        """Initialize the class."""
        self.name = name
        self.sound = sound

    def basic_info(self):
        """Return the name and sound of the animal."""
        print("The {} says {}.".format(self.name, self.sound))


def oop_1():
    """
    First question:
    What kinds of things are objects?
    Are classes objects? Are functions objects? Are variables objects?
    """
    print(type(Animal.__init__))
    print(type(Animal.basic_info))
    print(type(Animal))


def oop_2():
    """
    Second question:
    Are different instances of an object different objects?
    """

    a1 = Animal("cow", "moo")
    a2 = Animal("pig", "oink")
    a3 = Animal("duck", "quack")
    animals_1 = [a1, a2, a3]
    animals_2 = [a1, a2, a3]

    assert animals_1 == animals_2

oop_1()
oop_2()

