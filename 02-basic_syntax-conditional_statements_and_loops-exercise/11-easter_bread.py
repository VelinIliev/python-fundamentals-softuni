budget = float(input())
flour_price = float(input())

eggs_price = flour_price * .75
milk_price = (flour_price * 1.25) / 4

loaf_price = flour_price + eggs_price + milk_price

money_spend = 0
loaves_counter = 0
colored_eggs = 0

while True:
    if money_spend > budget:
        break

    if money_spend + loaf_price <= budget:
        loaves_counter += 1
        money_spend += loaf_price
        colored_eggs += 3
        if loaves_counter % 3 == 0:
            colored_eggs = colored_eggs - (loaves_counter - 2)
    elif money_spend + loaf_price > budget:
        break

money_left = budget - money_spend
print(f'You made {loaves_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
