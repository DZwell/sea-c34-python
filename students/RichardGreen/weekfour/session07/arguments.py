'''Argument Functions
Richard Green
Foundations 2 Python'''

# Advanced Argument Passing


def f0(x, y=0, z=2):
    '''Question what is the sum and product of the following
    integers? Description: This function accepts two numbers to add and
    multiples its sum. It emphaszies the use of argument passing.
    This will run with or without a z argument because a default
    has been provided Arguments: 3 integers. 2 mandatory the third
    optional'''
    return(x + y * z)

if __name__ == "__main__":

    print(f0(5, y=3, z=2))
    print(f0(1, y=2))
