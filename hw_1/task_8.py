STAR = '*'
SPACE = ' '
ONE = 1
rows = int(input('Сколько рядов у елки?: '))
sp = rows - ONE

for i in range(ONE, rows * 2, 2):
    print(SPACE * sp + STAR * i)
    sp -= ONE
