#!/usr/bin/env python
#####################
# HTML RENDER
# Richard Green


class Element(object):
    '''Create an Element class for rendering an html element
    (xml element). It should have class attributes for the tag name
    (html first) and the indentation (spaces to indent for pretty
    printing)'''
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""

    def append(self, string):
        '''Append to content.'''
        self.content += (
            u"{indent}{str}\n".format(indent=self.indent, str=str(string))
        )

    def render(self, file_out, ind=""):
        '''Render the tag and strings'''
        output = (
            u"{indent}<{tag}>\n"
            "{indent}{content}"
            "{indent}</{tag}>"
            .format(indent=ind, tag=self.tag, content=self.content)
        )
        file_out.write(output)
    # Now we can add our additional classes


class Html(Element):
    tag = u'html'

    def render(self, file_out, indent=""):
        '''Update the Html element class to render the <!DOCTYPE html> tag
         at the head of the page, before the html element.'''
        file_out.write('<!DOCTYPE html>\n')

        Element.render(self, file_out, indent)

# lets create the additional classes body P and head and have them inherit
# from the parent class element


class Body(Element):
    '''Create some subclasses of Element, for a <body> tag
    and <p> tag. All you should have to do is override the tag class
    attribute (you may need to add a tag class attribute to the Element
    class first...).'''

    tag = u'body'


class P(Element):
    '''Create a paragraph subclass of Element'''
    tag = u'p'


class Head(Element):
    '''Create a <head> element simple subclass.'''
    tag = u'head'

# lets create a class for one line tag and a render method which produces
# a single line output


class OneLineTag(Element):
    '''Create a OneLineTag subclass of Element'''
    tag = u''

    def render(self, file_out, indent=""):
        '''Extend the Element class to accept a set of attributes
        as keywords to the constructor, ie. (run_html_render.py)'''
        file_out.write('{}<{}{}>{}</{}>\n'.format(indent,
                                                  self.tag,
                                                  self.attributes,
                                                  self.contents[0],
                                                  self.tag))


class Title(OneLineTag):
    '''Create a Title subclass of OneLineTag class for the title.'''
    tag = 'title'


class A(OneLineTag):
    '''Create a A class for an anchor (link) element.'''

    tag = u'a'

    def __init__(self, html_address, text):
        '''You should be able to subclass from Element, and
        only override the __init__ Calling the Element __init__
        from the A __init__ OneLineTag.'''


class Ul(Element):
    '''Create Ul class for an unordered list (really
    simple subclass of Element)'''
    tag = u'u1'


class Li(Element):
    '''Create Li class for an element in a list'''
    tag = u'li'


class H(OneLineTag):
    def __init__(self, h_counter, header):
        '''Create a H class for one line tag'''

        self.tag = u'h' + str(h_counter)
        Element.__init__(self, header)


class SelfClosingTag(Element):
    def render(self, file_out, indent=""):
        '''Create a SelfClosingTag subclass of Element, to
        render tags. You will need to override the render method
        to render just the one tag and attributes, if any. Create
        a couple subclasses of SelfClosingTag for and <hr /> and <br />'''

        file_out.write('{}<{}{} />\n'.format(indent,
                                             self.tag,
                                             self.attributes))


class Hr(SelfClosingTag):
    '''Subclass of SelfClosingTag'''
    tag = u'hr'


class Br(SelfClosingTag):
    '''Subclass of SelfClosingTag'''
    tag = u'br'


class Meta(SelfClosingTag):
    '''Subclass of SelfClosingTag'''
    tag = u'meta'
