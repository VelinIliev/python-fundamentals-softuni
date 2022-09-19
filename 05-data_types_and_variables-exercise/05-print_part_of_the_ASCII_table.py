ascii_start = int(input())
ascii_stop  = int(input())

for character in range(ascii_start, ascii_stop + 1):
    print(chr(character), end=" ")