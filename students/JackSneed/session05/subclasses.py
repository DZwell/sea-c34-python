# Question 1

"""Can a I add an instance with a subclass?"""
class Build(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Build("I think", " I got it!")

class NewBuild(Build):
    def __init__(self, name):
        self.name = name

b = NewBuild("Jack")

if __name__ == '__main__':
    print("My name is {} and {}{}.".format(b.name, p.x, p.y))


# Question 2

"""Does child class inherit from parent class?"""
class Colors(object):

    color = "blue"

class Child_color(Colors):
    def __init__(self, color):
        self.color = color

if __name__ == '__main__':
    print(Child_color.color)


# Question 3

"""Can I overwrite parent class objects in a child class"""
class parent(object):

    home = "two-story"
    car = "black"

class child(parent):

    car = "blue"

if __name__ == '__main__':
    print("My parents have a {} home. They drive a {} car and mine is {}"
          .format(parent.home, parent.car, child.car))


# Question 4

"""Can I write a class of NFC West NFL teams?"""
class NFL(object):
    def __init__(self, name):

        self.name = name

class NFC_West(NFL):
    def __init__(self, name, color, mascot):

        self.name = name
        self.color = color
        self.mascot = mascot

    def introduction(self):

        intro = "The {name} wear {color} and {mascot} is the mascot"
        print(intro.format(
            name=self.name,
            color=self.color,
            mascot=self.mascot))

if (__name__ == "__main__"):
    t1 = NFC_West("Seahawks", "blue and green", "Blitz")
    t2 = NFC_West("Cardinals", "cardinal red", "Big Red")
    t3 = NFC_West("Rams", "mellennium blue and new century gold", "Rampage")
    t4 = NFC_West("49ers", "cardinal red and metallic gold", "Sourdough Sam")
    teams = [t1, t2, t3, t4]
    for i in teams:
        i.introduction()
