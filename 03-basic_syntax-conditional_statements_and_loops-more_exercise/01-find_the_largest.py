number = input()

new_number = [x for x in number]
new_number.sort(reverse = True)

print("".join(new_number))
