import re
text_string = input()

pattern = '([#]{1})([a-zA-Z]{3,})([#]{1,2})([a-zA-Z]{3,})([#]{1})|([@]{1})([a-zA-Z]{3,})([@]{1,2})([a-zA-Z]{3,})([@]{1})'
matches = re.findall(pattern, text_string)

valid_words = []
count_pairs = 0

for match in matches:
    # print(set(match))
    if len(set(match)) >= 4:
        if "##" in match or "@@" in match:
            count_pairs += 1
            pair = []
            for word in match:
                if len(word) >= 3:
                    pair.append(word)
            if pair[0] == pair[1][::-1]:
                valid_words.append(pair)


if count_pairs == 0:
    print('No word pairs found!')
else:
    print(f'{count_pairs} word pairs found!')

if len(valid_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    final_message = ""
    for n, pair in enumerate(valid_words, 1):
        if n == len(valid_words):
            final_message += f'{pair[0]} <=> {pair[1]}'
        else:
            final_message += f'{pair[0]} <=> {pair[1]}, '
    print(final_message)

# TODO: 88/100