days_of_adventure = int(input())
count_of_players = int(input())
groups_energy = float(input())
water_for_day = float(input())
food_for_day = float(input())

total_water = days_of_adventure * count_of_players * water_for_day
total_food = days_of_adventure * count_of_players * food_for_day

# print(total_water)
# print(total_food)
game_over = False

for current_day in range(1, days_of_adventure + 1):
    energy_lost = float(input())
    groups_energy -= energy_lost

    if groups_energy <= 0:
        print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
        game_over = True
        break

    if current_day % 2 == 0:
        groups_energy *= 1.05
        total_water *= .7

    if current_day % 3 == 0:
        groups_energy *= 1.10
        total_food = total_food - total_food / count_of_players


if not game_over:
    print(f'You are ready for the quest. You will be left with - {groups_energy:.2f} energy!')