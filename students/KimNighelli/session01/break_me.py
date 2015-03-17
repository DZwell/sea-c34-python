import datetime
#I use datetime all the time at work to deal with date format and timezone issues.

def syntax_error(some_date, some_fmt):
    return datetime.strptime()

def attribute_error(some_date, some_fmt):
    return datetime.strpptime()

def type_error(string, some_float):
    return string + some_float

def name_error():
    return x

#Syntax Error
# A syntax error occurs when Python syntax is incorrect. The syntax
# below is incorrect in the fmt block, there should not be three quotes.
syntax_error("2015-03-16", "%Y-"%m-%d")

#Error Received:
#  File "break_me.py", line 19
#    syntax_error("2015-03-16", "%Y-"%m-%d")
#                                       ^
#SyntaxError: invalid syntax
