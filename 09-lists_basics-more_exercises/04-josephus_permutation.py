starting_list = input()
k = int(input())

final_list = starting_list.split(" ")

result = []

index = k - 1

while len(final_list) > 0:

    peoples_to_remove = []
    if index < 0:
        break

    for i in range(len(final_list)):
        if i == index:
            peoples_to_remove.append(final_list[i])
            index += k

    if index > len(final_list) - 1:
        index = index - len(final_list)

    for x in peoples_to_remove:
        result.append(x)
        final_list.remove(x)

print_result = ",".join(result)
print(f'[{print_result}]')

# see 04-josephus_permutation-01.py