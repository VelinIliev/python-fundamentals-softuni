number_of_follows = int(input())

tank_capacity = 255
filled = 0

for _ in range(number_of_follows):
    fill = int(input())
    if filled + fill > tank_capacity:
        print("Insufficient capacity!")
    else:
        filled += fill

print(filled)