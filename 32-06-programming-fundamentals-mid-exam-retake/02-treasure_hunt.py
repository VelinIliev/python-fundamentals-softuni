loot = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break
    else:
        command = command.split(" ")
    if command[0] == "Loot":
        items = command[1::]  # may be Loot in items?
        for item in items:
            if item not in loot:
                loot.insert(0, item)
    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(loot):
            item_to_rearrange = loot.pop(index)
            loot.append(item_to_rearrange)
    elif command[0] == "Steal":
        items_to_steal = int(command[1])
        stolen_items = loot[-items_to_steal::]
        loot = loot[:-items_to_steal:]
        print(", ".join(stolen_items))

if len(loot) > 0:
    gain = 0
    for item in loot:
        gain += len(item)
    average = gain / len(loot)
    print(f'Average treasure gain: {average:.2f} pirate credits.')
else:
    print("Failed treasure hunt.")