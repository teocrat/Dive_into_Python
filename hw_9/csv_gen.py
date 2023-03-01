import csv
from random import randrange


def gen_csv(count_strings: int = 100, max_random: int = 100) -> None:
    res = []

    for i in range(count_strings):
        random_dict = {}
        for j in range(1, 4):
            random_dict[f'num{j}'] = randrange(max_random)
        res.append(random_dict)

    fieldnames = ['num1', 'num2', 'num3']
    with open('gen.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(res)


if __name__ == '__main__':
    gen_csv()
