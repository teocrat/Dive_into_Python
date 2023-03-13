class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __init__(self, lvl_ptrn, value):
        self.lvl_ptrn = lvl_ptrn
        self.value = value

    def __str__(self):
        if self.value < self.lvl_ptrn:
            return f'Уровень ниже образцового {self.lvl_ptrn}'


class AccessError(ProjectException):
    def __init__(self, spam_user, users):
        self.spam_user = spam_user
        self.users = users

    def __str__(self):
        if self.spam_user not in self.users:
            return 'Отказано в доступе'
