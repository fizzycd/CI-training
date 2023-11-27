import pytest
from main import five


def test_five():
    test = five()
    assert test == 5