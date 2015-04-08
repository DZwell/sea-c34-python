#!/usr/bin/env python
class Element(object):
    """ A class that renders to HTML per the class exercise
    """
    openingtag = '<>'
    closingtag = '</>'
    indent = '    '

    def __init__(self, content=None):
        if content:
            self.children = [content]
        else:
            self.children = []

    def append(self, element_to_append):
        self.children.append(element_to_append)

    def render(self, file_out, ind=""):
        file_out.write("\n" + ind + self.openingtag)
        for child in self.children:
            try:
                child.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write("\n")
                file_out.write(ind + self.indent + child)
        file_out.write("\n" + ind + self.closingtag)


class P(Element):

    openingtag = "<p>"
    closingtag = "</p>"


class Html(Element):

    openingtag = "<html>"
    closingtag = "</html>"


class Body(Element):

    openingtag = "<body>"
    closingtag = "</body>"
