array = input().split(" ")
array = [int(number) for number in array]

while True:
    command = input()
    if command == "end":
        break
    else:
        command = command.split(" ")
        # print(command)
        if command[0] == "swap":
            first_index = int(command[1])
            second_index = int(command[2])
            [array[first_index], array[second_index]] = [array[second_index], array[first_index]]
        elif command[0] == "multiply":
            first_index = int(command[1])
            second_index = int(command[2])
            array[first_index] *= array[second_index]
        elif command[0] == "decrease":
            array = [number - 1 for number in array]

array = [str(number) for number in array]
print(", ".join(array) )