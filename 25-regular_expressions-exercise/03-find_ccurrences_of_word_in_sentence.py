import re
text = input().lower()
word = input()

pattern = fr'\b{word}\b'
matches = re.findall(pattern, text)

print(len(matches))

# TODO: 80/100