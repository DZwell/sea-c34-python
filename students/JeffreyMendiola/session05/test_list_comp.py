"""
===============================================================================
file: test_list_comp.py
===============================================================================

Description:
     This is a test verifying that the count_evens function works properly.
===============================================================================
"""

import list_comp


def test_find_sum():
    assert(list_comp.count_evens([2, 1, 2, 3, 4]) == 3)
    assert(list_comp.count_evens([2, 2, 0]) == 3)
    assert(list_comp.count_evens([1, 3, 5]) == 0)
