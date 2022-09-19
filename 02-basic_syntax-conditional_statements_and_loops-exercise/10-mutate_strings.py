string1 = input()
string2 = input()

for index in range(len(string1)):
    if string1[index] != string2[index]:
        string1 = string1[:index] + string2[index] + string1[index + 1:]
        print(string1)

