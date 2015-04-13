# Can I have a class inside a class?


def q():
    class mother(object):
        def __init__(self):
            self.age = 30

        class child(object):
            def __init__(self):
                self.age2 = 1

    m = mother()
    print m.age  # Answer: 30

    print m.child.age2  # Answer: error

    x = m.child()
    print x.age2  # Answer: 1

    # Answer: Yes
