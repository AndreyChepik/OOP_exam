import pytest
import numpy
from Task_3_programm import funk


def test_funk():
    result = funk()
    params = funk.l
    assert result == numpy.prod(params)