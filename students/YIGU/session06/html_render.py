class Element(object):
    """Element for all classes"""
    tag = ""
    indent = "    "

    def __init__(self, content=None, **style):
        self.content = [content] if content else []
        self.style = style

    def append(self, list):
        self.content.append(list)

    def render(self, file_out, ind=""):
        file_out.write("\n" + ind + "<%s" % self.tag)
        for key, value in self.style.items():
            file_out.write(" %s='%s'" % (key, value))
        file_out.write(">")
        for list in self.content:
            try:
                list.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write("\n"+ind + self.indent+str(list))
        file_out.write("\n" + ind + "</%s>" % self.tag)


class Html(Element):
    """HTML tag."""
    tag = "html"

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html>")
        Element.render(self, file_out, ind)


class Body(Element):
    """body tag."""
    tag = "body"


class P(Element):
    """p tag."""
    tag = "p"


class Head(Element):
    """head tag."""
    tag = "head"


class OneLineTag(Element):
    """for one line tage"""
    def render(self, file_out, ind=""):
        file_out.write("\n" + ind + "<%s>" % self.tag)
        for list in self.content:
            try:
                list.render(file_out)
            except AttributeError:
                file_out.write(str(list))
        file_out.write("</%s>" % self.tag)


class Title(OneLineTag):
    """title tag."""
    tag = "title"


class SelfClosingTag(Element):
    """for self-closing tags"""
    def render(self, file_out, ind=""):
        file_out.write("\n"+ind+"<%s" % self.tag)
        for key, value in self.style.items():
            file_out.write(" %s='%s'" % (key, value))
        file_out.write(" />")


class Hr(SelfClosingTag):
    """hr tag."""
    tag = "hr"


class Br(SelfClosingTag):
    """br tag."""
    tag = "br"


class A(OneLineTag):
    """a tag."""
    tag = "a"

    def __init__(self, link, content):
        OneLineTag.__init__(self, content, href=link)


class Ul(Element):
    """ul tag."""
    tag = u"ul"


class Li(Element):
    """li tag."""
    tag = u"li"


class H(OneLineTag):
    def __init__(self, level, content=None, **styple):
        OneLineTag.__init__(self, content, **styple)

        self.tag = "h%i" % level


class Meta(SelfClosingTag):
    """Meta tag."""
    tag = "Meta"

    def __init__(self, content=None, **charset):
        SelfClosingTag.__init__(self, content, **charset)
