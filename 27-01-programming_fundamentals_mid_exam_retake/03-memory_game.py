elements = input().split(" ")
moves = 0
while True:
    command = input()
    if command == "end":
        print("Sorry you lose :(")
        print(" ".join(elements))
        break
    else:
        command = command.split(" ")
        first_index = int(command[0])
        second_index = int(command[1])
        moves += 1
        if first_index == second_index \
                or (first_index < 0 or first_index > len(elements) - 1)  \
                or (second_index < 0 or second_index > len(elements) - 1):
            middle = int(len(elements) / 2)
            new_element = f'-{moves}a'
            elements.insert(middle, new_element)
            elements.insert(middle, new_element)
            print("Invalid input! Adding additional elements to the board")
        elif elements[first_index] != elements[second_index]:
            print("Try again!")
        elif elements[first_index] == elements[second_index]:
            print(f"Congrats! You have found matching elements - {elements[first_index]}!")
            indexes_ty_delete = [first_index, second_index]
            sorted_indexes = sorted(indexes_ty_delete, reverse=True)
            for i in sorted_indexes:
                elements.pop(i)
        if len(elements) == 0:
            print(f'You have won in {moves} turns!')
            break

