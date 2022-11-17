numbers = [int(number) for number in input().split(", ")]

count_zeros = 0

for i, number in enumerate(numbers):
    if number == 0:
        count_zeros += 1
        numbers[i] = None

for zero in range(count_zeros):
    numbers.append(0)

final_numbers = [number for number in numbers if number is not None]

print(final_numbers)