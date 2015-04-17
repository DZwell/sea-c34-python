# Can I perform math with numbers outside of a static method?
class StaticAdder(object):
    @staticmethod
    def subtract(a, b):
        return a - b

print(StaticAdder.subtract(4, 5) * 10)

