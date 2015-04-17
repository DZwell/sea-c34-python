'''
This is the program that I'd like to test with the testing.py
program.
'''


def float_division(v1, v2):
    ''' Some tests on the values to complete float division '''
    try:
        return float(v1)/float(v2)
    except ZeroDivisionError:
        return "You cannot divide by 0"

if __name__ == "__main__":
    print float_division(0, 1)
    print float_division(1, 0)
    print float_division(2, 4)
    print float_division(4, 2)
    print float_division(4, 4)
