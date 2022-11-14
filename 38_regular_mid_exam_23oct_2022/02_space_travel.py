route_to_titan = input().split("||")
starting_fuel = int(input())
ammunition = int(input())

# print(route_to_titan, starting_fuel, ammunition)

for command in route_to_titan:
    if command == "Titan":
        print(f'You have reached Titan, all passengers are safe.')
        break
    else:
        command = command.split()
        action = command[0]
        amount = int(command[1])
    if action == "Travel":
        starting_fuel -= amount
        if starting_fuel >= 0:
            print(f'The spaceship travelled {amount} light-years.')
        else:
            print(f'Mission failed.')
            break
    elif action == "Enemy":
        if ammunition >= amount:
            ammunition -= amount
            print(f'An enemy with {amount} armour is defeated.')
        else:
            needed_fuel = amount * 2
            if starting_fuel - needed_fuel >= 0:
                print(f"An enemy with {amount} armour is outmaneuvered.")
                starting_fuel -= needed_fuel
            else:
                print(f'Mission failed.')
                break
    elif action == "Repair":
        starting_fuel += amount
        ammunition += amount * 2
        print(f'Ammunitions added: {amount * 2}.')
        print(f'Fuel added: {amount}.')