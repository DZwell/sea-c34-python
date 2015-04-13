# 1. Can I have two ifs?

q1 = [x * 2 for x in range(6) if (not x % 2) or (not x % 1)]

print q1

# Answer: Yes
# [0, 2, 4, 6, 8, 10]

# Can I loop for more than 2 times?

q2 = [x + y + z for x in range(3) for y in range(5, 7) for z in range(3)]

print q2

# Answer: Yes
# [5, 6, 7, 6, 7, 8, 6, 7, 8, 7, 8, 9, 7, 8, 9, 8, 9, 10]


# Can I use while loop?

q3 = [x ** 2 while x < 5]

# Answer: No
# SyntaxError: invalid syntax
