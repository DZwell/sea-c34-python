class Element(object):
    """An HTML element."""
    tag = u""
    indent = u"    "

    def __init__(self, content=None, **kwargs):
        self.content = [str(content)] if content else []
        self.attributes = kwargs

    def append(self, string):
        """Append string to content."""
        self.content.append(string)

    def render_opening_tag(self, file_out, ending=">\n"):
        file_out.write("<{}".format(self.tag))
        for key, value in self.attributes.iteritems():
            file_out.write(" {key}=\"{value}\"".format(key=key, value=value))
        file_out.write(ending)

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        file_out.write(ind)
        self.render_opening_tag(file_out)
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind + self.indent)
            else:
                file_out.write(ind)
                file_out.write(self.indent)
                file_out.write(item)
                file_out.write("\n")
        file_out.write(ind)
        file_out.write("</{}>\n".format(self.tag))


class Html(Element):
    """HTML tag."""
    tag = u"html"

    def render(self, file_out, ind=""):
        file_out.write(ind)
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, ind)


class Body(Element):
    """Body tag."""
    tag = u"body"


class Head(Element):
    """Head tag."""
    tag = u"head"


class OneLineTag(Element):
    """OneLineTag."""

    def render(self, file_out, ind=""):
        file_out.write(ind)
        self.render_opening_tag(file_out, ending=">")
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind + self.indent)
            else:
                file_out.write(item)
        file_out.write("</{}>\n".format(self.tag))


class SelfClosingTag(Element):
    """SelfClosingTag"""

    def render(self, file_out, ind=""):
        file_out.write(ind)
        self.render_opening_tag(file_out, ending=" />\n")


class Hr(SelfClosingTag):
    tag = u"hr"


class Br(SelfClosingTag):
    tag = u"br"


class Title(OneLineTag):
    """Title tag."""
    tag = u"title"


class P(Element):
    """P tag."""
    tag = u"p"


class A(OneLineTag):
    tag = u"a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        Element.__init__(self, content, **kwargs)


class Ul(Element):
    tag = u"ul"


class Li(Element):
    tag = u"li"


class H(OneLineTag):

    def __init__(self, headerlevel, content=None, **kwargs):
        self.tag = u"h{headerlevel}".format(headerlevel=headerlevel)
        Element.__init__(self, content, **kwargs)


class Meta(SelfClosingTag):
    tag = u"meta"
