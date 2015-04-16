"""
===============================================================================
file: test_iteration.py
===============================================================================

Description:
     This is a test verifying that the find_sum function works properly.
===============================================================================
"""

import iteration


def test_find_sum():
    assert(iteration.find_sum([25, 29, 31, 41]) == 126)
