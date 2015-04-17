# Trying out super(). Are they really the same?


def q():
    class father(object):
        def __init__(self):
            self.eyes = 'blue'

    class child1(father):
        def __init__(self):
            father.__init__(self)

    class child2(father):
        def __init__(self):
            super(child2, self).__init__()

    a = child1()
    b = child2()

    print a.eyes is b.eyes

q()
