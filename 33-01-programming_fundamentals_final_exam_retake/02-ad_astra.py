import re
text_string = input()

pattern = r'([\/|#])([a-zA-Z\s]+)([\/|#])([0-9]{2}\/[0-9]{2}\/[0-9]{2})([\/|#])([0-9]+)([\/|#])'
matches = re.findall(pattern, text_string)

products = []
for match in matches:
    products.append(list(match))

valid_products = []
for product in products:
    if len(set(product)) == 4:
        new_product = [product[1], product[3], product[5]]
        valid_products.append(new_product)

total_calories = 0
for product in valid_products:
    calories = int(product[2])
    total_calories += calories
days = total_calories // 2000

print(f'You have food to last you for: {days} days!')
for product in valid_products:
    print(f'Item: {product[0]}, Best before: {product[1]}, Nutrition: {product[2]}')