def key_func(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, list | set):
            value = str(value)
        new_dict[value] = key

    return new_dict


res = key_func(a=1, b=2, c=3, d=[1, 2, 3], e={4, 5, 6})
print(res)
