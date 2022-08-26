number_of_rows = int(input())

battle_field = []
for x in range(number_of_rows):
    row = input()
    row = row.split(" ")
    row = [int(number) for number in row]
    battle_field.append(row)

attacks = input()
attacks = attacks.split(" ")
destroyed_ships = 0

for attack in attacks:
    attack = attack.split("-")
    row_index = int(attack[0])
    col_index = int(attack[1])
    if battle_field[row_index][col_index] == 1:
        battle_field[row_index][col_index] -= 1
        destroyed_ships += 1
    elif battle_field[row_index][col_index] > 1:
        battle_field[row_index][col_index] -= 1

print(destroyed_ships)