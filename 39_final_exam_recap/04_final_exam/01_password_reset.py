password = input()

while True:
    command = input()
    if command == "Done":
        break
    command = command.split()
    action = command[0]
    if action == "TakeOdd":
        new_password = ""
        for i, char in enumerate(password):
            if i % 2 != 0:
                new_password += char
        password = new_password
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
        else:
            print('Nothing to replace!')
            continue
    print(password)

print(f'Your password is: {password}')