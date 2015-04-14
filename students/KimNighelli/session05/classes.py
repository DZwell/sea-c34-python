'''
This is for Task 16 - Investigate Session 6 - Classes

In this program, I will pose a variety of question that I had while
reviewing the session 6 slides on subclasses. Each question will be posed
in the docstring of the function corresponding to the question.

Kimberlee Nighelli 5 April 2015
'''


def pet_store():
    '''
    Can I use a class and methods to help craft some advertisements
    for some pets in a pet store?
    '''

    class Pet():
        ''' A class about the pets in a store '''

        def __init__(self, name, species, age, friendly):
            self.name = name
            self.species = species
            self.age = age
            self.friendly = friendly

        def advertisement(self):
            ''' Prints out an ad for each animal '''
            print "{name} is a {age} year old {species} in " \
                  "need of a home. Are they friendly? {friendly}, "\
                  "and they are in need of a lot of love.".format(
                      name=self.name, age=self.age, species=self.species,
                      friendly=self.friendly)

    penny = Pet("Penny", "Cat", 14, "Yes")
    gary = Pet("Gary", "Lizard", 3, "No")
    henry = Pet("Henry", "Cat", 1, "No")
    jake = Pet("Jake", "Dog", 4, "Yes")
    charlotte = Pet("Charlotte", "Tarantula", 3, "Maybe")
    craig = Pet("Craig", "Mouse", 9, "Yes")
    steven = Pet("Steven", "Dog", 1, "Yes")

    animals = [penny, gary, henry, jake, charlotte, craig, steven]
    for animal in animals:
        animal.advertisement()

if __name__ == "__main__":
    pet_store()

'''
Output
Penny is a 14 year old Cat in need of a home. Are they friendly? \
        Yes, and they are in need of a lot of love.
Gary is a 3 year old Lizard in need of a home. Are they friendly? \
        No, and they are in need of a lot of love.

etc.
'''
