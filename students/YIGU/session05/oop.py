# Can python handle multiple inheritance?

# 1. test 1 with same vars


def q1():
    class father1(object):
        def __init__(self):
            self.eyes = 'blue'
            self.hair = 'blond'

    class mother1(object):
        def __init__(self):
            self.eyes = 'brown'
            self.hair = 'black'

    class child1(father1, mother1):
        def __init__(self):
            # father1.__init__(self)
            mother1.__init__(self)
            father1.__init__(self)

        def get_eye_color(self):
            return self.eyes

        def get_hair_color(self):
            return self.hair

    c1 = child1()
    print c1.get_eye_color()
    print c1.get_hair_color()

# Answer: Yes. Inher from which ever come call last

# 2. test 2 with diff vars


def q2():
    class father2(object):
        def __init__(self):
            self.eyes = 'blue'

    class mother2(object):
        def __init__(self):
            self.hair = 'black'

    class child2(father2, mother2):
        def __init__(self):
            father2.__init__(self)
            mother2.__init__(self)

        def get_eye_color(self):
            return self.eyes

        def get_hair_color(self):
            return self.hair

    c2 = child2()
    print c2.get_eye_color()
    print c2.get_hair_color()

# Answer: Yes.
