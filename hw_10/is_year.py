ZERO = 0
TWO = 2
MIN_DATE = 1
MAX_DATE = 9999
FIRST_DAY = 1
LAST_DAY = 31
LEAP_DAY = 29
SMALL_YEAR = 4
MID_YEAR = 100
BIG_YEAR = 400
LONG_MONTH = [1, 3, 5, 7, 8, 10, 12]


class IsYear:

    def __init__(self, year: str):
        self.year = year

    @staticmethod
    def _leap_year(year: int) -> bool:
        return year % SMALL_YEAR == ZERO and year % MID_YEAR != ZERO or year % BIG_YEAR == ZERO

    def is_date(self) -> bool:
        d, m, y = map(int, self.year.split('.'))

        return (FIRST_DAY <= d <= LAST_DAY and m in LONG_MONTH or
                FIRST_DAY <= d < LAST_DAY and m not in LONG_MONTH and m != TWO or
                d == LEAP_DAY and m == TWO and self._leap_year(y)) and MIN_DATE <= y <= MAX_DATE


if __name__ == '__main__':

    y = IsYear('29.02.2021')
    print(y.is_date())
