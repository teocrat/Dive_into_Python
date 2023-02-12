ZERO = 0
WITHDRAWAL_PERCENTAGE = 1.5
MIN_TAX = 30
HUNDRED = 100
MAX_TAX = 600


def withdrawal_sum(withdrawal, account, account_amount):
    sum_per = withdrawal / HUNDRED * WITHDRAWAL_PERCENTAGE
    if account == ZERO:
        print('На Вашем счете 0, cнятие невозможно')
        return account
    else:
        if sum_per < MIN_TAX:
            sum_per = MIN_TAX
        elif sum_per > MAX_TAX:
            sum_per = MAX_TAX
        sum_withdrawal = withdrawal + sum_per
        if sum_withdrawal <= account:
            account_amount.append(f'Запрос на снятие: {withdrawal}')
            account_amount.append(f'Процент на снятие: {sum_per}')

            return account - sum_withdrawal
        else:
            print('Запрашиваемая сумма больше суммы на Вашем счете ')
            return account
