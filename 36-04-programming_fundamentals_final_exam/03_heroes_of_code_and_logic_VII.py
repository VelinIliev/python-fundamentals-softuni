number_of_heroes = int(input())
heroes = {}

max_hit_points = 100
max_mana_points = 200

for hero in range(number_of_heroes):
    entry = input().split(" ")
    hero_name = entry[0]
    hit_points = int(entry[1])
    mana_points = int(entry[2])
    heroes[hero_name] = {"hit points": hit_points, 'mana points': mana_points}

while True:
    command = input()
    if command == "End":
        break
    else:
        command = command.split(" - ")
        action = command[0]
        hero_name = command[1]

    if action == "Heal":
        amount = int(command[2])
        if hero_name in heroes:
            if heroes[hero_name]['hit points'] + amount > max_hit_points:
                amount = max_hit_points - heroes[hero_name]['hit points']
            heroes[hero_name]['hit points'] += amount
            print(f"{hero_name} healed for {amount} HP!")
    elif action == "Recharge":
        amount = int(command[2])
        if hero_name in heroes:
            if heroes[hero_name]['mana points'] + amount > max_mana_points:
                amount = max_mana_points - heroes[hero_name]['mana points']
            heroes[hero_name]['mana points'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if hero_name in heroes:
            if heroes[hero_name]['hit points'] - damage > 0:
                heroes[hero_name]['hit points'] -= damage
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit points']} HP left!")
            else:
                print(f'{hero_name} has been killed by {attacker}!')
                del heroes[hero_name]
    elif action == "CastSpell":
        mana_needed = int(command[2])
        spell_name = command[3]
        if hero_name in heroes:
            if heroes[hero_name]['mana points'] - mana_needed >= 0:
                heroes[hero_name]['mana points'] -= mana_needed
                print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]["mana points"]} MP!')
            else:
                print(f'{hero_name} does not have enough MP to cast {spell_name}!')

for hero, values in heroes.items():
    print(hero)
    print(f'  HP: {values["hit points"]}')
    print(f'  MP: {values["mana points"]}')