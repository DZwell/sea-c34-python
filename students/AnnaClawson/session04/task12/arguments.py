"""Question 1. What happens when you set default values
and then change the variable inside a function? This does not change the value.
"""

y = 4


def fun(x=y):
    y = 5
    print(u"x is: %s" % x)
fun()

"""Question 2. How do you get parameters out of the function?
You can pull them into a dictionary usiing the *args and **kwargs key words.
There can be any number of positional and optional arguments. However, keyword
args should follow after non-keyword ones.
"""

"""This will not work:
def print_myparams(*args, **kwargs):
    print(u"positional arguments: %s" % unicode(args))
    print(u"optional arguments: %s" % unicode(kwargs))

print_myparams(name = "Anna", age = 20, 6, 7, place = "Seattle")
"""

"""This will work:"""


def print_myparams(*args, **kwargs):
    print(u"positional arguments: %s" % unicode(args))
    print(u"optional arguments: %s" % unicode(kwargs))

print_myparams(6, 7, name="Anna", age=20, place="Seattle")

"""Question 3. How can you use dictionary keys with string formatting?
The string format method and using the keyword arguments symbol ** allow to do
this, as the following example demonstrates."""

mydict = {'name': 'Zoya', 'age': 9, 'grade': 3}
print(
    u'Hello, my name is {name}, I am {age} years old, and my grade is{grade}'
    .format(**mydict)
)
