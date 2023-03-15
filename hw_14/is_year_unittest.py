import unittest
from is_date import IsYear


class TestYear(unittest.TestCase):
    def setUp(self) -> None:
        self.y = IsYear('29.02.2021')
        self.year = 2021

    def test_leap_year(self):
        self.assertFalse(self.y.leap_year(2021))

    def test_is_date(self):
        self.assertFalse(self.y.is_date())


if __name__ == '__main__':
    y = IsYear('29.02.2021')
    print(y.is_date())
