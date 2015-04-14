# 1. Can I use comprehensions in Anonymous functions?

s = "a not very long string"
vowels = set('aeiou')

f = lambda s, vowels: {let for let in s if let in vowels}

print f(s, vowels)

# 2. Can I use map reduce the same time?
l = [2, 5, 7, 12, 6, 4]
print reduce(lambda x, y: x*y, map(lambda x: x * 2 + 10, l))

# Anwser:Yes
# 90478080

# 3. both f and g are function. Are they pointing to the same object?

f = lambda x, y: x+y


def g(x, y):
    return x+y

print f is g
# Answer: False
