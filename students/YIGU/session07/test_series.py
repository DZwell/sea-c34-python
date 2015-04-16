import pytest
from series import fibonacci
from series import sum_series


def test_fibonacci():
    # fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(5) == 5
    assert sum_series(0) == 0


def test_sum_series():
    # sum_series
    assert sum_series(1) == 1
    assert sum_series(5) == 5
    assert sum_series(6) == 8
    assert sum_series(0, 2, 1) == 2
    assert sum_series(5, 2, 1) == 11
    assert sum_series(5, 3, 4) == 29
