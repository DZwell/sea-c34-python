def squarepants():
    """
    How to use decorators to simplify a function?
    """

    class Square(object):

        def __init__(self, length=6):
            self.length = length
            self._area = length * length

        @property
        def area(self):
            return self._area

        @area.setter
        def area(self, value):
            self.length = value / value
            self._area = value

    spongebob = Square()
    print spongebob.length
    spongebob.length = 5
    print spongebob.length
    print spongebob.area


squarepants()
