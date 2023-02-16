from sys import argv

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


def _leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def is_date(date: str) -> bool:
    d, m, y = map(int, date.split('.'))

    return (FIRST_DAY <= d <= LAST_DAY and m in LONG_MONTH or
            FIRST_DAY <= d < LAST_DAY and m not in LONG_MONTH and m != TWO or
            d == LEAP_DAY and m == TWO and _leap_year(y)) and MIN_DATE <= y <= MAX_DATE


# if __name__ == '__main__':
#     d = '29.02.2012'
#     print(is_date(d))
if __name__ == '__main__':
    print(is_date(*(argv[1:])))
