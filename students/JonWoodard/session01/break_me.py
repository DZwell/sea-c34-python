"""
Create a module with four functions.
Each function will generate a built in error.
Resolve the errors in each function.
"""


def is_a_witch(answer="yes"):
    # How do we tell if she is a witch?
    witch = "Burn her!"
    answer = raw_input("Is she made of wood?\n-> ")
    # if answer.lower[0] == 'y':
    """
    This gives a TypeError:
    'builtin_function_or_method' object has no attribute '__getitem__'
    """
    if answer[0] == 'y':
        print(witch)
    else:
        print("Not a witch")
    """
    This prints 'witch' if the first letter in the user input is 'y'.
    It treats 'Y' as a 'no' answer.
    """


def witch_attributes():
    she = []
    # she.append "funny nose"
    """This is a syntax error due to missing '()'."""
    she.append("funny nose")
    she.append("pointy hat")
    she.append("turned me into a newt")
    print(she)


def made_of_wood():
    # How do you know if she's made of wood?
    # if 'Y' in raw_input(
    #    "Does she weigh the same as a duck?\n[Y]es or [N]o\n-> "
    #    ):
    # weight.append("duck")
    # if "duck" in weight:
    #    print("She's a witch!")
    """This gives a NameError: global name 'weight' is not defined."""
    weight = []
    if 'Y' in raw_input("Does she weigh the same as a duck?\n"
                        "[Y]es or [N]o\n-> "):
        weight.append("duck")
    if "duck" in weight:
        print("She's a witch!")


def witch():
    witch_dict = {1: "funny nose", 2: "pointy hat", 3: "warts", 4: "cat"}
    witch_list = []
    for key in witch_dict:
        witch_list.append(witch_dict[key])
    # for item in witch_list:
    #    item.sort
    """AttributeError: 'str' object has no attribute 'sort'"""
    print(sorted(witch_list))
