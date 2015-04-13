# 3 questions

# Q1: mapping looks fun!

l = ["Mary", "Josh", "Cassie"]


def thx(x):
    print "thanks, %s!" % x

map(thx, l)
print "a map is a " + str(type(map))

thxlist = map(lambda x: "thanks, %s!" % x, l)
print thxlist

# the second version created a list?

print "the second version created a " + str(type(thxlist))

# Q2: what happens if we use this w/ a dictionary?

d = {"Mary": 20, "Josh": 50, "Cassie": 100}
l = d.keys
print l


def thx2(dict):
    try:
        print "thanks, %s, for donating %i!" % dict.keys(), dict.values()
    except:
        print "well, that didn't work."

map(thx2, d)

# hmmm guess not.
# Q3 let's try filtering with a dictionary and a list:

newlist = filter(lambda x: x > 30, d.values())
print newlist
# this works! dang!

newlist2 = filter(lambda x: x != "Josh", l)
print newlist2
# this doesn't work whyyyyyyyy ? Says "TypeError:
# 'builtin_function_or_method' object is not iterable"
