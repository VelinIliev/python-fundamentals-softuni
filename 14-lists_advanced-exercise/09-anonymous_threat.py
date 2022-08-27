strings = input()

strings = strings.split(" ")

while True:
    command = input()

    if command == "3:1":
        break
    else:
        command = command.split(" ")

    if command[0] == "merge":

        start_index = int(command[1])

        if start_index < 0:
            start_index = 0

        if start_index > len(strings) - 1:
            start_index = len(strings) - 1

        end_index = int(command[2])

        if end_index < 0:
            end_index = 0

        if end_index > len(strings) - 1:
            end_index = len(strings) - 1

        merged_string = ""

        for x in range(start_index, end_index + 1):
            merged_string += strings[start_index]
            del strings[start_index]

        strings.insert(start_index, merged_string)

    elif command[0] == "divide":

        index = int(command[1])
        partitions = int(command[2])

        new_partitions = []

        if len(strings[index]) % partitions == 0:
            new_partition = ""

            for n, letter in enumerate(strings[index], start=1):
                new_partition += letter
                if n % (len(strings[index]) / partitions) == 0:
                    new_partitions.append(new_partition)
                    new_partition = ""

            del strings[index]

            for partition in reversed(new_partitions):
                strings.insert(index, partition)

        else:
            new_length = int(len(strings[index]) / partitions)
            new_partition = ""
            end = len(strings[index]) - new_length * (partitions - 1)

            for n, letter in enumerate(strings[index], start=1):
                new_partition += letter

                if n > end:
                    if n == len(strings[index]):
                        new_partitions.append(new_partition)
                elif n % new_length == 0:
                    new_partitions.append(new_partition)
                    new_partition = ""

            del strings[index]

            for partition in reversed(new_partitions):
                strings.insert(index, partition)

final_string = " ".join(strings)

print(final_string)

# TODO: not ready