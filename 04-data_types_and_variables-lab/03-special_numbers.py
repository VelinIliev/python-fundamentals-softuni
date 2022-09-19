n = int(input())

for number in range(1, n + 1):
    first_digit = number % 10
    second_digit = number // 10
    sum = first_digit + second_digit
    if sum == 5 or sum == 7 or sum == 11:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')
