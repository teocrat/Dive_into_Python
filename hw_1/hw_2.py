# простые числа
ZERO = 0
ONE = 1
TWO = 2
FIVE = 5
TEN = 10
ONE_HUNDRED_THOUSAND = 100_000

count = 0

while True:
    n = int(input('Введите положительное число до 100.000 '))
    if ZERO <= n <= ONE_HUNDRED_THOUSAND:
        break

for i in range(TWO, n // TWO + ONE):
    if n % i == 0:
        count += ONE
if count <= 0:
    res = "Число простое"
else:
    res = 'Число составное'

print(res)
