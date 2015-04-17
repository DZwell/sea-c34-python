# When I inherit staticmethod in a subclass, do I need to define the method as
# static?

"""
def q_1():
    class A(object):
        @staticmethod
        def a(x):
            return x

    class B(A):
        def a(x):
            return A.a(x)

    test = B()
    print test.a(1)

q_1()
"""


def q_2():
    class A(object):
        @staticmethod
        def a(x):
            return x

    class B(A):
        @staticmethod
        def a(x):
            return A.a(x)

    test = B()
    print test.a(1)

q_2()

# Answer: Yes. I need to define again.
