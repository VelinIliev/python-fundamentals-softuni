destinations = input()

while True:
    command = input()
    if command == "Travel":
        break
    else:
        command = command.split(" ")
        action = command[0]
        new_destinations = ""

        if action == "Add":
            instructions = command[1].split(":")
            index = int(instructions[1])
            new_string = instructions[2]
            if 0 <= index < len(destinations):
                for i in range(len(destinations)):
                    if i == index:
                        new_destinations += new_string
                    new_destinations += destinations[i]
        elif action == "Remove":
            instructions = command[1].split(":")
            start_index = int(instructions[1])
            end_index = int(instructions[2])
            if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations):
                for i in range(len(destinations)):
                    if i in range(start_index, end_index + 1):
                        new_destinations += ""
                    else:
                        new_destinations += destinations[i]
        elif action.startswith("Switch"):
            instructions = action.split(":")
            old_string = instructions[1]
            new_string = instructions[2]
            if old_string in destinations:
                new_destinations = destinations.replace(old_string, new_string)

        if len(new_destinations) > 0:
            destinations = new_destinations

        print(destinations)


print(f'Ready for world tour! Planned stops: {destinations}')