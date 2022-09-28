raw_activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    else:
        command = command.split(">>>")
        action = command[0]

    if action == "Slice":
        stat_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[:stat_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif action == "Flip":
        case = command[1]
        stat_index = int(command[2])
        end_index = int(command[3])
        if case == "Upper":
            raw_activation_key = raw_activation_key[:stat_index] + \
                                 raw_activation_key[stat_index:end_index].upper() +\
                                 raw_activation_key[end_index:]
            print(raw_activation_key)
        elif case == "Lower":
            raw_activation_key = raw_activation_key[:stat_index] + \
                                 raw_activation_key[stat_index:end_index].lower() + \
                                 raw_activation_key[end_index:]
            print(raw_activation_key)
    elif action == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print("Substring not found!")

print(f'Your activation key is: {raw_activation_key}')