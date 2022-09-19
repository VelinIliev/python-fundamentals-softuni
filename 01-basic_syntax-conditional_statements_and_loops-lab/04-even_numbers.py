number_of_numbers = int(input())

for _ in range(number_of_numbers):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        all_even = False
        break
else:
    print("All numbers are even.")