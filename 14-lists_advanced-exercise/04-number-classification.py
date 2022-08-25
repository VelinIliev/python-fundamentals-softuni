numbers = input()

numbers = numbers.split(", ")
numbers = [int(number) for number in numbers]

positives = [number for number in numbers if number >= 0]
negatives = [number for number in numbers if number < 0]
evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if number % 2 != 0]

positives_str = [str(number) for number in positives]
negatives_str = [str(number) for number in negatives]
evens_str = [str(number) for number in evens]
odds_str = [str(number) for number in odds]

positives_str = ", ".join(positives_str)
negatives_str = ", ".join(negatives_str)
evens_str = ", ".join(evens_str)
odds_str = ", ".join(odds_str)

print(f'Positive: {positives_str}')
print(f'Negative: {negatives_str}')
print(f'Even: {evens_str}')
print(f'Odd: {odds_str}')