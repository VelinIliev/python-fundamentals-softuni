strings = input().split(" ")

while True:
    command = input().split(" ")
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if start_index < end_index:
            if end_index >= len(strings):
                end_index = len(strings) - 1
            for num in range(start_index, end_index):
                strings[start_index] += f"{strings.pop(start_index + 1)}"

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])

        divider = len(strings[index]) // partitions
        string_to_change = strings.pop(index)
        new_string = []
        for x in range(partitions - 1):
            new_string.append(string_to_change[:divider])
            string_to_change = string_to_change[divider:]
        new_string.append(string_to_change)
        for x in new_string[::-1]:
            strings.insert(index, x)

print(" ".join(strings))

