n = int(input())

sum = 0

for i in range(n):
    character = input()
    sum += ord(character)

print(f'The sum equals: {sum}')