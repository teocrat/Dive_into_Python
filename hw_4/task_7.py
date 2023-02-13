ZERO = 0
COUNT = 1


def company_income(dictionary: dict[str, list[int]]) -> bool:
    count = ZERO
    for values in dictionary.values():
        if sum(values) > ZERO:
            count += COUNT
    if count == len(dictionary):
        return True
    else:
        return False


res = company_income({
    'Geely': [100_000_000, -230_000, 10_000, 200_000, -500_000, 300_000, -40_000, 100_000, - 50_000],
    'Haval': [500_000, 300_000, -200_000, 400_000, -250_000, 30_000, -40_000, 100_000, 40_000],
    'Exeed': [20_000_000, -40_000_000, 600_000, -100_000, 30_000, 340_000, -60_000],
    'Chery': [32_000_000, -20_000_000, 500_000, 45_000, -100_000, 120_000, 400_000, -450_000]
})
print(res)
