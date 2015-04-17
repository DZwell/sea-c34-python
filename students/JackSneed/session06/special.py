# Can I use __pow__ and __str__ string in a class to raise an int to a power?
class Raise(object):
    def __init__(self, value):
        self.value = value


    def __pow__(self, num):
        return Raise(self.value ** num)


    def __str__(self):
        return str(self.value)


high_rise = Raise(6)
print(high_rise ** 2)
