import json
from pathlib import Path


class User:
    def __init__(self, name: str, idx: int, lvl: int):
        self.name = name
        self.idx = idx
        self.lvl = lvl

    def __eq__(self, other):
        return self.idx == other.idx and self.name == other.name

    def __hash__(self):
        return hash((self.idx, self.name))

    def __repr__(self):
        return f'User(name={self.name}, idx={self.idx}, level={self.lvl})'


def read_user(file: Path) -> set[User]:
    with open(file, 'r', encoding='utf-8') as f:
        user_json = json.load(f)

    users = set()
    for lvl, v in user_json.items():
        for idx, name in v.items():
            users.add(User(name, idx, lvl))

    return users


if __name__ == '__main__':
    print(read_user(Path('names.json')))
