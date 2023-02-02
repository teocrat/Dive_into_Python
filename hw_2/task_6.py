# Банкомат
MULTIPLICITY = 50
WITHDRAWAL_PERCENTAGE = 1.5
MAX_SUM = 5_000_000
ZERO = 0
ONE = 1
TWO = 2
THREE = 3
TEN = 10
HUNDRED = 100
THIRTY = 30
SIX_HUNDRED = 600
account_amount = ZERO
count = ZERO

print('Добро пожаловать в банкомат!')
while True:
    wealth_tax = account_amount / HUNDRED * TEN
    accrued_interest = account_amount / HUNDRED * THREE
    n = int(input('Что Вы хотите сделать?\n1.Пополнить счет\n2.Снять наличные\n3.Выйти\n'))
    if account_amount > MAX_SUM:
        account_amount -= wealth_tax
    if n == ONE:
        refill = int(input('Введите сумму поплнения, кратную 50: '))
        if refill % MULTIPLICITY != ZERO:
            print('Введена сумма не кратная 50')
        else:
            account_amount += refill
            count += 1
            if count == THREE:
                account_amount += accrued_interest
                count = ZERO
            print(f'На Вашем cчете: {account_amount} ')

    elif n == TWO:
        withdrawal = int(input('Введите сумму, которую хотите снять, кратную 50.\nПроцент за снятие: 1.5 %,'
                               ' но не менее 30 и не более 600 \n'))

        if withdrawal % MULTIPLICITY != ZERO:
            print('Введена сумма не кратная 50')
        else:
            if account_amount == ZERO:
                print('На Вашем счете 0, cнятие невозможно')
            else:
                sum_per = withdrawal / HUNDRED * WITHDRAWAL_PERCENTAGE
                if sum_per < THIRTY:
                    sum_per = THIRTY
                elif sum_per > SIX_HUNDRED:
                    sum_per = SIX_HUNDRED
                sum_withdrawal = withdrawal + sum_per
                if sum_withdrawal > account_amount:
                    print('Запрашиваемая сумма больше суммы на Вашем счете ')
                    continue
                else:
                    account_amount -= sum_withdrawal
                    count += ONE
                    if count == THREE:
                        account_amount += accrued_interest
                        count = ZERO
                print(f'Вам выдана сумма {withdrawal}\nНа Вашем счете {account_amount}')
    elif n == THREE:
        print(f'До свидания!\nНа Вашем счете {account_amount}')
        break

    else:
        print('Введен неверный символ')
        continue
