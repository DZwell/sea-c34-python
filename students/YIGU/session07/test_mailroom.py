import pytest
from mailroom import is_number


def number_is_float():
    n = is_number(2)
    assert type(n) is float
