#!/usr/bin/python

import os, sys
"""Is it possible to print a directory?"""

path = "/Desktop/codefellowfiles/sea-c34-python/sea-c34-python/students/\
        JackSneed/session04"
dirs = os.listdir(path)

for i in dirs:
   print i
