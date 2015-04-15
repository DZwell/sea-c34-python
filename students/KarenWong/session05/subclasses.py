class Cat(object):
    def __init__(self, **kwargs):
        self.energy_points = 6
        self.color = "orange"
        self.favorite_food = "fish"
        for key, value in kwargs.items():
            setattr(self, key, value)


class Dog(object):
    def __init__(self, **kwargs):
        self.energy_points = 10
        self.color = "yellow"
        self.favorite_food = "rice"
        self.sound = "roar"
        for key, value in kwargs.items():
            setattr(self, key, value)

    def learning_ability(self, focus=2):
        self.learning_ability = 3 * focus
        print self.learning_ability


def add_attribute():
    """ Can we add a new attribute that the object does not initially have?"""
    fufu = Cat(energy_points=100, color="grey", favorite_food="tuna",
               sound="meow")
    print fufu.sound


def override_methods():
    """How do you override the learning_ability method of the Dog class?"""
    class Corgi(Dog):
        def __init__(self, **kwargs):
            Dog.__init__(self, **kwargs)
            self.energy_points = 12
            self.favorite_food = "sausage"
            self.sound = "roar"
            for key, value in kwargs.items():
                setattr(self, key, value)

        def learning_ability(self, focus=3):
            self.learning_ability = 3 * focus
            print self.learning_ability
    juju = Corgi()
    juju.learning_ability()
    print juju.color  # juju still inhereit the color from Dog class


# I copied the corgi class for testing purposes for the check_class function
class Corgi(Dog):
    def __init__(self, **kwargs):
        Dog.__init__(self, **kwargs)
        self.energy_points = 12
        self.favorite_food = "sausage"
        self.sound = "roar"
        for key, value in kwargs.items():
            setattr(self, key, value)

    def learning_ability(self, focus=3):
        self.learning_ability = 3 * focus
        print self.learning_ability
juju = Corgi()


def check_class():
    """
    How do you check whether Corgi is a subclass of Dog and juju is
    an instance of the corgi?
    """
    if issubclass(Corgi, Dog):
        print ("Corgi is a subclass of the Dog class")
    else:
        print("Corgi is not a subclass of the Dog class")
    if isinstance(juju, Corgi):
        print ("Juju is an instance of the corgi")
    else:
        print("Juju is not an instance of the corgi")


def override_attribute():
    """ How to override attributes of the cat object?"""
    class Tiger(Cat):
        def __init__(self, **kwargs):
            Cat.__init__(self, **kwargs)
            self.color = "white"
            self.favorite_food = "meat"
            self.has_stripes = True
    tim = Tiger()
    print tim.energy_points
    print tim.color
    print tim.favorite_food
    print tim.has_stripes

add_attribute()
override_methods()
check_class()
override_attribute()
