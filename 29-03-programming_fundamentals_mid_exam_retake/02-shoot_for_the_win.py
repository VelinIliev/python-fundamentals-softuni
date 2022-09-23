targets = input().split(" ")
targets = [int(number) for number in targets]

targets_hit = 0

while True:
    command = input()
    if command == "End":
        targets = [str(number) for number in targets]
        print(f'Shot targets: {targets_hit} -> {" ".join(targets)}')
        break
    else:
        index = int(command)

    if index > len(targets) - 1:
        continue
    else:
        if targets[index] != -1:
            targets_hit += 1
            reducer = targets[index]
            targets[index] = -1
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] > reducer:
                        targets[i] -= reducer
                    elif targets[i] <= reducer:
                        targets[i] += reducer
