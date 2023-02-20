import os


def ren_files(desired_name: str, count_int: int, source_ext: str,
              dest_ex: str, start_name: int, end_name: int, path: str) -> None:
    path, dirs, files = next(os.walk(path))
    for num in range(len(files)):
        f = files[num].split('.')
        if f[-1] == source_ext:
            old_name = os.path.join(path, files[num])
            n_f = f[0][start_name: end_name]
            new_name = os.path.join(path, f'{n_f}{desired_name}_{num:0{count_int}}.{dest_ex}')

            os.rename(old_name, new_name)


if __name__ == '__main__':
    path = 'C:\\Users\\Serge\\python_lessons\\Dive_into_Python\\lesson_7\\hw_7\\new_dir'
    ren_files('my_file', 2, 'txt', 'csv', 1, 5, path)
