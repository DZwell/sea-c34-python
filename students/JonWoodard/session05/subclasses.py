"""
Ask four questions about subclassing
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


class FarmAnimal(Animal):
    """A subclass of 'Animal'"""


class ZooAnimal(Animal):
    """Another subclass of 'Animal'."""

    def __init__(self, name, food):
        """Initialize ZooAnimal differently from other Animals"""
        self.name = name
        self.food = food

    def basic_info(self):
        """Return the name and food of the zoo animal."""
        print("The {} eats {}.".format(self.name, self.food))


class SeaAnimal(Animal):
    """A subclass of 'Animal' that lives in the water"""

    def __init__(self, name, attribute):
        """Initialize SeaAnimal differently from other Animals"""
        self.name = name
        self.attribute = attribute

    def basic_info(self):
        """Return the name and food of the zoo animal."""
        print("The {} is {}.".format(self.name, self.attribute))


class SeaMammal(SeaAnimal):
    """A subclass of a subclass"""

    def basic_info(self):
        """Return the name and food of the zoo animal."""
        print(
            "The {} is {}\n"
            "The {} is a mammal and breaths air!"
            .format(self.name, self.attribute, self.name)
            )


def subclass_1():
    """
    First question about subclasses:
    If a class is created, which contains a function,
    is that function available to subclasses created from that original
    class, without being explicitly created?
    """
    a1 = FarmAnimal("cow", "moo")
    a2 = FarmAnimal("pig", "oink")
    a3 = FarmAnimal("duck", "quack")
    animals = [a1, a2, a3]
    for item in animals:
        item.basic_info()

subclass_1()


def subclass_2():
    """
    Second question about subclasses:
    Can a subclass be initialized with different arguments than the parent?
    """
    z1 = ZooAnimal("lemur", "monkey chow")
    z2 = ZooAnimal("tiger", "meat")
    z3 = ZooAnimal("aardvaark", "termites")
    animals = [z1, z2, z3]
    for item in animals:
        item.basic_info()

subclass_2()


def subclass_3():
    """
    Third question about subclasses:
    Can you create a subclass from another subclass?
    """
    s1 = SeaAnimal("shark", "hungry")
    s2 = SeaAnimal("jellyfish", "spineless")
    s3 = SeaAnimal("tuna", "fast")
    sm1 = SeaMammal("blue whale", "enormous")
    animals = [s1, s2, s3, sm1]
    for item in animals:
        item.basic_info()


subclass_3()


def subclass_4():
    """
    Fourth question about subclasses:
    Can a subclass be made to treat functions differently than other
    subclasses of the same parent?
    """
    a1 = FarmAnimal("cow", "moo")
    z1 = ZooAnimal("tiger", "meat")
    s1 = SeaAnimal("tuna", "fast")
    animals = [a1, z1, s1]
    for item in animals:
        item.basic_info()

subclass_4()
