from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ONE = 1
n = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 10

while count:
    a = int(input(f'Угадай число от 0 до 1000, у тебя {count} попыток '))
    if a < n:
        print('Загаданное число больше')
        count -= ONE
    elif a > n:
        print('Загаданное число меньше')
        count -= ONE
    else:
        print(f'Ты угадал. загаданное число {n}')
        break
