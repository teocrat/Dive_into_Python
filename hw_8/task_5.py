import json
import os
import pickle


def find_json(directory: str) -> None:
    for path, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                with open(f'{path}\\{file}', 'r', encoding='utf-8') as f:
                    found_file = json.load(f)
                new_pickle = os.path.join(path, f'{file.split(".")[0]}.pickle')
                with open(new_pickle, 'wb') as f:
                    pickle.dump(found_file, f)


if __name__ == '__main__':
    find_json(os.path.abspath('../hw_8'))
