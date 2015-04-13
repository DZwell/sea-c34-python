# 3 questions

# Q1 WHOA seriously we can do this stuff in one line now?

listy = ["Apples", "Pears", "Oranges", "Peaches"]
list2 = ["Apples", "Oranges", "Grapes"]
new_list = ["yum" for fruit in listy for fruit in list2]
print new_list

# haah! ok, what did that just do? I might need to see this in a real world
# application...

# Q2: could this work for our homework mailroom project?

a_sequence = {"mary": 40, "josh": 20, "cassie": 100}
# new_dict = {key: value for key, value in a_sequence}
# print new_dict

# returns "too many values to unpack", why? let's try a range like the example:

print {i: "I have %i potato" % i for i in range(10)}
# print {"Donor name: %s" % s for keys in a_sequence.keys()}

# Q3: ok let's try lists instead...

list = [0, 2, 4, 6, 8, 10]
new_list = [(x + 2) for x in list if (x > 5)]
print new_list

# that works!
