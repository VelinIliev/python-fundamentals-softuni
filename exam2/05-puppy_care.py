purchased_food_kg = int(input())

food_in_grams = purchased_food_kg * 1000
eaten_food = 0

while True:
    food_per_day = input()
    if food_per_day == "Adopted":
        break
    else:
        food_per_day = int(food_per_day)
    eaten_food += food_per_day

if eaten_food <= food_in_grams:
    difference = food_in_grams - eaten_food
    print(f'Food is enough! Leftovers: {difference} grams.')
else:
    difference = eaten_food - food_in_grams
    print(f'Food is not enough. You need {difference} grams more.')