number_of_orders = int(input())

total = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed <= 2000:
        total_order = price_per_capsule * capsules_needed * days
        print(f'The price for the coffee is: ${total_order:.2f}')
        total += total_order

print(f'Total: ${total:.2f}')

