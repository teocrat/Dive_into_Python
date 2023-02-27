import csv
import json
import os
import pickle


def search_dir(directory: str) -> None:
    res = []
    for path, dirs, files in os.walk(directory, topdown=True, onerror=None, followlinks=False):
        for catalog in dirs:
            size_dir = 0
            for root, cat, files_cat in os.walk(f'{path}\\{catalog}'):
                for file in files_cat:
                    size_dir += os.path.getsize(f'{root}\\{file}')
            catalogs = {'path': path, 'searched': catalog, 'file_or_dir': 'it`s directory',
                        'size': f'{size_dir = } bytes'}
            res.append(catalogs)
        for file in files:
            size = os.path.getsize(f'{path}\\{file}')
            f = {'path': path, 'searched': file, 'file_or_dir': 'it`s file', 'size': f'{size = } bytes'}
            res.append(f)

    with open('search_dir.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=2)

    with open('search_dir.pickle', 'wb') as f:
        pickle.dump(res, f)

    fieldnames = ['path', 'searched', 'file_or_dir', 'size']
    with open('search_dir.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(res)


if __name__ == '__main__':
    search_dir('C:\\Users\\Serge\\python_lessons\\Dive_into_Python\\lesson_8')
