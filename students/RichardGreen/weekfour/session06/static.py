'''Question: How do I use static and class methods to operate off attributes
in my class Bicycle?'''

# Static method example


class Bicycle(object):
    def service_due(x):
        '''define a static method that determines if your bike is due for
           service'''

        if x > 50:
            print u"Your bike needs service"
        else:
            print u"Your bike does not need service"
    service_due = staticmethod(service_due)

    # Class Method example
    # preset tire pressure
    y = 90

    def pressure_check(cls, x):
        '''define a class method that determines if your bike has
        adequate tire pressure'''

        if x == 90:
            print u"Your tires have adequate pressure"
        if x > 90:
            print u"Your tires have too much air pressure"
        if x < 90:
            print u"Your tires need more air"
            print u"Approximately: (PSI)"
            print abs(cls.y - x)
        else:
            print u"There was something wrone with you entry"
            print u"Please try again"
    pressure_check = classmethod(pressure_check)

if __name__ == '__main__':

    Bicycle.service_due(2)
    Bicycle.service_due(45)
    Bicycle.service_due(55)

    Bicycle.pressure_check(5)
    Bicycle.pressure_check(67)
