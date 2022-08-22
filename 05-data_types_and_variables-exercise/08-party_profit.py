group_size = int(input())
number_of_days = int(input())

money_earned = 0

for day in range(1, number_of_days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5

    money_earned += 50
    food = group_size * 2
    money_earned -= food

    if day % 3 == 0:
        motivational_party = group_size * 3
        money_earned -= motivational_party
    if day % 5 == 0:
        if day % 3 != 0:
            slay_boss_monster = group_size * 20
        elif day % 3 == 0:
            slay_boss_monster = group_size * 18
        money_earned += slay_boss_monster

money_per_companion = money_earned / group_size

print(f'{group_size} companions received {int(money_per_companion)} coins each.')