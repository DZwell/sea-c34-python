'''Question: What super/magic method can I use to pass in
objects that I want into in my Bicycle class?'''


class Bicycle(object):
    def __init__(self):
        self.color = "red"
        self.gears = 12
        self.tires = "street"
    ''' I will implement the __getitem__ super method to
    pass in objects. I can then use [] index operators to
    access these obejcts.'''
    def __getitem__(self, items):
        print '%-10s  %s' % (type(items), items)

if __name__ == '__main__':

    mybike = Bicycle()
    # Lets test the differnet types of objects I can feed with getitem

    mybike[1]
    mybike['I want to ride my bicycle!']
    mybike[range(15)]
    mybike['Rich':'Green':40]
    mybike[object()]
