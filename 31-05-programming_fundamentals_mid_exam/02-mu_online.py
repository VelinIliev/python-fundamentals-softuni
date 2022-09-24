dungeons_rooms = input().split("|")

health = 100
bitcoins = 0

rooms = 0
pass_all = True

for room in dungeons_rooms:
    command = room.split(" ")
    rooms += 1
    if command[0] == "potion":
        amount_of_health = int(command[1])
        if health == 100:
            continue
        elif health + amount_of_health > 100:
            amount_of_health = 100 - health
            health = 100
        else:
            health += amount_of_health
        print(f'You healed for {amount_of_health} hp.')
        print(f'Current health: {health} hp.')
    elif command[0] == "chest":
        amount = int(command[1])
        bitcoins += amount
        print(f'You found {amount} bitcoins.')
    else:
        monster = command[0]
        attack_of_monster = int(command[1])
        if health - attack_of_monster > 0:
            print(f'You slayed {monster}.')
            health -= attack_of_monster
            # print(health)
        else:
            print(f"You died! Killed by {monster}.")
            print(f'Best room: {rooms}')
            pass_all = False
            break

if pass_all:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')