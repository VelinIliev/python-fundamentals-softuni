integers = input()

integers = integers.split(" ")
integers = [int(number) for number in integers]


while True:
    command = input()
    if command == "end":
        break
    else:
        command = command.split(" ")
        # print(command)
    if command[0] == "exchange":
        manipulation = command[0]
        index = int(command[1])
        if index < 0 or index > len(integers) - 1:
            print("Invalid index")
        else:
            new_integers = []
            for i in range(index + 1):

                new_integers.append(integers.pop(0))
            for i in range(len(new_integers)):
                integers.append(new_integers.pop(0))
    elif command[0] == "max":
        odd_or_even = command[1]
        max_n = -1000000000
        max_index = -1

        for index, number in enumerate(integers):
            if odd_or_even == "even":
                if number % 2 == 0 and number > max_n:
                    max_n = number
                    max_index = index
            elif number % 2 != 0 and number > max_n:
                max_n = number
                max_index = index
        if max_index > -1:
            print(max_index)
        else:
            print("No matches")
    elif command[0] == "min":
        odd_or_even = command[1]
        min_n = 1000000000
        min_index = -1

        for index, number in enumerate(integers):
            if odd_or_even == "even":
                if number % 2 == 0 and number < min_n:
                    min_n = number
                    min_index = index
            elif number % 2 != 0 and number < min_n:
                min_n = number
                min_index = index
        if min_index > -1:
            print(min_index)
        else:
            print("No matches")
    elif command[0] == "first":
        count = int(command[1])
        odd_or_even = command[2]
        invalid = False
        temp_list = []
        if count > len(integers):
            invalid = True
        elif odd_or_even == "even":
            for number in integers:
                if number % 2 == 0 and len(temp_list) < count:
                    temp_list.append(number)
        elif odd_or_even == "odd":
            for number in integers:
                if number % 2 != 0 and len(temp_list) < count:
                    temp_list.append(number)
        if invalid:
            print("Invalid count")
        else:
            print(temp_list)
    elif command[0] == "last":
        count = int(command[1])
        odd_or_even = command[2]
        invalid = False
        temp_list = []
        reversed_list = integers[::-1]
        if count > len(integers):
            invalid = True
        elif odd_or_even == "even":
            for number in reversed_list:
                if number % 2 == 0 and len(temp_list) < count:
                    temp_list.append(number)
        elif odd_or_even == "odd":
            for number in reversed_list:
                if number % 2 != 0 and len(temp_list) < count:
                    temp_list.append(number)
        if invalid:
            print("Invalid count")
        else:
            print(temp_list)

print(integers)

# TODO: not ready
