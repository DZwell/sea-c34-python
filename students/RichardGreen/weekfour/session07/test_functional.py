#!/usr/bin/env python

"""
code that tests functional.py

can be run with py.test
"""

import pytest  # used for the exception testing

from functional import funct_filter


def test_funct_filter_range_10():

    assert(funct_filter(range(10)) == [1, 3, 5, 7, 9])


def test_funct_filter_range_20():

    assert(funct_filter(range(20)) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])


def test_funct_filter_range_100():

    assert(funct_filter(range(100)) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
                                        21, 23, 25, 27, 29, 31, 33, 35, 37,
                                        39, 41, 43, 45, 47, 49, 51, 53, 55,
                                        57, 59, 61, 63, 65, 67, 69, 71, 73,
                                        75, 77, 79, 81, 83, 85, 87, 89, 91,
                                        93, 95, 97, 99])


def funct_filter_range_2():

    print(funct_filter(range(2)) == 1)
