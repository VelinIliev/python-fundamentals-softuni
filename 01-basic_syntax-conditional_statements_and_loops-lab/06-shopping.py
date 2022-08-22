budget = int(input())
money_spend = 0

while True:
    price = input()
    if price == "End":
        break
    else:
        price = int(price)

    if money_spend + price <= budget:
        money_spend += price
    elif money_spend + price > budget:
        print(f'You went in overdraft!')
        money_spend += price
        break

if money_spend <= budget:
    print("You bought everything needed.")