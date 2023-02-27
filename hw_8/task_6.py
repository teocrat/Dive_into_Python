import csv
import pickle
from pathlib import Path


def pickle2csv(file: Path) -> None:
    with open(file, 'rb') as f:
        received_file = pickle.load(f)
    fieldnames = []
    for field_name in received_file[0].keys():
        fieldnames.append(field_name)

    with open(f'{file.stem}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(received_file)


if __name__ == '__main__':
    pickle2csv(Path('json_in.pickle'))
