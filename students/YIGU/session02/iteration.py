#session02 Task5 iteration.py

w="harlem shake"
"""question1: for loop-use for loop to print 'harlem shake' letter by letter"""

for i in w:
	print (i)

"""
answer is
h
a
r
l
e
m

s
h
a
k
e
"""

"""question2: Write q1 with while loop"""
i=0
while i < len(w):
	print w[i]
	i=i+1

"""
answer is
h
a
r
l
e
m

s
h
a
k
e
"""
""" question3: Write q2 with a break"""
i=0
t=True
while t:
	if i ==len(w):
		break
	print w[i]
	i=i+1

"""
answer is
h
a
r
l
e
m

s
h
a
k
e
"""