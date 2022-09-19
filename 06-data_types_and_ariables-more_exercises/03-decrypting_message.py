key = int(input())
number_of_letters = int(input())

for _ in range(number_of_letters):
    letter = input()
    print(chr(ord(letter) + key), end="")