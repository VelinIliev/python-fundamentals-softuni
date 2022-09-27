password = input()

while True:
    command = input()
    if command == "Done":
        break
    else:
        command = command.split(" ")
        action = command[0]

    if action == "TakeOdd":
        new_raw_password = ''
        for n, char in enumerate(password):
            if n % 2 != 0:
                new_raw_password += char
        password = new_raw_password
        print(password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring_to_remove = password[index: index + length:]
        password = password.replace(substring_to_remove, "", 1)
        print(password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f'Your password is: {password}')