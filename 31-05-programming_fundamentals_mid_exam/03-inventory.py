# You will receive a journal with some collecting items,
# separated with a comma and a space (", ").
journal = input().split(", ")

# After that, until receiving "Craft!" you will be
# receiving different commands split by " - ":

while True:
    command = input()
    if command == "Craft!":
        break
    else:
        command = command.split(" - ")
    action = command[0]
    item = command[1]
    #"Collect - {item}" - you should add the given
    # item to your inventory. If the item already exists,
    # you should skip this line.
    if action == "Collect":
        if item not in journal:
            journal.append(item)
    #"Drop - {item}" - you should remove the item
    # from your inventory if it exists.
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    #"Combine Items - {old_item}:{new_item}" - you should
    # check if the old item exists. If so, add the new
    # item after the old one. Otherwise, ignore the command.
    elif action == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)
    # "Renew – {item}" – if the given item exists,
    # you should change its position and put it last in your inventory.
    elif action == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

# After receiving "Craft!" print the items in your inventory, separated by ", ".
print(", ".join(journal))