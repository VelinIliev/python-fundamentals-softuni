n = int(input())

for num in range(1, n + 1):
    digits = num
    first_digit = num % 10
    second_digit = num // 10

    if first_digit + second_digit == 5 or first_digit + second_digit == 7 or first_digit + second_digit == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
