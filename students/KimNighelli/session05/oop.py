'''
This file is for Task 16- Exploring Session 6- Object Oriented
Programming.

In this file I will write two functions that answer some questions about
Object Oriented Programming that I had while reading through the session 6
notes. Questions will be posed in each function's docstring.

Kimberlee Nighelli 5 April 2015
'''

# Question 1


def inheritance():
    '''
    Question: How does a major aspect of OOP - inheritance - work and what
    does it look like?
    This function will show that properties of a class are shared
    with any class that may be a subclass of it.
    '''

    class Mammals(object):
        ''' A class grouping common mammal characteristics. '''
        legs = 4
        blood = "warm"

        def __init__(self, demeanor=None):
            self.demeanor = demeanor

        def about_mammals(self):
            ''' Returns a descriptor string about a mammal '''
            print "Mammals have %d legs and are %s "\
                  "blooded" % (self.legs, self.blood)

    class Dogs(Mammals):
        ''' A subclass of Mammals describing dogs '''
        # The Dogs subclass inherits all the attributes of Mammals
        pass

    dog = Dogs()
    dog.about_mammals()


# Question 2

def person_dict():
    '''
    Can I store data in a dictionary using a class method as
    opposed to hand-entering it? By creating a method in a
    class- I can easily add future entries.
    '''
    d = {}

    class Person(object):
        ''' A class holding information about people '''

        def __init__(self, name, age, address, email):
            self.name = name
            self.age = age
            self.address = address
            self.email = email

        def add_to_dict(self):
            ''' Adds entries to the d dictionary '''
            d[self.name] = {}
            d[self.name]["age"] = self.age
            d[self.name]["address"] = self.address
            d[self.name]["email"] = self.email

    joe = Person("Joe Smith", "28", "45 Juniper Ave", "jsmith@netzero.com")
    mary = Person("Mary Alice", 54, "9 Harvard Rd", "ma@aol.com")
    joe.add_to_dict()
    mary.add_to_dict()
    print d


if __name__ == "__main__":
    inheritance()
    person_dict()

'''
Output
Mammals have 4 legs and are warm blooded

{'Joe Smith': {'age': '28', 'email': 'jsmith@netzero.com',
'address': '45 Juniper Ave'}, 'Mary Alice': {'age': 54, 'email':
'ma@aol.com', 'address': '9 Harvard Rd'}}
'''
