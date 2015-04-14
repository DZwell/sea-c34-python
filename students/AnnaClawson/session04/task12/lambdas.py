"""Question 1. What are lambdas? They are anonymous functions that don't need
to be defined. The advantage of using them is when you need to call a function
as soon as you create it and do not need to store it in memory for the rest of
the program execution."""

f = lambda x, y: x + y
print f("I love ", "Python")

"""Question 2. What's a good way to use lambdas? One way to use lambdas is
to do a one-time manipulation on a sequence of objects such, as map a function
onto a list."""

list = [5, 4, 2, 9, 15]
print map(lambda x: x * 5, list)
print filter(lambda x: not x % 5, list)

"""Question 3. What's a good use of reduce function? One case is when you have
a nested list that you would like to reduce into a non-nested list."""
list = [[10, 45, 20], [11, 74, 35], [5, 4, 3]]
print reduce(lambda x, y: x + y, list)
