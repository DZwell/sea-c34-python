# -*- coding: utf-8 -*-
import sys

lang = "English"

if (len(sys.argv) > 1):
    lang = sys.argv[1]

if (lang == "English"):
    print("Hello, world!")

elif (lang == "Vietnamese"):
    print(u"xin chào thế giới !")

# Add elif branches here to handle other languages!

else:
    raise RuntimeError("This shouldn't happen!")

<<<<<<< HEAD
1++

=======
>>>>>>> 6d22b5c1ca727e30378ed07ffb7a9fc067aa46d3

