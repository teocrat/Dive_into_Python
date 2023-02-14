def f_path(path: str) -> tuple[str]:
    path_1 = path.split('\\')
    path_2 = path_1[-1].split('.')
    return ('/'.join(path_1[:-1]), path_2[0], path_2[1])


print(f_path("C:\\Users\Serge\python_lessons\Dive_into_Python\lesson_5\hw_5\path_to_file.py"))
