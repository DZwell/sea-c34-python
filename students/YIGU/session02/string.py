#session02 Task5 string.py

w="harlem shake"

"""queston1: print "harlem shake" in upper case 3 times."""
print w.upper()*3
#answer is HARLEM SHAKEHARLEM SHAKEHARLEM SHAKE

"""question2: Password maker. Ask user for password input and print out recommend password."""

i=raw_input("please write down your password-->")
print "%s is not secure. How about 'PassWord' as your password?" %i
#answer is lala is not secure. How about 'PassWord' as your password?

"""question3: replace "harlem shake" with "~" """

q3="~".join(w.split(' '))

#answer is harlem~shake