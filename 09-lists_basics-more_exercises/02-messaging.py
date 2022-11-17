numbers_as_string = input()
string = input()

numbers_str = numbers_as_string.split(" ")

for number in numbers_str:
    index = 0
    for digit in number:
        index += int(digit)
    if index > len(string):
        index = index - len(string)
    print(string[index], end="")
    string = string[:index] + string[index + 1:]
