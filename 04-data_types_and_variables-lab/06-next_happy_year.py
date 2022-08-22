year = int(input())

next_happy_year = 0

while True:
    year += 1
    test_year = str(year)
    year_as_list = []
    for letter in test_year:
        year_as_list.append(int(letter))
    non_repeated_digits = []
    for i in year_as_list:
        if i not in non_repeated_digits:
            non_repeated_digits.append(i)
    if len(non_repeated_digits) == len(year_as_list):
        next_happy_year = test_year
        break

print(next_happy_year)

