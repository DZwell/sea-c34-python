def color(*page_colors, **kwargs):
    """I am testing keyword arguments, while also learning
    to write better docstrings.

    Args:
        *args: These set my foreground and background color.
        **kwargs: These set link and visited link colors.

    Return:
        A string listing the values of my page colors will be returned.

    """
    print(u"Fore and background-colors are set to %s and %s." % (page_colors))
    print(u"Links have the colors: %s" % (kwargs))

color('#000000', '#ffffff', link_color='eeeeee', visited_link_color='rrrrrr')


def after(**t):
    """Using the format method, can I format a keyword argument form a dict
    when strutured in a function call?
    """
    print(u"{furniture} are beautiful next to a {structure}.".format(t))

    # Conclusion: This method returns several Keyword Errors

after(furniture="chairs", structure="window")


def correct():
    """Can I successfully use format to put dict values in a string?"""
    n = {u"furniture": u"Chairs", "structure": "windows"}
    print(u"{furniture} are beautiful next toC{structure}.".format(n))


correct()
