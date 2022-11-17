from math import ceil

numbers = [int(number) for number in input().split(", ")]

max_n = max(numbers)

boundary = ceil(max_n / 10)

for x in range(1, boundary + 1):
    list_10s = [number for number in numbers if x * 10 - 9 <= number <= x * 10]
    print(f"Group of {x}0's: {list_10s}")