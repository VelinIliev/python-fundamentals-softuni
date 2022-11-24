number_of_heroes = int(input())
heroes = {}

for hero in range(number_of_heroes):
    new_data = input().split()
    name = new_data[0]
    hp = int(new_data[1])
    if hp > 100:
        hp = 100
    mp = int(new_data[2])
    if mp > 200:
        mp = 200
    heroes[name] = {"hp": hp, "mp": mp}

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" - ")
    action = command[0]
    hero_name = command[1]
    if action == "CastSpell":
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]["mp"] >= mp_needed:
            heroes[hero_name]["mp"] -= mp_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]["mp"]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if heroes[hero_name]["hp"] - damage > 0:
            heroes[hero_name]["hp"] -= damage
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]["hp"]} HP left!')
        else:
            del heroes[hero_name]
            print(f'{hero_name} has been killed by {attacker}!')
    elif action == "Recharge":
        amount = int(command[2])
        if heroes[hero_name]["mp"] + amount > 200:
            amount = 200 - heroes[hero_name]["mp"]
        heroes[hero_name]["mp"] += amount
        print(f'{hero_name} recharged for {amount} MP!')
    elif action == "Heal":
        amount = int(command[2])
        if heroes[hero_name]["hp"] + amount > 100:
            amount = 100 - heroes[hero_name]["hp"]
        heroes[hero_name]["hp"] += amount
        print(f'{hero_name} healed for {amount} HP!')

for hero, values in heroes.items():
    print(hero)
    print(f'HP: {values["hp"]}')
    print(f'MP: {values["mp"]}')