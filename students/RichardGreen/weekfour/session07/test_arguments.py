#!/usr/bin/env python

"""
code that test arguments.py

can be run with py.test
"""

import pytest  # used for the exception testing

from arguments import f0


def test_f0_5_3_2():

    assert(f0(5, 3, 2) == 11)


def test_f0_1_2():

    assert(f0(1, 2) == 5)
