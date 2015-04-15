#!/usr/bin/env python
class Element(object):
    """ The main abstract class that renders to HTML per the requirements
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


class OneLineTag(Element):
    """Abstract class for one line tags"""
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


class SelfClosingTag(Element):
    """Abstract class for Self Closing Tags"""
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
        file_out.write(" /" + self.c)


class P(Element):
    """Paragraph tag class"""
    openingtag = "<p"
    closingtag = "</p"


class Html(Element):
    """HTML tag class"""
    openingtag = "<!DOCTYPE html> \n <html"
    closingtag = "</html"


class Body(Element):
    """Body tag class"""
    openingtag = "<body"
    closingtag = "</body"


class Ul(Element):
    """Unordered list tag class"""
    openingtag = "<ul"
    closingtag = "</ul"


class Li(Element):
    """Ordered List tag class"""
    openingtag = "<li"
    closingtag = "</li"


class Title(OneLineTag):
    """Title tag class which inherits from OneLineTag"""
    openingtag = "<title"
    closingtag = "</title"


class Head(Element):
    """Head tag class"""
    openingtag = "<head"
    closingtag = "</head"


class Meta(SelfClosingTag):
    """Meta tag class"""
    openingtag = '<meta'


class A(OneLineTag):
    """A tag class"""
    openingtag = "<a"
    closingtag = "</a"

    def __init__(self, link, content=None):
            OneLineTag.__init__(self, content, href=link)


class Hr(SelfClosingTag):
    """Hr tag class"""
    openingtag = "<hr"


class Br(SelfClosingTag):
    """Br tag class"""
    openingtag = "<br"


class H(OneLineTag):
    """Header tag class"""
    openingtag = "<h"
    closingtag = "</h"

    def __init__(self, number, content=None, **kwargs):
            self.openingtag = self.openingtag + str(number)
            self.atts = kwargs

            if content:
                self.children = [content]
            else:
                self.children = []
