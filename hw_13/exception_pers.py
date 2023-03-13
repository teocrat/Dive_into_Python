class PersonException(Exception):
    pass


class PersNameError(PersonException):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def __str__(self):
        if not self.param1 or not self.param2:
            return f'Неправильный формат имени'


class AgeError(PersonException):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        if self.age <= 0:
            return 'Неправильный формат возраста'
