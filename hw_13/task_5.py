import json
from pathlib import Path

from task_6 import AccessError, LevelError
from task_4 import User


class Project:

    def __init__(self):
        self.me = None
        self._users = set()

    def read_user(self, file: Path) -> set[User]:
        with open(file, 'r', encoding='utf-8') as f:
            user_json = json.load(f)

        for lvl, v in user_json.items():
            for id, name in v.items():
                self._users.add(User(name, int(id), int(lvl)))
        return self._users

    def sign_in(self, name, idx):
        spam_user = User(name=name, idx=idx, lvl=0)
        if spam_user not in self._users:
            raise AccessError(spam_user, self._users)
        for user in self._users:
            if user == spam_user:
                self.me = user
                return user

    def add_user(self, name, idx, lvl):
        spam_user = User(name=name, idx=idx, lvl=lvl)
        if spam_user.lvl < self.me.lvl:
            raise LevelError(self.me.lvl, spam_user.lvl)
        self._users.add(spam_user)
        return spam_user


if __name__ == '__main__':
    p = Project()
    res = p.read_user(Path('names.json'))
    print(f'{res =}')
    print(p.sign_in("gtr", 5))
    print((p.add_user('asdwq', 67, 6)))
    print(f'{res =}')
