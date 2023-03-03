class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Fish(Animal):

    def __init__(self, color, *args):
        self.color = color
        super().__init__(*args)

    def get_color(self):
        return f'Цвет рыбы {self.name} - {self.color}'


class Bird(Animal):

    def __init__(self, is_flies, *args):
        self.is_flies = is_flies
        super().__init__(*args)

    def __str__(self):
        spam = 'летает' if self.is_flies else 'ходит'
        return f'Перед нами птица {self.name}. Ей {self.age} лет. Эта птица {spam}'


class Dog(Animal):

    def __init__(self, height, *args):
        self.height = height
        super().__init__(*args)

    def get_height(self):
        if self.height < 0.5:
            return f'{self.name} маленький собачонок'
        elif 0.5 < self.height < 1:
            return f'{self.name} обычная собака'
        return f'Wow! The dog {self.name} is {self.height} meters tall! BIG FOOT!!!'


class MakeAnimal:

    @staticmethod
    def make_animal(type_of_animal, *args):
        if type_of_animal == 'dog':
            return Dog(*args)
        elif type_of_animal == 'bird':
            return Bird(*args)
        elif type_of_animal == 'fish':
            return Fish(*args)


if __name__ == '__main__':
    app = MakeAnimal()
    d = app.make_animal('dog', 0.3, 'Бобик', 1)
    print(d.name)
    print(f'Возраст - {d.age}')
    print(d.get_height())
    print()
    f = app.make_animal('fish', 'красный', 'лосось', 3)
    print(f.name)
    print(f'Возраст - {f.age}')
    print(f.get_color())
    b = app.make_animal('bird', False, 'страус', 12)
    print()
    print(b.name)
    print(f'Возраст - {b.age}')
    print(b)
