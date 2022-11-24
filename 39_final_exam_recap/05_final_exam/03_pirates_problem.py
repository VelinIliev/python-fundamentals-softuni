cities = {}

while True:
    command = input()
    if command == "Sail":
        break
    command = command.split("||")
    name = command[0]
    population = int(command[1])
    gold = int(command[2])
    if name not in cities:
        cities[name] = {"population": population, "gold": gold}
    else:
        cities[name]['population'] += population
        cities[name]['gold'] += gold

while True:
    command = input()
    if command == "End":
        break
    command = command.split("=>")
    action = command[0]
    citi = command[1]
    if action == "Plunder":
        people = int(command[2])
        gold = int(command[3])
        print(f'{citi} plundered! {gold} gold stolen, {people} citizens killed.')
        cities[citi]["population"] -= people
        cities[citi]["gold"] -= gold
        if cities[citi]["population"] <= 0 or cities[citi]["gold"] <= 0:
            del cities[citi]
            print(f'{citi} has been wiped off the map!')
    elif action == "Prosper":
        gold = int(command[2])
        if gold >= 0:
            cities[citi]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {citi} now has {cities[citi]['gold']} gold.")
        else:
            print('Gold added cannot be a negative number!')

if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for citi, values in cities.items():
        print(f'{citi} -> Population: {values["population"]} citizens, Gold: {values["gold"]} kg')
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
