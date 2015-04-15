#!/usr/bin/env python

# Question 1

"""Can I write a class of NFC teams divided by divisional subclasses?"""
class NFC(object):
    def __init__(self, name):

        self.name = name

class NFC_West(NFC):
    def __init__(self, name):

        self.name = name

    def call(self):

        intro = "{name}"
        print(intro.format(
            name=self.name))

class NFC_East(NFC_West):
    def __init__(self, name):

        self.name = name

class NFC_North(NFC_West):
    def __init__(self, name):

        self.name = name

class NFC_South(NFC_West):
    def __init__(self, name):

        self.name = name

# Question 2

"""
Will the team names in the classes that are
subclasses of NFC_West be called?

"""
if (__name__ == "__main__"):
    t1 = NFC_West("Seahawks")
    t2 = NFC_West("Cardinals")
    t3 = NFC_West("Rams")
    t4 = NFC_West("49ers")
    teams1 = [t1, t2, t3, t4]
    print("\n{:20}\n".format(
          "NFC West"))
    for i in teams1:
        i.call()
    t5 = NFC_South("Saints")
    t6 = NFC_South("Buccaneers")
    t7 = NFC_South("Panthers")
    t8 = NFC_South("Falcons")
    teams2 = [t5, t6, t7, t8]
    print("\n{:20}\n".format(
          "NFC South"))
    for i in teams2:
        i.call()
    t9 = NFC_East("Cowboys")
    t10 = NFC_East("Eagles")
    t11 = NFC_East("Redskins")
    t12 = NFC_East("Giants")
    teams3 = [t9, t10, t11, t12]
    print("\n{:20}\n".format(
          "NFC East"))
    for i in teams3:
        i.call()
    t13 = NFC_North("Lions")
    t14 = NFC_North("Packers")
    t15 = NFC_North("Bears")
    t16 = NFC_North("Vikings")
    teams4 = [t13, t14, t15, t16]
    print("\n{:20}\n".format(
          "NFC North"))
    for i in teams4:
        i.call()
