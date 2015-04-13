"""
===============================================================================
file: test_iteration.py
===============================================================================

Description:
     These are some test verifying that the fibonacci, lucas, and sum series
     functions work properly.
===============================================================================
"""

import iteration


def test_find_sum():
    assert(iteration.find_sum([25, 29, 31, 41]) == 126)
