numbers = [float(number) for number in input().split(" ")]


def return_abs_value(number):
    number = abs(number)
    return number


for i in range(len(numbers)):
    numbers[i] = return_abs_value(numbers[i])

print(numbers)