pirate_ship_status = input().split(">")
pirate_ship_status = [int(number) for number in pirate_ship_status]
war_ship_status = input().split(">")
war_ship_status = [int(number) for number in war_ship_status]
max_health = int(input())
is_not_sunk = True
while True:
    command = input()
    if command == "Retire":
        break
    else:
        command = command.split(" ")
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 < index < len(war_ship_status) - 1:
            war_ship_status[index] -= damage
            if war_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_not_sunk = False
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index <= end_index and start_index >= 0 and end_index <= len(pirate_ship_status) - 1:
            for section in range(start_index, end_index + 1):
                pirate_ship_status[section] -= damage
                if pirate_ship_status[section] <= 0:
                    is_not_sunk = False
                    print("You lost! The pirate ship has sunken.")
                    break
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index >= 0 and index <= len(pirate_ship_status) - 1:
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health
    elif command[0] == "Status":
        sections_need_repair = 0
        for section in pirate_ship_status:
            if section < max_health * .2:
                sections_need_repair += 1
        print(f'{sections_need_repair} sections need repair.')
if is_not_sunk:
    pirate_ship_sum = sum(pirate_ship_status)
    war_ship_sum = sum(war_ship_status)
    print(f'Pirate ship status: {pirate_ship_sum}')
    print(f'Warship status: {war_ship_sum}')