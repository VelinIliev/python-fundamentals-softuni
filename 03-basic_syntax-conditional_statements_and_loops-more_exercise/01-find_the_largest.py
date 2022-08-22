number = input()

new_number = []
for x in number:
    new_number.append(int(x))

new_number.sort(reverse = True)

largest_number = ""

for y in new_number:
    largest_number += str(y)

print(int(largest_number))
