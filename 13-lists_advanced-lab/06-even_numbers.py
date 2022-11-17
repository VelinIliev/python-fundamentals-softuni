numbers = [int(number) for number in input().split(", ")]

indexes_of_even_numbers = []
for index, number in enumerate(numbers):
    if number % 2 == 0:
        indexes_of_even_numbers.append(index)

print(indexes_of_even_numbers)