text = input()

# print(text)
new_text = ""

for i in range(len(text)):
    if text[i] == ">":
        strength = int(text[i+1])
        # print(text[i+1:i+1+strength:1])
        print(strength)


print(new_text)

# TODO: tasks from 7 to 10 - not ready
