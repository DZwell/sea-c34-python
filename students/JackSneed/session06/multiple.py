# Can a child class run the functions of several parents with
# multiple inheritance?
class Color1(object):

    def red(self):
        print("I am red.")


class Color2(object):

    def yellow(self):
        print("I am yellow.")


class Color3(object):
    def orange(self):
        print("We make orange!")


class Mix(Color1, Color2, Color3):
    pass


cb = Mix()
cb.red()
cb.yellow()
cb.orange()

