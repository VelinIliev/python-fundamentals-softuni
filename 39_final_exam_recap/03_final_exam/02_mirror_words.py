import re

work_string = input()

pattern = r'(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'

matches = re.findall(pattern, work_string)

mirror_words = []
for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word == second_word[::-1]:
        mirror_words.append(f'{first_word} <=> {second_word}')

if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print('No word pairs found!')

if mirror_words:
    print(f'The mirror words are:')
    print(", ".join(mirror_words))
else:
    print(f'No mirror words!')