#!/usr/bin/env python

"""
===============================================================================
file: html_render.py
===============================================================================
Programmer: Jeffrey Mendiola
Date: 04/08/2015
Course: SEA-C34: Foundations II: Python
Time: MW 7:00pm - 9:00pm
Instructor: Paul Pham
Task: #17 HTML Renderer
Description:
     This program generates and renders html pages in a nicely indented format.
===============================================================================
"""


class Element(object):
    """Element class renders an html element (xml element)"""
    tag_name = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        """Element content and attribute initialization"""
        self.attributes = kwargs
        self.attr = ""
        for attr_key, attr_val in self.attributes.items():
            self.attr += " {key}=\"{val}\"".format(key=attr_key, val=attr_val)

        if content:
            self.children = [content]
        else:
            self.children = []

    def append(self, string):
        """append a string to element tag"""
        self.children.append(string)

    def render(self, file_out, line=""):
        """renders the tag and the strings in the content"""
        file_out.write(line + "<" + self.tag_name + self.attr + ">\n")

        for child in self.children:
            try:
                child.render(file_out, self.indent + line)
            except AttributeError:
                file_out.write(self.indent + line + child + "\n")

        file_out.write(line + "</" + self.tag_name + ">\n")


class Html(Element):
    """
    document type declaration: <!DOCTYPE>
    element: <html>
    """
    tag_name = "html"
    doctype_decl = "<!DOCTYPE>\n"

    def render(self, file_out, line=""):
        """render document type declaration"""
        file_out.write(self.doctype_decl)
        Element.render(self, file_out, line="")


class Body(Element):
    """element: <body>"""
    tag_name = "body"


class P(Element):
    """element: <p>"""
    tag_name = "p"


class Head(Element):
    """element: <head>"""
    tag_name = "head"


class OneLineTag(Element):
    """OneLineTag class renders everything on one line"""
    def render(self, file_out, line=""):
        file_out.write(line + "<" + self.tag_name + self.attr + ">")

        for child in self.children:
            try:
                child.render(file_out, line)
            except AttributeError:
                file_out.write(child)

        file_out.write("</" + self.tag_name + ">\n")


class Title(OneLineTag):
    """element: <title>"""
    tag_name = "title"


class SelfClosingTag(Element):
    """SelfClosingTag class renders a self closing tag"""
    def render(self, file_out, line=""):
        file_out.write(line + "<" + self.tag_name + self.attr + " />\n")


class Hr(SelfClosingTag):
    """element: <hr />"""
    tag_name = "hr"


class Br(SelfClosingTag):
    """element: <br />"""
    tag_name = "br"


class A(OneLineTag):
    """element: <a>"""
    tag_name = "a"

    def __init__(self, link, content, **kwargs):
        """override init to accept a link"""
        self.link = link
        self.content = content
        Element.__init__(self, content=None, href=link, **kwargs)


class Ul(Element):
    """element: <ul>"""
    tag_name = "ul"


class Li(Element):
    """element: <li>"""
    tag_name = "li"


class H(OneLineTag):
    """element: <h>"""
    tag_name = "h"

    def __init__(self, h_size, content=None, **kwargs):
        """override init to accept header size (i.e h1, h2, ...)"""
        self.tag_name = self.tag_name + str(h_size)
        Element.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):
    """element: <meta>"""
    tag_name = "meta"
