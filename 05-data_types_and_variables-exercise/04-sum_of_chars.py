number_of_characters = int(input())

sum_of_characters = 0

for _ in range(number_of_characters):
    character = input()
    sum_of_characters += ord(character)

print(f'The sum equals: {sum_of_characters}')