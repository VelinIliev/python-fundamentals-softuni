import re
string_txt = input()

number_pattern = r'[0-9]'
number_matches = re.findall(number_pattern, string_txt)
number_matches = [int(number) for number in number_matches]


cool_threshold = 1

for number in number_matches:
    cool_threshold *= number

print(f'Cool threshold: {cool_threshold}')

emoji_pattern = r'::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*'
emoji_matches = re.findall(emoji_pattern, string_txt)
print(f'{len(emoji_matches)} emojis found in the text. The cool ones are:')

cool_emojis = []
for emoji in emoji_matches:
    sum = 0
    for char in emoji:
        if char != ":" and char != "*":
            sum += ord(char)
    if sum >= cool_threshold:
        cool_emojis.append(emoji)

for emoji in cool_emojis:
    print(emoji)