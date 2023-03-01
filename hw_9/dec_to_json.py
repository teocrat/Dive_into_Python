import csv
import json
from pathlib import Path
from typing import Callable


def eq_to_json(func: Callable):
    def wrapper():
        source_list = func()
        end_list = []
        res_list = []
        with open(Path('gen.csv'), 'r', encoding='utf-8') as f:
            csv_str = csv.reader(f)
            for row in csv_str:
                a, b, c = row[0], row[1], row[2]
                res_list.append([a, b, c])
        for i, data in enumerate(source_list):
            dict_res = {f'a = {res_list[i][0]}, b = {res_list[i][1]}, c = {res_list[i][2]}':
                        f'x1 = {data[0]}, x2 = {data[1]}'}
            end_list.append(dict_res)
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(end_list, f, indent=2)
        return func

    return wrapper()
