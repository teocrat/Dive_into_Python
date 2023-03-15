import pytest
from is_date import IsYear


def test_leap_year():
    y = IsYear('29.02.2021')
    year = 2021
    assert y.leap_year(year) == False


def test_is_date():
    y = IsYear('29.02.2021')
    assert y.is_date() == False


if __name__ == '__main__':
    pytest.main(['-v'])
