numbers = input()


def sorting_func(numbers):
    sorted_numbers = numbers.split(" ")
    sorted_numbers = [int(number) for number in sorted_numbers]

    return sorted(sorted_numbers)


print(sorting_func(numbers))