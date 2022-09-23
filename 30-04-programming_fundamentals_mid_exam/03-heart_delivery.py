neighborhood = input().split("@")
neighborhood = [int(number) for number in neighborhood]

index = 0

while True:
    command = input()
    if command == "Love!":
        print(f"Cupid's last position was {index}.")
        if sum(neighborhood) == 0:
            print("Mission was successful.")
        else:
            counter = 0
            for house in neighborhood:
                if house > 0:
                    counter += 1
            print(f"Cupid has failed {counter} places.")
        break
    else:
        command = command.split(" ")
        length = int(command[1])

    if index + length < len(neighborhood):
        index += length
    else:
        while index + length > len(neighborhood) - 1:
            index = 0
            length = length - len(neighborhood)

    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    elif neighborhood[index] > 0:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day.")
