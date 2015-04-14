def function_builder(n):
    l = []
    for i in range(n + 1):
        l.append(lambda x, y=i: x + y)
    return l

the_list = function_builder(5)

print the_list[0](2) == 2
print the_list[1](2) == 3
print the_list[5](1)
