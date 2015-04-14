# Rewrite: the first 3 numbers are: %i, %i, %i"%(1,2,3)
# for an arbitrary number of numbers...

def makestring(list):
    print "the first three numbers are" + str(list[0:3])

list1 = [1, 2, 3]
list2 = [2, 3, 6, 7]

# print makestring(mylist)

def crazystring(list):
    print "the first three numbers are %i, %i, %i" % tuple(list[0:3])

crazystring(list1)
crazystring(list2)

print makestring(list1)
print makestring(list2)


def first_three(numbers):
    a = numbers[:3]
    print a
    print('The first three numbers are %i, %i, %i') % a

first_three((4, 5, 6, 7, 8))

# for marco polo:
# open text file
# read the whole text, concatenate the lines to make one giant string.
# split into words, using " " to divvy into words.
# store in word list
# create empty dictionary
# a = current word, b = current word + 1, c = current word + 2
# make new dictionary: keys are the three words, values are the # of occurances
# for each set of three words, if present, add them.
# if tuple already present, increase the value by 1

import io

f = io.open("marco-polo.txt", encoding="utf-8")
#dir(f)
text_string = f.readlines()
#help(f.readlines)
type(text_string)
text = "".join(text_string)
len(text)
words = text.split()
len(words)

D = {}
for (i, word in enumerate(words):
    a = word
    b = words[i+1]
    c = words[i+2]
    d = 0
    if ((a,b,c) in D.keys()):
        d=D[(a,b,c)]


