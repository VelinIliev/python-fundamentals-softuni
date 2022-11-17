numbers = [int(number) for number in input().split(", ")]

positives = [number for number in numbers if number >= 0]
negatives = [number for number in numbers if number < 0]
evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if number % 2 != 0]

print(f'Positive: {", ".join(str(x) for x in positives)}')
print(f'Negative: {", ".join(str(x) for x in negatives)}')
print(f'Even: {", ".join(str(x) for x in evens)}')
print(f'Odd: {", ".join(str(x) for x in odds)}')