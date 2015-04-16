import unittest
import pytest
from list_comp import count_evens


def test_list_comp():
    ''' Test the outputs of the count_evens function in list_comp.py'''
    assert count_evens([2, 4, 5, 7]) == 2
    assert count_evens([-3, -2, -1, 0, 1, 2, 3, 4]) == 4
    assert count_evens([3, 5, 9, 273]) == 0
    assert count_evens([8, 2, 7, 1, 0, 2, 2, 0, 5, 9, 3, 22, 104]) == 8
