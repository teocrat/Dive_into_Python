HUNDRED = 100

names = ['Иван Петров', 'Александр Симонов', 'Сергей Васин']
salaries = [100_000, 120_000, 90_000]
percents = ['10.25%', '15.65%', '18.45%']

dict_bon = {name: sal * float(perc.replace('%', '')) / HUNDRED for name, sal, perc in zip(names, salaries, percents)}

print(dict_bon)
