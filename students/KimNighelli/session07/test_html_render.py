import unittest
import pytest
import html_render
import codecs
import cStringIO
import sys


def test_html_render():
    '''
    Test the output of the render function in the
    Title class of html_render.py
    '''
    tag = "title"
    t = html_render.Title(u"PythonClass = Revision 1087:")
    fd = cStringIO.StringIO()
    t.render(fd)
    assert fd.getvalue() == "<title>PythonClass = Revision 1087:</title>\n"
