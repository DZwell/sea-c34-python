#!/usr/bin/env python
"""
This is for Task 17 - HTML Renderer.

In this task, I create an API to render a nicely indented
html page.

Kimberlee Nighelli - 6 April 2015
"""


class Element(object):
    ''' The main superclass, takes in some Element object '''
    tag = ""
    indent = "    "

    def __init__(self, content=None, **attrs):
        self.content = []
        self.attributes = attrs

        if content is not None:
            self.content.append(content)

    def append(self, string):
        ''' Adds another string to the existing content '''
        self.content.append(string)

    def render(self, file_out, ind=""):
        ''' Renders the output to a file '''
        file_out.write(ind)
        file_out.write("<%s" % (self.tag))
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"' % (key, value))
        file_out.write(">\n")
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind+self.indent)
            else:
                file_out.write(ind+self.indent)
                file_out.write(item)
                file_out.write("\n")
        file_out.write(ind)
        file_out.write("</%s>\n" % (self.tag))


class Html(Element):
    ''' An HTML subclass of Element for the HTML tag '''
    tag = "html"

    def render(self, file_out, ind=""):
        '''
        Overrides Element's render function to write the DOCTYPE
        file before the tag. Renders the output to a file
        '''
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, ind="")


class Body(Element):
    ''' A body subclass of Element for the body tag '''
    tag = "body"


class P(Element):
    ''' A p subclass of Element for the p tag'''
    tag = "p"


class Head(Element):
    ''' A head subclass of Element for the head tag '''
    tag = "head"


class OneLineTag(Element):
    '''
    A subclass of Element. Overrides Element's render function
    to render the content on one line'''

    def render(self, file_out, ind=""):
        '''
        Overrides Element's render function to
        render the content on one line
        '''
        file_out.write(ind)
        file_out.write("<%s" % (self.tag))
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"' % (key, value))
        file_out.write(">")
        for item in self.content:
            file_out.write(item)
        file_out.write("</%s>\n" % (self.tag))


class Title(OneLineTag):
    ''' A title subclass of OneLineTag for the title tag '''
    tag = "title"


class SelfClosingTag(Element):
    '''
    A subclass of Element to render self-closing tags
    like <hr /> and <br />
    '''

    def __init__(self, **attrs):
        ''' Note: only attributes are passed in '''
        self.attributes = attrs

    def render(self, file_out, ind=""):
        '''
        Overrides Element's render function to write
        self-closing tags
        '''
        file_out.write(ind)
        file_out.write("<%s" % (self.tag))
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"' % (key, value))
        file_out.write(" />\n")


class Hr(SelfClosingTag):
    ''' A hr subclass of SelfClosingTag for the hr tag '''
    tag = "hr"


class Br(SelfClosingTag):
    ''' A br subclass of SelfClosingTag for the br tag '''
    tag = "br"


class Meta(SelfClosingTag):
    ''' A meta subclass of SelfClosingTag for the meta tag '''
    tag = "meta"


class A(Element):
    ''' An a subclass of Element for the a tag '''
    tag = "a"

    def __init__(self, link, content):
        Element.__init__(self, content, href=link)


class Ul(Element):
    ''' A ul subclass of Element for the ul tag '''
    tag = "ul"


class Li(Element):
    ''' A li subclass of Element for the li tag '''
    tag = "li"


class H(OneLineTag):
    ''' An h subclass of OneLineTag for the h tag '''

    def __init__(self, level, content, **attrs):
        OneLineTag.__init__(self, content, **attrs)
        self.level = level
        self.tag = "h%d" % (self.level)
