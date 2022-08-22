lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

money_spend = 0
shield_broken_counter = 0

for lost_battle in range(1, lost_fights_count + 1):
    if lost_battle % 2 == 0:
        money_spend += helmet_price
    if lost_battle % 3 == 0:
        money_spend += sword_price
    if lost_battle % 2 == 0 and lost_battle % 3 == 0:
        money_spend += shield_price
        shield_broken_counter += 1
    if shield_broken_counter == 2:
        money_spend += armor_price
        shield_broken_counter = 0

print(f"Gladiator expenses: {money_spend:.2f} aureus")
