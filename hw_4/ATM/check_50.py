ZERO = 0


def checker(r, MULTIPLICITY=50):
    if r % MULTIPLICITY == ZERO:
        return True
    else:
        print('Введена сумма не кратная 50')
        return False
