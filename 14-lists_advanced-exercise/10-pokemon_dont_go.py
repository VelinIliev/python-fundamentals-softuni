sequence = input()
sequence = sequence.split(" ")
sequence = [int(number) for number in sequence]

# print(sequence)
removed_sum = 0

while len(sequence) > 0:
    index = int(input())

    if index < 0:
        increase = sequence[0]
        removed_sum += increase
        sequence[0] = sequence[-1]
    elif index > len(sequence) - 1:
        increase = sequence[-1]
        removed_sum += increase
        sequence[-1] = sequence[0]
    else:
        increase = sequence[index]
        removed_sum += increase
        del sequence[index]

    for i in range(len(sequence)):
        if sequence[i] <= increase:
            sequence[i] += increase
        elif sequence[i] > increase:
            sequence[i] -= increase

print(removed_sum)
