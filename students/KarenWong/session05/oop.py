class Dog(object):
    def __init__(self, energy_points=10, color="yellow", favorite_food="rice",
                 sound="roar"):
        self.energy_points = energy_points
        self.color = color
        self.favorite_food = favorite_food
        self.sound = sound


def doggie():
    """
    How to create an instance of an object that has both similar and
    different attributes than the class
    """
    haru = Dog(color="brown")
    print haru.color
    print haru.sound


def monster():
    """ Can we use kwargs** (dictoionary) as argument for __init__ function"""
    class Monster:

        def __init__(self, **kwargs):
            self.hit_points = kwargs.get("hit_points", 1)
            self.weapon = kwargs.get("weapon", "sword")
            self.color = kwargs.get("color", "yellow")
            self.sound = kwargs.get("sound", "roar")

    bobo = Monster(color="red", sound="tweet")
    print bobo.hit_points
    print bobo.color
    print bobo.sound
    print bobo.weapon


doggie()
monster()
