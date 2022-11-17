numbers = [int(x) for x in input().split(" ")]
numbers_to_remove = int(input())

sorted_numbers = sorted(numbers)

for i in range(numbers_to_remove):
    numbers.remove(sorted_numbers[i])

print(", ".join(str(x) for x in numbers))