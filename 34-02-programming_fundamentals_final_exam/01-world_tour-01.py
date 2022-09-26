destinations = input()
# print(len(destinations))
while True:
    command = input()
    if command == "Travel":
        break
    elif len(command.split(" ")) > 1:
        command = command.split(" ")
        action = command[0]
    elif len(command.split(":")) > 1:
        command = command.split(":")
        action = command[0]

    if action == "Add":
        command[1] = command[1].split(":")
        index = int(command[1][1])
        new_string = command[1][2]
        new_destinations = ""
        if 0 <= index <= len(destinations):
            for i in range(len(destinations)):
                if i == index:
                    new_destinations += new_string
                new_destinations += destinations[i]
        destinations = new_destinations
    elif action == "Remove":
        command[1] = command[1].split(":")
        start_index = int(command[1][1])
        end_index = int(command[1][2])
        new_destinations = ""
        if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations) and start_index < end_index:
            for i in range(len(destinations)):
                if i in range(start_index, end_index + 1):
                    new_destinations += ""
                else:
                    new_destinations += destinations[i]
        destinations = new_destinations
    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)
    print(destinations)

print(f'Ready for world tour! Planned stops: {destinations}')