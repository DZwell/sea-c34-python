'''Question: How do I assign attributes/properties to my class Bicycle?
How to construct methods for getting and setting those properties?'''


class Bicycle(object):
    '''Create an object called bicycle that contains color, gears,
    and tire properties'''
    def __init__(self):
        self.color = "red"
        self.gears = 12
        self.tires = "street"

    def set_bike_info(self, x, y, z):
        '''method to set bicycle properties'''
        self.color = x
        self.gears = y
        self.tires = z

    def get_bike_info(self):
        '''method to retrieve bicycle properties'''
        return(self.color, self.gears, self.tires)

if __name__ == '__main__':

    mybike = Bicycle()
    print(mybike.get_bike_info())
    mybike.set_bike_info("green", "15", "trail")
    print(mybike.get_bike_info())
