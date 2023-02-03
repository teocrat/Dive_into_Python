ZERO = 0
NINE = 9
HEX = 16

hex_num = ['A', 'B', 'C', 'D', 'E', 'F']
int_num = [10, 11, 12, 13, 14, 15]
num = int(input('Enter number '))
a = ''
work_num = num

while work_num > ZERO:
    b = work_num % HEX
    if b > NINE:
        for key, item in enumerate(int_num):
            if item == b:
                a = hex_num[key] + a
    else:
        a = str(work_num % 16) + a
    work_num //= HEX
print(a)
print(f'{hex(num) = }')
