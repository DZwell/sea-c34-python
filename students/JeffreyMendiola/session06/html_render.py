#!/usr/bin/env python

# =============================================================================
# Step 1
# =============================================================================


class Element(object):
    """
    Step 1: Create an Element class for rendering an html element (xml element)
    """
    tag_name = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):

        self.attributes = kwargs
        self.attr = ""
        for attr_key, attr_val in self.attributes.items():
            self.attr = " {key}=\"{val}\"".format(key=attr_key, val=attr_val)

        if content:
            self.children = [content]
        else:
            self.children = []

    def append(self, string):
        self.children.append(string)

    def render(self, file_out, line=""):
        file_out.write(line + "<" + self.tag_name + self.attr + ">\n")

        for child in self.children:
            try:
                child.render(file_out, self.indent + line)
            except AttributeError:
                file_out.write(self.indent + line + child + "\n")

        file_out.write(line + "</" + self.tag_name + ">\n")

# =============================================================================
# Step 2
# =============================================================================


class Html(Element):
    tag_name = "html"
    doctype_decl = "<!DOCTYPE>\n"

    def render(self, file_out, line=""):
        file_out.write(self.doctype_decl)
        Element.render(self, file_out, line="")


class Body(Element):
    tag_name = "body"


class P(Element):
    tag_name = "p"

# =============================================================================
# Step 3
# =============================================================================


class Head(Element):
    tag_name = "head"


class OneLineTag(Element):
    def render(self, file_out, line=""):
        file_out.write(line + "<" + self.tag_name + self.attr + ">")

        for child in self.children:
            try:
                child.render(file_out, line)
            except AttributeError:
                file_out.write(child)

        file_out.write("</" + self.tag_name + ">\n")


class Title(OneLineTag):
    tag_name = "title"

# =============================================================================
# Step 4
# Edit Element to accept a set of attributes as keywords to the constructor
# =============================================================================

# =============================================================================
# Step 5
# =============================================================================


class SelfClosingTag(Element):
    def render(self, file_out, line=""):
        file_out.write(line + "<" + self.tag_name + self.attr + " />\n")


class Hr(SelfClosingTag):
    tag_name = "hr"


class Br(SelfClosingTag):
    tag_name = "br"

# =============================================================================
# Step 6
# =============================================================================


class A(OneLineTag):
    tag_name = "a"

    def __init__(self, link, content, **kwargs):
        self.link = link
        self.content = content
        Element.__init__(self, content=None, href=link, **kwargs)

# =============================================================================
# Step 7
# =============================================================================


class Ul(Element):
    tag_name = "ul"


class Li(Element):
    tag_name = "li"


class H(OneLineTag):
    tag_name = "h"

    def __init__(self, h_size, content, **kwargs):
        self.tag_name = self.tag_name + str(h_size)
        Element.__init__(self, content, **kwargs)
