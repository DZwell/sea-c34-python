# 1. For the list1, list2 mutate example, I think list1[1] and list[2] from
# stack memory are maping to the same object on heap memoy. I will like to
# simple example to prof it. This can make sure I understand it right.
list1 = [1, 2]
list2 = list1
print list1
print list2
print list2 is list1

list1.append(3)
print list1
print list2
print list2 is list1

# 2. Function arguments in variables for sets?
# sets cannot be positional arguments or keyword arguments
# What is going to happen?
myset = set([1, 3, 2])


def f(x, y, z):
    print "x is %s, y is %s, z is %s" % (x, y, z)

f(myset)
# TypeError
f(*myset)
# It works. And the set got sorted.
# x is 1, y is 2, z is 3
f(**myset)
# TypeError
f(***myset)
# SyntaxError

# Anwser: We can use set as tuple but it get sorted.

# 3. Sets are mutatable. If I use "set" operation from math class, what is
# going to happen?

pythoni = "python" + "i"
python_set = set(pythoni)
marathon = "marathon"
marathon_fset = set(marathon)

union = python_set.union(marathon_fset)
print union

python_set.remove('i')
print python_set
print union

# Answer: different objects.
