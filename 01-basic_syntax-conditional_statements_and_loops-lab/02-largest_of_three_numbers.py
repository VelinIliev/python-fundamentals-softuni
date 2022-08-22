numbers = []
max_number = -10000

for x in range(3):
    number = int(input())
    numbers.append(number)

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)