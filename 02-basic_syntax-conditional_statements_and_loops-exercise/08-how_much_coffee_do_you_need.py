coffee_needed = 0

while True:
    command = input()
    if command == "END":
        break
    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_needed += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_needed += 2

if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)