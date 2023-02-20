__all__ = ['make_files']

import os
from random import choices, randint
from string import ascii_letters, digits


def _create_files(extension: str, min_name: int = 6,
                 max_name: int = 30, min_b: int = 256, max_b: int = 4096, quantity: int = 42) -> None:
    for _ in range(quantity):
        name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(min_b, max_b))
        with open(f'{name}.{extension}', 'wb') as f:
            f.write(data)


def make_files(ext: dict, directory: str) -> None:
    if not os.path.isdir(directory):
        os.mkdir(directory)
    os.chdir(directory)
    for ext, count in ext.items():
        file = f'{directory}{_create_files(ext, quantity=count)}'
        if os.path.exists(file):
            continue


if __name__ == '__main__':
    data = {
        'txt': 2,
        'bin': 3
    }
    directory = 'C:\\Users\\Serge\python_lessons\\Dive_into_Python\\lesson_7\\hw_7\\new_dir\\'
    make_files(data, directory)
