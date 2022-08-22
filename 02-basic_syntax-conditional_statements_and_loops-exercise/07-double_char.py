while True:
    string = input()
    if string == "End":
        break
    elif string != "SoftUni":
        for letter in string:
            print(f'{letter * 2}', end = "")
        print()