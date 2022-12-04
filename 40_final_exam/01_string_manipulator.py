start_string = input()

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    action = command[0]
    if action == "Translate":
        char, replacement = command[1], command[2]
        start_string = start_string.replace(char, replacement)
        print(start_string)
    elif action == "Includes":
        substring = command[1]
        print("True" if substring in start_string else "False")
    elif action == "Start":
        substring = command[1]
        print("True" if start_string.startswith(substring) else "False")
    elif action == "Lowercase":
        start_string = start_string.lower()
        print(start_string)
    elif action == "FindIndex":
        char = command[1]
        print(start_string.rindex(char))
    elif action == "Remove":
        start_index, count = int(command[1]), int(command[2])
        end_index = start_index + count
        start_string = start_string[:start_index] + start_string[end_index:]
        print(start_string)