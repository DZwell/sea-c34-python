"""Question 1. Can I combine string methods and list comprehensions to alter
a list? In the example below, we capitalize each word in the list.
"""

my_list = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']
new_list = [word.capitalize() for word in my_list]
# print(new_list)

"""Question 2. Can I use list comprehensions to concatenate two lists?
The example below demonstrates it.
"""

list1 = ['Anna', 'Keith', 'John', 'Lucy', 'Linda']
list2 = ['Swanson', 'Smith']
new_list = [[a + " " + b for a in list1] for b in list2]
# print(new_list)

"""Question 3. Can I update one dictionary from another using comprehensions?
The example below shows that if keys in the two dictionaries match
the values in dict1 get replaced by values from dict2.
"""

dict1 = {
    'Shelly': 5,
    'Laura': 22,
    'Dan': 17,
    'Anna': 2
}
dict2 = {
    'Anna': 42,
    'Keith': 55,
    'Lucy': 30,
    'Margaret': 21
}

new_dict = {k: v for d in (dict1, dict2) for k, v in d.iteritems()}
print(new_dict)
