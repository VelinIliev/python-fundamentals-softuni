encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break
    command = command.split("|")
    operation = command[0]
    if operation == "ChangeAll":
        old_letter = command[1]
        new_letter = command[2]
        encrypted_message = encrypted_message.replace(old_letter, new_letter)
    elif operation == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif operation == "Move":
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

print(f'The decrypted message is: {encrypted_message}')