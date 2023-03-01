from cmath import sqrt

from lesson_9.hw_9.dec_equation import dec_eq
from lesson_9.hw_9.dec_to_json import eq_to_json

TWO = 2
FOUR = 4


@eq_to_json
@dec_eq
def qua_equation(a: int = 3, b: int = 5, c: int = 6) -> tuple:
    if a == 0:
        return 'Это не квадратное уравнение'
    d = b ** TWO - FOUR * a * c
    x1 = (-b + sqrt(d)) / (TWO * a)
    x2 = (-b - sqrt(d)) / (TWO * a)
    return [x1, x2]


if __name__ == '__main__':
    qua_equation()
