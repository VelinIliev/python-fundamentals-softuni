divisor = int(input())
boundary = int(input())

max_number = 0

for x in range(1, boundary + 1):
    if x % divisor == 0:

        if x > max_number:
            max_number = x

print(max_number)