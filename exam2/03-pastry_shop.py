type_of_sweet = input()
number_of_sweets = int(input())
day_of_month = int(input())

price = 0

if type_of_sweet == "Cake":
    if day_of_month <= 15:
        price = 24
    elif day_of_month > 15:
        price = 28.70
elif type_of_sweet == "Souffle":
    if day_of_month <= 15:
        price = 6.66
    elif day_of_month > 15:
        price = 9.80
elif type_of_sweet == "Baklava":
    if day_of_month <= 15:
        price = 12.60
    elif day_of_month > 15:
        price = 16.98

total = number_of_sweets * price

if day_of_month <= 22:
    if 100 <= total <= 200:
        total *= .85
    elif total > 200:
        total *= .75

    if day_of_month <= 15:
        total *= .9

print(f'{total:.2f}')