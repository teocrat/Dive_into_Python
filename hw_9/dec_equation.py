import csv
from pathlib import Path
from typing import Callable


def dec_eq(func: Callable):
    def wrapper():
        with open(Path('gen.csv'), 'r', encoding='utf-8') as f:
            csv_str = csv.reader(f)
            res = []
            for row in csv_str:
                res.append(func(int(row[0]), int(row[1]), int(row[2])))
        return res

    return wrapper
