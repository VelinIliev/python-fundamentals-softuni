heroes = {}

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    action = command[0]
    name = command[1]
    if action == "Enroll":
        if name not in heroes:
            heroes[name] = []
        else:
            print(f'{name} is already enrolled.')
    elif action == 'Learn':
        spell = command[2]
        if name not in heroes:
            print(f"{name} doesn't exist.")
        elif spell in heroes[name]:
            print(f"{name} has already learnt {spell}.")
        else:
            heroes[name].append(spell)
    elif action == 'Unlearn':
        spell = command[2]
        if name not in heroes:
            print(f"{name} doesn't exist.")
        elif spell not in heroes[name]:
            print(f"{name} doesn't know {spell}.")
        else:
            heroes[name].remove(spell)

print('Heroes:')
for hero, values in heroes.items():
    print(f'== {hero}: {", ".join(values)}')