from percents import wealth


def check_max_sum(account, account_amount, MAX_SUM=5_000_000):
    if account > MAX_SUM:
        w = wealth(account)
        account -= w
        account_amount.append(f'Налог на богатых: {w}')
    return account
