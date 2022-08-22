string = input()

indexes = []

for n, i in enumerate(string):
    if chr(90) >= i >= chr(65):
        indexes.append(n)

print(indexes)
