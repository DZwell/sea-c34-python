# Can I override properties from a inherit class?


def q():
    class C(object):
        _x = None

        def getx(self):
            return self._x

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x
        x = property(getx, setx, delx, "docstring")

    class D(C):
        def getx(self):
            return 16

        def delx(self):
            del self._x
        x = property(getx, C.setx, delx, "docstring")

    d = D()
    print d.x

q()

# Answer: Yes
