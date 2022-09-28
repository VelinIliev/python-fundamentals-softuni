number_of_dragons = int(input())

dragons = {}

for dragon in range(number_of_dragons):
    data = input().split(" ")
    type_of_dragon = data[0]
    name = data[1]
    damage = int(data[2]) if data[2] != "null" else 45
    health = int(data[3]) if data[3] != "null" else 250
    armor = int(data[4]) if data[4] != "null" else 10
    if type_of_dragon not in dragons:
        dragons[type_of_dragon] = {name: {'damage': damage, 'health': health, 'armor': armor}}
    elif type_of_dragon in dragons :
        dragons[type_of_dragon][name] = {'damage': damage, 'health': health, 'armor': armor}
for type_of_dragon, values in dragons.items():
    sorted_dragons = sorted(values.items(), key=lambda item: item[0])
    sum_damage = 0
    sum_health = 0
    sum_armor = 0
    count = len(dragons[type_of_dragon])
    for data in values.values():
        sum_damage += data['damage']
        sum_health += data['health']
        sum_armor += data['armor']
    average_damage = sum_damage / count
    average_health = sum_health / count
    average_armor = sum_armor / count
    print(f'{type_of_dragon}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})')
    for data in sorted_dragons:
        name = data[0]
        new_data = dict(data[1])
        damage = new_data['damage']
        health = new_data['health']
        armor = new_data['armor']
        print(f'-{name} -> damage: {damage}, health: {health}, armor: {armor}')