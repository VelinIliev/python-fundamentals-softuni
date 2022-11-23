import re

text_string = input()

FOOD_PER_DAY = 2000

pattern = r'(#|\|)([a-zA-Z ]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]{1,5})\1'
matches = re.findall(pattern, text_string)

total_calories = 0
food_items = []
for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = int(match[3])
    total_calories += calories
    food_items.append(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')

days = total_calories // FOOD_PER_DAY
print(f'You have food to last you for: {days} days!')
print('\n'.join(food_items))