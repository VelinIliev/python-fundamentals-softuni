n = int(input())

all_even = True

for x in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        all_even = False
        break

if all_even:
    print("All numbers are even.")