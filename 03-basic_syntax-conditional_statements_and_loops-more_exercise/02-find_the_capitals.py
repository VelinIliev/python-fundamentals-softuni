string = input()

indexes = []

for index, char in enumerate(string):
    if chr(90) >= char >= chr(65):
        indexes.append(index)

print(indexes)
