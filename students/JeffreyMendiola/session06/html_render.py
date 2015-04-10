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

        if content:
            self.children = [content]
        else:
            self.children = []

    def append(self, string):
        self.children.append(string)

    def render(self, file_out, line=""):
        file_out.write(line + "<" + self.tag_name + ">\n")
        for attr_key, attr_val in self.attributes.items():
            file_out.write(
                " {key}=\"{value}\"".format(key=attr_key, value=attr_val))

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
        file_out.write(line + "<" + self.tag_name + ">")

        for child in self.children:
            try:
                child.render(file_out, line)
            except AttributeError:
                file_out.write(child)

        file_out.write("</" + self.tag_name + ">\n")


class Title(OneLineTag):
    tag_name = "title"
