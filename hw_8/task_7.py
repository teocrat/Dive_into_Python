import csv
import pickle
from pathlib import Path


def csv2pickle_str(file: Path) -> pickle:
    pickle_list = []
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                list_key = row
                continue
            pickle_dict = {}
            for j, item in enumerate(row):
                pickle_dict[list_key[j]] = item
            pickle_list.append(pickle_dict)

    return pickle.dumps(pickle_list)


if __name__ == '__main__':
    print(csv2pickle_str(Path('json_in.csv')))
