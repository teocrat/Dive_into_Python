ONE = 1
double_el = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 'g', 'g', 'g', 'g', False, False, 23, 45, None, None]
res = []
for i in double_el:
    if double_el.count(i) > ONE:
        if i not in res:
            res.append(i)
print(res)
