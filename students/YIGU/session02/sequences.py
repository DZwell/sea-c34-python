#session02 Task5 sequences.py

w="harlem shake"
"""question1:what is the length of 'harlem shake'?"""

q1=len(w)
print q1
#answer is 12

"""question2: what is backward of 'harlem shake'?"""

for i in range(len(w)):
	i=i+1
	print w[-i]
"""answer is
e
k
a
h
s

m
e
l
r
a
h
"""

"""question3: Please save answer from q2 as a single mutable object list"""
q3=[]
for i in range(len(w)):
	i=i+1
	q3.append(w[-i])

print q3
#answer is ['e', 'k', 'a', 'h', 's', ' ', 'm', 'e', 'l', 'r', 'a', 'h']