__all__ = ['dict_mistery']

_dict_clue = {}


def _guess_word(mystery: str, clue_list: list[str], attempt=3) -> int:
    print(mystery)
    count = 1
    while attempt:
        answer = input(f'Отгадайте загадку. У Вас {attempt} попытки. ').lower()
        if answer in clue_list:
            return count
        else:
            attempt -= 1
            count += 1
    return 0


def _attempt_guess(mystery: str, attempt: int) -> dict:
    global _dict_clue
    _dict_clue[mystery] = attempt
    return _dict_clue


def dict_mistery() -> None:
    d_m = {'Висит груша, нельзя скушать': ['лампочка', 'тетя груша повесилась'],
           'Зимой и летом - одним цветом': ['елка', 'ель', 'елочка', 'солдат'],
           'У него огромный рот, он зовется …': ['бегемот', 'кашалот']
           }
    for key, item in d_m.items():
        _attempt_guess(key, _guess_word(key, item))


def print_res_guess(d_cl: dict) -> None:
    print(*(f'\nЗагадка "{key}" была отгадана с {item} попытки' for key, item in d_cl.items()))


if __name__ == '__main__':
    dict_mistery()
    print_res_guess(_dict_clue)
