from printing import pr_account
from percents import wealth
from accrued_int import acc_int
from check_50 import checker
from withdrawal import withdrawal_sum
from counter import counter
from check_max_sum import check_max_sum
from refill import refill

ONE = 1
TWO = 2
THREE = 3

account_amount = []
account = 0
count = 0

print('Добро пожаловать в банкомат!')
while True:

    n = int(input('\nЧто Вы хотите сделать?\n1.Пополнить счет\n2.Снять наличные\n3.Выйти\n'))
    account = check_max_sum(account, account_amount)

    if n == ONE:
        ref = int(input('Введите сумму поплнения, кратную 50: '))
        if not checker(ref):
            continue
        count = counter(count)
        account = refill(ref, account, account_amount)
        account = acc_int(count, account, account_amount)
        pr_account(account, account_amount)
    elif n == TWO:
        withdrawal = int(input('Введите сумму, которую хотите снять, кратную 50.\nПроцент за снятие: 1.5 %,'
                               ' но не менее 30 и не более 600 \n'))
        if not checker(withdrawal):
            continue
        count = counter(count)
        acc_int(count, account, account_amount)
        account = withdrawal_sum(withdrawal, account, account_amount)
        pr_account(account, account_amount)
    elif n == THREE:
        pr_account(account, account_amount)

        break

    else:
        print('Введен неверный символ')
        continue
