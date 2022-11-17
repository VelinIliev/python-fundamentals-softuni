numbers = input()


def min_max_and_sum(numbers):
    numbers_list = [int(number) for number in numbers.split(" ")]
    max_number = max(numbers_list)
    min_number = min(numbers_list)
    sum_list = sum(numbers_list)
    return f'The minimum number is {min_number} \n' \
           f'The maximum number is {max_number} \n' \
           f'The sum number is: {sum_list}'


print(min_max_and_sum(numbers))