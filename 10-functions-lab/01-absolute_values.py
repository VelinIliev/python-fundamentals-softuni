numbers = input()

numbers = numbers.split(" ")
numbers = [float(number) for number in numbers]


# def return_abs_value(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = abs(numbers[i])
#     print(numbers)
#
# return_abs_value(numbers)

def return_abs_value(number):
    number = abs(number)
    return number


for i in range(len(numbers)):
    numbers[i] = return_abs_value(numbers[i])

print(numbers)