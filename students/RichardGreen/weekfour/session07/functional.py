'''Argument Functions
Richard Green
Foundations 2 Python'''

# Functional programming

x = range(0, 20)

# lambda


def funct_filter(x):
    '''Question:How can I use lambda to filter a data set to
    only look for those values not divisible by 2? Arguments: a string
    (range of integers)'''
    return filter(lambda x: x % 2, x)

if __name__ == "__main__":

    print(funct_filter(range(2)))
