import pytest
from lambdahw import list_functions


def lam_test():
    functions = list_functions(5)
    assert functions[0](2) == 2
    assert functions[1](2) == 3
    assert functions[2](2) == 4
