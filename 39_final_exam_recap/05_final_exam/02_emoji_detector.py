import re

input_string = input()

pattern_emoji = r'(::|\*\*)([A-Z][a-z]{2,})\1'
pattern_numbers = r'[0-9]'

matches_emoji = re.findall(pattern_emoji, input_string)
matches_numbers = re.findall(pattern_numbers, input_string)
matches_numbers = [int(x) for x in matches_numbers]
cool_threshold = 1
for number in matches_numbers:
    cool_threshold *= number
cool_emojis = []
for emoji in matches_emoji:
    coolness = 0
    for char in emoji[1]:
        coolness += ord(char)
    if coolness > cool_threshold:
        cool_emojis.append(emoji[0]+emoji[1]+emoji[0])

print(f'Cool threshold: {cool_threshold}')
print(f'{len(matches_emoji)} emojis found in the text. The cool ones are:')
print("\n".join(cool_emojis))