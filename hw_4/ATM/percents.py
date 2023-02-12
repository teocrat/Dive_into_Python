THREE = 3
TEN = 10
HUNDRED = 100


def wealth(account):
    wealth_tax = account / HUNDRED * TEN
    return wealth_tax


def accrued_interest(account):
    accrued = account / HUNDRED * THREE
    return accrued
