income = input().split(", ")
count_of_beggars = int(input())

income = [int(x) for x in income]

income_per_beggar = []

for beggar in range(1, count_of_beggars + 1):
    profit = 0
    next_sum = 0
    for n, money in enumerate(income, 1):
        if n == beggar or next_sum == n:
            profit += money
            next_sum = n + count_of_beggars
    income_per_beggar.append(profit)

print(income_per_beggar)



