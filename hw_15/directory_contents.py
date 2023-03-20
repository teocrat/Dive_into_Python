import os
from collections import namedtuple
import argparse


def dir_cont(directory: str):
    DirCont = namedtuple('DirCont', ['filename', 'extension', 'dirname'])
    res = []
    for path, dirs, files in os.walk(directory, topdown=True, onerror=None, followlinks=False):
        for catalog in dirs:
            res.append(DirCont(catalog, 'no extension', path))
        for file in files:
            f, ex = os.path.splitext(file)
            res.append(DirCont(f, ex, path))

    return res


def parser_func():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', default='C:\\')
    args = parser.parse_args()
    return dir_cont(f'{args.directory}')


if __name__ == '__main__':
    # d = dir_cont('C:\\Users\\Serge\\python_lessons\\Dive_into_Python\\lesson_15')
    # for item in d:
    #     print(item)
    print(parser_func())
