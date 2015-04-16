import unittest
import pytest
import break_me


def test_type():
    ''' Test the outputs of the type_error function '''
    with pytest.raises(TypeError):
        break_me.type_error("String", 11.13)
