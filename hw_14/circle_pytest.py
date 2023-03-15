from circle import Circle

import pytest


def test_len_circle():
    assert Circle(3).len_circle() == 18.84955592153876


def test_square():
    assert Circle(3).square() == 28.274333882308138


if __name__ == '__main__':
    pytest.main(['-v'])
