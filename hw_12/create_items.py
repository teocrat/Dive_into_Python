import csv


def create_csv():
    res_list = []

    n_s = input('Введите имя, отчество, фамилию студента: ').split()
    file = '_'.join(n_s)

    while True:
        i_s = input('Введите предмет студента или для выхода ENTER: ')
        if i_s == '':
            break
        mark_list = []
        test_list = []
        res_list.append({'Предмет': i_s, 'Оценки': mark_list, 'Баллы': test_list})
        while True:
            m_s = int(input('Введите оцеку по предмету '))
            r_t = int(input('Введите балл  по тесту по предмету или для выхода 0: '))
            if r_t == 0:
                break
            mark_list.append(m_s)
            test_list.append(r_t)

    print(res_list)
    with open(f'{file}.csv', 'w', encoding='utf-8') as f:
        fieldnames = ['Предмет', 'Оценки', 'Баллы']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(res_list)


if __name__ == '__main__':
    while True:
        q = input('Для выхода введите q + ENTER, для продолжения ENTER ')
        if q == 'q':
            break
        else:
            create_csv()
