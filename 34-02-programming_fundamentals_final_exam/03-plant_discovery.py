number_of_lines = int(input())

plants = {}

for line in range(number_of_lines):
    entry = input().split("<->")
    plant = entry[0]
    rarity = int(entry[1])
    plants[plant] = {"rarity": rarity, 'rating': []}


while True:
    command = input()
    if command == "Exhibition":
        break
    else:
        command = command.split(": ")
        action = command[0]
        instructions = command[1].split(" - ")
        plant = instructions[0]
    if action == "Rate":
        rating = int(instructions[1])
        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print("error")
    elif action == "Update":
        new_rarity = int(instructions[1])
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print("error")
    elif action == "Reset":
        plant = instructions[0]
        if plant in plants:
            plants[plant]["rating"] = []
        else:
            print("error")

print("Plants for the exhibition:")
for plant, values in plants.items():
    rarity = values['rarity']
    rating = values['rating']
    avg_rating = 0
    if len(rating) != 0:
        avg_rating = sum(rating) / len(rating)
    print(f'- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}')

