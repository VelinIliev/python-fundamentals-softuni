year = int(input())

next_happy_year = 0

while True:
    year += 1
    test_year = str(year)
    year_as_list = [letter for letter in test_year]

    non_repeated_digits = []
    for digit in year_as_list:
        if digit not in non_repeated_digits:
            non_repeated_digits.append(digit)
    if len(non_repeated_digits) == len(year_as_list):
        next_happy_year = test_year
        break

print(next_happy_year)

