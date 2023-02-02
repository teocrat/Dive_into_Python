import re
from math import gcd
from fractions import Fraction

ZERO = 0
ONE = 1
fr_1 = input('fr_1 = ')
fr_2 = input('fr_2 = ')

a_1 = int(re.split(r'/', fr_1)[ZERO])
d_1 = int(re.split(r'/', fr_1)[ONE])
a_2 = int(re.split(r'/', fr_2)[ZERO])
d_2 = int(re.split(r'/', fr_2)[ONE])

if a_1 + a_2 == d_1 == d_2:
    print(f'{fr_1} + {fr_2} = 1')
elif d_1 == d_2:
    print(f'{fr_1} + {fr_2} = {a_1 + a_2}/{d_1}')
else:
    cd = int(d_1 * d_2 / gcd(d_1, d_2))
    rn = int(cd / d_1 * a_1 + cd / d_2 * a_2)
    g = gcd(cd, rn)
    a = int(rn / g)
    d = int(cd / g)
    if a == d:
        print('1')
    else:
        print(f'{fr_1} + {fr_2} = {a}/{d} ')
print(f'Проверка: {Fraction(fr_1)} + {Fraction(fr_2)} = {Fraction(fr_1) + Fraction(fr_2)}')

mult_a = a_1 * a_2
mult_d = d_1 * d_2
mult_g = gcd(mult_a, mult_d)
print(f'{fr_1} * {fr_2} = {int(mult_a / mult_g)}/{int(mult_d / mult_g)} ')
print(f'Проверка: {Fraction(fr_1)} * {Fraction(fr_2)} = {Fraction(fr_1) * Fraction(fr_2)}')
