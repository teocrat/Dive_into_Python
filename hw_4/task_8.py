ONE = 1
fers = 23
fer = 0
seds = 45
sed = 0
ases = 34
ase = 0
s = 556


def value_substitution(**kwargs) -> None:
    for key, value in kwargs.items():
        for key_2 in kwargs.keys():
            if key_2 == key[0:-1]:
                kwargs[key_2] = value
        if key[-1] == 's' and len(key) > ONE:
            kwargs[key] = None
    for k, v in kwargs.items():
        print(f'{k} = {v}')


value_substitution(fers=23, fer=0, seds=45, sed=0, ases=34, ase=0, s=556)
