n = int(input())

for i in range(n):
    string = input()
    pure = True
    for letter in string:
        if letter == "," or letter == "." or letter == "_":
            pure = False
    if pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')