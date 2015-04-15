"""
Ask one question about classes in python
"""


class FarmAnimal(object):
    """
    One question:
    How do you create a new class?
    """
    def __init__(self, name, sound):
        """Initialize the class."""
        self.name = name
        self.sound = sound

    def basic_info(self):
        """Return the name and sound of the farm_animal."""
        print("The {} says {}.".format(self.name, self.sound))

if __name__ == "__main__":
    a1 = FarmAnimal("cow", "moo")
    a2 = FarmAnimal("pig", "oink")
    a3 = FarmAnimal("duck", "quack")
    animals = [a1, a2, a3]
    for a in animals:
        a.basic_info()
