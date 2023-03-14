from lesson_13.hw_13.exception_pers import PersNameError, AgeError


class CheckName:
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
            raise PersNameError(self.param1(value), self.param2(value))


class Person:
    name = CheckName(str.isalpha, str.istitle)
    surname = CheckName(str.isalpha, str.istitle)

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        if age <= 0:
            raise AgeError(age)
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    pers = Person('John', 'Smith', 34)
    print(pers.get_full_name())
    print(pers.get_age())
    pers.birthday()
    print(pers.get_age())
