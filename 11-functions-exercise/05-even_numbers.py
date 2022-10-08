numbers = input()


def even_numbers(numbers):
    numbers_list = numbers.split(" ")
    numbers_list = [int(number) for number in numbers_list]

    def check_even(number):
        if number % 2 == 0:
            return True

        return False

    even_numbers_iterator = filter(check_even, numbers_list)
    numbers_list = [even_number for even_number in even_numbers_iterator]

    return numbers_list


print(even_numbers(numbers))
