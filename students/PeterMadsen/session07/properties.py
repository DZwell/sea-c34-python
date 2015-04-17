"""Why use a property versus just a class attribute?"""


class DontMessWithMe(object):
    def __init__(self, foo):
        self._foo = foo

    @property
    def _foo(self):
        return self._foo


if __name__ == '__main__':
    tester = DontMessWithMe(2)
    tester._foo = 10
