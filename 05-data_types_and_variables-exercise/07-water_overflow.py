n = int(input())

tank_capacity = 255

filled = 0

for litters in range(n):
    fill = int(input())
    if filled + fill > tank_capacity:
        print("Insufficient capacity!")
    else:
        filled += fill

print(filled)