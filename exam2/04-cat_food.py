number_of_cats = int(input())

kg_food = 12.45

small_cats = 0
big_cats = 0
enormous_cats = 0
eaten_food = 0

for cat in range(number_of_cats):
    cat_food = float(input())
    if 100 <= cat_food < 200:
        small_cats += 1
    elif 200 <= cat_food < 300:
        big_cats += 1
    elif 300 <= cat_food < 400:
        enormous_cats += 1

    eaten_food += cat_food

print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {big_cats} cats.')
print(f'Group 3: {enormous_cats} cats.')
total = (eaten_food / 1000) * kg_food
print(f'Price for food per day: {total:.2f} lv.')