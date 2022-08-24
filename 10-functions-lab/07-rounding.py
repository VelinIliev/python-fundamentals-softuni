numbers = input()


def round_numbers(numbers):
    numbers = numbers.split(" ")
    numbers = [float(number) for number in numbers]
    numbers = [int(round(number, 0)) for number in numbers]
    return numbers


print(round_numbers(numbers))