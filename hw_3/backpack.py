things_for_the_trip = {
    'knife': 1,
    'rope': 3,
    'tent': 8,
    'rubber boat': 10,
    'sleeping bag': 5,
    'food': 4,
    'first_aid_kit': 1
}
backpack = 15
things_in_backpack = []
weight = []
for key, item in things_for_the_trip.items():
    if sum(weight) < backpack:
        weight.append(item)
        things_in_backpack.append(key)
for i in range(len(things_in_backpack)):
    print(things_in_backpack[i])
