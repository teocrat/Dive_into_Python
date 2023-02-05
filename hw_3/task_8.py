ONE = 1

three_friends = {
    'John': ('toothbrush', 'toothpaste', 'knife', 'water', 'canned food', 'matches', 'pasta'),
    'Tom': ('toothbrush', 'toothpaste', 'knife', 'lighter', 'flashlight', 'matches', 'flammable liquid'),
    'Sam': ('toothbrush', 'toothpaste', 'knife', 'water', 'canned food', 'matches', 'pasta'),

}

all_items = []
for key in three_friends:
    for j in three_friends[key]:
        all_items.append(j)

unique_items = []
for i in all_items:
    if all_items.count(i) == ONE:
        unique_items.append(i)

friend_without_item = set()
items_everyone_has = set()
for key in three_friends:
    for j in three_friends[key]:
        if j not in unique_items:
            items_everyone_has.add(j)
        else:
            friend_without_item.add(key)
        if all_items.count(j) == len(three_friends):
            items_everyone_has.discard(j)


print(f'{all_items = }')
print(f'{unique_items = }')
print(f'{friend_without_item = }')
print(f'{items_everyone_has = }')
