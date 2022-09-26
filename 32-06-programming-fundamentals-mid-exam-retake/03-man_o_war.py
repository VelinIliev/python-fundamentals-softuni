# Create a program that tracks the battle and either chooses a
# winner or prints a stalemate. On the first line, you will
# receive the status of the pirate ship, which is a string representing
# integer sections separated by ">".
# On the second line, you will receive the same type of status, but for the warship:
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
pirate_ship_status = input().split(">")
pirate_ship_status = [int(number) for number in pirate_ship_status]
war_ship_status = input().split(">")
war_ship_status = [int(number) for number in war_ship_status]
max_health = int(input())
is_not_sunk = True
# The following lines represent commands until "Retire":
while True:
    command = input()
    if command == "Retire":
        break
    else:
        command = command.split(" ")
    #"Fire {index} {damage}" - the pirate ship attacks the warship with
    # the given damage at that section. Check if the index is valid and if not,
    # skip the command. If the section breaks (health <= 0) the warship sinks,
    # print the following and stop the program: "You won! The enemy ship has sunken."
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 < index < len(war_ship_status) - 1:
            war_ship_status[index] -= damage
            if war_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_not_sunk = False
                break
    # •	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate
    # ship with the given damage at that range (indexes are inclusive).
    # Check if both indexes are valid and if not, skip the command.
    # If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
    # "You lost! The pirate ship has sunken."
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
    # •	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health.
    # Check if the index is valid and if not, skip the command.
    # The health of the section cannot exceed the maximum health capacity.
    elif command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if index >= 0 and index <= len(pirate_ship_status) - 1:
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health:
                pirate_ship_status[index] = max_health
    # •	"Status" - prints the count of all sections of the pirate ship that need repair soon,
    # which are all sections that are lower than 20% of the maximum health capacity. Print the following:
    # "{count} sections need repair."
    elif command[0] == "Status":
        sections_need_repair = 0
        for section in pirate_ship_status:
            if section < max_health * .2:
                sections_need_repair += 1
        print(f'{sections_need_repair} sections need repair.')
# In the end, if a stalemate occurs, print the status of both ships,
# which is the sum of their individual sections, in the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"
if is_not_sunk:
    pirate_ship_sum = sum(pirate_ship_status)
    war_ship_sum = sum(war_ship_status)
    print(f'Pirate ship status: {pirate_ship_sum}')
    print(f'Warship status: {war_ship_sum}')