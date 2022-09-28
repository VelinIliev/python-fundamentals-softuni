targeted_cities = {}

while True:
    command = input()
    if command == "Sail":
        break
    else:
        command = command.split("||")
        city = command[0]
        population = int(command[1])
        gold = int(command[2])
        if city not in targeted_cities:
            targeted_cities[city] = {'population': population, 'gold': gold}
        elif city in targeted_cities:
            targeted_cities[city]['population'] += population
            targeted_cities[city]['gold'] += gold

while True:
    command = input()
    if command == "End":
        break
    else:
        command = command.split("=>")
        action = command[0]
        city = command[1]

    if action == "Plunder":
        people = int(command[2])
        gold = int(command[3])
        if city in targeted_cities:
            targeted_cities[city]['population'] -= people
            targeted_cities[city]['gold'] -= gold
            print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
            if targeted_cities[city]['population'] <= 0 or targeted_cities[city]['gold'] <= 0:
                del targeted_cities[city]
                print(f'{city} has been wiped off the map!')
    elif action == "Prosper":
        gold = int(command[2])
        if city in targeted_cities:
            if gold < 0:
                print(f'Gold added cannot be a negative number!')
            else:
                targeted_cities[city]['gold'] += gold
                print(f'{gold} gold added to the city treasury. {city} now has {targeted_cities[city]["gold"]} gold.')

if len(targeted_cities) <= 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f'Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:')
    for city,v in targeted_cities.items():
        print(f'{city} -> Population: {v["population"]} citizens, Gold: {v["gold"]} kg')