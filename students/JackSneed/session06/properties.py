# Can I get the property method to work?
class Mix(object):

        def __init__(self, x="blue", y="black", z="green"):
            self._x = x
            self._y = y
            self._z = z


        def fget(self):
            print self._x
            print self._y
            print self._z

        r = property(fget)

c = Mix()
c.r

