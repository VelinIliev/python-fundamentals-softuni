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
        if 0 > index > len(integers) - 1:
            print("Invalid index")
        else:
            new_integers = []
            for i in range(index):
                new_integers.append(integers.pop(i))

            for i in range(len(new_integers)):
                integers.append(new_integers.pop(0))
            print(index)
    elif command[0] == "max":


print(integers)