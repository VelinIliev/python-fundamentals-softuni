characters = input().split(", ")

chars = {}

for char in characters:
    chars[char] = ord(char)

print(chars)