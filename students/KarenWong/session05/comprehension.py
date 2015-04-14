def devowel():
    """
    How to devowel a sentence using list comprehensions?
    """
    sentence = "I want a big chessburger"
    vowels = "aeiou"
    nonvowels = ''.join(l for l in sentence if l not in vowels)
    print nonvowels


def find_vowel():
    """
    How to find all the vowels in a string?
    """
    s = "I want a soy latte"
    vowels = set("aeiou")
    print {let for let in s if let in vowels}


def update_dict():
    """
    How to update a dictionary using dict comprehension?
    """
    my_dict = {"first name": "Karen"}
    my_dict = {"last name": "Wong" for key, value in my_dict.items()}
    print my_dict

devowel()
find_vowel()
update_dict()
