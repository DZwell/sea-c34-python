"""Can paths be used for anything other than opening a file?"""
import os
# we can print the current working directory
cwd = os.getcwd()
print "The current working directory is " + cwd
# we can see all the files in that directory
print os.listdir(cwd)
