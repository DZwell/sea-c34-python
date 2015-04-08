#!/usr/bin/env python


class Element(object):
    """
    Step 1: Create an Element class for rendering an html element (xml element)
    """
    tag_name = "html"
    indent = "    "

    def __init__(self, content=None):
        self.content = self.indent + str(content) if content else ""

    def append(self, string):
        self.content += (
            "{indent}{string}\n".format(indent=self.indent, string=string)
        )

    def render(self, file_out, line=""):
        file_out.write(
            "{indent}<{tag}>\n"
            "{indent}{content}"
            "{indent}</{tag}>"
            .format(indent=line, tag=self.tag_name, content=self.content)
        )
