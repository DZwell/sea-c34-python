def no_init():
    """
    What happens if I don't use 'def __init__' and then try to create \
    an instance of a class and pass it values right away?
    """
    class Animal(object):
        species = "Quad-Pedal"
        name = "Bowser"

    Rabbit = Animal("Test-Pedal", "Bugs")  # Returns a type error.


def with_init():
    """
    Can I repeat the above step, yet successfully create a Rabbit instance \
    of Animal?
    """
    class Animal(object):

        def __init__(self, species, name):
            self.species = species
            self.name = name

    rabbit = Animal("Test-Pedal", "Bugs")
    print(rabbit)


if __name__ == '__main__':
    # no_init()  # Returns a type error.
    with_init()
