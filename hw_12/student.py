import csv
from statistics import mean


class CheckValue:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.param1(value) and self.param2(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad {value}')


class Student:
    first_name = CheckValue(str.isalpha, str.istitle)
    surname = CheckValue(str.isalpha, str.istitle)
    last_name = CheckValue(str.isalpha, str.istitle)

    def __init__(self, first_name, surname, last_name):
        self.first_name = first_name
        self.surname = surname
        self.last_name = last_name
        self.full_name = f'{self.first_name}_{self.surname}_{self.last_name}'
        self.d = []
        with open(f'{self.full_name}.csv', 'r', encoding='utf-8') as f:
            fieldnames = ['Предмет', 'Оценки', 'Баллы']
            self.items = csv.DictReader(f, fieldnames=fieldnames)

            for i, v in enumerate(self.items):
                if i == 0:
                    continue
                self.d.append(v)
        self.marks = []
        for item in self.d:
            self.marks.append(item['Оценки'])

        self.num = []
        for data in self.marks:
            for num in data.replace('[', '').replace(']', '').replace(',', ' ').split():
                if num.isdigit():
                    self.num.append(int(num))

    def __str__(self):
        print(f'{self.full_name}:\n{self.d}\n Средний балл по всем оценкам: {mean(self.num)}')
        for item in self.d:
            print(f'{item["Предмет"]},'
                  f' средний бал '
                  f'{mean([int(item) for item in item["Баллы"].replace("[", "").replace("]", "").replace(",", " ").split()])}')
        return ''


if __name__ == '__main__':
    s1 = Student('Eddy', 'Van', 'Halen')
    print(s1)
    s2 = Student('Axel', 'Rudy', 'Pell')
    print(s2)
