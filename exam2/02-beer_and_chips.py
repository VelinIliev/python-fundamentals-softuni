from math import ceil
name = input()
budget = float(input())
beers_number = int(input())
chips_number = int(input())

beer_price = 1.2
total_beer = beers_number * beer_price
chips_price = total_beer * .45
total_chips = ceil(chips_number * chips_price)

total = total_chips + total_beer

if total <= budget:
    money_rest = budget - total
    print(f"{name} bought a snack and has {money_rest:.2f} leva left.")
else:
    difference = total - budget
    print(f"{name} needs {difference:.2f} more leva!")