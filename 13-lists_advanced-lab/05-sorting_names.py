names = input()
names = names.split(", ")
names.sort()


def sort_by_length(e):
    return len(e)


names.sort(key=sort_by_length, reverse=True)

print(names)
