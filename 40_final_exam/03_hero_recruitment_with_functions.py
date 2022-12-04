heroes = {}


def enroll(name):
    if name not in heroes:
        heroes[name] = []
    else:
        print(f'{name} is already enrolled.')


def learn(name, spell):
    if name not in heroes:
        print(f"{name} doesn't exist.")
    elif spell in heroes[name]:
        print(f"{name} has already learnt {spell}.")
    else:
        heroes[name].append(spell)


def unlearn(name, spell):
    if name not in heroes:
        print(f"{name} doesn't exist.")
    elif spell not in heroes[name]:
        print(f"{name} doesn't know {spell}.")
    else:
        heroes[name].remove(spell)


def print_results():
    print('Heroes:')
    for hero, values in heroes.items():
        print(f'== {hero}: {", ".join(values)}')


def main():
    while True:
        command = input()
        if command == "End":
            print_results()
            break
        command = command.split()
        action, name = command[0], command[1]
        if action == "Enroll":
            enroll(name)
        elif action == 'Learn':
            spell = command[2]
            learn(name, spell)
        elif action == 'Unlearn':
            spell = command[2]
            unlearn(name, spell)


main()
