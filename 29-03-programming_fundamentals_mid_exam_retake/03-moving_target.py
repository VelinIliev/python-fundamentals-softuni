targets = input().split(" ")
targets = [int(number) for number in targets]

while True:
    command = input()
    if command == "End":
        targets = [str(number) for number in targets]
        print("|".join(targets))
        break
    else:
        command = command.split(" ")
    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if index < 0 or index >= len(targets):
            print("Invalid placement!")
        else:
            targets.insert(index, value)
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        if index - radius < 0 or index + radius > len(targets):
            print("Strike missed!")
        else:
            for i in range(index + radius, index - radius - 1, -1):
                targets.pop(i)




