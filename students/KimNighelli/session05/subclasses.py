'''
This is for Task 16 - Investigate Session 6 - Subclasses

In this program, I will pose a variety of question that I had while
reviewing the session 6 slides on subclasses. Each question will be posed
in the docstring of the function corresponding to the question.

Kimberlee Nighelli 5 April 2015
'''


def question_1():

    ''' Can I override a class property in a subclass? '''

    class Cloud(object):
        ''' A class describing cloud properties '''
        base = "CCN"  # Cloud Condensation Nuclei

        def __init__(self, height, subtype):
            self.height = height
            self.subtype = subtype

    class Pyrocumulus(Cloud):
        ''' An volcanic subclass of cloud '''
        base = "Ash"

    pyro = Pyrocumulus(height="any", subtype="volcanic")
    print pyro.base


def question_2():
    ''' Can I add additional variables to a constructor in a subclass? '''

    class Cloud(object):
        ''' A class describing cloud properties '''
        base = "CCN"  # Cloud Condensation Nuclei

        def __init__(self, height, subtype):
            self.height = height
            self.subtype = subtype

    class Ice(Cloud):
        ''' An ice subclass of cloud '''
        def __init__(self, height, subtype, h2oState):
            self.h2oState = h2oState
            Cloud.__init__(self, height, subtype)

    ice_cloud = Ice(height="any", subtype="cold", h2oState="iced")
    print ice_cloud.h2oState


def question_3():
    ''' Can you run a class method in a subclass? '''

    class Cloud(object):
        ''' A class describing cloud properties '''
        base = "CCN"  # Cloud Condensation Nuclei

        def __init__(self, height, subtype):
            self.height = height
            self.subtype = subtype

        def generate_name(self):
            ''' Generates the name of the cloud based on properties '''
            print "The name of this cloud is {height}-{subtype}".format(
                  height=self.height, subtype=self.subtype)

    class Ice(Cloud):
        ''' An ice subclass of cloud '''
        pass

    q3 = Ice(height="cirro", subtype="status")
    q3.generate_name()


def question_4():
    '''
    Can I print only the subclasses are instances of a certain superclass?
    '''

    class Cloud(object):
        ''' A class describing cloud properties '''
        base = "CCN"  # Cloud Condensation Nuclei

        def __init__(self, height, subtype):
            self.height = height
            self.subtype = subtype

    class Ice(Cloud):
        ''' An ice subclass of cloud '''
        def __init__(self, height, subtype, h2oState):
            self.h2oState = h2oState
            Cloud.__init__(self, height, subtype)

    class Liquid(Cloud):
        ''' A liquid subclass of cloud '''
        def __init__(self, height, subtype, h2oState):
            self.h2oState = h2oState
            Cloud.__init__(self, height, subtype)

    class Fog(Liquid):
        ''' A fog subclass of liquid'''
        pass

    class Cirrostratus(Ice):
        ''' A cirrostratus subclass of ice '''
        pass

    class Nimbostratus(Liquid):
        ''' A nimbrostratus subclass of liquid '''
        pass

    fog = Fog(height="surface", subtype="other", h2oState="liquid")
    cs = Cirrostratus(height="high", subtype="flat", h2oState="ice")
    nbs = Nimbostratus(height="variable", subtype="rain", h2oState="liquid")
    cloud_types = [fog, cs, nbs]
    for cloud in cloud_types:
        if isinstance(cloud, Ice):
            print type(cloud).__name__


if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    question_4()

'''
Output:
Ash # Q1
iced # Q2
The name of this cloud is cirro-status # Q3
Cirrostratus #Q4
'''
