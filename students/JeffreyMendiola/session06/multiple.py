"""
===============================================================================
file: multiple.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/08/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #18 Investigate Session 7
===============================================================================
"""

# Can a subclass inherit multiple classes?


class Profile(object):
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


class BoxingAttributes(object):
    def __init__(self, speed, power, defense, heart):
        self.speed = speed
        self.power = power
        self.defense = defense
        self.heart = heart


class BoxingPromoter(object):
    def __init__(self, promoter):
        self.promoter = promoter


class Boxer(Profile, BoxingAttributes, BoxingPromoter):
    def __init__(self, name, age, country,
                 speed, power, defense, heart,
                 promoter):
        Profile.__init__(self, name, age, country)
        BoxingAttributes.__init__(self, speed, power, defense, heart)
        BoxingPromoter.__init__(self, promoter)

MP = Boxer("Manny Pacquiao", 36, "Philippines", 10, 10, 10, 10, "Top Rank")

print(
    """
    Boxer Profile
    Name: {n}
    Age: {a}
    Country: {c}
    Promoter: {pr}
    Speed: {s}
    Power: {p}
    Defense: {d}
    Heart: {h}
    """.format(n=MP.name, a=MP.age, c=MP.country, pr=MP.promoter,
               s=MP.speed, p=MP.power, d=MP.defense, h=MP.heart)

)
