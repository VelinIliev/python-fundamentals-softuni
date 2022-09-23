numbers = input().split(" ")
numbers = [int(number) for number in numbers]
average = sum(numbers) / len(numbers)

greater_then_average = []

sorted_numbers = sorted(numbers, reverse=True)
for number in sorted_numbers:
    if number > average:
        greater_then_average.append(number)

if len(greater_then_average) == 0:
    print("No")
elif len(greater_then_average) > 5:
    greater_then_average = [str(number) for number in greater_then_average]
    print(" ".join(greater_then_average[:5]))
else:
    greater_then_average = [str(number) for number in greater_then_average]
    print(" ".join(greater_then_average))