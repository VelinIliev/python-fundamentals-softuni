journal = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        print(", ".join(journal))
        break
    else:
        command = command.split(" - ")
        action = command[0]
        item = command[1]

    if action == "Collect":
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        if old_item in journal:
            for i in range(len(journal)):
                if journal[i] == old_item:
                    journal.append(new_item)
    elif action == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

# TODO: 70/100