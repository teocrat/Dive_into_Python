# треугольник
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a + b < c or a + c < b or c + b < a:
    res = 'Треугольник не существует'
elif a == b == c:
    res = 'Треугольник равносторонний'
elif a == b or a == c or b == c:
    res = 'Треугольник равнобедренный'
else:
    res = 'Треугольник разносторонний'

print(res)