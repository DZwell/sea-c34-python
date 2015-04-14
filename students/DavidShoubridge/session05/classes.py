def change_class_data():
    """
    Can I change class specific data without changing instance specific data \
    after the object has been created.
    """
    class Animal(object):
        num_legs = 4
        num_ears = 2

        def __init__(self, name, sound):
            self.name = name
            self.sound = sound

    mutant_dog = Animal("Bowsario", "KOWABUNGAAAAA!")
    print(mutant_dog.num_legs, mutant_dog.name, mutant_dog.sound)

    mutant_dog.num_legs = 5
    print(mutant_dog.num_legs, mutant_dog.name, mutant_dog.sound)

change_class_data()
