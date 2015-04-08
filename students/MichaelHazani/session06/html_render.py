#!/usr/bin/env python
class Element(object):
    """ A class that renders to HTML per the class exercise
    """
    tag = 'html'
    indent = '    '

    def __init__(self, content=None):
        if content:
            self.content += content
        else:
            self.content = ""

    def append(self, element_to_append):
        self.content += (self.indent + element_to_append)

    def render(self, file_out, ind=""):
        outstring = (self.indent + "<" + self.tag + ">\n"
                     + self.indent + self.content + "\n"
                     + self.indent + "</" + self.tag + ">")
        file_out.write(outstring)
