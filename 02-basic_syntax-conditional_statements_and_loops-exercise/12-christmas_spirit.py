items_to_buy = int(input())
days_until_xmas = int(input())

ornament_set_price = 2
ornament_set_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17

money_spend = 0
xmas_spirit_points = 0
last_day = 0

for day in range(1, days_until_xmas + 1):
    if day % 11 == 0:
        items_to_buy += 2
    if day % 2 == 0:
        money_spend += ornament_set_price * items_to_buy
        xmas_spirit_points += ornament_set_points
    if day % 3 == 0:
        money_spend += (tree_skirt_price + tree_garland_price) * items_to_buy
        xmas_spirit_points += (tree_skirt_points + tree_garland_points)
    if day % 5 == 0:
        money_spend += tree_lights_price * items_to_buy
        xmas_spirit_points += tree_lights_points
    if day % 3 == 0 and day % 5 == 0:
        xmas_spirit_points += 30
    if day % 10 == 0:
        xmas_spirit_points -= 20
        money_spend += tree_skirt_price + tree_garland_price + tree_lights_price
    last_day = day

if last_day % 10 == 0:
    xmas_spirit_points -= 30

print(f"Total cost: {money_spend}")
print(f"Total spirit: {xmas_spirit_points}")