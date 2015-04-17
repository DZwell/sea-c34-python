# What happen when I create a method with double underscores?


def q():
    def _test_():
        print "This is a test"

    _test_()

    class A(object):
        def _test_(self):
            print "This is also a test"
    a = A()
    a._test_()

q()

# Anwser: No error.
