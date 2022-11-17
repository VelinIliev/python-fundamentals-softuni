numbers = input()


def round_numbers(numbers):
    return [int(float(number)) for number in numbers.split(" ")]


print(round_numbers(numbers))