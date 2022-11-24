raw_activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print(f'Substring not found!')
    elif action == "Flip":
        upper_or_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if upper_or_lower == "Upper":
            raw_activation_key = raw_activation_key[:start_index] + \
                                 raw_activation_key[start_index:end_index].upper() + \
                                 raw_activation_key[end_index:]
        elif upper_or_lower == "Lower":
            raw_activation_key = raw_activation_key[:start_index] + \
                                 raw_activation_key[start_index:end_index].lower() + \
                                 raw_activation_key[end_index:]
        print(raw_activation_key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

print(f'Your activation key is: {raw_activation_key}')