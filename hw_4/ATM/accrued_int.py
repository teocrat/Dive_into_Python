from percents import accrued_interest

THREE = 3


def acc_int(count, account, account_amount):
    if count == THREE:
        a_i = accrued_interest(account)
        account += a_i
        account_amount.append(f'Поступление процентов на счет: {a_i:.2f}')
    return account
