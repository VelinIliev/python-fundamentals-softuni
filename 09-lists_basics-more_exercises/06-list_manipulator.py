list = [int(number) for number in input().split(" ")]

while True:
    command = input()
    if command == "end":
        break
    else:
        command = command.split(" ")
    if command[0] == "exchange":
        index = int(command[1])
        if index > len(list) - 1 or index < 0:
            print("Invalid index")
        else:
            for i in range(index + 1):
                x = list.pop(0)
                list.append(x)
    elif command[0] == "max":
        max_type = command[1]
        max_index = 0
        max_number = -1
        if command[1] == "odd":
            for index, number in enumerate(list):
                if number % 2 != 0 and number >= max_number:
                    max_index = index
                    max_number = number
        elif command[1] == "even":
            for index, number in enumerate(list):
                if number % 2 == 0 and number >= max_number:
                    max_index = index
                    max_number = number
        if max_number < 0:
            print("No matches")
        else:
            print(max_index)
    elif command[0] == "min":
        min_type = command[1]
        min_index = 0
        min_number = 1001
        if command[1] == "odd":
            for index, number in enumerate(list):
                if number % 2 != 0 and number <= min_number:
                    min_index = index
                    min_number = number
        elif command[1] == "even":
            for index, number in enumerate(list):
                if number % 2 == 0 and number <= min_number:
                    min_index = index
                    min_number = number
        if min_number > 1000:
            print("No matches")
        else:
            print(min_index)
    elif command[0] == "first":
        count = int(command[1])
        if count > len(list):
            print("Invalid count")
        else:
            type_of = command[2]
            first_list = []
            if type_of == "even":
                for number in list:
                    if number % 2 == 0:
                        first_list.append(number)
            elif type_of == "odd":
                for number in list:
                    if number % 2 != 0:
                        first_list.append(number)
            print(first_list[:count:])
    elif command[0] == "last":
        count = int(command[1])
        if count > len(list):
            print("Invalid count")
        else:
            type_of = command[2]
            last_list = []
            if type_of == "even":
                for number in list:
                    if number % 2 == 0:
                        last_list.append(number)
            elif type_of == "odd":
                for number in list:
                    if number % 2 != 0:
                        last_list.append(number)
            print(last_list[-count:])

print(list)
