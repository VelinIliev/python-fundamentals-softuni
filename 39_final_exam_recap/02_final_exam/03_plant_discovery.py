number_of_lines = int(input())
plants = {}

for line in range(number_of_lines):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": int(rarity), "rating": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(': ')
    action = command[0]
    plant = command[1].split(" - ")[0]
    if plant not in plants:
        print('error')
    elif action == "Rate":
        new_rating = int(command[1].split(" - ")[1])
        plants[plant]['rating'].append(new_rating)
    elif action == "Update":
        new_rarity = int(command[1].split(" - ")[1])
        plants[plant]['rarity'] = new_rarity
    elif action == "Reset":
        plants[plant]['rating'] = []

print('Plants for the exhibition:')
for plant, values in plants.items():
    if values['rating']:
        average_rating = sum(values['rating']) / len(values['rating'])
    else:
        average_rating = 0
    print(f'- {plant}; Rarity: {values["rarity"]}; Rating: {average_rating:.2f}')