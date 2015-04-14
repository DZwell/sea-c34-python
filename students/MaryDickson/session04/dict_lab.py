mydict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print mydict
mydict.pop("cake")
print mydict
mydict["fruit"] = "mango"
print mydict
print mydict.keys()
print mydict.values()
print "cake" in mydict.keys()
print "mango" in mydict.values()

# using a dict constructor and zip build a dictionary of
# numbers from zero to fifteen
# and the hexadecimal equivalent (string is fine).


def hexnums():
    nums = range(0, 16)
    hexs = range(0, 10) + ["A", "B", "C", "D", "E", "F"]
    list = dict(zip(nums, hexs))
    return list

print hexnums()

newdict = mydict.copy()
print newdict

# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of a's in each value.


def changevals(dict):
    thisdict = {}
    for k, v in dict.items():
        newdict[k] = v.count("a")
    return thisdict

print changevals(newdict)
print "new dict:" + str(newdict)
print "old dict:" + str(mydict)

"""
Create sets s2, s3 and s4 that contain numbers from zero through twenty,
divisible 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
"""

s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))
print s2, s3, s4


def issubset(set1, set2):
    answer = True
    for x in set1:
        if x in set2:
            continue
        else:
            answer = False
            return answer
    return answer

print "Is s3 a subset of s2?"
print issubset(s3, s2)
print s3.issubset(s2)
print "Is s4 a subset of s2?"
print issubset(s4, s2)


pythonset = set("Python")
pythonset.update(["i"])
print pythonset

"""
Create a set with the letters in 'Python' and add 'i' to the set.
Create a frozenset with the letters in 'marathon'
display the union and intersection of the two sets.
"""

marathonset = frozenset('marathon')
print "sets combined:"
print pythonset.union(marathonset)
print "common letters:"
print pythonset.intersection(marathonset)
