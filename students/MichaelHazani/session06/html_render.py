#!/usr/bin/env python
class Element(object):
    """ A class that renders to HTML per the class exercise
    """
    openingtag = '<'
    closingtag = '</'
    indent = '    '
    c = ">"

    def __init__(self, content=None, **kwargs):

        self.atts = kwargs

        if content:
            self.children = [content]
        else:
            self.children = []

    def append(self, element_to_append):
        self.children.append(element_to_append)

    def render(self, file_out, ind=""):
        file_out.write("\n" + ind + self.openingtag)
        for atri, val in self.atts.items():
            file_out.write(" %s=\"%s\"" % (atri, val))
        file_out.write(self.c)
        for child in self.children:
            try:
                child.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write("\n")
                file_out.write(ind + self.indent + child)
        file_out.write("\n" + ind + self.closingtag + self.c)


class P(Element):

    openingtag = "<p"
    closingtag = "</p"


class Html(Element):

    openingtag = "<html"
    closingtag = "</html"


class Body(Element):

    openingtag = "<body"
    closingtag = "</body"


class OneLineTag(Element):

    def render(self, file_out, ind=""):
        file_out.write("\n" + ind + self.openingtag)
        for atri, val in self.atts.items():
            file_out.write(" %s=\"%s\"" % (atri, val))
        file_out.write(self.c)
        for child in self.children:
            try:
                child.render(file_out)
            except AttributeError:
                file_out.write(child)
        file_out.write(self.closingtag + self.c)


class Title(OneLineTag):

    openingtag = "<title"
    closingtag = "</title"


class Head(Element):

    openingtag = "<head"
    closingtag = "</head"


class SelfClosingTag(Element):

    def render(self, file_out, ind=""):
        file_out.write("\n" + ind + self.openingtag)
        for atri, val in self.atts.items():
            file_out.write(" %s=\"%s\"" % (atri, val))
        for child in self.children:
            try:
                child.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write("\n")
                file_out.write(ind + self.indent + child)


class A(OneLineTag):
    openingtag = "<a"
    closingtag = "</a"

    def __init__(self, link, content=None):
            OneLineTag.__init__(self, content, href=link)


class Hr(SelfClosingTag):
    openingtag = "<hr />"


class Br(SelfClosingTag):
    openingtag = "<br />"
