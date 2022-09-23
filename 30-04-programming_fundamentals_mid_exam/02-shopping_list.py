shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    else:
        command = command.split(" ")
    if command[0] == "Urgent":
        item = command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif command[0] == "Unnecessary":
        item = command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif command[0] == "Correct":
        old_item = command[1]
        new_item = command[2]
        if old_item in shopping_list:
            for i in range(len(shopping_list)):
                if shopping_list[i] == old_item:
                    shopping_list[i] = new_item
    elif command[0] == "Rearrange":
        item = command[1]
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

print(", ".join(shopping_list))