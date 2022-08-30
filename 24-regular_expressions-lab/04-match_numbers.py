import re

pattern = r"(^|(?<=\s)-?)([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
text = input()
matches = re.findall(pattern, text)

for match in matches:
    # print(match, end=" ")
    # # print()
    print("".join(match), end=" ")

# TODO: 70/100
