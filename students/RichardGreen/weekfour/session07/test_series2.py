#!/usr/bin/env python

"""
code that tests Series.py

can be run with py.test
"""

import pytest  # used for the exception testing


from series import lucas, fibonacci


def test_lucas_15():

    assert(lucas(15) == 1364)


def test_fibonacci_15():

    assert(fibonacci(15) == 610)
