concealed_message = input()

while True:
    command = input()
    if command == "Reveal":
        break
    else:
        instructions = command.split(":|:")
        action = instructions[0]
    if action == "ChangeAll":
        old_string = instructions[1]
        new_string = instructions[2]
        concealed_message = concealed_message.replace(old_string, new_string)
        print(concealed_message)
    elif action == "Reverse":
        substring = instructions[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message += substring
            print(concealed_message)
        else:
            print("error")
    elif action == "InsertSpace":
        index = int(instructions[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index::]
        print(concealed_message)

print(f'You have a new text message: {concealed_message}')