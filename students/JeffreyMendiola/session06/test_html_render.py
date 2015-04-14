"""
===============================================================================
file: test_html_render.py
===============================================================================

Description:
     This is a test verifying that the html_render program works properly.
===============================================================================
"""

import html_render
import cStringIO


def test_html_render():
    page = html_render.H(2, "PythonClass - Class 6 example")
    f = cStringIO.StringIO()
    page.render(f)
    assert(f.getvalue() == "<h2>PythonClass - Class 6 example</h2>\n")
